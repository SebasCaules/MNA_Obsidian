---
tags: [guia, vectores, matrices, determinantes]
fuente: raw/Practicas/Guias_TP2026/Guia_TP_II_MNA_ITBA_2025.pdf
unidad: II
---

# Guía de Trabajos Prácticos II — Vectores, Matrices y Determinantes

## Operaciones con vectores de $\mathbb{R}^n$ y $\mathbb{C}^n$

### Ejercicio 1

Determine cuáles de los siguientes vectores son iguales:

$$u_1 = (1, 2, 3),\quad u_2 = (2, 3, 1),\quad u_3 = (1, 3, 2),\quad u_4 = (2, 3, 1)$$

### Ejercicio 2

Considera los vectores en $\mathbb{C}^3$:

$$w_1 = (2 + 3i,\, 4 - i,\, 3),\quad w_2 = (3 - 2i,\, 5i,\, 4 - 6i)$$

Determine:
- a) $w_1 + w_2$
- b) $(5 - 2i)\, w_1$

### Ejercicio 3

Sean los vectores en $\mathbb{R}^3$:

$$u = (2, -7, 1),\quad v = (-3, 0, 4),\quad w = (0, 5, -8).$$

Encuentre:

$$a = 3u - 4v,\quad b = 2u + 3v - 5w.$$

### Ejercicio 4

Encuentra $x$ e $y$ que verifiquen:
- a) $(x, 3) = (2,\, x + y)$
- b) $(4, y) = x\,(2, 3)$

### Ejercicio 5

Escribe el vector $v = (1, 2)$ como una combinación lineal de los vectores:

$$u_1 = (1, 1),\quad u_2 = (1, -1),\quad u_3 = (1, -3)$$

¿Es única la solución de este sistema?

### Ejercicio 6

Encuentra $a$ y $b$ reales tales que:

$$(2, 3) = a\,(1, 4) + b\,(-4, -16)$$

### Ejercicio 7

Mediante el software de cálculo (Matlab, Octave o Scilab), determine los números $\alpha, \beta, \gamma$ tal que el vector $v = (2, -5, 3)$ sea combinación lineal de los vectores $w_1, w_2$ y $w_3$, es decir:

$$v = \alpha w_1 + \beta w_2 + \gamma w_3$$

con

$$w_1 = (1, -3, 2),\quad w_2 = (2, -4, -1),\quad w_3 = (1, -5, 1)$$

## Matrices y Determinantes

### Ejercicio 1

Sean las matrices $A \in \mathbb{R}^{2\times 3}$, $B \in \mathbb{R}^{2\times 3}$ y $C \in \mathbb{R}^{3\times 4}$. Calcular cuando esté definido:

- a) $3A + 2B$
- b) $AC + 5BC + C$
- c) $A - 5B$
- d) $BC$
- e) $C'\, B'$
- f) $A\, B'$

Donde:

$$A = \begin{pmatrix} 1 & 2 & 4 \\ 7 & 5 & 3 \end{pmatrix},\quad B = \begin{pmatrix} 7 & 5 & -3 \\ 5 & 2 & 6 \end{pmatrix},\quad C = \begin{pmatrix} 1 & -2 & 0 & 3 \\ 4 & -5 & 1 & 2 \\ 2 & 3 & 1 & 4 \end{pmatrix}$$

### Ejercicio 2

Determine todas las matrices $B$ que conmutan con la siguiente matriz cuadrada:

$$A = \begin{pmatrix} 3 & 1 \\ 1 & 0 \end{pmatrix}$$

### Ejercicio 3

Exhibir todas las matrices $A$ de $\mathbb{R}^{2\times 2}$ tal que:

- a) $A^2 = -I$ (matrices involutivas de orden 2)
- b) $A^2 = I$ (matrices involutivas de orden 2)
- c) $A^2 = 0$ (matrices nilpotentes de orden 2)
- d) $A^2 = A$ (matrices idempotentes)

### Ejercicio 4

Sea $A \in \mathbb{R}^{3\times 3}$ tal que:

$$A = \begin{pmatrix} 1 & -1 & 0 \\ 0 & 1 & 0 \\ 2 & 0 & 1 \end{pmatrix}$$

- a) Halla $A^{-1}$.
- b) Halla $(A')^{-1}$.

### Ejercicio 5

Sea $A_i \in \mathbb{R}^3$ y $A \in \mathbb{R}^{3\times 3}$, tal que $A = (A_1, A_2, A_3)$ con $\det(A) = -3$.

Calcule $\det\left(\tfrac{3}{4} A^{-1} B'\right)$ si $B = (A_1 - 3A_3,\, A_3,\, A_1 - A_2)$.

### Ejercicio 6

Sea $A_i \in \mathbb{R}^4$ y $A \in \mathbb{R}^{4\times 4}$, tal que $A = (A_1, A_2, A_3, A_4)$ con $\det(A) = k \ne 0$.

Calcule $\det\left(\tfrac{2}{3} B^{-1} A^2\right)$ si $B = (A_1 - A_2,\, A_3 - 2A_4,\, A_3,\, A_2)$.

### Ejercicio 7

Sea $A \in \mathbb{R}^{3\times 3}$ y $k \in \mathbb{R}$. Encuentre los valores de $k$ tal que la matriz $A$ sea singular:

$$A = \begin{pmatrix} k - 1 & -2 & 3 \\ k + 2 & -1 & 0 \\ 0 & 0 & 3 - k \end{pmatrix}$$

### Ejercicio 8

Halle los valores de $k$ que hacen inversible a la matriz $P$:

$$P = \begin{pmatrix} 1 & 1 & 0 \\ -2k - 1 & 2 & 0 \\ 0 & 3 & k \end{pmatrix}$$

### Ejercicio 9

Estudiar el carácter del sistema según los valores de los parámetros $a$ y $b$:

$$\begin{cases} x + y + z = a \\ x - y = 0 \\ 3x + y + bz = 0 \end{cases}$$

### Ejercicio 10

Dado el sistema de ecuaciones:

$$\begin{cases} -2x - 4y + 6z = 4 \\ -3x - 3y + 8z = 4 \\ 3y - z = k \end{cases}$$

- a) Para qué valores de $k$ el sistema es compatible determinado (tiene solución única).
- b) Para qué valores de $k$ el sistema es compatible indeterminado (tiene infinitas soluciones).
- c) Para qué valor de $k$ el sistema es incompatible (no tiene soluciones).
- d) Halle las soluciones del sistema homogéneo.
- e) Halle las soluciones del sistema para el valor de $k$ hallado en b).
