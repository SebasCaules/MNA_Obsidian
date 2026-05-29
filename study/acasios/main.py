# MNA - Menu principal
# Casio Graph 90+E (= fx-CG50), app PYTHON, MicroPython 1.9.4.
# Pantalla: ~21 cols x ~8 filas. Menu paginado (6 por pagina).
#
# FLUJO: elegis 1 ejercicio -> cargas datos -> vuelca toda la salida -> CORTA.
# Al cortar el script ya podes scrollear para arriba y revisar los pasos.
# Para hacer otro ejercicio: volver a correr main.
from io_util import clr, LW

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

PER_PAGE = 6  # 6 items + 1 prompt = 7 lineas. Entra en la shell.


def menu():
    page = 0
    pages = (len(MENU) + PER_PAGE - 1) // PER_PAGE
    while True:
        clr()
        start = page * PER_PAGE
        end = min(start + PER_PAGE, len(MENU))
        for i in range(start, end):
            print("{:2d}){}".format(i + 1, MENU[i][0]))
        # Hint embebido en el prompt (no usa una linea extra).
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
            return
        if 1 <= n <= len(MENU):
            name, mod_name = MENU[n - 1]
            # Banner: al scrollear arriba se ve que ejercicio fue.
            clr()
            print(name)
            try:
                mod = __import__(mod_name)
                mod.run()
            except Exception as e:
                print("ERR:", e)
            # Marca de fin: el script termina aca -> scrollear ^ para revisar.
            print("=" * LW)
            print("FIN - scroll ^ p/ver")
            return  # CORTA. No vuelve al menu (asi no queda input trabando).


menu()
