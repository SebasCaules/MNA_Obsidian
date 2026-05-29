# Transformada de Fourier continua: pares estandar + numerica
import math
from io_util import (clr, pause, ask_int, ask_float, step, menu_pick)

PI = math.pi

def integrate(f_re, f_im, a, b, n=400):
    """Integra f = f_re + i f_im en [a,b] via Simpson."""
    if n % 2:
        n += 1
    h = (b - a) / n
    sr = f_re(a) + f_re(b)
    si = f_im(a) + f_im(b)
    for i in range(1, n):
        x = a + i * h
        w = 4 if i % 2 else 2
        sr += w * f_re(x)
        si += w * f_im(x)
    return (sr * h / 3.0, si * h / 3.0)

def tf_pulso_rect():
    a = ask_float("a(|t|<a/2):")
    w_max = ask_float("w_max:")
    K = 12
    step("F=a sinc(wa/2)")
    print(" w   |F(w)|")
    for k in range(K + 1):
        w = -w_max + 2 * w_max * k / K
        if abs(w) < 1e-10:
            Fw = a
        else:
            Fw = 2 * math.sin(w * a / 2) / w
        print("{:5.2f} {:.4g}".format(w, abs(Fw)))
        if (k + 1) % 6 == 0:
            pause()
    pause()

def tf_triangulo():
    n = ask_float("n([-n,n]):")
    w_max = ask_float("w_max:")
    K = 12
    step("F=sinc^2(wn/2)")
    print(" w    F(w)")
    for k in range(K + 1):
        w = -w_max + 2 * w_max * k / K
        if abs(w) < 1e-10:
            Fw = 1.0
        else:
            arg = w * n / 2
            Fw = (math.sin(arg) / arg) ** 2
        print("{:5.2f} {:.4g}".format(w, Fw))
        if (k + 1) % 6 == 0:
            pause()
    pause()

def tf_exp_decay():
    a = ask_float("a(>0):")
    w_max = ask_float("w_max:")
    K = 12
    step("F=1/(a+iw)")
    print(" w   |F|  arg")
    for k in range(K + 1):
        w = -w_max + 2 * w_max * k / K
        mod = 1.0 / (a * a + w * w) ** 0.5
        ph = -math.atan2(w, a)
        print("{:5.2f} {:.3g} {:.2g}".format(w, mod, ph))
        if (k + 1) % 6 == 0:
            pause()
    pause()

def tf_numerica():
    # integra x(t) e^{-iwt} numericamente
    print("Polin. en [a,b]")
    print("c0+c1 t+c2 t^2..")
    deg = ask_int("grado(0-3):")
    coefs = []
    for d in range(deg + 1):
        coefs.append(ask_float("c" + str(d) + ":"))
    a = ask_float("a inf:")
    b = ask_float("b sup:")
    w_max = ask_float("w_max:")
    def p(t):
        s = 0.0
        for d in range(len(coefs)):
            s += coefs[d] * (t ** d)
        return s
    K = 10
    step("F(w) grilla")
    print(" w   Re   Im   |F|")
    for k in range(K + 1):
        w = -w_max + 2 * w_max * k / K
        Fr, Fi = integrate(lambda t: p(t) * math.cos(-w * t),
                           lambda t: p(t) * math.sin(-w * t),
                           a, b)
        mod = (Fr * Fr + Fi * Fi) ** 0.5
        print("{:4.1f}".format(w))
        print(" {:.3g}".format(Fr))
        print(" {:.3g}".format(Fi))
        print(" |{:.3g}|".format(mod))
        pause()
    pause()

def run():
    while True:
        clr()
        op = menu_pick([
            "Rect (sinc)",
            "Tri (sinc^2)",
            "Exp -at u(t)",
            "Polin. num.",
            "Volver",
        ], "Op")
        if op == 0:
            tf_pulso_rect()
        elif op == 1:
            tf_triangulo()
        elif op == 2:
            tf_exp_decay()
        elif op == 3:
            tf_numerica()
        else:
            break
