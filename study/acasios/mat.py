# Operaciones matriciales basicas - sin numpy
# Convencion: matriz = lista de filas (listas de floats)

def shape(A):
    return (len(A), len(A[0]) if A else 0)

def zeros(n, m):
    return [[0.0] * m for _ in range(n)]

def eye(n):
    I = zeros(n, n)
    for i in range(n):
        I[i][i] = 1.0
    return I

def copy(A):
    return [row[:] for row in A]

def transpose(A):
    n, m = shape(A)
    T = zeros(m, n)
    for i in range(n):
        for j in range(m):
            T[j][i] = A[i][j]
    return T

def matmul(A, B):
    nA, mA = shape(A)
    nB, mB = shape(B)
    if mA != nB:
        raise ValueError("matmul dim")
    C = zeros(nA, mB)
    for i in range(nA):
        for j in range(mB):
            s = 0.0
            for k in range(mA):
                s += A[i][k] * B[k][j]
            C[i][j] = s
    return C

def matvec(A, v):
    n, m = shape(A)
    if len(v) != m:
        raise ValueError("matvec dim")
    out = [0.0] * n
    for i in range(n):
        s = 0.0
        for j in range(m):
            s += A[i][j] * v[j]
        out[i] = s
    return out

def scale(A, c):
    return [[c * x for x in row] for row in A]

def add(A, B):
    n, m = shape(A)
    return [[A[i][j] + B[i][j] for j in range(m)] for i in range(n)]

def sub(A, B):
    n, m = shape(A)
    return [[A[i][j] - B[i][j] for j in range(m)] for i in range(n)]

def dot(u, v):
    s = 0.0
    for i in range(len(u)):
        s += u[i] * v[i]
    return s

def norm(v):
    return dot(v, v) ** 0.5

def vscale(v, c):
    return [c * x for x in v]

def vsub(u, v):
    return [u[i] - v[i] for i in range(len(u))]

def vadd(u, v):
    return [u[i] + v[i] for i in range(len(u))]

def normalize(v):
    n = norm(v)
    if n < 1e-12:
        return [0.0] * len(v)
    return [x / n for x in v]

def gauss_jordan(A, b=None, eps=1e-10):
    """Reduce [A|b] a forma escalonada reducida. Devuelve (R, b_red, pivots)."""
    n, m = shape(A)
    R = copy(A)
    if b is None:
        bb = [[0.0] for _ in range(n)]
    else:
        # b puede ser vector o matriz
        if isinstance(b[0], list):
            bb = copy(b)
        else:
            bb = [[bi] for bi in b]
    bcols = len(bb[0])
    pivots = []
    row = 0
    for col in range(m):
        if row >= n:
            break
        # buscar pivot
        pivrow = -1
        pivval = eps
        for k in range(row, n):
            if abs(R[k][col]) > pivval:
                pivval = abs(R[k][col])
                pivrow = k
        if pivrow < 0:
            continue
        # swap
        if pivrow != row:
            R[row], R[pivrow] = R[pivrow], R[row]
            bb[row], bb[pivrow] = bb[pivrow], bb[row]
        # normalizar fila
        pv = R[row][col]
        for j in range(m):
            R[row][j] /= pv
        for j in range(bcols):
            bb[row][j] /= pv
        # eliminar otras filas
        for k in range(n):
            if k == row:
                continue
            factor = R[k][col]
            if abs(factor) < eps:
                continue
            for j in range(m):
                R[k][j] -= factor * R[row][j]
            for j in range(bcols):
                bb[k][j] -= factor * bb[row][j]
        pivots.append((row, col))
        row += 1
    return R, bb, pivots

def solve(A, b, eps=1e-10):
    """Resuelve Ax=b. Devuelve (x_p, null_basis). Si incompatible: (None, None)."""
    n, m = shape(A)
    R, bb, pivots = gauss_jordan(A, b, eps)
    # set() no existe en MicroPython 1.9.4 (Casio) - uso lista
    pivot_cols = [c for _, c in pivots]
    for i in range(n):
        all_zero = all(abs(R[i][j]) < eps for j in range(m))
        if all_zero and abs(bb[i][0]) > eps:
            return None, None
    x_p = [0.0] * m
    for r_idx, c_idx in pivots:
        x_p[c_idx] = bb[r_idx][0]
    free_cols = [c for c in range(m) if c not in pivot_cols]
    null_basis = []
    for fc in free_cols:
        v = [0.0] * m
        v[fc] = 1.0
        for r_idx, c_idx in pivots:
            v[c_idx] = -R[r_idx][fc]
        null_basis.append(v)
    return x_p, null_basis

def inverse(A, eps=1e-10):
    n, m = shape(A)
    if n != m:
        raise ValueError("inverse: no cuadrada")
    I = eye(n)
    R, bb, pivots = gauss_jordan(A, I, eps)
    if len(pivots) < n:
        return None
    return bb

def det(A):
    n, m = shape(A)
    if n != m:
        raise ValueError("det: no cuadrada")
    M = copy(A)
    sign = 1.0
    for i in range(n):
        # pivot
        piv = i
        for k in range(i, n):
            if abs(M[k][i]) > abs(M[piv][i]):
                piv = k
        if abs(M[piv][i]) < 1e-12:
            return 0.0
        if piv != i:
            M[i], M[piv] = M[piv], M[i]
            sign = -sign
        for k in range(i + 1, n):
            factor = M[k][i] / M[i][i]
            for j in range(i, n):
                M[k][j] -= factor * M[i][j]
    d = sign
    for i in range(n):
        d *= M[i][i]
    return d

def rank(A, eps=1e-10):
    R, _, pivots = gauss_jordan(A, None, eps)
    return len(pivots)

def gram_schmidt(cols):
    """Aplica GS clasico a una lista de columnas (vectores). Devuelve (V, normas).
    V es la lista de vectores normalizados. normas[i] = ||u_i||."""
    V = []
    normas = []
    for a in cols:
        u = a[:]
        for v in V:
            c = dot(a, v)
            u = vsub(u, vscale(v, c))
        nu = norm(u)
        normas.append(nu)
        if nu < 1e-10:
            V.append([0.0] * len(a))
        else:
            V.append([x / nu for x in u])
    return V, normas
