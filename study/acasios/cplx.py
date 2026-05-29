# Numeros complejos: polar<->binomica, raices, potencias
import math
from io_util import pause, ask_float, ask_int, menu_pick, step, clr

PI = math.pi

def arg_pi(a, b):
    """Argumento en [0, 2*pi)."""
    if b == 0:
        return 0.0 if a > 0 else PI
    if a == 0:
        return PI / 2 if b > 0 else 3 * PI / 2
    # cuadrante I
    if a > 0 and b > 0:
        return math.atan(b / a)
    if a < 0 and b > 0:
        return PI - math.atan(abs(b) / abs(a))
    if a < 0 and b < 0:
        return PI + math.atan(abs(b) / abs(a))
    # a > 0, b < 0
    return 2 * PI - math.atan(abs(b) / abs(a))

def bin_to_pol():
    print("z=a+i*b")
    a = ask_float("a:")
    b = ask_float("b:")
    rho = (a * a + b * b) ** 0.5
    th = arg_pi(a, b)
    step("modulo,arg")
    print("rho={:.6g}".format(rho))
    print("th={:.6g}".format(th))
    print("  ={:.4f}pi".format(th / PI))
    print("z={:.4g}e^(i*{:.4g})".format(rho, th))
    pause()

def pol_to_bin():
    print("z=rho*e^(i th)")
    rho = ask_float("rho:")
    th = ask_float("th(rad):")
    a = rho * math.cos(th)
    b = rho * math.sin(th)
    step("Binomica")
    print("z={:.6g}".format(a))
    print(" +i*{:.6g}".format(b))
    pause()

def roots():
    print("Raices n-es z")
    a = ask_float("Re(z):")
    b = ask_float("Im(z):")
    n = ask_int("n:")
    rho = (a * a + b * b) ** 0.5
    th = arg_pi(a, b)
    rn = rho ** (1.0 / n)
    step("rho^1/n={:.4g}".format(rn))
    print("th base={:.4g}".format(th))
    for k in range(n):
        ak = (th + 2 * PI * k) / n
        wa = rn * math.cos(ak)
        wb = rn * math.sin(ak)
        print("w{}={:.4g}".format(k, wa))
        print(" +i*{:.4g}".format(wb))
        print(" arg={:.3g}pi".format(ak / PI))
        if (k + 1) % 2 == 0:
            pause()
    pause()

def power():
    print("z^n, z=a+ib")
    a = ask_float("a:")
    b = ask_float("b:")
    n = ask_int("n:")
    rho = (a * a + b * b) ** 0.5
    th = arg_pi(a, b)
    step("z^n=rho^n e^in0")
    rn = rho ** n
    an = n * th
    wa = rn * math.cos(an)
    wb = rn * math.sin(an)
    print("|z^n|={:.6g}".format(rn))
    print("arg={:.6g}".format(an))
    print("z^n={:.4g}".format(wa))
    print(" +i*{:.4g}".format(wb))
    pause()

def run():
    # Elige variante (input al principio) y corre una vez; despues corta.
    op = menu_pick([
        "Bin->polar",
        "Polar->bin",
        "Raices n-esim",
        "Pot z^n",
    ])
    if op == 0:
        bin_to_pol()
    elif op == 1:
        pol_to_bin()
    elif op == 2:
        roots()
    elif op == 3:
        power()
