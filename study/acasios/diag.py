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
    print("tr={:.4g}".format(tr))
    print("det={:.4g}".format(de))
    # det~0 -> L es factor comun: p(L)=L^2-tr*L=L(L-tr)
    scl = 1.0 + abs(a) + abs(b) + abs(c) + abs(d)
    if abs(de) < 1e-7 * scl:
        print("det~0: L factor")
        print("p(L)=L(L-tr)")
        print("L=0, L={:.4g}".format(tr))
        return [tr, 0.0] if tr >= 0 else [0.0, tr]
    print("disc={:.4g}".format(disc))
    if disc < -1e-10:
        print("autoval cpx:")
        re = tr / 2
        im = (-disc) ** 0.5 / 2
        print("L1={:.4g}".format(re))
        print(" +{:.4g}i".format(im))
        print("L2={:.4g}".format(re))
        print(" -{:.4g}i".format(im))
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
    print("p(L)=L^3+")
    print("a={:.4g}".format(a))
    print("b={:.4g}".format(b))
    print("c={:.4g}".format(c))
    # c~0 (det A=0) -> L es factor comun:
    # p(L)=L^3+a*L^2+b*L = L(L^2+a*L+b)
    # Resolvemos el cuadratico exacto (evita ruido de Cardano).
    scl = 1.0 + abs(a) + abs(b)
    if abs(c) < 1e-7 * scl:
        print("c~0: L factor")
        print("p=L(L^2+aL+b)")
        disc2 = a * a - 4 * b
        print("disc2={:.4g}".format(disc2))
        if disc2 < -1e-10:
            print("L=0 y 2 cpx:")
            re = -a / 2
            im = (-disc2) ** 0.5 / 2
            print("Re={:.4g}".format(re))
            print("Im=+-{:.4g}".format(im))
            return None
        sd2 = max(0.0, disc2) ** 0.5
        r1 = (-a + sd2) / 2
        r2 = (-a - sd2) / 2
        lams = [0.0, r1, r2]
        for i in range(len(lams)):
            for j in range(i + 1, len(lams)):
                if lams[j] > lams[i]:
                    lams[i], lams[j] = lams[j], lams[i]
        return lams
    # depresion: L = y - a/3
    p = b - a * a / 3.0
    q = 2 * a ** 3 / 27.0 - a * b / 3.0 + c
    print("dep p={:.4g}".format(p))
    print("dep q={:.4g}".format(q))
    disc = -4 * p ** 3 - 27 * q * q
    print("disc={:.4g}".format(disc))
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
            # OJO: u+v es raiz de la cubica DEPRIMIDA (en y). El autovalor es
            # lambda = y - a/3. Antes no se deshacia la depresion -> imprimia mal.
            real_root = (u + v) - a / 3.0          # autovalor real
            re = -(u + v) / 2.0 - a / 3.0           # Re de las complejas
            im = (3.0 ** 0.5) / 2.0 * abs(u - v)    # parte imaginaria
            print("L1(real)={:.4g}".format(real_root))
            print("L2,3 Re={:.4g}".format(re))
            print("   Im=+-{:.4g}".format(im))
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
    lams = [y - a / 3.0 for y in roots]
    # sorted() no esta en MicroPython del Casio - bubble sort descendente
    for i in range(len(lams)):
        for j in range(i + 1, len(lams)):
            if lams[j] > lams[i]:
                lams[i], lams[j] = lams[j], lams[i]
    return lams

def autovec(A, lam, n, eps=1e-6):
    """Devuelve base del nucleo de (lambda I - A).
    eps flojo (1e-6) porque Cardano introduce ruido O(1e-8) en autovalores
    repetidos, y con el default tight (1e-10) el ruido oculta la
    deficiencia de rango y la base sale vacia."""
    M = [[(lam if i == j else 0.0) - A[i][j] for j in range(n)]
         for i in range(n)]
    _, base = mat.solve(M, [0.0] * n, eps=eps)
    return base


def cluster_eigvals(lams, tol=1e-6):
    """Agrupa autovalores numericamente iguales.
    Devuelve lista [(L_promedio, multiplicidad), ...].
    Necesario porque Cardano para raices multiples da valores cercanos pero
    distintos (ej. 4.000000048 y 3.999999951) y hay que tratarlos como uno."""
    clusters = []
    for L in lams:
        merged = False
        for i in range(len(clusters)):
            Lc = clusters[i][0]
            mc = clusters[i][1]
            scale = max(1.0, abs(Lc))
            if abs(L - Lc) < tol * scale:
                new_avg = (Lc * mc + L) / (mc + 1)
                clusters[i] = (new_avg, mc + 1)
                merged = True
                break
        if not merged:
            clusters.append((L, 1))
    return clusters

def analizar(A, n):
    # Analisis de diagonalizacion de una matriz YA armada (numerica).
    # Lo usa diagonalizar() y tambien param.py (hallar a,b y diagonalizar).
    show_mat(A, "A")
    step("P(L) caract.")
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
    for i in range(len(lams)):
        print("L{}={:.6g}".format(i + 1, lams[i]))
    pause()
    # Agrupar autovalores con multiplicidad (Cardano ruidoso en raices dobles)
    clusters = cluster_eigvals(lams)
    # autovectores por cluster
    P_cols = []
    D_vals = []
    for ci in range(len(clusters)):
        L = clusters[ci][0]
        mult = clusters[ci][1]
        if mult > 1:
            step("S_L={:.4g} m={}".format(L, mult))
        else:
            step("S_L={:.4g}".format(L))
        base = autovec(A, L, n)
        if not base:
            print("(S vacio?)")
            continue
        if len(base) < mult:
            print("dimK=", len(base), "<m=", mult)
            print("(NO diag.)")
        for v in base:
            show_vec(v, "v")
            P_cols.append(v)
            D_vals.append(L)
    pause()
    if len(P_cols) < n:
        print("NO diagonaliz.")
        print("dim=", len(P_cols), "<n=", n)
        pause()
        return
    # armar P, D
    step("Armando P,D")
    P = mat.transpose(P_cols)  # cols como columnas
    D = [[D_vals[i] if i == j else 0.0 for j in range(n)]
         for i in range(n)]
    show_mat(P, "P")
    pause()
    show_mat(D, "D")
    pause()
    # verificacion
    AP = mat.matmul(A, P)
    PD = mat.matmul(P, D)
    diff = max(abs(AP[i][j] - PD[i][j]) for i in range(n) for j in range(n))
    print("|AP-PD|={:.4g}".format(diff))
    pause()

def diagonalizar():
    n = ask_int("n(2 o 3):")
    A = read_mat(n, n, "A")
    analizar(A, n)

def run():
    # Un solo worker: se corre y el script corta (scroll ^ para revisar).
    diagonalizar()
