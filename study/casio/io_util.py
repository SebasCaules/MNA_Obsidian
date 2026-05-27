# IO util - entrada/salida amigable para Casio fx-CG50
# Display 21x7. Entrada fila por fila.

def clr():
    # Limpia la pantalla con 8 newlines
    for _ in range(8):
        print()

def pause(msg="[Enter]"):
    try:
        input(msg)
    except Exception:
        pass

def ask_int(prompt="n: "):
    while True:
        s = input(prompt).strip()
        try:
            return int(s)
        except Exception:
            print("? entero")

def ask_float(prompt="x: "):
    while True:
        s = input(prompt).strip()
        try:
            return float(s)
        except Exception:
            print("? real")

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
            raise ValueError("?: " + tok)
    return out

def read_vec(n, prompt="v"):
    while True:
        s = input(prompt + " (" + str(n) + "): ")
        try:
            v = parse_csv(s)
            if len(v) != n:
                print("len?")
                continue
            return v
        except Exception as e:
            print(e)

def read_mat(rows, cols, prompt="A"):
    print(prompt + " " + str(rows) + "x" + str(cols) + ":")
    M = []
    for i in range(rows):
        v = read_vec(cols, "f" + str(i + 1))
        M.append(v)
    return M

def fmt_num(x, w=8, p=4):
    # Numero con p decimales, ancho w
    if abs(x) < 1e-12:
        x = 0.0
    s = "{:.{p}g}".format(x, p=p)
    return s

def show_mat(M, label="", per_row=4):
    # Muestra matriz fila por fila. per_row: max columnas por linea
    if label:
        print(label + ":")
    if not M:
        print("(vacia)")
        return
    rows = len(M)
    cols = len(M[0])
    for i in range(rows):
        if cols <= per_row:
            line = " ".join(fmt_num(M[i][j]) for j in range(cols))
            print(line)
        else:
            # particionar
            for k in range(0, cols, per_row):
                end = min(k + per_row, cols)
                line = "[c{}-{}] ".format(k + 1, end)
                line += " ".join(fmt_num(M[i][j]) for j in range(k, end))
                print(line)

def show_vec(v, label=""):
    if label:
        print(label + ":")
    print(" ".join(fmt_num(x) for x in v))

def step(title):
    # Imprime un titulo de paso y pausa
    print()
    print("-- " + title + " --")

def menu_pick(options, title="Opcion"):
    print(title + ":")
    for i, opt in enumerate(options):
        print("{:2d}) {}".format(i + 1, opt))
    while True:
        n = ask_int("> ")
        if 1 <= n <= len(options):
            return n - 1
        print("?")
