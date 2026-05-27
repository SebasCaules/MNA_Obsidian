---
tags: [pizarron, determinantes, sarrus, cofactores, propiedades-determinante, matriz-singular, sistemas-parametricos]
fuente: raw/Practicas/Pizarrones/clase_3.pdf
tipo: escaneo
---

# Pizarrón — Clase 3: Determinantes, propiedades y discusión de sistemas paramétricos

Tema: cálculo de determinantes (Sarrus, cofactores), propiedades, búsqueda de valores que vuelven singular o invertible una matriz, y discusión de sistemas $Ax = b$ paramétricos por compatibilidad.

## Página 1 — Sarrus (3×3) y método de cofactores

**Regla de Sarrus (matrices 3×3).** Recordatorio 2×2: $\det = \begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc$.

**Ejercicio.** $M = \begin{pmatrix} 2 & 1 & 3 \\ -1 & 4 & 0 \\ 6 & -2 & 1 \end{pmatrix}$.

Por Sarrus (sumando diagonales descendentes y restando ascendentes; se replican abajo las dos primeras filas):
$$\det(M) = 2 \cdot 4 \cdot 1 + (-1)\cdot(-2)\cdot 3 + 6 \cdot 1 \cdot 0 \;-\; \big[6 \cdot 4 \cdot 3 + 2 \cdot (-2) \cdot 0 + (-1) \cdot 1 \cdot 1\big]$$
$$= 8 + 6 + 0 - [72 + 0 - 1] = 14 - 71 = \boxed{-57}.$$

**Método de adjuntos / cofactores** (para orden $n \geq 3$).

**Ejercicio.** $A = \begin{pmatrix} 1 & 0 & 2 & 0 \\ 3 & -1 & 1 & 0 \\ 0 & 2 & 0 & 1 \\ 4 & 0 & -2 & 1 \end{pmatrix}$. Desarrollo por la **columna 4** (tiene dos ceros).

$$\det A = a_{14} C_{14} + a_{24} C_{24} + a_{34} C_{34} + a_{44} C_{44}$$
$$C_{ij} = (-1)^{i+j} \cdot \operatorname{Menor}_{ij}$$

Como $a_{14} = a_{24} = 0$:
$$\det(A) = 1 \cdot (-1)^{3+4} \begin{vmatrix} 1 & 0 & 2 \\ 3 & -1 & 1 \\ 4 & 0 & -2 \end{vmatrix} + 1 \cdot (-1)^{4+4} \begin{vmatrix} 1 & 0 & 2 \\ 3 & -1 & 1 \\ 0 & 2 & 0 \end{vmatrix}$$

Primer menor (desarrollando por columna 2, que tiene un único $-1$ no nulo):
$$\begin{vmatrix} 1 & 0 & 2 \\ 3 & -1 & 1 \\ 4 & 0 & -2 \end{vmatrix} = (-1)\cdot(-1)^{2+2}\begin{vmatrix} 1 & 2 \\ 4 & -2 \end{vmatrix} = -1 \cdot (-2 - 8) = -1 \cdot (-10) = 10$$

(En el pizarrón aparece como $-1 \cdot [1 \cdot (-1)\cdot(-2) - (-8)] = -1 \cdot 10 = -10$, indicando el signo del cofactor por separado.)

Segundo menor:
$$\begin{vmatrix} 1 & 0 & 2 \\ 3 & -1 & 1 \\ 0 & 2 & 0 \end{vmatrix} = 12 - 2 = 10$$

$$\det(A) = -1\cdot 10 + 1 \cdot 10 = -10 + 10 = \boxed{0}.$$

## Página 2 — Propiedades de determinantes (operaciones por columnas)

**Ejercicio.** Se da $A = (A_1, A_2, A_3) \in \mathbb{R}^{3\times 3}$ con $\det(A) = -3$. Calcular $\det\!\big(\tfrac{3}{4} A^{-1} B^\top\big)$ donde $B = (A_1 - 3A_3,\; A_3,\; A_1 - A_2)$.

Propiedades:
$$\det\!\left(\tfrac{3}{4} A^{-1} B^\top\right) = \left(\tfrac{3}{4}\right)^3 \det(A^{-1}) \det(B^\top) \quad \text{[}\det(kM) = k^n \det(M),\; \det(MN) = \det(M)\det(N)\text{]}$$
$$= \tfrac{27}{64} \cdot \tfrac{1}{\det(A)} \cdot \det(B) \quad \text{[}\det(A^{-1}) = 1/\det(A),\; \det(B^\top) = \det(B)\text{]}$$

Cálculo de $\det(B)$ por operaciones de columna:
- $C_1 \to C_1 + 3C_2$: $\det(B) = \det(A_1, A_3, A_1 - A_2)$.

(Notación: las columnas son las dadas; $C_1 = A_1 - 3A_3$ pasa a $C_1 + 3 C_2 = A_1 - 3A_3 + 3A_3 = A_1$, asumiendo $C_2 = A_3$.)
- $C_3 \to C_3 - C_1$: $\det(B) = \det(A_1, A_3, -A_2)$.
- Factorizar el escalar $-1$ de la última columna: $\det(B) = (-1)\det(A_1, A_3, A_2)$.
- Intercambio $C_2 \leftrightarrow C_3$: $\det(B) = (-1)(-1) \det(A_1, A_2, A_3) = \det(A) = -3$.

$$\det\!\left(\tfrac{3}{4} A^{-1} B^\top\right) = \tfrac{27}{64} \cdot \tfrac{1}{-3} \cdot (-3) = \boxed{\tfrac{27}{64}}.$$

**Ejercicio.** Sea $A \in \mathbb{R}^{4\times 4}$ con $\det(A) = k \neq 0$. Calcular $\det\!\big(\tfrac{2}{3} B^{-1} A^2\big)$ donde $B = (A_1 - A_2,\; A_3 - 2A_4,\; A_3,\; A_2)$.

- $C_1 \to C_1 + C_4$: $\det(B) = \det(A_1,\; A_3 - 2A_4,\; A_3,\; A_2)$.
- $C_2 \to C_2 - C_3$: $\det(B) = \det(A_1,\; -2A_4,\; A_3,\; A_2) = -2\det(A_1, A_4, A_3, A_2)$.
- $C_4 \leftrightarrow C_2$: $\det(B) = -2\cdot(-1)\det(A_1, A_2, A_3, A_4) = 2 \cdot \det(A)$.

> ⚠️ En el pizarrón figura $\det(B) = -2\,\det(A) = -2k$ (el profesor cuenta sólo un intercambio implícito; corrige más adelante o asume orden distinto). Tomamos el valor que aparece en el pizarrón: $\det(B) = -2k$.

## Página 3 — Cierre del cálculo y matriz singular paramétrica

$$\det\!\left(\tfrac{2}{3} B^{-1} A^2\right) = \left(\tfrac{2}{3}\right)^4 \det(B^{-1}) \det(A^2) = \tfrac{16}{81}\cdot \tfrac{1}{\det(B)}\cdot \det(A)^2 = \tfrac{16}{81}\cdot \tfrac{1}{-2k}\cdot k^2 = \boxed{-\tfrac{8k}{81}}.$$

**Ejercicio.** Encontrar $k \in \mathbb{R}$ para que $A$ sea singular ($\det A = 0$), con
$$A = \begin{pmatrix} k - 1 & -2 & 3 \\ k + 2 & -1 & 0 \\ 0 & 0 & 3 - k \end{pmatrix}.$$

Desarrollando por la fila 3 (sólo un elemento no nulo):
$$\det(A) = (3 - k)\,\big[(k - 1)(-1) - (-2)(k + 2)\big] = (3 - k)\,[-k + 1 + 2k + 4] = (3 - k)(k + 5) = 0$$

$$\boxed{\text{Singular si } k = 3 \;\lor\; k = -5.}$$

**Ejercicio.** Hallar los valores de $k$ que hacen invertible a $P$ ($\det(P) \neq 0$):
$$P = \begin{pmatrix} 1 & 1 & 0 \\ -2k - 1 & 2 & 0 \\ 0 & 3 & k \end{pmatrix}.$$

Desarrollo por la columna 3 (solo el $k$ del elemento $P_{33}$ no es nulo):
$$\det(P) = k\,\begin{vmatrix} 1 & 1 \\ -2k - 1 & 2 \end{vmatrix} = k\,[2 - (-2k - 1)] = k(2k + 3) = 2k^2 + 3k.$$

$$\det(P) = 0 \;\Leftrightarrow\; k(2k + 3) = 0 \;\Leftrightarrow\; k = 0 \;\lor\; k = -\tfrac{3}{2}.$$

$$\boxed{P \text{ es invertible si } k \neq 0 \;\land\; k \neq -\tfrac{3}{2}.}$$

## Página 4 — Discusión de sistemas paramétricos: SCD / SCI / SI

**Ejercicio.**
$$\begin{cases} x + y + z = a \\ x - y = 0 \\ 3x + y + bz = 0 \end{cases} \;\Rightarrow\; A = \begin{pmatrix} 1 & 1 & 1 \\ 1 & -1 & 0 \\ 3 & 1 & b \end{pmatrix}$$

$$\det(A) = -b + 1 - [-3 + b] = -2b + 4.$$

**SCD** $\Leftrightarrow \det(A) \neq 0 \Leftrightarrow b \neq 2$, con $a \in \mathbb{R}$ y $b \in \mathbb{R} - \{2\}$.

**Si $b = 2$** ($\det A = 0$): escalonar matriz ampliada
$$\left(\begin{array}{ccc|c} 1 & 1 & 1 & a \\ 1 & -1 & 0 & 0 \\ 3 & 1 & 2 & 0 \end{array}\right) \xrightarrow[F_3 - 3F_1]{F_2 - F_1} \left(\begin{array}{ccc|c} 1 & 1 & 1 & a \\ 0 & -2 & -1 & -a \\ 0 & -2 & -1 & -3a \end{array}\right) \xrightarrow{F_3 - F_2} \left(\begin{array}{ccc|c} 1 & 1 & 1 & a \\ 0 & -2 & -1 & -a \\ 0 & 0 & 0 & -2a \end{array}\right)$$

- **SI** $\Leftrightarrow -2a \neq 0 \Leftrightarrow a \neq 0$.
- **SCI** $\Leftrightarrow -2a = 0 \Leftrightarrow a = 0$.

**Ejercicio.**
$$\begin{cases} -2x - 4y + 6z = 4 \\ -3x - 3y + 8z = 4 \\ 3y - z = k \end{cases} \;\Rightarrow\; A = \begin{pmatrix} -2 & -4 & 6 \\ -3 & -3 & 8 \\ 0 & 3 & -1 \end{pmatrix}$$

$$\det(A) = -6 - 54 - [-48 - 12] = -60 + 60 = 0 \;\Rightarrow\; A \text{ singular.}$$

- **SCD** $\Rightarrow$ nunca (el determinante es siempre 0).
- Analizar **SI / SCI**:

$$\left(\begin{array}{ccc|c} -2 & -4 & 6 & 4 \\ -3 & -3 & 8 & 4 \\ 0 & 3 & -1 & k \end{array}\right) \xrightarrow{F_1 / (-2)} \left(\begin{array}{ccc|c} 1 & 2 & -3 & -2 \\ -3 & -3 & 8 & 4 \\ 0 & 3 & -1 & k \end{array}\right) \xrightarrow{F_2 + 3F_1}$$

## Página 5 — Cierre de la discusión y SCI

$$\left(\begin{array}{ccc|c} 1 & 2 & -3 & -2 \\ 0 & 3 & -1 & -2 \\ 0 & 3 & -1 & k \end{array}\right) \xrightarrow{F_3 - F_2} \left(\begin{array}{ccc|c} 1 & 2 & -3 & -2 \\ 0 & 3 & -1 & -2 \\ 0 & 0 & 0 & k + 2 \end{array}\right)$$

- **SCI** $\Leftrightarrow k + 2 = 0 \Leftrightarrow k = -2$.
- **SI** $\Leftrightarrow k + 2 \neq 0 \Leftrightarrow k \neq -2$.

**Resolución en el caso SCI** ($k = -2$):
$$\begin{cases} x + 2y - 3z = -2 \quad (1) \\ 3y - z = -2 \;\Rightarrow\; z = 3y + 2 \end{cases}$$

Reemplazando en (1):
$$x + 2y - 3(3y + 2) = -2 \;\Rightarrow\; x + 2y - 9y - 6 = -2 \;\Rightarrow\; x = 7y + 4.$$

Parametrizando $y = t$:
$$(x, y, z) = (7t + 4,\; t,\; 3t + 2) = (7t,\; t,\; 3t) + (4,\; 0,\; 2) = t\,(7, 1, 3) + (4, 0, 2).$$
