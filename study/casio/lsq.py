# Cuadrados minimos via ecuaciones normales (con QR para estabilidad opcional)
import math
from io_util import (clr, pause, ask_int, ask_float, read_vec, show_mat,
                     show_vec, step, menu_pick)
import mat

# Modelos disponibles: indice -> (nombre, lista de funciones base f_k(x))
MODELOS = [
    ("y = a + b x", [lambda x: 1.0, lambda x: x]),
    ("y = a + b x + c x^2", [lambda x: 1.0, lambda x: x, lambda x: x * x]),
    ("y = a cos x + b sen x", [math.cos, math.sin]),
    ("y = a + b cos x + c sen x",
     [lambda x: 1.0, math.cos, math.sin]),
    ("y = a e^x + b e^-x",
     [lambda x: math.exp(x), lambda x: math.exp(-x)]),
]

def mmcc():
    n_p = ask_int("# puntos: ")
    xs = []
    ys = []
    print("Cargar (x_i, y_i):")
    for i in range(n_p):
        v = read_vec(2, "p" + str(i + 1))
        xs.append(v[0])
        ys.append(v[1])
    print("Modelo:")
    for i, (nm, _) in enumerate(MODELOS):
        print("{}) {}".format(i + 1, nm))
    sel = ask_int("> ") - 1
    funcs = MODELOS[sel][1]
    m = len(funcs)
    A = [[funcs[k](xs[i]) for k in range(m)] for i in range(n_p)]
    step("A (matriz disenio)")
    show_mat(A)
    pause()
    AT = mat.transpose(A)
    ATA = mat.matmul(AT, A)
    ATb = mat.matvec(AT, ys)
    step("A^T A x = A^T b")
    show_mat(ATA, "A^T A")
    show_vec(ATb, "A^T b")
    inv = mat.inverse(ATA)
    if inv is None:
        print("Sistema degenerado")
        pause()
        return
    x = mat.matvec(inv, ATb)
    step("Solucion")
    show_vec(x, "coef")
    # residuo
    Ax = mat.matvec(A, x)
    r = [Ax[i] - ys[i] for i in range(n_p)]
    norm_r = mat.norm(r)
    print("||Ax - b|| =", norm_r)
    pause()

def run():
    while True:
        clr()
        print("== Cuad. minimos ==")
        op = menu_pick(["MMCC modelo lineal", "Volver"], "Op")
        if op == 0:
            mmcc()
        else:
            break
