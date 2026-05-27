# Diagonalizacion: p_A(lambda), autovalores, autovectores, P, D
import math
from io_util import (clr, pause, ask_int, read_mat, show_mat, show_vec,
                     step, menu_pick)
import mat

def eigvals_2x2(A):
    a, b = A[0][0], A[0][1]
    c, d = A[1][0], A[1][1]
    tr = a + d
    de = a * d - b * c
    disc = tr * tr - 4 * de
    print("tr =", tr, "det =", de, "disc =", disc)
    if disc < -1e-10:
        print("autovalores complejos:")
        re = tr / 2
        im = (-disc) ** 0.5 / 2
        print("L1 =", re, "+", im, "i")
        print("L2 =", re, "-", im, "i")
        return None
    sd = max(0.0, disc) ** 0.5
    return [(tr + sd) / 2, (tr - sd) / 2]

def eigvals_3x3(A):
    # p(L) = L^3 + a*L^2 + b*L + c
    # con: a = -tr(A), b = sum minores principales 2x2, c = -det(A)
    tr = sum(A[i][i] for i in range(3))
    M00 = A[1][1] * A[2][2] - A[1][2] * A[2][1]
    M11 = A[0][0] * A[2][2] - A[0][2] * A[2][0]
    M22 = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    b1 = M00 + M11 + M22
    de = mat.det(A)
    a = -tr
    b = b1
    c = -de
    print("p(L) = L^3 + ({:.4g})L^2 + ({:.4g})L + ({:.4g})".format(a, b, c))
    # depresion: L = y - a/3
    p = b - a * a / 3.0
    q = 2 * a ** 3 / 27.0 - a * b / 3.0 + c
    print("depresion: y^3 + ({:.4g})y + ({:.4g}) = 0".format(p, q))
    disc = -4 * p ** 3 - 27 * q * q
    print("disc =", disc)
    roots = []
    if abs(p) < 1e-10 and abs(q) < 1e-10:
        roots = [0.0, 0.0, 0.0]
    elif disc > -1e-10 and p < -1e-10:
        # trigonometrico
        r = ((-p / 3.0)) ** 0.5
        cos_arg = (3 * q) / (2 * p) * ((-3.0 / p) ** 0.5)
        # clamp
        cos_arg = max(-1.0, min(1.0, cos_arg))
        ang = math.acos(cos_arg) / 3.0
        for k in range(3):
            y = 2 * r * math.cos(ang - 2 * math.pi * k / 3.0)
            roots.append(y)
    else:
        # Cardano clasico - puede tener complejas
        s = (-(q / 2.0))
        d2 = q * q / 4.0 + p ** 3 / 27.0
        if d2 >= 0:
            d = d2 ** 0.5
            u3 = -q / 2.0 + d
            v3 = -q / 2.0 - d
            def cbrt(x):
                return -((-x) ** (1.0 / 3.0)) if x < 0 else x ** (1.0 / 3.0)
            u = cbrt(u3)
            v = cbrt(v3)
            roots = [u + v]
            # las otras dos son complejas conjugadas
            re = -(u + v) / 2
            print("L1 (real) =", re + (u + v))
            print("L2,3 complejas conj con Re =", re)
            return None
        else:
            # 3 reales pero p>0 raro
            r = ((-p / 3.0)) ** 0.5
            cos_arg = (3 * q) / (2 * p) * ((-3.0 / p) ** 0.5)
            cos_arg = max(-1.0, min(1.0, cos_arg))
            ang = math.acos(cos_arg) / 3.0
            for k in range(3):
                y = 2 * r * math.cos(ang - 2 * math.pi * k / 3.0)
                roots.append(y)
    # deshacer depresion
    lams = sorted([y - a / 3.0 for y in roots], reverse=True)
    return lams

def autovec(A, lam, n):
    """Devuelve base del nucleo de (lambda I - A)."""
    M = [[(lam if i == j else 0.0) - A[i][j] for j in range(n)]
         for i in range(n)]
    _, base = mat.solve(M, [0.0] * n)
    return base

def diagonalizar():
    n = ask_int("n (2 o 3): ")
    A = read_mat(n, n, "A")
    show_mat(A, "A")
    step("Polinomio caracteristico")
    if n == 2:
        lams = eigvals_2x2(A)
    elif n == 3:
        lams = eigvals_3x3(A)
    else:
        print("Solo 2 o 3")
        pause()
        return
    if lams is None:
        pause()
        return
    print("Autovalores:")
    for i, L in enumerate(lams):
        print("L{} = {:.6g}".format(i + 1, L))
    pause()
    # autovectores
    P_cols = []
    D_vals = []
    used = []
    for L in lams:
        # detectar si ya lo procesamos (dentro de tol)
        seen = False
        for L0 in used:
            if abs(L - L0) < 1e-6:
                seen = True
                break
        step("Autoespacio L = {:.4g}".format(L))
        base = autovec(A, L, n)
        if not base:
            print("(no hay autovec / multiple)")
            continue
        for v in base:
            show_vec(v, "v")
            P_cols.append(v)
            D_vals.append(L)
        used.append(L)
    pause()
    if len(P_cols) < n:
        print("NO diagonalizable")
        print("(dim total autov:", len(P_cols), "< ", n, ")")
        pause()
        return
    # armar P, D
    step("Armando P, D")
    P = mat.transpose(P_cols)  # cols como columnas
    D = [[D_vals[i] if i == j else 0.0 for j in range(n)]
         for i in range(n)]
    show_mat(P, "P")
    pause()
    show_mat(D, "D = diag")
    pause()
    # verificacion
    AP = mat.matmul(A, P)
    PD = mat.matmul(P, D)
    diff = max(abs(AP[i][j] - PD[i][j]) for i in range(n) for j in range(n))
    print("Verif |AP - PD|_inf =", diff)
    pause()

def run():
    while True:
        clr()
        print("== Diagonalizar ==")
        op = menu_pick([
            "Diagonalizar (n=2 o 3)",
            "Volver",
        ], "Op")
        if op == 0:
            diagonalizar()
        else:
            break
