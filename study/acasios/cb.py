# Cambio de base: P = M_{B2 B1}(id), coordenadas
from io_util import (clr, pause, ask_int, read_mat, read_vec, show_mat,
                     show_vec, step, menu_pick)
import mat

def cambio_base():
    n = ask_int("dim:")
    print("B1 vectores:")
    B1 = read_mat(n, n, "B1")  # filas = vectores en canonica
    print("B2 vectores:")
    B2 = read_mat(n, n, "B2")
    # P_{B2 B1}: cada col es [b_i^{B1}]_{B2}
    # Resolvemos B2^T * c_i = b_i^{B1}
    B2T = mat.transpose(B2)
    P_cols = []
    step("B1 en coord B2")
    for i in range(len(B1)):
        b1 = B1[i]
        x, _ = mat.solve(B2T, b1)
        if x is None:
            print("B2 no es base")
            pause()
            return
        show_vec(x, "[b1_" + str(i + 1) + "]B2")
        P_cols.append(x)
    pause()
    P = mat.transpose(P_cols)
    step("P=M_{B2B1}(id)")
    show_mat(P, "P")
    pause()
    # coordenadas de un vector v
    v = read_vec(n, "v(can)")
    # [v]_B1: B1^T x = v
    B1T = mat.transpose(B1)
    vB1, _ = mat.solve(B1T, v)
    show_vec(vB1, "[v]B1")
    if vB1 is not None:
        vB2 = mat.matvec(P, vB1)
        show_vec(vB2, "[v]B2=P[v]B1")
    pause()

def run():
    # Un solo worker: se corre y el script corta (scroll ^ para revisar).
    cambio_base()
