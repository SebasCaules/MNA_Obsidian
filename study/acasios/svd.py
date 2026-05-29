# SVD via A^T A (para matrices chicas, n,m <= 4)
import math
from io_util import (clr, pause, ask_int, read_mat, show_mat, show_vec,
                     step, menu_pick)
import mat
import diag

def svd():
    n = ask_int("filas A:")
    m = ask_int("cols A:")
    A = read_mat(n, m, "A")
    show_mat(A, "A")
    pause()
    # decidir via A^T A o A A^T (menor)
    if m <= n:
        step("Via AtA {}x{}".format(m, m))
        M = mat.matmul(mat.transpose(A), A)  # m x m
        show_mat(M, "AtA")
        pause()
        if m == 2:
            lams = diag.eigvals_2x2(M)
        elif m == 3:
            lams = diag.eigvals_3x3(M)
        else:
            print("m no soport.")
            pause()
            return
        if lams is None:
            print("autoval cpx?!")
            pause()
            return
        # sorted() no esta en MicroPython del Casio - bubble sort descendente
        for i in range(len(lams)):
            for j in range(i + 1, len(lams)):
                if lams[j] > lams[i]:
                    lams[i], lams[j] = lams[j], lams[i]
        sigmas = [max(0.0, L) ** 0.5 for L in lams]
        step("V.singulares")
        for i in range(len(sigmas)):
            print("s{}={:.6g}".format(i + 1, sigmas[i]))
        pause()
        # Agrupar autovalores con multiplicidad para que un sigma doble no
        # genere dos llamadas separadas a autovec (que con ruido FP devuelven
        # base vacia).
        clusters = diag.cluster_eigvals(lams)
        V_cols = []
        for ci in range(len(clusters)):
            L = clusters[ci][0]
            mult = clusters[ci][1]
            base = diag.autovec(M, L, m)
            if not base:
                print("L={} sin v".format(L))
                continue
            # Tomar exactamente mult vectores y ortonormalizar
            if len(base) > mult:
                base = base[:mult]
            v_norm, _ = mat.gram_schmidt(base)
            for v in v_norm:
                V_cols.append(v)
        # completar si menos de m
        while len(V_cols) < m:
            # vector e_i ortogonal a los existentes
            for k in range(m):
                e = [0.0] * m
                e[k] = 1.0
                u = e[:]
                for v in V_cols:
                    c = mat.dot(u, v)
                    u = mat.vsub(u, mat.vscale(v, c))
                nu = mat.norm(u)
                if nu > 1e-8:
                    V_cols.append([x / nu for x in u])
                    break
        V_cols = V_cols[:m]
        step("V cols")
        for i in range(len(V_cols)):
            show_vec(V_cols[i], "v" + str(i + 1))
        pause()
        # U
        U_cols = []
        for i in range(m):
            if sigmas[i] > 1e-10:
                Av = mat.matvec(A, V_cols[i])
                u = [x / sigmas[i] for x in Av]
                U_cols.append(u)
        # completar U a base de R^n con A^T x = 0
        if len(U_cols) < n:
            null_b = mat.solve(mat.transpose(A), [0.0] * m)[1]
            extra, _ = mat.gram_schmidt(null_b) if null_b else ([], [])
            # ortogonalizar contra U_cols
            for e in extra:
                u = e[:]
                for v in U_cols:
                    u = mat.vsub(u, mat.vscale(v, mat.dot(e, v)))
                nu = mat.norm(u)
                if nu > 1e-8:
                    U_cols.append([x / nu for x in u])
                    if len(U_cols) >= n:
                        break
        # rellenar con canonicos si todavia falta
        while len(U_cols) < n:
            for k in range(n):
                e = [0.0] * n
                e[k] = 1.0
                u = e[:]
                for v in U_cols:
                    u = mat.vsub(u, mat.vscale(v, mat.dot(e, v)))
                nu = mat.norm(u)
                if nu > 1e-8:
                    U_cols.append([x / nu for x in u])
                    break
        U_cols = U_cols[:n]
        step("U cols")
        for i in range(len(U_cols)):
            show_vec(U_cols[i], "u" + str(i + 1))
        pause()
        # armar matrices
        U = mat.transpose(U_cols)
        V = mat.transpose(V_cols)
        S = mat.zeros(n, m)
        for i in range(min(n, m)):
            if i < len(sigmas):
                S[i][i] = sigmas[i]
        step("Verif")
        VT = mat.transpose(V)
        USVT = mat.matmul(mat.matmul(U, S), VT)
        diff = 0.0
        for i in range(n):
            for j in range(m):
                diff = max(diff, abs(USVT[i][j] - A[i][j]))
        print("|USVt-A|={:.4g}".format(diff))
        show_mat(S, "Sigma")
        pause()
    else:
        print("pasar A^T (n<m)")
        pause()

def run():
    while True:
        clr()
        op = menu_pick(["SVD generico", "Volver"], "Op")
        if op == 0:
            svd()
        else:
            break
