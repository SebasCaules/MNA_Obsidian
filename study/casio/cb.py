# Cambio de base: P = M_{B2 B1}(id), coordenadas
from io_util import (clr, pause, ask_int, read_mat, read_vec, show_mat,
                     show_vec, step, menu_pick)
import mat

def cambio_base():
    n = ask_int("dim del esp: ")
    print("B1 (cargar vectores):")
    B1 = read_mat(n, n, "B1")  # filas = vectores en canonica
    print("B2 (cargar vectores):")
    B2 = read_mat(n, n, "B2")
    # P_{B2 B1}: cada col es [b_i^{B1}]_{B2}
    # Resolvemos B2^T * c_i = b_i^{B1}
    B2T = mat.transpose(B2)
    P_cols = []
    step("Expresando B1 en coordenadas B2")
    for i, b1 in enumerate(B1):
        x, _ = mat.solve(B2T, b1)
        if x is None:
            print("B2 no es base")
            pause()
            return
        show_vec(x, "[b1_" + str(i + 1) + "]_B2")
        P_cols.append(x)
    pause()
    P = mat.transpose(P_cols)
    step("P = M_{B2 B1}(id)")
    show_mat(P, "P")
    pause()
    # coordenadas de un vector v
    v = read_vec(n, "v (canonica)")
    # [v]_B1: B1^T x = v
    B1T = mat.transpose(B1)
    vB1, _ = mat.solve(B1T, v)
    show_vec(vB1, "[v]_B1")
    if vB1 is not None:
        vB2 = mat.matvec(P, vB1)
        show_vec(vB2, "[v]_B2 = P [v]_B1")
    pause()

def run():
    while True:
        clr()
        print("== Cambio de base ==")
        op = menu_pick([
            "P = M_{B2 B1}(id)",
            "Volver",
        ], "Op")
        if op == 0:
            cambio_base()
        else:
            break
