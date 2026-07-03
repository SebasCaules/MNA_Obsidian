# Factorizacion PA = LU (Doolittle con pivoteo parcial)
from io_util import clr, pause, ask_int, read_mat, show_mat, step, menu_pick
import mat

def plu():
    # Acepta matrices n x m (no solo cuadradas). L: n x n, U: n x m, P: n x n.
    n = ask_int("filas:")
    m = ask_int("cols:")
    A = read_mat(n, m, "A")
    show_mat(A, "A")
    pause()
    L = mat.eye(n)
    P = mat.eye(n)
    U = mat.copy(A)
    for j in range(min(n, m)):
        # pivoteo parcial: max |U[i][j]| con i>=j
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
            # tras pivotear, la columna ya es ~0 bajo la diag: nada que eliminar
            # (L[.,j]=0). Antes abortaba; ahora sigue y arma P,L,U completos.
            step("col {}: piv~0".format(j + 1))
        else:
            for i in range(j + 1, n):
                m_ij = U[i][j] / U[j][j]
                L[i][j] = m_ij
                for k in range(j, m):
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
    # verificacion PA = LU
    LU = mat.matmul(L, U)
    PA = mat.matmul(P, A)
    diff = max(abs(LU[i][j] - PA[i][j]) for i in range(n) for j in range(m))
    print("|PA-LU|={:.4g}".format(diff))
    pause()

def run():
    # Un solo worker: se corre y el script corta (scroll ^ para revisar).
    plu()
