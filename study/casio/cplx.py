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
    print("z = a + i*b")
    a = ask_float("a: ")
    b = ask_float("b: ")
    rho = (a * a + b * b) ** 0.5
    th = arg_pi(a, b)
    step("Modulo y argumento")
    print("rho = {:.6g}".format(rho))
    print("theta = {:.6g}".format(th))
    print("       = {:.4f} pi".format(th / PI))
    print("z = {:.4g} * e^(i*{:.4g})".format(rho, th))
    pause()

def pol_to_bin():
    print("z = rho * e^(i*th)")
    rho = ask_float("rho: ")
    th = ask_float("theta (rad): ")
    a = rho * math.cos(th)
    b = rho * math.sin(th)
    step("Forma binomica")
    print("z = {:.6g} + i*{:.6g}".format(a, b))
    pause()

def roots():
    print("Raices n-esimas de z")
    a = ask_float("Re(z): ")
    b = ask_float("Im(z): ")
    n = ask_int("n: ")
    rho = (a * a + b * b) ** 0.5
    th = arg_pi(a, b)
    rn = rho ** (1.0 / n)
    step("rho^(1/n) = {:.6g}".format(rn))
    print("theta base = {:.6g}".format(th))
    for k in range(n):
        ak = (th + 2 * PI * k) / n
        wa = rn * math.cos(ak)
        wb = rn * math.sin(ak)
        print("w{} = {:.4g} + i*{:.4g}".format(k, wa, wb))
        print("   arg = {:.4g} pi".format(ak / PI))
    pause()

def power():
    print("z^n con z = a+ib")
    a = ask_float("a: ")
    b = ask_float("b: ")
    n = ask_int("n: ")
    rho = (a * a + b * b) ** 0.5
    th = arg_pi(a, b)
    step("z^n = rho^n e^(i n theta)")
    rn = rho ** n
    an = n * th
    wa = rn * math.cos(an)
    wb = rn * math.sin(an)
    print("|z^n| = {:.6g}".format(rn))
    print("arg = {:.6g}".format(an))
    print("z^n = {:.6g} + i*{:.6g}".format(wa, wb))
    pause()

def run():
    while True:
        clr()
        print("== Complejos ==")
        op = menu_pick([
            "Binomica -> polar",
            "Polar -> binomica",
            "Raices n-esimas",
            "Potencia z^n",
            "Volver",
        ], "Op")
        if op == 0:
            bin_to_pol()
        elif op == 1:
            pol_to_bin()
        elif op == 2:
            roots()
        elif op == 3:
            power()
        else:
            break
