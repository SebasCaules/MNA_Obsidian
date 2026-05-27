# MNA - Menu principal
# Casio fx-CG50 / fx-9750GIII MicroPython
# Display: 21 cols x 7 rows
from io_util import pause, clr, ask_int

MENU = [
    ("TL nuc/img/antiim", "tl"),
    ("Diagonalizar",      "diag"),
    ("Cambio de base",    "cb"),
    ("LU / PLU",          "lu"),
    ("QR (Gram-Schmidt)", "qr"),
    ("SVD",               "svd"),
    ("Pseudoinversa",     "pinv"),
    ("Cuad. minimos",     "lsq"),
    ("Complejos",         "cplx"),
    ("Series Fourier",    "fs"),
    ("Transf. Fourier",   "tf"),
    ("EDP dif. finitas",  "edp"),
]

def menu():
    while True:
        clr()
        print("=== MNA ITBA ===")
        for i, (name, _) in enumerate(MENU):
            print("{:2d}) {}".format(i + 1, name))
        print(" 0) Salir")
        try:
            n = ask_int("Opcion: ")
        except Exception:
            continue
        if n == 0:
            break
        if 1 <= n <= len(MENU):
            mod_name = MENU[n - 1][1]
            try:
                mod = __import__(mod_name)
                mod.run()
            except Exception as e:
                print("ERR:", e)
                pause()

menu()
