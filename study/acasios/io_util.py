# IO util - entrada/salida para Casio fx-CG50 / 9750GIII
# Display real medido: ~19 chars de ancho, 6-7 filas visibles.
# Estrategia: cada bloque cabe en <=6 lineas; lo largo va por chunks con pause().

LW = 19  # ancho visible

def clr():
    # Empuja la pantalla previa con 7 saltos (lineas visibles).
    for _ in range(7):
        print()

def pause(msg="[Enter]"):
    try:
        input(msg)
    except Exception:
        pass

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
        if multi and k < len(chunks) - 1:
            try:
                input("+")  # pausa entre chunks
            except Exception:
                pass

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
    # title se ignora para ahorrar 1 linea en la pantalla del Casio.
    # Hint en el prompt, no en linea aparte.
    for i in range(len(options)):
        print("{:2d}){}".format(i + 1, options[i]))
    while True:
        n = ask_int("Op:")
        if 1 <= n <= len(options):
            return n - 1
        print("?")
