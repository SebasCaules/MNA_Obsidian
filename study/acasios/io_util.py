# IO util - Casio Graph 90+E (= fx-CG50), app PYTHON, MicroPython 1.9.4
#
# Pantalla fisica: LCD color 396 x 224 px.
# Shell de Python (fuente grande): ~21 caracteres de ancho x ~8 lineas.
#   - El editor muestra 7 lineas x 21 chars; la shell ronda lo mismo.
#   - No hay wrap horizontal "lindo": si una linea pasa de 21 se corta feo,
#     por eso TODO se arma para entrar en <=21 columnas.
#
# REGLA DE ORO DEL SCROLL (lo importante de este archivo):
#   En la shell solo se puede scrollear el historial CUANDO el script TERMINO.
#   Si hay un input() pendiente, la pantalla queda trabada en esa linea y no
#   se puede mover. Por eso la estrategia es:
#       1) pedir TODOS los datos primero (inputs al principio),
#       2) volcar TODA la salida de una (sin pausas en el medio),
#       3) terminar el script -> ahi recien se scrollea para arriba.
#   Consecuencia: pause() es un NO-OP a proposito (no traba el scroll), y main
#   corre UN ejercicio y corta.

LW = 21   # ancho visible en chars
ROWS = 8  # lineas visibles aprox (no se usa para paginar: se scrollea al final)


def clr():
    # Separador visual entre secciones (ayuda a ubicarse al scrollear arriba).
    # NO limpia de verdad: la shell ya arranca limpia al correr el script.
    print("=" * LW)


def pause(msg="[Enter]"):
    # NO-OP intencional. Antes pausaba con input() entre pantallas, pero eso
    # trababa el scroll. Ahora la salida se vuelca entera y se scrollea al
    # terminar el script. Se deja la funcion para no tocar las ~80 llamadas
    # repartidas en los modulos.
    return


def ask_int(prompt="n:"):
    while True:
        s = input(prompt).strip()
        try:
            return int(s)
        except Exception:
            print("?int")


def ask_float(prompt="x:"):
    while True:
        s = input(prompt).strip()
        try:
            return float(s)
        except Exception:
            print("?real")


def parse_csv(s):
    # "1, 2.5, -3" -> [1.0, 2.5, -3.0]
    out = []
    for tok in s.replace(";", ",").split(","):
        tok = tok.strip()
        if tok == "":
            continue
        try:
            out.append(float(tok))
        except Exception:
            raise ValueError("?:" + tok)
    return out


def read_vec(n, prompt="v"):
    while True:
        s = input(prompt + str(n) + ":")
        try:
            v = parse_csv(s)
            if len(v) != n:
                print("len?")
                continue
            return v
        except Exception as e:
            print(e)


def read_mat(rows, cols, prompt="A"):
    print(prompt + str(rows) + "x" + str(cols) + ":")
    M = []
    for i in range(rows):
        v = read_vec(cols, "f" + str(i + 1) + "/")
        M.append(v)
    return M


def fmt_num(x, p=4):
    # Numero con p cifras significativas (formato g).
    # MicroPython 1.9.4 no soporta "{:.{p}g}" anidado.
    if abs(x) < 1e-12:
        x = 0.0
    fmt = "{:." + str(p) + "g}"
    return fmt.format(x)


def _rjust(s, w):
    # MicroPython 1.9.4 no tiene str.rjust
    pad = w - len(s)
    if pad <= 0:
        return s
    return " " * pad + s


def _col_widths(cells, rows, cols):
    widths = [0] * cols
    for j in range(cols):
        w = 0
        for i in range(rows):
            L = len(cells[i][j])
            if L > w:
                w = L
        widths[j] = w
    return widths


def _chunk_cols(widths, lw):
    # Particiona las columnas en bloques cuyo ancho total quepa en lw.
    chunks = []
    cols = len(widths)
    start = 0
    while start < cols:
        end = start
        used = 0
        while end < cols:
            extra = widths[end] + (1 if end > start else 0)
            if used + extra > lw:
                break
            used += extra
            end += 1
        if end == start:
            end = start + 1  # forzar al menos una columna
        chunks.append((start, end))
        start = end
    return chunks


def show_mat(M, label="", lw=LW):
    # Muestra matriz, partiendo columnas si no entran en lw.
    # Los bloques de columnas se imprimen uno abajo del otro (sin pausas):
    # se scrollea al final para verlos todos.
    if label:
        print(label + ":")
    if not M:
        print("(vacia)")
        return
    rows = len(M)
    cols = len(M[0])
    cells = [[fmt_num(M[i][j]) for j in range(cols)] for i in range(rows)]
    widths = _col_widths(cells, rows, cols)
    chunks = _chunk_cols(widths, lw)
    multi = len(chunks) > 1
    for k in range(len(chunks)):
        cs = chunks[k][0]
        ce = chunks[k][1]
        if multi:
            print("c{}-{}:".format(cs + 1, ce))
        for i in range(rows):
            parts = []
            for j in range(cs, ce):
                parts.append(_rjust(cells[i][j], widths[j]))
            print(" ".join(parts))


def show_vec(v, label="", lw=LW):
    if label:
        print(label + ":")
    if not v:
        print("()")
        return
    cells = [fmt_num(x) for x in v]
    line = ""
    for c in cells:
        nxt = (line + " " + c) if line else c
        if len(nxt) > lw and line:
            print(line)
            line = c
        else:
            line = nxt
    if line:
        print(line)


def step(title):
    # Titulo de paso. Si pasa de lw, se trunca con "..."
    if len(title) > LW - 4:
        title = title[:LW - 7] + "..."
    print()
    print("-- " + title)


def menu_pick(options, title=""):
    # Eleccion de variante. Es un input AL PRINCIPIO (antes de imprimir nada),
    # asi que no molesta al scroll. title se ignora para ahorrar 1 linea.
    for i in range(len(options)):
        print("{:2d}){}".format(i + 1, options[i]))
    while True:
        n = ask_int("Op:")
        if 1 <= n <= len(options):
            return n - 1
        print("?")
