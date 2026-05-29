# MNA - Menu principal
# Casio fx-CG50 / fx-9750GIII (MicroPython 1.9.4)
# Display real: ~19 cols x 6-7 filas. Menu paginado en 2 pags de 6.
from io_util import pause, clr

MENU = [
    ("TL n/im/ai",   "tl"),
    ("Diagonaliz.",  "diag"),
    ("Cb base",      "cb"),
    ("LU PA=LU",     "lu"),
    ("QR Gram-Sch",  "qr"),
    ("SVD",          "svd"),
    ("A+ pseudoinv", "pinv"),
    ("MMCC",         "lsq"),
    ("Complejos",    "cplx"),
    ("Fourier ser",  "fs"),
    ("Fourier tr",   "tf"),
    ("EDP dif.fin",  "edp"),
]

PER_PAGE = 5  # 5 items + 1 prompt = 6 lineas. Cabe en displays de 6-7 filas.

def menu():
    page = 0
    pages = (len(MENU) + PER_PAGE - 1) // PER_PAGE
    while True:
        clr()
        start = page * PER_PAGE
        end = min(start + PER_PAGE, len(MENU))
        for i in range(start, end):
            print("{:2d}){}".format(i + 1, MENU[i][0]))
        # Hint embebido en el prompt (no usa una linea extra)
        if pages > 1:
            prompt = "Op(0=fin n=pg{}):".format(((page + 1) % pages) + 1)
        else:
            prompt = "Op(0=fin):"
        try:
            s = input(prompt).strip().lower()
        except Exception:
            continue
        if s == "n" or s == "":
            page = (page + 1) % pages
            continue
        try:
            n = int(s)
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
