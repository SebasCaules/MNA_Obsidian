# Cuadrados minimos via ecuaciones normales
import math
from io_util import (clr, pause, ask_int, ask_float, read_vec, show_mat,
                     show_vec, step, menu_pick)
import mat

# Modelos disponibles: nombres cortos para caber en 19 cols
MODELOS = [
    ("y=a+bx", [lambda x: 1.0, lambda x: x]),
    ("y=a+bx+cx^2", [lambda x: 1.0, lambda x: x, lambda x: x * x]),
    ("y=a cos+b sen", [math.cos, math.sin]),
    ("y=a+b cos+c sen", [lambda x: 1.0, math.cos, math.sin]),
    ("y=a e^x+b e^-x", [lambda x: math.exp(x), lambda x: math.exp(-x)]),
]

def mmcc():
    n_p = ask_int("#ptos:")
    xs = []
    ys = []
    print("(x_i, y_i):")
    for i in range(n_p):
        v = read_vec(2, "p" + str(i + 1))
        xs.append(v[0])
        ys.append(v[1])
    print("Modelo:")
    for i in range(len(MODELOS)):
        print("{}){}".format(i + 1, MODELOS[i][0]))
    sel = ask_int(">") - 1
    funcs = MODELOS[sel][1]
    m = len(funcs)
    A = [[funcs[k](xs[i]) for k in range(m)] for i in range(n_p)]
    step("A diseno")
    show_mat(A)
    pause()
    AT = mat.transpose(A)
    ATA = mat.matmul(AT, A)
    ATb = mat.matvec(AT, ys)
    step("AtA x=Atb")
    show_mat(ATA, "AtA")
    show_vec(ATb, "Atb")
    pause()
    inv = mat.inverse(ATA)
    if inv is None:
        print("sist. degenerado")
        pause()
        return
    x = mat.matvec(inv, ATb)
    step("Solucion")
    show_vec(x, "coef")
    # residuo
    Ax = mat.matvec(A, x)
    r = [Ax[i] - ys[i] for i in range(n_p)]
    norm_r = mat.norm(r)
    print("||Ax-b||={:.4g}".format(norm_r))
    pause()

def run():
    # Un solo worker: se corre y el script corta (scroll ^ para revisar).
    mmcc()
