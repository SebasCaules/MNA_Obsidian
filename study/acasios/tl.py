# Transformaciones lineales: nucleo, imagen, antiimagen, rango
from io_util import (clr, pause, ask_int, read_mat, read_vec,
                     show_mat, show_vec, step, menu_pick)
import mat

def nucleo_imagen():
    n = ask_int("filas A:")
    m = ask_int("cols A:")
    A = read_mat(n, m, "A")
    show_mat(A, "A")
    step("RREF: N(T) Im(T)")
    R, _, pivots = mat.gauss_jordan(A, None)
    show_mat(R, "rref")
    print("rg=", len(pivots))
    print("dim N=", m - len(pivots))
    pause()
    # Nucleo: Ax = 0
    x_p, null_b = mat.solve(A, [0.0] * n)
    step("Base N(T)")
    if not null_b:
        print("N(T)={0}")
    else:
        for i in range(len(null_b)):
            show_vec(null_b[i], "n" + str(i + 1))
    pause()
    step("Base Im(T)")
    print("(cols pivote de A)")
    cols_piv = [c for _, c in pivots]
    for c in cols_piv:
        col = [A[i][c] for i in range(n)]
        show_vec(col, "c" + str(c + 1))
    pause()

def antiimagen():
    n = ask_int("filas A:")
    m = ask_int("cols A:")
    A = read_mat(n, m, "A")
    b = read_vec(n, "b")
    step("Resuelvo Ax=b")
    x_p, null_b = mat.solve(A, b)
    if x_p is None:
        print("INCOMPAT: b!Im(T)")
        pause()
        return
    show_vec(x_p, "x_p")
    if null_b:
        print("Sol gral:")
        print("x=x_p+sum t_i n_i")
        for i in range(len(null_b)):
            show_vec(null_b[i], "n" + str(i + 1))
    else:
        print("Sol unica.")
    pause()

def matriz_por_regla():
    print("T:R^n->R^m")
    print("dar T(e_j) por col")
    n = ask_int("dim dom:")
    m = ask_int("dim cod:")
    A = []
    for j in range(n):
        v = read_vec(m, "T(e" + str(j + 1) + ")")
        A.append(v)
    # A = columnas son T(e_j) -> transponer
    A = mat.transpose(A)
    step("Mat canonica A")
    show_mat(A)
    pause()

def run():
    while True:
        clr()
        op = menu_pick([
            "N(T),Im,rg",
            "Antiimagen b",
            "Mat. por regla",
            "Volver",
        ], "Op")
        if op == 0:
            nucleo_imagen()
        elif op == 1:
            antiimagen()
        elif op == 2:
            matriz_por_regla()
        else:
            break
