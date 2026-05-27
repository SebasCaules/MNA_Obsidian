---
tags: [guia, ortogonalidad, gram-schmidt, qr, lu]
fuente: raw/Practicas/Guias_TP2026/Guia_TP_VI_MNA_ITBA_2025.pdf
unidad: VI
---

# Guía de Trabajos Prácticos VI — Ortogonalidad. Descomposición QR y LUP

## Ejercicio 1

Usando el método de ortonormalización de Gram-Schmidt, encuentre una base ortonormal del subespacio generado por los vectores

$$a_1 = (1; -1; 0; 0)^\top,\quad a_2 = (0; 1; -1; 0)^\top,\quad a_3 = (0; 0; 1; -1)^\top$$

Coloque la base resultante como vectores columna de una matriz $Q$. Muestre que:

- a) $Q^\top Q = I_3$
- b) $QQ^\top = \begin{pmatrix} 1 & 0 & \cdot & \cdot \\ 0 & 1 & 0 & \cdot \\ \cdot & 0 & 1 & 0 \\ \cdot & \cdot & 0 & 1 \end{pmatrix}$. ¿Qué conclusiones puede obtener a partir de estos cálculos?

## Ejercicio 2

Consideremos el espacio vectorial $P_1$ formado por el conjunto de polinomios de grado 1 con coeficientes reales y el producto interno

$$\langle (a_0 + a_1 x)(b_0 + b_1 x)\rangle = a_0 b_0 + 2 a_1 b_1$$

Sea $B = \{1 + x;\, 1 - x\}$ una base de $P_1$. Halla una base ortonormal de $P_1$ a partir de ella.

## Ejercicio 3

Encuentre la descomposición QR de las siguientes matrices. Compare los resultados con la orden `qr(A)` y `qr(A, 0)` de matlab/octave. Interprete las diferencias si las hay.

$$A = \begin{pmatrix} 1 & 2 \\ 1 & 4 \end{pmatrix},\quad B = \begin{pmatrix} 3 & 0 \\ 4 & 5 \end{pmatrix},\quad C = \begin{pmatrix} 1 & 1 \\ 2 & 3 \\ 2 & 1 \end{pmatrix},$$

$$D = \begin{pmatrix} -1 & 6 & 6 \\ 3 & -8 & 3 \\ 1 & -2 & 6 \\ 1 & -4 & -3 \end{pmatrix},\quad E = \begin{pmatrix} 1 & 3 & 5 \\ -1 & -3 & 1 \\ 0 & 2 & 3 \\ 1 & 5 & 2 \\ 1 & 5 & 8 \end{pmatrix}$$

## Ejercicio 4

Encuentre la factorización LU parcial de las siguientes matrices:

$$A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 5 & 4 \\ 3 & 0 & 1 \end{pmatrix},\quad B = \begin{pmatrix} 1 & 2 & -3 & 1 \\ 2 & 4 & 0 & 7 \\ -1 & 3 & 2 & 0 \end{pmatrix},\quad A = \begin{pmatrix} 3 & 0 & 1 \\ 2 & 5 & 4 \\ 1 & 2 & 3 \end{pmatrix}$$

## Ejercicio 5

Se puede demostrar que los polinomios $P = \{1, x, x^2, x^3, \dots\}$ representan una base de las funciones reales que tienen derivadas de todo orden en $[-1, 1]$. Utilizando el proceso de ortogonalización de Gram-Schmidt, encuentre los primeros tres elementos de la base ortonormal con el producto interno definido por:

$$\langle p_n(x), p_m(x)\rangle = \int_{-1}^{1} p_n(x)\, p_m(x)\, dx$$

dar una expresión de los infinitos elementos de la base.

## Ejercicio 6

Sea $U$ la matriz triangular superior, compruebe que resolver el sistema

$$U b = c$$

Desarrolla una función en matlab/octave llamada `BackwardSust(U,c)` tal que `b = BackwardSust(U,c)`. Aplicarla para resolver el sistema

$$\begin{pmatrix} 2 & 1 & -1 & 1 \\ 0 & 5 & -\tfrac{3}{2} & -\tfrac{1}{2} \\ 0 & 0 & \tfrac{14}{5} & -\tfrac{7}{5} \\ 0 & 0 & 0 & \tfrac{7}{2} \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{pmatrix} = \begin{pmatrix} 5 \\ -\tfrac{3}{2} \\ \tfrac{14}{5} \\ 14 \end{pmatrix}$$

## Ejercicio 7

Sea $L$ una matriz triangular inferior, compruebe que la resolución del sistema

$$\begin{pmatrix} 1 & 0 & 0 & 0 \\ -1 & 1 & 0 & 0 \\ -1 & -3 & 1 & 0 \\ 1 & -1 & 0 & 1 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \\ -4 \\ 3 \end{pmatrix}$$

En base a los ejercicios anteriores, resolver el sistema de ecuaciones lineales $A x = b$:

- a) Utilizando la factorización QR. $A x = QRx = b$; primero resolvemos
  $$Qz = b,\quad Rx = z$$
  Como $Q$ es ortonormal, su inversa coincide con su traspuesta $z = Q^\top b$ y como $R$ es triangular superior, se aplica el método del problema 6.
- b) Utilizando la factorización $PLU$. Sabemos que entonces para resolver $Ax = b$, multiplicamos a izquierda por $P$ y aplicamos la factorización LU y el procedimiento para QR:
  $$Ax = b \;\Rightarrow\; PAx = Pb \;\Rightarrow\; LUx = Pb \;\Rightarrow\; Lz = Pb \;\Rightarrow\; Ux = z$$

## Ejercicio 8

Resuelva los sistemas de ecuaciones lineales: a, b empleando factorización QR y c, d empleando factorización LU.

**a)**

$$A = \begin{pmatrix} 2 & 1 & -1 & 1 \\ -1 & 2 & -1 & -1 \\ 1 & 1 & 2 & -1 \\ -1 & 1 & 1 & 2 \end{pmatrix},\quad b = \begin{pmatrix} 5 \\ -4 \\ 5 \\ 12 \end{pmatrix}$$

**b)**

$$A = \begin{pmatrix} 2 & 3 & -2 \\ 2 & 4 & -1 \\ -2 & 1 & 8 \end{pmatrix},\quad b = \begin{pmatrix} 14 \\ 27 \\ 52 \end{pmatrix}$$

**c)**

$$A = \begin{pmatrix} 3 & 1 & 1 & 0 \\ -6 & 2 & 2 & 2 \\ 3 & 3 & 2 & -1 \\ 3 & 7 & 2 & 0 \end{pmatrix},\quad b = \begin{pmatrix} -2 \\ -12 \\ 7 \\ -5 \end{pmatrix}$$

**d)**

$$A = \begin{pmatrix} 0 & 0 & 4 \\ 1 & 3 & 2 \\ 2 & 8 & 4 \end{pmatrix},\quad b = \begin{pmatrix} -8 \\ 1 \\ 6 \end{pmatrix}$$
