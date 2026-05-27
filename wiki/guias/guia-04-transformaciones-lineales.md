---
tags: [guia, transformaciones-lineales]
fuente: raw/Practicas/Guias_TP2026/Guia_TP_IV_MNA_ITBA_2025.pdf
unidad: IV
---

# Guía de Trabajos Prácticos IV — Transformaciones lineales

## Ejercicio 1

Determina si las siguientes funciones son lineales.

- a) $f : \mathbb{R}^3 \to \mathbb{R}^3$ tal que $f(x_1, x_2, x_3) = (2x_1 - 7x_3,\, 0,\, 3x_2 + 2x_3)$.
- b) $f : \mathbb{R}^2 \to \mathbb{R}^3$ tal que $f(x_1, x_2) = (x_1 - x_2,\, 2x_2,\, 1 + x_1)$.
- c) $f : \mathbb{C} \to \mathbb{C}$ tal que $f(z) = \overline{z}$.
- d) $f : \mathbb{R}^{2\times 2} \to \mathbb{R}$; $f\begin{pmatrix}a_{11} & a_{12} \\ a_{21} & a_{22}\end{pmatrix} = a_{11} a_{22} - a_{12} a_{21}$.
- e) $\operatorname{tr} : \mathbb{K}^{n\times n} \to \mathbb{K}$, con $\mathbb{K} = \mathbb{R}$ o $\mathbb{K} = \mathbb{C}$.
- f) $t : \mathbb{K}^{n\times m} \to \mathbb{K}^{m\times n}$, $t(A) = A'$, con $\mathbb{K} = \mathbb{R}$ o $\mathbb{K} = \mathbb{C}$.
- g) $T : C^1(\mathbb{R}) \to C(\mathbb{R})$, $T(f) = 3(f')^2$.
- h) $T : C^1(\mathbb{R}) \to C(\mathbb{R})$, $T(f) = 3f'' - 5f' + 6f$.
- i) $T : L^1([a, b]) \to \mathbb{R}$, $T(f) = \int_a^b f(x)\, g(x)\, dx$ con $g \in L^1$.

## Ejercicio 2

Sea $f : \mathbb{R}^n \to \mathbb{R}^m$ tal que $f(X) = AX$, donde $A \in \mathbb{R}^{m\times n}$. Prueba que $f$ es una transformación lineal.

## Ejercicio 3

Sea la transformación lineal $D : P_2 \to P_2$ tal que $D(p) = p'(x)$. Encuentra la matriz asociada con esta transformación.

## Ejercicio 4

Interpretar geométricamente las siguientes transformaciones lineales $f : \mathbb{R}^2 \to \mathbb{R}^2$:

- a) $f(x, y) = (x, 0)$.
- b) $f(x, y) = (0, y)$.
- c) $f(x, y) = (x, -y)$.
- d) $f(x, y) = \left(\dfrac{x+y}{2},\, \dfrac{x+y}{2}\right)$.
- e) $f(x, y) = (x \cos t - y \sin t,\; x \sin t + y \cos t)$.

## Ejercicio 5

Probar que existe una única transformación lineal $f : \mathbb{R}^2 \to \mathbb{R}^2$ tal que $f(1, 1) = (-5, 3)$ y $f(-1, 1) = (5, 2)$. Para dicha $f$, determinar $f(5, 3)$ y $f(-1, 2)$.

## Ejercicio 6

Sean $B_1$ y $B_2$ bases de $\mathbb{R}^2$ y

$$P = \begin{pmatrix} 1 & 1 \\ 0 & -3 \end{pmatrix}$$

la matriz de cambio de base de $B_1$ a $B_2$.

- a) Si $u_{B_1} = \begin{pmatrix}1 \\ 4\end{pmatrix}$, calcula $u_{B_2}$.
- b) Si $v_{B_2} = \begin{pmatrix}3 \\ 5\end{pmatrix}$, calcula $v_{B_1}$.
- c) Si $B_1 = \left\{\begin{pmatrix}1 \\ 3\end{pmatrix},\, \begin{pmatrix}0 \\ 4\end{pmatrix}\right\}$, obtener $B_2$. ¿Es única?

Ver resolución de incisos a) y b) en [[../resueltos/resueltos-algebra]].

## Ejercicio 7

Determinar si existe una transformación lineal $f : \mathbb{R}^2 \to \mathbb{R}^2$ tal que verifique:

$$f(1, 1) = (2, 6),\quad f(-1, 1) = (2, 1),\quad f(2, 7) = (5, 3).$$

## Ejercicio 8

Dada $F : \mathbb{R}^3 \to P_1$ cuya matriz asociada es:

$$M_{BE} = \begin{pmatrix} 1 & 0 & 1 \\ -1 & 0 & 0 \end{pmatrix}$$

Siendo $B = \{(1, 0, 0), (1, 1, 0), (1, 0, 1)\}$ y $E = \{1, t\}$.

- a) Hallar una base para el Núcleo de $F$.
- b) Un $v \in \mathbb{R}^3$ tal que $F(v) = -1 + t$.

## Ejercicio 9

Hallar las coordenadas de $v \in V$ respecto de la base $B$ en los siguientes casos:

- a) $v = \begin{pmatrix}1 \\ 1 \\ 1\end{pmatrix} \in \mathbb{R}^3$, $B = \left\{\begin{pmatrix}1 \\ 0 \\ 2\end{pmatrix},\, \begin{pmatrix}1 \\ 2 \\ -3\end{pmatrix},\, \begin{pmatrix}2 \\ 2 \\ 0\end{pmatrix}\right\}$, $\mathbb{K} = \mathbb{R}$.
- b) $v = \begin{pmatrix}2 - i \\ 2 + 3i\end{pmatrix} \in \mathbb{C}^2$, $B = \left\{\begin{pmatrix}1 + i \\ -i\end{pmatrix},\, \begin{pmatrix}i \\ 1 - i\end{pmatrix}\right\}$, $\mathbb{K} = \mathbb{C}$.

## Ejercicio 10

Sea la transformación lineal $F : \mathbb{R}^2 \to P_1$ tal que viene representada en las bases $B_1$ de $\mathbb{R}^2$ y $B_2$ de $P_1$.

$$A = \begin{pmatrix} 1 & 2 \\ 1 & 2 \end{pmatrix};\quad B_1 = \left\{\begin{pmatrix}1 \\ 0\end{pmatrix},\, \begin{pmatrix}1 \\ 1\end{pmatrix}\right\};\quad B_2 = \{1,\, 1 - x\}$$

- a) Halla $[F(v)]_{B_2}$ si $v = \begin{pmatrix}2 \\ 1\end{pmatrix}$ expresado en la base canónica.
- b) Halla una base del núcleo de $F$.
- c) Encuentra una base para la imagen de $F$.
