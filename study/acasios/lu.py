# Factorizacion PA = LU (Doolittle con pivoteo parcial)
from io_util import clr, pause, ask_int, read_mat, show_mat, step, menu_pick
import mat

def plu():
    n = ask_int("n cuadr:")
    A = read_mat(n, n, "A")
    show_mat(A, "A")
    pause()
    L = mat.eye(n)
    P = mat.eye(n)
    U = mat.copy(A)
    for j in range(n):
        # pivot parcial: max |U[i][j]| con i>=j
        piv = j
        for i in range(j + 1, n):
            if abs(U[i][j]) > abs(U[piv][j]):
                piv = i
        if piv != j:
            U[j], U[piv] = U[piv], U[j]
            P[j], P[piv] = P[piv], P[j]
            for k in range(j):
                L[j][k], L[piv][k] = L[piv][k], L[j][k]
            step("P:F{}<>F{}".format(j + 1, piv + 1))
        if abs(U[j][j]) < 1e-12:
            print("piv=0, A sing.")
            pause()
            return
        for i in range(j + 1, n):
            m_ij = U[i][j] / U[j][j]
            L[i][j] = m_ij
            for k in range(j, n):
                U[i][k] -= m_ij * U[j][k]
        step("Tras col {}".format(j + 1))
        show_mat(U, "U")
        pause()
    step("Resultado")
    show_mat(P, "P")
    pause()
    show_mat(L, "L")
    pause()
    show_mat(U, "U")
    # verificacion
    LU = mat.matmul(L, U)
    PA = mat.matmul(P, A)
    diff = max(abs(LU[i][j] - PA[i][j]) for i in range(n) for j in range(n))
    print("|PA-LU|={:.4g}".format(diff))
    pause()

def run():
    while True:
        clr()
        op = menu_pick(["PA=LU Doolittle", "Volver"], "Op")
        if op == 0:
            plu()
        else:
            break
