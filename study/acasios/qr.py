# Factorizacion QR via Gram-Schmidt clasico
from io_util import (clr, pause, ask_int, read_mat, show_mat, show_vec,
                     step, menu_pick)
import mat

def qr_factor():
    n = ask_int("filas A:")
    m = ask_int("cols A:")
    A = read_mat(n, m, "A")
    show_mat(A, "A")
    pause()
    # columnas de A
    cols = [[A[i][j] for i in range(n)] for j in range(m)]
    V = []
    R = mat.zeros(m, m)
    for j in range(m):
        a_j = cols[j]
        u = a_j[:]
        step("Col {}".format(j + 1))
        for i in range(len(V)):
            v = V[i]
            c = mat.dot(a_j, v)
            R[i][j] = c
            print("<a{},v{}>={:.4g}".format(j + 1, i + 1, c))
            u = mat.vsub(u, mat.vscale(v, c))
        nu = mat.norm(u)
        R[j][j] = nu
        print("||u{}||={:.4g}".format(j + 1, nu))
        if nu < 1e-10:
            print("col LD: no QR")
            pause()
            return
        v_new = [x / nu for x in u]
        show_vec(v_new, "v" + str(j + 1))
        V.append(v_new)
        pause()
    Q = mat.transpose(V)  # cols = v_i
    step("Resultado")
    show_mat(Q, "Q")
    pause()
    show_mat(R, "R")
    pause()
    # verificacion
    QR = mat.matmul(Q, R)
    diff = max(abs(QR[i][j] - A[i][j]) for i in range(n) for j in range(m))
    print("|QR-A|={:.4g}".format(diff))
    QtQ = mat.matmul(mat.transpose(Q), Q)
    diff2 = 0.0
    for i in range(m):
        for j in range(m):
            target = 1.0 if i == j else 0.0
            diff2 = max(diff2, abs(QtQ[i][j] - target))
    print("|QtQ-I|={:.4g}".format(diff2))
    pause()

def run():
    while True:
        clr()
        op = menu_pick(["QR Gram-Sch", "Volver"], "Op")
        if op == 0:
            qr_factor()
        else:
            break
