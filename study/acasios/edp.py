# EDPs: diferencias finitas implicitas (calor, onda, conveccion)
# Resuelve con algoritmo de Thomas (tridiagonal)
import math
from io_util import (clr, pause, ask_int, ask_float, step, menu_pick,
                     show_vec)

def thomas(a, b, c, d):
    """Resuelve sistema tridiagonal:
    a[i]*u[i-1] + b[i]*u[i] + c[i]*u[i+1] = d[i]   con a[0]=0, c[N-1]=0
    """
    n = len(d)
    cp = [0.0] * n
    dp = [0.0] * n
    cp[0] = c[0] / b[0]
    dp[0] = d[0] / b[0]
    for i in range(1, n):
        denom = b[i] - a[i] * cp[i - 1]
        cp[i] = c[i] / denom if i < n - 1 else 0.0
        dp[i] = (d[i] - a[i] * dp[i - 1]) / denom
    u = [0.0] * n
    u[n - 1] = dp[n - 1]
    for i in range(n - 2, -1, -1):
        u[i] = dp[i] - cp[i] * u[i + 1]
    return u

def edp_calor_dir():
    # u_t = u_xx, Dirichlet
    print("u_t=u_xx,x[0,L]")
    L = ask_float("L:")
    N = ask_int("nodos int:")
    dt = ask_float("dt:")
    K = ask_int("#pasos:")
    print("u(x,0):")
    print("1)sen(pi x/L)")
    print("2)cos(pi x/L)")
    print("3)x*(L-x)")
    print("4)exp(-x^2)")
    op = ask_int(">")
    h = L / (N + 1)
    r = dt / (h * h)
    print("h={:.4g}".format(h))
    print("r={:.4g}".format(r))
    # u_0, u_{N+1} bordes Dirichlet
    uL = ask_float("u(0,t):")
    uR = ask_float("u(L,t):")
    # condicion inicial en nodos internos
    u = []
    for i in range(1, N + 1):
        x = i * h
        if op == 1:
            u.append(math.sin(math.pi * x / L))
        elif op == 2:
            u.append(math.cos(math.pi * x / L))
        elif op == 3:
            u.append(x * (L - x))
        else:
            u.append(math.exp(-x * x))
    step("u^0")
    show_vec(u)
    pause()
    # avanzar
    for k in range(K):
        a = [0.0] + [-r] * (N - 1)
        b = [1.0 + 2 * r] * N
        c = [-r] * (N - 1) + [0.0]
        d = u[:]
        d[0] += r * uL
        d[N - 1] += r * uR
        u = thomas(a, b, c, d)
        if (k + 1) % max(1, K // 4) == 0:
            step("u^{} t={:.3f}".format(k + 1, (k + 1) * dt))
            show_vec(u)
            pause()
    step("Final")
    show_vec(u)
    pause()

def edp_onda():
    # u_tt = u_xx, esquema implicito 3 niveles, Dirichlet
    print("u_tt=u_xx Dir")
    print("u(0,t)=u(L,t)=0")
    L = ask_float("L:")
    N = ask_int("nodos int:")
    dt = ask_float("dt:")
    K = ask_int("#pasos:")
    print("u(x,0):")
    print("1)sen(pi x/L)")
    init = ask_int(">")
    h = L / (N + 1)
    r = (dt * dt) / (h * h)
    print("h={:.4g}".format(h))
    print("r={:.4g}".format(r))
    u_prev = []
    for i in range(1, N + 1):
        x = i * h
        if init == 1:
            u_prev.append(math.sin(math.pi * x / L))
        else:
            u_prev.append(0.0)
    # asumimos u_t(x,0) = 0 -> u^1 = u^0
    u_cur = u_prev[:]
    step("u^0")
    show_vec(u_cur)
    pause()
    for k in range(K):
        # (1+2r) u_i^{k+1} - r u_{i-1}^{k+1} - r u_{i+1}^{k+1}
        #   = 2 u_i^k - u_i^{k-1}
        a = [0.0] + [-r] * (N - 1)
        b = [1.0 + 2 * r] * N
        c = [-r] * (N - 1) + [0.0]
        d = [2 * u_cur[i] - u_prev[i] for i in range(N)]
        u_next = thomas(a, b, c, d)
        u_prev = u_cur
        u_cur = u_next
        if (k + 1) % max(1, K // 4) == 0:
            step("u^{}".format(k + 1))
            show_vec(u_cur)
            pause()
    step("Final")
    show_vec(u_cur)
    pause()

def edp_conveccion():
    # u_t + c u_x = nu u_xx, Dirichlet
    print("u_t+c u_x=nu u_xx")
    L = ask_float("L:")
    N = ask_int("nodos int:")
    dt = ask_float("dt:")
    K = ask_int("#pasos:")
    cc = ask_float("c vel:")
    nu = ask_float("nu dif:")
    uL = ask_float("u(0,t):")
    uR = ask_float("u(L,t):")
    h = L / (N + 1)
    rA = dt * cc / (2 * h)      # adveccion centrada
    rD = nu * dt / (h * h)      # difusion
    u = []
    for i in range(1, N + 1):
        x = i * h
        u.append(math.sin(math.pi * x / L))
    for k in range(K):
        a = [0.0] + [-rA - rD] * (N - 1)
        b = [1.0 + 2 * rD] * N
        c = [rA - rD] * (N - 1) + [0.0]
        d = u[:]
        d[0] -= (-rA - rD) * uL
        d[N - 1] -= (rA - rD) * uR
        u = thomas(a, b, c, d)
        if (k + 1) % max(1, K // 3) == 0:
            step("u^{}".format(k + 1))
            show_vec(u)
            pause()
    step("Final")
    show_vec(u)
    pause()

def run():
    while True:
        clr()
        op = menu_pick([
            "Calor Dir",
            "Onda 3 niv",
            "Conv-difus",
            "Volver",
        ], "Op")
        if op == 0:
            edp_calor_dir()
        elif op == 1:
            edp_onda()
        elif op == 2:
            edp_conveccion()
        else:
            break
