# Param x autovector: hallar parametros para que v sea autovector + diagonaliz.
#
# Ej tipico:  A = [[1,0,b],[1,1,0],[1,1,a]],  pedir que (0,-1,1) sea autovector.
#   a) halla a,b (y el autovalor L) resolviendo el sistema lineal A v = L v.
#   b) arma la A numerica y la diagonaliza (reusa diag.analizar).
#
# Idea (parte a): con A = A0 + sum_j p_j * E_j  (E_j marca donde va el param j),
#   A v = A0 v + sum_j p_j (E_j v) = L v
#   => sum_j p_j (E_j v) - L v = -(A0 v)
# Sistema lineal en las incognitas x = [p_1,...,p_k, L]. Lo resuelve mat.solve.
from io_util import ask_int, read_vec, step, pause
import mat
import diag

# Para la captura a archivo: param llama a diag (que imprime), avisamos para
# que cap_start tambien duplique los print de diag.
_CAP_HELPERS = (diag,)

_LETRAS = "abcdefghijklmnopqrstuvwxyz"


def _z(x):
    # Limpia el "cero negativo" (-0.0) y ruido chico para que imprima 0.
    return 0.0 if abs(x) < 1e-12 else x


def parse_entry(tok):
    # "3"->(3,None) ; "a"->(1,'a') ; "-a"->(-1,'a') ; "2a"->(2,'a') ; "1.5b"->(1.5,'b')
    tok = tok.strip()
    ch = tok[-1]
    if ch.lower() in _LETRAS:
        pre = tok[:-1].strip()
        if pre == "" or pre == "+":
            coef = 1.0
        elif pre == "-":
            coef = -1.0
        else:
            coef = float(pre)
        return (coef, ch.lower())
    return (float(tok), None)


def read_param_mat(n):
    # Lee A con entradas numericas O letras (parametros). Devuelve:
    #   A0    : parte conocida (los lugares con parametro quedan en 0)
    #   cells : lista (i, j, coef, nombre) de las posiciones con parametro
    #   params: nombres de parametros en orden de aparicion
    print("A: num o letra")
    print("(ej f: 1,0,b)")
    A0 = mat.zeros(n, n)
    cells = []
    params = []
    for i in range(n):
        while True:
            s = input("f{}/{}:".format(i + 1, n))
            toks = []
            for t in s.replace(";", ",").split(","):
                if t.strip() != "":
                    toks.append(t)
            if len(toks) != n:
                print("len?")
                continue
            tmpA = []
            tmpcells = []
            ok = True
            try:
                for j in range(n):
                    coef, pname = parse_entry(toks[j])
                    if pname is None:
                        tmpA.append(coef)
                    else:
                        tmpA.append(0.0)
                        tmpcells.append((i, j, coef, pname))
            except Exception:
                print("?entrada")
                ok = False
            if not ok:
                continue
            for j in range(n):
                A0[i][j] = tmpA[j]
            for c in tmpcells:
                cells.append(c)
                if c[3] not in params:
                    params.append(c[3])
            break
    return A0, cells, params


def run():
    n = ask_int("n(2 o 3):")
    if n < 2 or n > 3:
        print("Solo 2 o 3")
        return
    print("Autovector v:")
    v = read_vec(n, "v")
    A0, cells, params = read_param_mat(n)
    k = len(params)

    # Sistema:  sum_j p_j (E_j v) - L v = -(A0 v)   (incognitas: params..., L)
    Av0 = mat.matvec(A0, v)
    M = mat.zeros(n, k + 1)
    for c in cells:
        ci, cj, coef, pname = c[0], c[1], c[2], c[3]
        t = params.index(pname)
        M[ci][t] += coef * v[cj]
    for i in range(n):
        M[i][k] = -v[i]
    rhs = [-Av0[i] for i in range(n)]

    x_p, null = mat.solve(M, rhs)
    if x_p is None:
        print("v NO es autovec")
        print("(sist incompat)")
        return

    step("a) Parametros")
    for t in range(k):
        print("{}={:.6g}".format(params[t], _z(x_p[t])))
    lam = _z(x_p[k])
    print("L={:.6g}".format(lam))
    if null:
        print("(infinitas sol:")
        print(" hay libre/s)")

    # Armar A numerica con los valores hallados
    A = mat.copy(A0)
    for c in cells:
        ci, cj, coef, pname = c[0], c[1], c[2], c[3]
        t = params.index(pname)
        A[ci][cj] = A0[ci][cj] + coef * x_p[t]
    pause()

    step("b) Diagonaliz?")
    diag.analizar(A, n)
