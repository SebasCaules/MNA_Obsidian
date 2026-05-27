---
tags: [parcial, ip, resolucion, transformaciones-lineales, diagonalizacion, nucleo-imagen]
fuente: raw/Practicas/Modelos_Examenes/MNA_IP_Tema_I_Resolucion.pdf
tipo: ip
tema: 1
tiene_resolucion: true
---

# Primer Parcial de Métodos Numéricos Avanzados — Tema I (Resolución)

## Ejercicio 1

Dada la Transformación Lineal $T : \mathbb{R}^3 \to \mathbb{R}^3 : T(x, y, z) = (2x - y + z,\ x + y - z,\ z + y - x)$

a) Hallar el Núcleo y la Imagen
b) Hallar $(x, y, z)$, si existe, de modo que $T(x, y, z) = (1, 1, -2)$

### Resolución

**a)** Para hallar el núcleo se hace $T(x, y, z) = 0$, lo que implica resolver el sistema de ecuaciones

$$2x - y + z = 0,\quad x + y - z = 0,\quad z + y - x = 0$$

De la segunda ecuación $z = x + y$. Reemplazando en la primera:

$$2x - y + x + y = 0 \implies x = 0 \implies y = z \implies y = 0 \implies z = 0$$

Finalmente $N(T) = \{(0, 0, 0)\}$. Luego por el Teorema de la dimensión $R(T) = \mathbb{R}^3$.

**b)** En este caso hay que resolver el sistema

$$2x - y + z = 1,\quad x + y - z = 1,\quad z + y - x = -2$$

De la segunda ecuación se tiene que $z = x + y - 1$. Reemplazando en la primera queda

$$2x - y + x + y = 2 \implies x = 2/3 \implies z = y - 1/3$$

Reemplazando en la tercera se tiene $y - 1/3 + y - 2/3 = -2 \implies y = -1/2 \implies z = -5/6$.

Luego el valor buscado es $\left(\dfrac{2}{3}, -\dfrac{1}{2}, -\dfrac{5}{6}\right)$.

## Ejercicio 2

Sea $F : \mathbb{R}^3 \to \mathbb{R}^3$ una transformación lineal tal que

$$M(F)_{EE} = \begin{pmatrix} 1 & 0 & 1 \\ 0 & k & 1 \\ 0 & 9 & k \end{pmatrix}$$

a) Hallar todos los valores de $k$ para los cuales $F$ es diagonalizable.
b) Para $k = 3$ hallar una base $B$ de $\mathbb{R}^3$ tal que $M(F)_{BB}$ sea diagonal y dar la expresión de $M(F)_{BB}$.

### Resolución

Se rebautiza $A = M(F)_{EE}$. Luego

$$A_\lambda = \begin{pmatrix} \lambda - 1 & 0 & -1 \\ 0 & \lambda - k & -1 \\ 0 & -9 & \lambda - k \end{pmatrix},\quad p_A(\lambda) = \begin{vmatrix} \lambda - 1 & 0 & -1 \\ 0 & \lambda - k & -1 \\ 0 & -9 & \lambda - k \end{vmatrix} = (\lambda - 1)\left[(\lambda - k)^2 - 9\right]$$

$$p_A(\lambda) = (\lambda - 1)[\lambda - (k + 3)][\lambda - (k - 3)]$$

Claramente $k + 3 \ne k - 3$. Se analizarán casos:

**i)** Si $k + 3 \ne 1$ y $k - 3 \ne 1$, o sea $k \ne -2$ y $k \ne 4$, es diagonalizable.

**ii)** Si $k = -2$ se tiene

$$p_A(\lambda) = (\lambda - 1)^2(\lambda + 5),\quad A_1 = \begin{pmatrix} 0 & 0 & -1 \\ 0 & 3 & -1 \\ 0 & -9 & 3 \end{pmatrix} \implies z = 0,\ y = 0$$

Luego hay un solo autovector $v_1 = (1, 0, 0)$. No es diagonalizable.

**iii)** Si $k = 4$ queda

$$p_A(\lambda) = (\lambda - 1)^2(\lambda - 7),\quad A_1 = \begin{pmatrix} 0 & 0 & -1 \\ 0 & -3 & -1 \\ 0 & -9 & -3 \end{pmatrix} \implies z = 0,\ y = 0$$

Luego hay un solo autovector $v_1 = (1, 0, 0)$. No es diagonalizable.

Finalmente sólo será diagonalizable si $k \in \mathbb{R} - \{-2, 4\}$.

**b)** Si $k = 3$ se tiene

$$A_\lambda = \begin{pmatrix} \lambda - 1 & 0 & -1 \\ 0 & \lambda - 3 & -1 \\ 0 & -9 & \lambda - 3 \end{pmatrix} \implies p_A(\lambda) = (\lambda - 1)[(\lambda - 3)^2 - 9] \implies p_A(\lambda) = \lambda(\lambda - 1)(\lambda - 6)$$

Para $\lambda = 0$:

$$A_0 = \begin{pmatrix} -1 & 0 & -1 \\ 0 & -3 & -1 \\ 0 & -9 & -3 \end{pmatrix} \implies z = -3y,\ x = 3y \implies v_0 = (3, 1, -3)$$

Para $\lambda = 1$:

$$A_1 = \begin{pmatrix} 0 & 0 & -1 \\ 0 & -2 & -1 \\ 0 & -9 & -2 \end{pmatrix} \implies z = y = 0 \implies v_1 = (1, 0, 0)$$

Para $\lambda = 6$:

$$A_6 = \begin{pmatrix} 5 & 0 & -1 \\ 0 & 3 & -1 \\ 0 & -9 & 3 \end{pmatrix} \implies z = 3y = 5x \implies v_6 = (3, 5, 15)$$

$$B = \{(3, 1, -3),\ (1, 0, 0),\ (3, 5, 15)\},\quad M(T)_{BB} = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 6 \end{pmatrix}$$

## Ejercicio 3

Considere la matriz

$$A = \begin{pmatrix} 0.92 & 1.44 \\ 1.44 & 0.08 \end{pmatrix}$$

a) Realizar la descomposición en valores singulares.
b) Realizar la factorización QR.

*(El PDF de resolución no incluye desarrollo para este ejercicio.)*

## Ejercicio 4

Dado el siguiente conjunto de datos

| x | y |
|---|---|
| $0$ | $+0.97$ |
| $\pi/4$ | $+1.42$ |
| $\pi$ | $-1.04$ |

Usando cuadrados mínimos, realice el ajuste de los datos experimentales a la ecuación $y(x) = a \cos(x) + b \sin(x)$ utilizando descomposición QR.

*(El PDF de resolución no incluye desarrollo para este ejercicio.)*

## Ejercicio 5

Sea $H = \langle x^2 + 2x - 1,\ x^2 + x + a^2 - 4,\ x^2 - 2x + 3 \rangle \subset P_2$. Determinar todos los valores de $a$ si existen para que $\dim(H) = 2$ y $x^2 + a - 1 \in H$.

*(El PDF de resolución no incluye desarrollo para este ejercicio.)*
