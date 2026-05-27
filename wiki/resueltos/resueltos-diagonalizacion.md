---
tags: [resueltos, diagonalizacion, autovalores]
fuente: raw/Practicas/Ejercicios_Resueltos/Ejercicios_Diagonalizacion_Resueltos.pdf
unidad: V
---

# Ejercicios Resueltos — Diagonalización

Ver enunciados relacionados en [[../guias/guia-05-diagonalizacion]].

## Ejercicio 1

Sea $M = \begin{pmatrix} 3 & 1 & 2 \\ 0 & a & 0 \\ 1 & -1 & 2 \end{pmatrix}$. Hallar los valores de $a \in \mathbb{R}$ para que $M$ sea diagonalizable.

### Resolución

$$p_A(\lambda) = |\lambda I - A| = \begin{vmatrix} \lambda - 3 & -1 & -2 \\ 0 & \lambda - a & 0 \\ -1 & 1 & \lambda - 2 \end{vmatrix} = (\lambda - a)\left[(\lambda - 3)(\lambda - 2) - 2\right]$$

$$= (\lambda - a)(\lambda^2 - 5\lambda + 4) = (\lambda - a)(\lambda - 4)(\lambda - 1)$$

$$\boxed{p_A(\lambda) = (\lambda - a)(\lambda - 4)(\lambda - 1)}$$

Se analizarán 3 casos:

**i)** Si $a \ne 4$ y $a \ne 1$, $M$ es diagonalizable (tres autovalores distintos).

**ii)** Si $a = 4$ se tiene $p_A(\lambda) = (\lambda - 4)^2(\lambda - 1)$. Calculamos $A_4 = 4I - A$:

$$A_4 = \begin{pmatrix} 1 & -1 & -2 \\ 0 & 0 & 0 \\ -1 & 1 & 2 \end{pmatrix} \xrightarrow{F_3 \to F_3 + F_1} \begin{pmatrix} 1 & -1 & -2 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$$

Se tiene $y = x - 2z$ luego $S_4 = \langle (1, 1, 0),\, (0, -2, 1)\rangle$. La dimensión de $S_4$ es 2, por tanto para $a = 4$, $M$ resulta diagonalizable.

**iii)** Si $a = 1$ se tiene $p_A(\lambda) = (\lambda - 4)(\lambda - 1)^2$.

$$A_1 = \begin{pmatrix} -2 & -1 & -2 \\ 0 & 0 & 0 \\ -1 & 1 & -1 \end{pmatrix} \xrightarrow{F_3 \to 2F_3 - F_1} \begin{pmatrix} -2 & -1 & -2 \\ 0 & 0 & 0 \\ 0 & 3 & 0 \end{pmatrix}$$

Se tiene $3y = 0 \Rightarrow y = 0$ y $-2x - 2z = 0 \Rightarrow z = -x$, luego $S_1 = \langle (1, 0, -1)\rangle$. La dimensión es 1, por tanto para $a = 1$, $M$ no es diagonalizable.

## Ejercicio 2

Sea $T : \mathbb{R}^3 \to \mathbb{R}^3$ una transformación lineal cuya matriz asociada es simétrica y además cumple que $T(1, 0, 0) = (2, 0, 1)$, $T(0, 1, 0) = (0, 3, 0)$ y el vector $(1, 1, 1)$ es autovector. Encuentre los autovalores y autoespacios asociados y justifique por qué son ortogonales.

### Resolución

Si se consideran $(\mathbb{R}^3, E)$ y suponemos que $T(0, 0, 1) = (a, b, c)$ se puede escribir

$$M(T) = \begin{pmatrix} 2 & 0 & a \\ 0 & 3 & b \\ 1 & 0 & c \end{pmatrix}$$

Como $A = A^t \Rightarrow a = 1,\; b = 0$, luego:

$$M(T) = \begin{pmatrix} 2 & 0 & 1 \\ 0 & 3 & 0 \\ 1 & 0 & c \end{pmatrix}$$

Por otro lado, como $(1, 1, 1)$ es autovector:

$$\begin{pmatrix} 2 & 0 & 1 \\ 0 & 3 & 0 \\ 1 & 0 & c \end{pmatrix} \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} = \lambda \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} \Rightarrow \begin{pmatrix} 3 \\ 3 \\ 1 + c \end{pmatrix} = \begin{pmatrix} \lambda \\ \lambda \\ \lambda \end{pmatrix} \Rightarrow \lambda = 3,\; c = 2$$

De donde $\lambda = 3$ es autovalor doble y $S_3 = \langle (0, 1, 0),\, (1, 1, 1)\rangle$. Para calcular el autovalor faltante se considera $S_3^\perp = \langle (1, 0, -1)\rangle$. Para sacar el autovalor faltante:

$$\begin{pmatrix} 2 & 0 & 1 \\ 0 & 3 & 0 \\ 1 & 0 & 2 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix} \Rightarrow \lambda = 1$$

Los autoespacios son ortogonales por ser $M(T)$ simétrica (teorema espectral).

## Ejercicio 3

Sea $A = \begin{pmatrix} 4 & 0 & 0 \\ 3 & -a & 3 \\ a+1 & -6 & 7 \end{pmatrix}$. Hallar los valores de $a \in \mathbb{R}$ para que $(1, 2, 3)$ sea autovector de $A$. Para el valor hallado dar si es posible una base $B = \{(1, 2, 3),\, v,\, w\}$ con $v, w$ autovectores de $A$.

### Resolución

Si $(1, 2, 3)$ es autovector de $A$ se debe cumplir:

$$\begin{pmatrix} 4 & 0 & 0 \\ 3 & -a & 3 \\ a+1 & -6 & 7 \end{pmatrix} \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} = \lambda \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} \Rightarrow \begin{pmatrix} 4 \\ 12 - 2a \\ a + 10 \end{pmatrix} = \begin{pmatrix} \lambda \\ 2\lambda \\ 3\lambda \end{pmatrix} \Rightarrow \lambda = 4,\; a = 2$$

Para hallar la base se buscan los otros autovalores. Reemplazando $a = 2$:

$$A = \begin{pmatrix} 4 & 0 & 0 \\ 3 & -2 & 3 \\ 3 & -6 & 7 \end{pmatrix},\quad A_\lambda = \lambda I - A = \begin{pmatrix} \lambda - 4 & 0 & 0 \\ -3 & \lambda + 2 & -3 \\ -3 & 6 & \lambda - 7 \end{pmatrix}$$

$$p_A(\lambda) = \begin{vmatrix} \lambda - 4 & 0 & 0 \\ -3 & \lambda + 2 & -3 \\ -3 & 6 & \lambda - 7 \end{vmatrix} = (\lambda - 4)\left[(\lambda + 2)(\lambda - 7) + 18\right] = (\lambda - 4)(\lambda^2 - 5\lambda + 4)$$

$$p_A(\lambda) = 0 \iff \lambda_{1,2} = \tfrac{5 \pm 3}{2} \Rightarrow \lambda_1 = 4,\; \lambda_2 = 1 \Rightarrow p_A(\lambda) = (\lambda - 4)^2(\lambda - 1)$$

Calculamos los autovectores. Para $\lambda = 1$:

$$A_1 = \begin{pmatrix} -3 & 0 & 0 \\ -3 & 3 & -3 \\ -3 & 6 & -6 \end{pmatrix} \Rightarrow x = 0,\; y = z \Rightarrow v_1 = (0, 1, 1)$$

Hasta acá la base quedaría $B = \{(1, 2, 3),\, v,\, (0, 1, 1)\}$. Para $\lambda = 4$:

$$A_4 = \begin{pmatrix} 0 & 0 & 0 \\ -3 & 6 & -3 \\ -3 & 6 & -3 \end{pmatrix} \Rightarrow -3x + 6y - 3z = 0 \Rightarrow z = 2y - x$$

Para completar la base se hace:

$$\begin{vmatrix} 1 & 2 & 3 \\ 0 & 1 & 1 \\ a & b & 2b - a \end{vmatrix} \ne 0 \Rightarrow 2b - a - b - a \ne 0 \Rightarrow b \ne 2a$$

Se elige $v_4 = (1, 1, 1)$. Luego $B = \{(1, 2, 3),\, (1, 1, 1),\, (0, 1, 1)\}$.

## Ejercicio 4

Sea $F : \mathbb{R}^3 \to \mathbb{R}^3$ una transformación lineal tal que

$$M(F)_{EE} = \begin{pmatrix} 1 & 0 & 1 \\ 0 & k & 1 \\ 0 & 9 & k \end{pmatrix}$$

**a)** Hallar todos los valores de $k$ para los cuales $F$ es diagonalizable.

**b)** Para $k = 3$ hallar una base $B$ de $\mathbb{R}^3$ tal que $M(F)_{BB}$ sea diagonal y dar la expresión de $M(F)_{BB}$.

### Resolución

Se rebautiza $A = M(F)_{EE}$. Luego:

$$A_\lambda = \begin{pmatrix} \lambda - 1 & 0 & -1 \\ 0 & \lambda - k & -1 \\ 0 & -9 & \lambda - k \end{pmatrix}$$

$$p_A(\lambda) = (\lambda - 1)\left[(\lambda - k)^2 - 9\right]$$

$$p_A(\lambda) = (\lambda - 1)[\lambda - (k + 3)][\lambda - (k - 3)]$$

Claramente $k + 3 \ne k - 3$. Se analizan casos:

**i)** Si $k + 3 \ne 1$ y $k - 3 \ne 1$, o sea $k \ne -2$ y $k \ne 4$, es diagonalizable.

**ii)** Si $k = -2$:

$$p_A(\lambda) = (\lambda - 1)^2(\lambda + 5),\quad A_1 = \begin{pmatrix} 0 & 0 & -1 \\ 0 & 3 & -1 \\ 0 & -9 & 3 \end{pmatrix} \Rightarrow z = 0,\; y = 0$$

Hay un solo autovector $v_1 = (1, 0, 0)$. No es diagonalizable.

**iii)** Si $k = 4$:

$$p_A(\lambda) = (\lambda - 1)^2(\lambda - 7),\quad A_1 = \begin{pmatrix} 0 & 0 & -1 \\ 0 & -3 & -1 \\ 0 & -9 & -3 \end{pmatrix} \Rightarrow z = 0,\; y = 0$$

Hay un solo autovector $v_1 = (1, 0, 0)$. No es diagonalizable.

Finalmente solo será diagonalizable si $k \in \mathbb{R} - \{-2, 4\}$.

**b)** Si $k = 3$:

$$A_\lambda = \begin{pmatrix} \lambda - 1 & 0 & -1 \\ 0 & \lambda - 3 & -1 \\ 0 & -9 & \lambda - 3 \end{pmatrix} \Rightarrow p_A(\lambda) = (\lambda - 1)[(\lambda - 3)^2 - 9] = \lambda(\lambda - 1)(\lambda - 6)$$

Para $\lambda = 0$:

$$A_0 = \begin{pmatrix} -1 & 0 & -1 \\ 0 & -3 & -1 \\ 0 & -9 & -3 \end{pmatrix} \Rightarrow z = -3y,\; x = 3y \Rightarrow v_0 = (3, 1, -3)$$

Para $\lambda = 1$:

$$A_1 = \begin{pmatrix} 0 & 0 & -1 \\ 0 & -2 & -1 \\ 0 & -9 & -2 \end{pmatrix} \Rightarrow z = y = 0 \Rightarrow v_1 = (1, 0, 0)$$

Para $\lambda = 6$:

$$A_6 = \begin{pmatrix} 5 & 0 & -1 \\ 0 & 3 & -1 \\ 0 & -9 & 3 \end{pmatrix} \Rightarrow z = 3y = 5x \Rightarrow v_6 = (3, 5, 15)$$

$$B = \{(3, 1, -3),\, (1, 0, 0),\, (3, 5, 15)\},\quad M(T)_{BB} = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 6 \end{pmatrix}$$

## Ejercicio 5

Sean $B_1 = \{(1, 2, 3),\, (0, 1, 1),\, (0, 1, -1)\}$ y $B_2 = \{(0, 0, 1),\, (1, 0, 0),\, (0, -1, 0)\}$ dos bases de $\mathbb{R}^3$ y $T : \mathbb{R}^3 \to \mathbb{R}^3$ una transformación lineal tal que

$$M(T)_{B_1 B_2} = \begin{pmatrix} 4 & 1 & 1 \\ k & 1 & -1 \\ -2 & -1 & -1 \end{pmatrix}$$

Hallar todos los valores reales de $K$ para que $w = (1, 0, 1)$ sea un autovector de $T$.

### Resolución

Si $w$ es autovector de $T$ se cumplirá $T(w) = \lambda w$ para algún $\lambda \in \mathbb{R}$. Luego $[T(w)]_{B_2} = \lambda [w]_{B_2}$. Por otro lado $[T(w)]_{B_2} = M(T)_{B_1 B_2} [w]_{B_1}$. Luego $M(T)_{B_1 B_2} [w]_{B_1} = \lambda [w]_{B_2}$.

Primero calculamos las coordenadas de $w$ en las bases $B_1$ y $B_2$:

**i) En $B_1$:** $(1, 0, 1) = \alpha (1, 2, 3) + \beta (0, 1, 1) + \gamma (0, 1, -1)$

$$\Rightarrow \alpha = 1,\; 2\alpha + \beta + \gamma = 0,\; 3\alpha + \beta - \gamma = 1 \Rightarrow \beta + \gamma = -2,\; \beta - \gamma = -2$$

$$\Rightarrow \beta = -2,\; \gamma = 0 \Rightarrow [w]_{B_1} = (1, -2, 0)$$

**ii) En $B_2$:** $(1, 0, 1) = \delta (0, 0, 1) + \mu (1, 0, 0) + \theta (0, -1, 0)$

$$\Rightarrow \mu = 1,\; \theta = 0,\; \delta = 1 \Rightarrow [w]_{B_2} = (1, 1, 0)$$

Aplicando:

$$\begin{pmatrix} 4 & 1 & 1 \\ k & 1 & -1 \\ -2 & -1 & -1 \end{pmatrix} \begin{pmatrix} 1 \\ -2 \\ 0 \end{pmatrix} = \lambda \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} \Rightarrow \begin{pmatrix} 2 \\ k - 2 \\ 0 \end{pmatrix} = \begin{pmatrix} \lambda \\ \lambda \\ 0 \end{pmatrix} \Rightarrow \lambda = 2,\; k = 4$$
