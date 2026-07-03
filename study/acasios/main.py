# MNA - Menu principal. Punto de entrada del set de scripts.
# Casio Graph 90+E (= fx-CG50), app PYTHON, MicroPython 1.9.4.
# Pantalla: ~21 cols x ~8 filas. Menu paginado (6 por pagina).
#
# FLUJO: elegis 1 ejercicio -> cargas datos -> vuelca toda la salida -> CORTA.
# Al cortar el script ya podes scrollear para arriba y revisar los pasos.
# Para hacer otro ejercicio: volver a correr main.
#
# IMPORTS: todos los .py (main.py + modulos) van JUNTOS en una misma carpeta,
# tanto en el repo como en la Casio. Asi el import directo anda sin tocar el
# path (la Casio no importa desde subcarpetas).
from io_util import clr, LW, ask_int, cap_start, cap_stop, cap_save

MENU = [
    ("TL n/im/ai/B", "tl"),
    ("Diagonaliz.",  "diag"),
    ("Param autovec","param"),
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


def ask_ej():
    # Numero de ejercicio del parcial (1-5). Define el nombre del .py de salida.
    while True:
        e = ask_int("ej(1-5):")
        if 1 <= e <= 5:
            return e
        print("1-5")


def menu(ej):
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
            mod = None
            try:
                mod = __import__(mod_name)
            except Exception as e:
                print("imp err:", e)
            if mod is not None:
                # Captura: duplica al buffer la salida de io_util + del modulo.
                cap_start(mod)
                try:
                    mod.run()
                except Exception as e:
                    print("ERR:", e)
                cap_stop(mod)
            # Marca de fin: el script termina aca -> scrollear ^ para revisar.
            print("=" * LW)
            print("FIN - scroll ^ p/ver")
            # Volcado a archivo afuera de la carpeta (para scrollear izq/der).
            ruta = cap_save(ej, name)
            if ruta:
                print("guardado: " + ruta)
            else:
                print("no guardo (sin FS?)")
            return  # CORTA. No vuelve al menu (asi no queda input trabando).


menu(ask_ej())
