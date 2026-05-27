# Transformaciones lineales: nucleo, imagen, antiimagen, rango
from io_util import (clr, pause, ask_int, read_mat, read_vec,
                     show_mat, show_vec, step, menu_pick)
import mat

def nucleo_imagen():
    n = ask_int("n (filas A): ")
    m = ask_int("m (cols A): ")
    A = read_mat(n, m, "A")
    show_mat(A, "A")
    step("Reduzco A para hallar N(T) e Im(T)")
    R, _, pivots = mat.gauss_jordan(A, None)
    show_mat(R, "rref(A)")
    print("rg(A) =", len(pivots))
    print("dim N(T) =", m - len(pivots))
    pause()
    # Nucleo: Ax = 0
    x_p, null_b = mat.solve(A, [0.0] * n)
    step("Base de N(T)")
    if not null_b:
        print("N(T) = {0}")
    else:
        for i, v in enumerate(null_b):
            show_vec(v, "n" + str(i + 1))
    pause()
    step("Base de Im(T)")
    print("(columnas LI de A: pivote en col c)")
    cols_piv = [c for _, c in pivots]
    for c in cols_piv:
        col = [A[i][c] for i in range(n)]
        show_vec(col, "col" + str(c + 1))
    pause()

def antiimagen():
    n = ask_int("n (filas A): ")
    m = ask_int("m (cols A): ")
    A = read_mat(n, m, "A")
    b = read_vec(n, "b")
    step("Resuelvo Ax = b")
    x_p, null_b = mat.solve(A, b)
    if x_p is None:
        print("INCOMPATIBLE: b no esta en Im(T)")
        pause()
        return
    show_vec(x_p, "x particular")
    if null_b:
        print("Solucion general:")
        print("x = x_p + sum(t_i * n_i)")
        for i, v in enumerate(null_b):
            show_vec(v, "n" + str(i + 1))
    else:
        print("Solucion unica.")
    pause()

def matriz_por_regla():
    print("T:R^n -> R^m por regla")
    print("Carga T(e_j) col por col")
    n = ask_int("dim dominio: ")
    m = ask_int("dim codom: ")
    A = []
    for j in range(n):
        v = read_vec(m, "T(e" + str(j + 1) + ")")
        A.append(v)
    # A = columnas son T(e_j) -> transponer
    A = mat.transpose(A)
    step("Matriz canonica A")
    show_mat(A)
    pause()

def run():
    while True:
        clr()
        print("== TL ==")
        op = menu_pick([
            "Nucleo + Imagen + rg",
            "Antiimagen de b",
            "Matriz por regla",
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
