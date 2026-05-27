---
tags: [parcial, ip, resolucion, transformaciones-lineales, diagonalizacion, autovalores, polinomios, subespacios]
fuente: raw/Practicas/Modelos_Examenes/MNA_IP_Tema_V_Resoloucion.pdf
tipo: ip
tema: 5
tiene_resolucion: true
---

# Primer Parcial de Métodos Numéricos Avanzados — Tema V (Resolución)

## Ejercicio 1

Sea $T : \mathbb{R}^3 \to \mathbb{R}^3 : M_{EE}(T) = \begin{pmatrix} p & 3 & 2 \\ 0 & 1 & 1 \\ q & 0 & 1 \end{pmatrix}$

a) Hallar $p, q \in \mathbb{R}$, si existe, tal que $\dim(N(T)) \ne 0$.
b) Para $p = 2$ y $q = 0$, obtener los autovalores de la matriz y decidir si $T$ es o no diagonalizable.

### Resolución

**a)** Basta ver para qué valores de $p$ y $q$ es $|M_{EE}(T)| = 0$:

$$\begin{vmatrix} p & 3 & 2 \\ 0 & 1 & 1 \\ q & 0 & 1 \end{vmatrix} = 0 \implies p + 3q - 2q = 0 \implies p + q = 0 \iff p = -q$$

**b)**

$$A_\lambda = \begin{pmatrix} \lambda - 2 & -3 & -2 \\ 0 & \lambda - 1 & -1 \\ 0 & 0 & \lambda - 1 \end{pmatrix}$$

Luego $p_A(\lambda) = (\lambda - 2)(\lambda - 1)^2$. Veamos qué ocurre si $\lambda = 1$:

$$A_1 = \begin{pmatrix} -1 & -3 & -2 \\ 0 & 0 & -1 \\ 0 & 0 & 0 \end{pmatrix}$$

$A_1$ tiene rango 2 y por tanto su espacio nulo $S_1$ tiene dimensión 1. Luego no es diagonalizable.

## Ejercicio 2

Sea la Transformación Lineal $T : P_2 \to \mathbb{R}^4 : T(a + b x + c x^2) = (2a - 2b,\ c,\ a - b,\ b - a)$

a) Hallar $M_{B_1 B_2}(T)$ para $B_1 = \{-1,\ x + 1,\ x^2\}$ y $B_2 = \{(0, 1, -1, 0),\ (1, 0, 0, 0),\ (0, 0, 1, 0),\ (0, 0, 0, 1)\}$.
b) Hallar una base y dimensiones para $N(T)$ y $R(T)$.

### Resolución

**a)** $T(-1) = (-2, 0, -1, 1)$, $T(x + 1) = (0, 0, 0, 0)$, $T(x^2) = (0, 1, 0, 0)$.

Ahora se deben hallar las coordenadas de cada vector hallado en la base $B_2$.

$[T(-1)]_{B_2} = (0, -2, -1, 1)$, $[T(x + 1)]_{B_2} = (0, 0, 0, 0)$ y $[T(x^2)]_{B_2} = (1, 0, 1, 0)$.

Luego

$$M_{B_1 B_2}(T) = \begin{pmatrix} 0 & 0 & 1 \\ -2 & 0 & 0 \\ -1 & 0 & 1 \\ 1 & 0 & 0 \end{pmatrix}$$

**b)** Una forma de hallar la base del núcleo es hacer $T(a + b x + c x^2) = (0, 0, 0, 0)$, lo que implica $(2a - 2b,\ c,\ a - b,\ b - a) = (0, 0, 0, 0) \implies a = b,\ c = 0$. Luego reemplazando sería $p(x) = a + a x$.

Una base del núcleo es $B_{N(T)} = \{1 + x\}$ y una base de la imagen será $B_{R(T)} = \{(-2, 0, -1, 1),\ (0, 1, 0, 0)\}$.

## Ejercicio 3

Sea

$$A = \left\{\begin{pmatrix} a & b \\ c & d \end{pmatrix} : 2a + 3b - c = 0 \land b - 2d = 0\right\}$$

un subespacio de $(\mathbb{R}^{2 \times 2}, +, \mathbb{R}, \cdot)$.

a) Hallar una base $B$ y la dimensión de $A$.
b) Hallar las coordenadas de $\begin{pmatrix} -3 & 2 \\ 0 & 1 \end{pmatrix}$ en $B$.

### Resolución

**a)** $b = 2d$ y $c = 2a + 3b = 2a + 6d$. Reemplazando se tiene que un elemento genérico de $A$ es

$$\begin{pmatrix} a & 2d \\ 2a + 6d & d \end{pmatrix} = a \begin{pmatrix} 1 & 0 \\ 2 & 0 \end{pmatrix} + d \begin{pmatrix} 0 & 2 \\ 6 & 1 \end{pmatrix} \implies B = \left\{\begin{pmatrix} 1 & 0 \\ 2 & 0 \end{pmatrix},\ \begin{pmatrix} 0 & 2 \\ 6 & 1 \end{pmatrix}\right\}$$

**b)**

$$\begin{pmatrix} -3 & 2 \\ 0 & 1 \end{pmatrix} = \alpha \begin{pmatrix} 1 & 0 \\ 2 & 0 \end{pmatrix} + \beta \begin{pmatrix} 0 & 2 \\ 6 & 1 \end{pmatrix} \implies \alpha = -3,\ \beta = 1$$

Luego $\left[\begin{pmatrix} -3 & 2 \\ 0 & 1 \end{pmatrix}\right]_B = \begin{pmatrix} -3 \\ 1 \end{pmatrix}$.
