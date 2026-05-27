# Series de Fourier: coeficientes a_n, b_n, c_n con integracion numerica
import math
from io_util import (clr, pause, ask_int, ask_float, step, menu_pick)

PI = math.pi

# Templates de funciones por tramos
TEMPLATES = [
    ("x(t) = t en (-pi, pi), T=2pi", lambda t: t, -PI, PI),
    ("x(t) = t^2 en (-pi, pi)", lambda t: t * t, -PI, PI),
    ("x(t) = t en (0, 2pi)", lambda t: t, 0.0, 2 * PI),
    ("x(t) = t^2 en (0, 2pi)", lambda t: t * t, 0.0, 2 * PI),
    ("x(t) = |t| en (-pi, pi)", lambda t: abs(t), -PI, PI),
    ("x(t) = 1 si t>0 sino -1, (-pi,pi)",
     lambda t: 1.0 if t > 0 else -1.0, -PI, PI),
    ("x(t) = e^t en (-pi, pi)", lambda t: math.exp(t), -PI, PI),
    ("x(t) = 1-t en (0,1), T=1",
     lambda t: 1.0 - t, 0.0, 1.0),
    ("x(t) = t-[t], T=1 (en [0,1])",
     lambda t: t - math.floor(t), 0.0, 1.0),
]

def integrate(f, a, b, n=400):
    """Simpson compuesta."""
    if n % 2:
        n += 1
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        x = a + i * h
        s += (4 if i % 2 else 2) * f(x)
    return s * h / 3.0

def serie_trig():
    print("Templates:")
    for i, (nm, _, _, _) in enumerate(TEMPLATES):
        print("{}) {}".format(i + 1, nm))
    sel = ask_int("> ") - 1
    nm, f, a, b = TEMPLATES[sel]
    T = b - a
    w0 = 2 * PI / T
    print("T =", T, "w0 =", w0)
    N = ask_int("# armonicos: ")
    step("Coeficientes")
    a0 = (2 / T) * integrate(f, a, b)
    print("a0 = {:.6g}  (a0/2 = {:.6g})".format(a0, a0 / 2))
    for n in range(1, N + 1):
        an = (2 / T) * integrate(lambda t: f(t) * math.cos(n * w0 * t), a, b)
        bn = (2 / T) * integrate(lambda t: f(t) * math.sin(n * w0 * t), a, b)
        print("n={}: a={:.6g} b={:.6g}".format(n, an, bn))
        if n % 4 == 0:
            pause()
    pause()

def coef_exp():
    print("Templates:")
    for i, (nm, _, _, _) in enumerate(TEMPLATES):
        print("{}) {}".format(i + 1, nm))
    sel = ask_int("> ") - 1
    nm, f, a, b = TEMPLATES[sel]
    T = b - a
    w0 = 2 * PI / T
    N = ask_int("|n| max: ")
    step("c_n (parte real / imag)")
    for n in range(-N, N + 1):
        cr = (1 / T) * integrate(lambda t: f(t) * math.cos(-n * w0 * t), a, b)
        ci = (1 / T) * integrate(lambda t: f(t) * math.sin(-n * w0 * t), a, b)
        mod = (cr * cr + ci * ci) ** 0.5
        print("c{} = {:.5g} + i {:.5g}  |c|={:.5g}".format(n, cr, ci, mod))
        if (n - (-N)) % 5 == 4:
            pause()
    pause()

def convergencia():
    print("Templates:")
    for i, (nm, _, _, _) in enumerate(TEMPLATES):
        print("{}) {}".format(i + 1, nm))
    sel = ask_int("> ") - 1
    nm, f, a, b = TEMPLATES[sel]
    T = b - a
    w0 = 2 * PI / T
    t0 = ask_float("t0: ")
    eps = 1e-4
    fp = f(t0 + eps)
    fm = f(t0 - eps)
    ft = (fp + fm) / 2
    print("x(t0+) =", fp)
    print("x(t0-) =", fm)
    print("Promedio (= valor SF) =", ft)
    N = ask_int("# armonicos suma: ")
    a0 = (2 / T) * integrate(f, a, b)
    s = a0 / 2
    for n in range(1, N + 1):
        an = (2 / T) * integrate(lambda t: f(t) * math.cos(n * w0 * t), a, b)
        bn = (2 / T) * integrate(lambda t: f(t) * math.sin(n * w0 * t), a, b)
        s += an * math.cos(n * w0 * t0) + bn * math.sin(n * w0 * t0)
    print("S_N(t0) =", s)
    pause()

def run():
    while True:
        clr()
        print("== Series Fourier ==")
        op = menu_pick([
            "Coef trigonom a_n b_n",
            "Coef exponencial c_n",
            "Convergencia en t0",
            "Volver",
        ], "Op")
        if op == 0:
            serie_trig()
        elif op == 1:
            coef_exp()
        elif op == 2:
            convergencia()
        else:
            break
