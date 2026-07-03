# Series de Fourier: coeficientes a_n, b_n, c_n con integracion numerica
import math
from io_util import (clr, pause, ask_int, ask_float, step, menu_pick)

PI = math.pi

# Templates con nombres cortos (<=19 chars con prefijo "N)")
TEMPLATES = [
    ("t en(-pi,pi)", lambda t: t, -PI, PI),
    ("t^2 en(-pi,pi)", lambda t: t * t, -PI, PI),
    ("t en(0,2pi)", lambda t: t, 0.0, 2 * PI),
    ("t^2 en(0,2pi)", lambda t: t * t, 0.0, 2 * PI),
    ("|t| en(-pi,pi)", lambda t: abs(t), -PI, PI),
    ("sgn(t)(-pi,pi)", lambda t: 1.0 if t > 0 else -1.0, -PI, PI),
    ("e^t en(-pi,pi)", lambda t: math.exp(t), -PI, PI),
    ("1-t en(0,1)", lambda t: 1.0 - t, 0.0, 1.0),
    ("t-[t] en(0,1)", lambda t: t - math.floor(t), 0.0, 1.0),
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

def _pick_template():
    print("Templates:")
    for i in range(len(TEMPLATES)):
        print("{}){}".format(i + 1, TEMPLATES[i][0]))
        if (i + 1) % 5 == 0:
            pause()
    return ask_int(">") - 1

def serie_trig():
    sel = _pick_template()
    nm, f, a, b = TEMPLATES[sel]
    T = b - a
    w0 = 2 * PI / T
    print("T={:.4g}".format(T))
    print("w0={:.4g}".format(w0))
    N = ask_int("#arm:")
    step("Coefs")
    a0 = (2 / T) * integrate(f, a, b)
    print("a0={:.4g}".format(a0))
    # cte = a0/2 = (1/T)int f = valor medio = el TERMINO CONSTANTE de la serie.
    print("=>cte={:.4g}".format(a0 / 2))
    pause()
    for n in range(1, N + 1):
        an = (2 / T) * integrate(lambda t: f(t) * math.cos(n * w0 * t), a, b)
        bn = (2 / T) * integrate(lambda t: f(t) * math.sin(n * w0 * t), a, b)
        print("n={}".format(n))
        print(" a={:.4g}".format(an))
        print(" b={:.4g}".format(bn))
        if n % 2 == 0:
            pause()
    pause()

def coef_exp():
    sel = _pick_template()
    nm, f, a, b = TEMPLATES[sel]
    T = b - a
    w0 = 2 * PI / T
    N = ask_int("|n|max:")
    step("c_n (Re,Im)")
    for n in range(-N, N + 1):
        cr = (1 / T) * integrate(lambda t: f(t) * math.cos(-n * w0 * t), a, b)
        ci = (1 / T) * integrate(lambda t: f(t) * math.sin(-n * w0 * t), a, b)
        mod = (cr * cr + ci * ci) ** 0.5
        print("c{}={:.4g}".format(n, cr))
        print(" +i{:.4g}".format(ci))
        print(" |c|={:.4g}".format(mod))
        if (n - (-N) + 1) % 2 == 0:
            pause()
    pause()

def convergencia():
    sel = _pick_template()
    nm, f, a, b = TEMPLATES[sel]
    T = b - a
    w0 = 2 * PI / T
    t0 = ask_float("t0:")
    eps = 1e-4
    # Periodizamos las muestras a [a,b) para detectar bien el salto en los
    # bordes del periodo (antes f(t0-eps) se salia del dominio y daba mal).
    fp = f(a + ((t0 + eps - a) % T))
    fm = f(a + ((t0 - eps - a) % T))
    ft = (fp + fm) / 2
    print("x(t0+)={:.4g}".format(fp))
    print("x(t0-)={:.4g}".format(fm))
    print("prom={:.4g}".format(ft))
    pause()
    N = ask_int("#arm suma:")
    a0 = (2 / T) * integrate(f, a, b)
    s = a0 / 2
    for n in range(1, N + 1):
        an = (2 / T) * integrate(lambda t: f(t) * math.cos(n * w0 * t), a, b)
        bn = (2 / T) * integrate(lambda t: f(t) * math.sin(n * w0 * t), a, b)
        s += an * math.cos(n * w0 * t0) + bn * math.sin(n * w0 * t0)
    print("S_N(t0)={:.4g}".format(s))
    pause()

def run():
    # Elige variante (input al principio) y corre una vez; despues corta.
    op = menu_pick([
        "Coef a_n b_n",
        "Coef c_n exp",
        "Conv en t0",
    ])
    if op == 0:
        serie_trig()
    elif op == 1:
        coef_exp()
    elif op == 2:
        convergencia()
