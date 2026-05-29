# Pseudoinversa de Moore-Penrose: via (A^T A)^-1 A^T o via A^T (A A^T)^-1
from io_util import (clr, pause, ask_int, read_mat, show_mat, step, menu_pick)
import mat

def pinv():
    n = ask_int("filas:")
    m = ask_int("cols:")
    A = read_mat(n, m, "A")
    show_mat(A, "A")
    AT = mat.transpose(A)
    if n >= m:
        step("AtA {}x{}".format(m, m))
        M = mat.matmul(AT, A)
        show_mat(M, "AtA")
        inv = mat.inverse(M)
        if inv is None:
            print("AtA no inv: SVD")
            pause()
            return
        P = mat.matmul(inv, AT)  # m x n
    else:
        step("AAt {}x{}".format(n, n))
        M = mat.matmul(A, AT)
        show_mat(M, "AAt")
        inv = mat.inverse(M)
        if inv is None:
            print("AAt no inv: SVD")
            pause()
            return
        P = mat.matmul(AT, inv)  # m x n
    step("A+")
    show_mat(P, "A+")
    pause()
    # verifico A A+ A = A
    AAA = mat.matmul(mat.matmul(A, P), A)
    diff = 0.0
    for i in range(n):
        for j in range(m):
            diff = max(diff, abs(AAA[i][j] - A[i][j]))
    print("|AA+A-A|={:.4g}".format(diff))
    pause()

def run():
    # Un solo worker: se corre y el script corta (scroll ^ para revisar).
    pinv()
