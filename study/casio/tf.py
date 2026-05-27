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
    a = ask_float("ancho a (pulso |t|<a/2): ")
    w_max = ask_float("w_max (graficar): ")
    K = 20
    step("F(w) = a sinc(wa/2)")
    print(" w     |F(w)|")
    for k in range(K + 1):
        w = -w_max + 2 * w_max * k / K
        if abs(w) < 1e-10:
            Fw = a
        else:
            Fw = 2 * math.sin(w * a / 2) / w
        print("{:6.3f}  {:.5g}".format(w, abs(Fw)))
    pause()

def tf_triangulo():
    n = ask_float("n (Lambda_n soporte [-n,n]): ")
    w_max = ask_float("w_max: ")
    K = 20
    step("F(w) = sinc^2(wn/2)")
    print(" w     F(w)")
    for k in range(K + 1):
        w = -w_max + 2 * w_max * k / K
        if abs(w) < 1e-10:
            Fw = 1.0
        else:
            arg = w * n / 2
            Fw = (math.sin(arg) / arg) ** 2
        print("{:6.3f}  {:.5g}".format(w, Fw))
    pause()

def tf_exp_decay():
    a = ask_float("a (a>0): ")
    w_max = ask_float("w_max: ")
    K = 20
    step("F(w) = 1/(a + iw); muestro |F|")
    print(" w     |F(w)|   arg(F)")
    for k in range(K + 1):
        w = -w_max + 2 * w_max * k / K
        mod = 1.0 / (a * a + w * w) ** 0.5
        ph = -math.atan2(w, a)
        print("{:6.3f}  {:.4g}  {:.3g}".format(w, mod, ph))
    pause()

def tf_numerica():
    # integra x(t) e^{-iwt} numericamente
    print("Pulso polinomico en [a,b]")
    print("Coef del polinomio: c0 + c1 t + c2 t^2 + ... (max 3)")
    deg = ask_int("grado (0..3): ")
    coefs = []
    for d in range(deg + 1):
        coefs.append(ask_float("c" + str(d) + ": "))
    a = ask_float("a (limite inf): ")
    b = ask_float("b (limite sup): ")
    w_max = ask_float("w_max: ")
    def p(t):
        s = 0.0
        for d, c in enumerate(coefs):
            s += c * (t ** d)
        return s
    K = 14
    step("F(w) en grilla")
    print(" w     Re(F)  Im(F)  |F|")
    for k in range(K + 1):
        w = -w_max + 2 * w_max * k / K
        Fr, Fi = integrate(lambda t: p(t) * math.cos(-w * t),
                           lambda t: p(t) * math.sin(-w * t),
                           a, b)
        mod = (Fr * Fr + Fi * Fi) ** 0.5
        print("{:5.2f} {:6.3g} {:6.3g} {:.4g}".format(w, Fr, Fi, mod))
    pause()

def run():
    while True:
        clr()
        print("== Transf Fourier ==")
        op = menu_pick([
            "Pulso rect (sinc)",
            "Triangulo (sinc^2)",
            "Exp e^{-at} u(t)",
            "Pulso polinomico num.",
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
