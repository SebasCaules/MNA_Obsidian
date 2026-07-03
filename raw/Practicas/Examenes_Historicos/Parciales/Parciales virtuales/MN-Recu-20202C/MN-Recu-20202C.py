########################################################################################################################
# Métodos Numéricos(93.54) - 2do Cuatrimestre 2020  - Olivia De Vincenti - Legajo 60354
# Recuperatorio de parcial
########################################################################################################################

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

########################################################################################################################
# Implementación de ruku4
# edo: EDO. Si es de segundo orden, x'=x[0] y x=x[1]
# t0: Inicio del intervalo de tiempo
# tf: Fin del intervalo de tiempo
# h: Paso
# ci: Condiciones iniciales. IMPORTANTE: Si la EDO es de orden 2 x0[0]=x'(0) y x0[1]=x(0)
# Devuelve arreglo con los valores de t y x que representan la función buscada
# ----------------------------------------------------------------------------------------------------------------------
def ruku4(edo, t0, tf, h, ci):
  time = np.arange(t0, tf + h, h)
  x = np.zeros((len(time), len(ci)))
  x[0] = ci
  fvec = np.zeros((4, len(ci)))
  for i, t in enumerate(time[:-1]):
    fvec[0] = edo(t, x[i])
    fvec[1] = edo(t + h / 2, x[i] + h * fvec[0] / 2)
    fvec[2] = edo(t + h / 2, x[i] + h * fvec[1] / 2)
    fvec[3] = edo(t + h, x[i] + h * fvec[2])
    x[i + 1] = x[i] + h * (np.dot(np.array([1, 2, 2, 1]), fvec) / 6)
  return time, x
########################################################################################################################


########################################################################################################################
# EJERCICIO 1
# Resuelve: x'' + tanh(cos(t)x'x) + x = 0 con las condiciones iniciales x(0)=1 y x'(0)=1
# ----------------------------------------------------------------------------------------------------------------------
print("\nEJERCICIO 1")

def edo(t, x):
    return np.array([- np.tanh(np.cos(t)*x[0]*x[1]) - x[1], x[0]])

x0 = np.array([1.0, 1.0])
t0 = 0
tf = 50
Emax = 1e-6
n = 4

# Para estimar el paso, tengo que estimar c, tomo un h cualquiera (que converja)
h1 = 0.5
t1, x1 = ruku4(edo, t0, tf, h1, x0)
t2, x2 = ruku4(edo, t0, tf, h1/2, x0)
carr = np.zeros(len(x1))
for i in range(len(carr)):
    carr[i] = np.abs(x2[2*i][1] - x1[i][1])/((1-1/2**n)*h1**n) # Estimo c para cada valor
    c = max(carr)                                           # Tomo el máximo, que dará el menor paso
print("c estimado:", c)
h = 0.9*np.power(Emax/c, 1/n)                               # Estimo paso, para garantizar un error menor a Emax,
print("h estimado:", h)                                     # tomo el 90%

t, x = ruku4(edo, t0, tf, h, x0)                            # Resuelvo el problema

# Cálculo del error
t_2, x_2 = ruku4(edo, t0, tf, h/2, x0)
err_x = np.zeros(len(x))
for i in range(len(err_x) - 1):
    err_x[i] = 2**n * np.abs(x_2[2*i][1] - x[i][1])/(2**n - 1)   # Estimo el error para cada valor
Error_x = max(err_x)                                            # Busco el máximo
print("Error en x:", Error_x)

err_d = np.zeros(len(x))
for i in range(len(err_d) - 1):
    err_d[i] = 2**n * np.abs(x_2[2*i][0] - x[i][0])/(2**n - 1)   # Estimo el error para cada valor
Error_d = max(err_d)                                            # Busco el máximo
print("Error en x':", Error_d)

plt.plot(t, x[:, 1])                                        # Grafico función
plt.title("Función")
plt.ylabel("x")
plt.xlabel("t")
plt.show()

plt.plot(t, x[:, 0])                                        # Grafico derivada
plt.title("Derivada")
plt.xlabel("t")
plt.ylabel("x")
plt.show()

plt.plot(t, err_x)                                            # Grafico el error
plt.title("Error")
plt.xlabel("t")
plt.ylabel("x")
plt.show()

plt.plot(t, err_d)                                            # Grafico el error
plt.title("Error")
plt.xlabel("t")
plt.ylabel("x")
plt.show()
########################################################################################################################


########################################################################################################################
# bisec:
# Método de la biseccion en [a, b] con tolerancia 'tol', recibe callback a la funcion para evaluarla
# Converge sólo si hay un único cero, chequear
# Fórmula error total: |e_n|<=(b_0 - a_0)/2^(n+1) entonces el error del paso anterior es: |e_(n+1)|<=|e_n|/2 (CV lneal)
# ----------------------------------------------------------------------------------------------------------------------
def bisec(a, b, f, tol=np.finfo(float).eps, max_i=100):
    newa = a
    newb = b
    n = int(np.ceil(np.log2((newb - newa) / tol)) - 1)      # Calcula las iteraciones necesarias para el error pedido
    print(f"Se precisan {n} iteraciones")
    if n > max_i:
        print(f"El número de iteraciones necesario es mayor al máximo, se realizarán {max_i} iteraciones")
        n = max_i
    for i in range(n):
        c = newa + (newb - newa) / 2                        # Calcula c
        if (f(c) * f(newa)) >= 0:                           # Se fija ell signo de f(c)
            newa = c                                        # Si es igual al de a, a = c
        else:
            newb = c                                        # Si es igual al de b, b = c
        print(f"Raíz en iteración {i + 1}: {(newa + newb) / 2}")
    return (newa + newb) / 2
########################################################################################################################


########################################################################################################################
# EJERCICIO 2
# Encuentra el primer cero de: f(x) = x^4 + x^3 + x^2 + x - 40
# ----------------------------------------------------------------------------------------------------------------------
print("\nEJERCICIO 2")
print(bisec(2, 3, lambda x: x**4 + x**3 + x**2 + x - 40, 2e-16))
########################################################################################################################


########################################################################################################################
# leastsqr:
# Resuelve el problema de cuadrados mínimos usando descomposición QR (argmin||A.x-b||)
# Recibe la matriz A y el vector b. Devuelve el vector x.
# ----------------------------------------------------------------------------------------------------------------------
def leastqr(A, b):

    # Factorización QR
    QR = desc_qr(A)                                     # Realizo la descomposición QR
    Q1 = QR[0]                                          # Recupero Q1 de m*n y ortonormal de A
    R1 = QR[1]                                          # Recupero R1 triangular superior de n*n

    # Resuelvo para encontrar x mínima                  # R1.x = Q^T.b
    C = np.dot(np.transpose(Q1), b)                     # C = Q1^T.b
    x = rev_subs(R1, C)                                 # R1.x = C

    return x
########################################################################################################################


########################################################################################################################
# desc_qr:
# Realiza la descomposición QR reducida usando Gram-Schmidt. Devuelve Q1 y R1
# ----------------------------------------------------------------------------------------------------------------------
def desc_qr(A):
    m = A.shape[0]                                         # Defino las dimensiones m y n
    n = A.shape[1]

    Q = np.zeros(shape=(m, n))                             # Creo las matrices base
    R = np.zeros(shape=(n, n))

    for i in range(n):
        p = A[:, i]
        for k in range(i):                  # Calculo las proyecciones (Q[:, k] nunca va a ser nula porque es ortogonal)
            p = p - (np.dot(A[:, i], Q[:, k])/np.linalg.norm(Q[:, k])) * Q[:, k]
        Q[:, i] = p/np.linalg.norm(p)                      # Normalizo la columna
        R[i, i] = np.linalg.norm(p)                        # Calculo la diagonal de R
        for j in range(i + 1, n):
            R[i, j] = np.dot(A[:, j], Q[:, i])             # Calculo la esquina superior de R

    return Q, R
########################################################################################################################


########################################################################################################################
# rev_subs:
# Resuelve un sistema por sustitución hacia atrás (A.x = y). Devuelve x
# La matriz A ingresada debe ser triangular superior, y debe ser un vector
# ----------------------------------------------------------------------------------------------------------------------
def rev_subs(A, y):
    m = A.shape[0]                                                          # Defino m
    x = np.zeros(shape=(m, 1))                                              # Crea el vector base
    for i in range(m):
        d = 0
        for j in range(i):
            d += A[m - i - 1, m - j - 1] * x[m - j - 1]                     # Calcula los términos conocidos
        x[m - i - 1] = (1/A[m - i - 1, m - i - 1])*(y[m - i - 1] - d)       # Calcula una de las componente

    return x
########################################################################################################################


########################################################################################################################
# EJERCICIO 3
# Ajuste por cuadrados mínimos
# ----------------------------------------------------------------------------------------------------------------------
print("\nEJERCICIO 3")
df = pd.read_csv("p53.csv")
x = np.array(df["x"].tolist())
y = np.array(df["y"].tolist())
n = x.shape[0]
fig, ax = plt.subplots()
ax.plot(x, y, ".", label="puntos")


A = np.zeros((x.size, 3))                   # Armo matriz A
A[:, 0] = np.sqrt(abs(x[:]))
A[:, 1] = np.cos(np.sqrt(abs(x[:])))
A[:, 2] = 1

ya = leastqr(A, y) .flatten()               # Busco coeficientes que mejor ajustan a la función
print("Coeficientes:", ya)

# Armo función de ajuste
def f(x):
    return ya[0]*np.sqrt(abs(x)) + ya[1]*np.cos(np.sqrt(abs(x))) + ya[2]

x = range(-50, 50)                          # Valores del eje x que toma el gráfico
plt.plot(x, [f(i) for i in x], label="Función de ajuste")       # Grafico función ajustada
ax.legend()
plt.show()
########################################################################################################################





