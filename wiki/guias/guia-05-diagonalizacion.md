---
tags: [guia, diagonalizacion, autovalores, autovectores]
fuente: raw/Practicas/Guias_TP2026/Guia_TP_V_MNA_ITBA_2025.pdf
unidad: V
---

# Guía de Trabajos Prácticos V — Autovalores y autovectores

## Ejercicio 1

Considere las siguientes matrices:

$$A = \begin{pmatrix} 1 & 0 \\ 2 & 3 \end{pmatrix},\quad C = \begin{pmatrix} 2 & 1 & 1 \\ 2 & 3 & 2 \\ 3 & 3 & 4 \end{pmatrix},\quad B = \begin{pmatrix} 7 & 2 \\ -15 & -4 \end{pmatrix},\quad D = \begin{pmatrix} 1 & -2 \\ 1 & 3 \end{pmatrix}$$

- a) Encuentra los autovalores, los autovectores y la matriz de diagonalización (matriz de autovectores) para cada matriz.
- b) Verifica que la traza de las matrices es igual a la suma de los autovalores, su determinante al producto y es un invariante (tiene el mismo valor que la traza de la matriz original).

## Ejercicio 2

Dadas las matrices:

$$A = \begin{pmatrix} 3 & -1 & 1 \\ 0 & 2 & 0 \\ 1 & -1 & 3 \end{pmatrix},\quad B = \begin{pmatrix} 5 & 0 & 0 \\ 0 & -1 & 1 \\ 3 & 0 & -1 \end{pmatrix}$$

halla, para cada una de ellas: su espectro, su radio espectral; la multiplicidad algebraica de cada autovalor y la multiplicidad geométrica. En los casos que sea posible, proporciona la matriz de paso.

## Ejercicio 3

Encuentre una matriz que tenga como espectro de autovalores, el siguiente conjunto: $\{1;\, -2;\, 3\}$.

## Ejercicio 4

Se tiene una matriz $A \in \mathbb{R}^{2\times 2}$ cuyos elementos son desconocidos, pero se sabe que sus autovalores son $3$ y $\tfrac{1}{3}$, y los correspondientes autovectores son $\begin{pmatrix}1 \\ 1\end{pmatrix}$ y $\begin{pmatrix}-1 \\ 1\end{pmatrix}$. Determina el vector $Ax$ si $x = \begin{pmatrix}9 \\ 1\end{pmatrix}$.

## Ejercicio 5

Se sabe que los autovalores de una matriz $B$ de $3 \times 3$ son $0$, $1$ y $2$. Esta información es suficiente para encontrar tres de los cuatro incisos siguientes:

- a) el rango de $B$,
- b) el determinante de $B^T B$,
- c) los autovalores de $B^T B$,
- d) los autovalores de $(B + I_3)^{-1}$

## Ejercicio 6

Calcular los valores propios reales $\lambda$ y los subespacios fundamentales asociados con $\lambda$ para la transformación lineal definida por $f(x, y, z) = (-x - z,\; -7x + 4y + 13z,\; x - 3z)$.

## Ejercicio 7

Si los autovalores de una matriz $A$ de $3 \times 3$ son $1$, $1$ y $2$, ¿de cuáles de las siguientes afirmaciones se tiene la certeza de que son verdaderas? Proporcione un razonamiento de por qué son verdaderas o un ejemplo si no lo son.

- a) $A$ es invertible.
- b) $A$ es diagonalizable.
- c) $A$ no es diagonalizable.

## Ejercicio 8

Suponga que $A$ es una matriz simétrica de $3 \times 3$ con autovalores $0$, $1$ y $2$.

- a) ¿Qué propiedades pueden garantizarse para los autovectores unitarios $u, v, w$ correspondientes a los autovalores $0$, $1$ y $2$, respectivamente?
- b) En términos de $u, v, w$, describa el espacio nulo y el espacio columna de $A$.
- c) Encuentre un vector $x$ que cumpla $Ax = v + w$. ¿Es $x$ único?
- d) ¿Qué condiciones debe cumplir $b$ para que $Ax = b$ tenga una solución?
- e) Si $u, v, w$ son las columnas de $S$, ¿cuáles son $S^{-1}$ y $S^{-1} A S$?

Ver ejercicios resueltos en [[../resueltos/resueltos-diagonalizacion]].
