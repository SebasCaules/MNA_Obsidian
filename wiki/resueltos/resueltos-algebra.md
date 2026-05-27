---
tags: [resueltos, algebra-lineal, cambio-de-base]
fuente: raw/Practicas/Ejercicios_Resueltos/Ejercicios_Algebra_Lineal_Resueltos.pdf
unidad: IV
---

# Ejercicios Resueltos — Álgebra Lineal (cambio de base)

Ver enunciado relacionado en [[../guias/guia-04-transformaciones-lineales]] (Ejercicio 6).

## Ejercicio 1

Sean $B_1$ y $B_2$ bases de $\mathbb{R}^2$ y

$$P = \begin{pmatrix} 1 & 1 \\ 0 & -3 \end{pmatrix}$$

la matriz de cambio de base de $B_1$ a $B_2$.

**a)** Si $[u]_{B_1} = (1, 4)$. Hallar $[u]_{B_2}$.

**b)** Si $[v]_{B_2} = (3, 5)$. Hallar $[v]_{B_1}$.

**c)** Si $B_1 = \{(1, 3), (0, 4)\}$ obtener $B_2$. ¿Es única?

### Resolución

**a)** $[u]_{B_2} = P\, [u]_{B_1}$, luego:

$$[u]_{B_2} = \begin{pmatrix} 1 & 1 \\ 0 & -3 \end{pmatrix} \begin{pmatrix} 1 \\ 4 \end{pmatrix} = \begin{pmatrix} 5 \\ -12 \end{pmatrix}$$

**b)** Se tiene

$$\begin{pmatrix} 3 \\ 5 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 0 & -3 \end{pmatrix} \begin{pmatrix} c_1 \\ c_2 \end{pmatrix},\quad [u]_{B_1} = \begin{pmatrix} c_1 \\ c_2 \end{pmatrix}$$

De ahí $c_1 + c_2 = 3$ y $-3 c_2 = 5 \Rightarrow c_2 = -\tfrac{5}{3} \Rightarrow c_1 = \tfrac{14}{3}$. Luego:

$$[v]_{B_1} = \begin{pmatrix} \tfrac{14}{3} \\ -\tfrac{5}{3} \end{pmatrix}$$

**c)** Sea $B_2 = \{w_1, w_2\}$ la base buscada. Las columnas de $P$ son las coordenadas de $w_1$ y $w_2$ en la base $B_1$. Luego:

$$w_1 = 1\cdot(1, 3) + 0\cdot(0, 4) = (1, 3)$$
$$w_2 = 1\cdot(1, 3) - 3\cdot(0, 4) = (1, -9)$$

Luego $B_2 = \{(1, 3),\, (1, -9)\}$.
