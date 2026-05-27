---
tags: [pizarron, vectores-complejos, sistemas-lineales, combinacion-lineal, matrices-idempotentes]
fuente: raw/Practicas/Pizarrones/Clase2 (1).pdf
tipo: escaneo
---

# Pizarrón — Clase 2: Vectores en $\mathbb{C}^n$, sistemas lineales y matrices idempotentes

Continuación de la práctica. Repaso de partes real/imaginaria para vectores complejos, sistemas $Ax = b$ (compatibles / incompatibles), combinaciones lineales y resolución de $A^2 = A$.

## Página 1 — Ejercicio 3: parte real e imaginaria de un vector complejo

Si $\vec a \in \mathbb{C}^n$, escribir $\vec a = \binom{a + iy}{x + iy} = \binom{a}{x} + i\binom{b}{y}$ (versión $\mathbb{C}^2$):

$$\operatorname{Re}\{\vec a\} = \binom{a}{x}, \qquad \operatorname{Im}\{\vec a\} = \binom{b}{y}.$$

**Ejemplo.** $\vec a_1 = \binom{1 + i}{3 - 2i}$, $\vec a_2 = \binom{10 + 8i}{5 + i\sqrt{3}}$ en $\mathbb{C}^2$.

$$\operatorname{Re}\{\vec a_1\} = \binom{1}{3}, \quad \operatorname{Im}\{\vec a_1\} = \binom{1}{-2}$$
$$\operatorname{Re}\{\vec a_2\} = \binom{10}{5}, \quad \operatorname{Im}\{\vec a_2\} = \binom{8}{\sqrt{3}}$$

$$\vec a_1 + \vec a_2 = \binom{1 + i + 10 + 8i}{3 - 2i + 5 + i\sqrt{3}} = \binom{11 + 9i}{8 + i(\sqrt{3} - 2)}$$

Con $\alpha = i\sqrt{3}$:
$$\alpha \vec a_1 = i\sqrt{3}\binom{1 + i}{3 - 2i} = \binom{i\sqrt{3} - \sqrt{3}}{3i\sqrt{3} + 2\sqrt{3}}.$$

**Ejercicio 5.** $\vec v = \binom{1}{2}$, $\vec u_1 = \binom{1}{1}$, $\vec u_2 = \binom{1}{-1}$, $\vec u_3 = \binom{1}{-3}$.

Combinación lineal: $\vec v = \alpha \vec u_1 + \beta \vec u_2 + \gamma \vec u_3$, $\alpha, \beta, \gamma \in \mathbb{R}$.

$$\binom{1}{2} = \alpha\binom{1}{1} + \beta\binom{1}{-1} + \gamma\binom{1}{-3} = \binom{\alpha + \beta + \gamma}{\alpha - \beta - 3\gamma}$$

Sistema:
$$\begin{cases} \alpha + \beta + \gamma = 1 \\ \alpha - \beta - 3\gamma = 2 \end{cases}$$

(Etiquetado como "sistema de ecuaciones" en el pizarrón.)

## Página 2 — Sistema $Ax = b$: clasificación y resolución

$$\begin{pmatrix} 1 & 1 & 1 \\ 1 & -1 & -3 \end{pmatrix} \begin{pmatrix} \alpha \\ \beta \\ \gamma \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \end{pmatrix} \;\Rightarrow\; A\vec x = \vec b$$

**Clasificación de sistemas:**
- **Incompatible** (no existe solución).
- **Compatible indeterminado** (tiene infinitas soluciones).
- **Compatible determinado** (tiene una única solución).

Para este sistema:
$$\begin{cases} \alpha + \beta + \gamma = 1 \quad (\text{I}) \\ \alpha - \beta - 3\gamma = 2 \quad (\text{II}) \end{cases}$$

De (II): $\alpha = \beta + 3\gamma + 2$.

Reemplazando en (I): $\beta + 3\gamma + 2 + \beta + \gamma = 1 \;\Rightarrow\; 2\beta + 4\gamma = -1 \;\Rightarrow\; \beta + 2\gamma = -\tfrac{1}{2}$.

$$\boxed{\;\beta = -\tfrac{1}{2} - 2\gamma\;}$$

$$\alpha = \beta + 3\gamma + 2 = -\tfrac{1}{2} - 2\gamma + 3\gamma + 2 = \tfrac{3}{2} + \gamma$$

**Solución del sistema:**
$$\boxed{\;\operatorname{sol}: \begin{pmatrix} \tfrac{3}{2} + \gamma \\ -\tfrac{1}{2} - 2\gamma \\ \gamma \end{pmatrix}\;} \;\Rightarrow\; \vec x = \underbrace{\begin{pmatrix} \tfrac{3}{2} \\ -\tfrac{1}{2} \\ 0 \end{pmatrix}}_{\vec x_p \text{ (solución particular)}} + \gamma\, \underbrace{\begin{pmatrix} 1 \\ -2 \\ 1 \end{pmatrix}}_{\vec x_h \text{ (sol. del homogéneo)}}$$

**Sistema homogéneo asociado** $A\vec x = \vec 0$:
$$\begin{cases} \alpha + \beta + \gamma = 0 \quad (\text{I}) \\ \alpha - \beta - 3\gamma = 0 \quad (\text{II}) \end{cases}$$

(I) + (II): $2\alpha - 2\gamma = 0 \;\Rightarrow\; \alpha = \gamma$.
(I) − (II): $2\beta + 4\gamma = 0 \;\Rightarrow\; \beta = -2\gamma$.

$$\operatorname{sol\ del\ homogéneo}: \begin{pmatrix} \gamma \\ -2\gamma \\ \gamma \end{pmatrix}.$$

## Página 3 — Verificación, escalonamiento y ejercicio 7

**Verificar que $\vec x_p$ es solución del sistema:**
$$A \vec x_p = \begin{pmatrix} 1 & 1 & 1 \\ 1 & -1 & -3 \end{pmatrix}\begin{pmatrix} \tfrac{3}{2} \\ -\tfrac{1}{2} \\ 0 \end{pmatrix} = \begin{pmatrix} \tfrac{3}{2} - \tfrac{1}{2} + 0 \\ \tfrac{3}{2} + \tfrac{1}{2} + 0 \end{pmatrix} = \binom{1}{2}.\;\checkmark$$

**Test** para $\gamma = 1$: $\beta = -\tfrac{1}{2} - 2 = -\tfrac{5}{2}$, $\alpha = \tfrac{3}{2} + 1 = \tfrac{5}{2}$.

Comprobación con la combinación: $\tfrac{5}{2}\binom{1}{1} - \tfrac{5}{2}\binom{1}{-1} + \binom{1}{-3} = \binom{1}{2}.\;\checkmark$

**Resolución por escalonamiento.**
$$\begin{cases} \alpha + \beta + \gamma = 1 \\ \alpha - \beta - 3\gamma = 2 \end{cases} \;\Rightarrow\; A = \begin{pmatrix} 1 & 1 & 1 \\ 1 & -1 & -3 \end{pmatrix},\quad b = \binom{1}{2}$$

$$\left(\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\ 1 & -1 & -3 & 2 \end{array}\right) \xrightarrow{F_2 - F_1} \left(\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\ 0 & -2 & -4 & 1 \end{array}\right) \xrightarrow{\tfrac{1}{-2}F_2} \left(\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\ 0 & 1 & 2 & -\tfrac{1}{2} \end{array}\right)$$

$$\begin{cases} \alpha + \beta + \gamma = 1 \\ \beta + 2\gamma = -\tfrac{1}{2} \end{cases}$$

**Ejercicio 7.** $\vec v = \begin{pmatrix} 2 \\ -5 \\ 3 \end{pmatrix}$, $\vec\omega_1 = \begin{pmatrix} 1 \\ -3 \\ 2 \end{pmatrix}$, $\vec\omega_2 = \begin{pmatrix} 2 \\ -4 \\ -1 \end{pmatrix}$, $\vec\omega_3 = \begin{pmatrix} 1 \\ -5 \\ 1 \end{pmatrix}$.

$\vec v = \alpha \vec\omega_1 + \beta \vec\omega_2 + \gamma \vec\omega_3$:

$$\begin{cases} \alpha + 2\beta + \gamma = 2 \\ -3\alpha - 4\beta - 5\gamma = -5 \\ 2\alpha + \beta - \gamma = 1 \end{cases} \;\Rightarrow\; A = \begin{pmatrix} 1 & 2 & 1 \\ -3 & -4 & -5 \\ 2 & 1 & -1 \end{pmatrix},\quad b = \begin{pmatrix} 2 \\ -5 \\ 3 \end{pmatrix}$$

$$\vec x = \begin{pmatrix} \alpha \\ \beta \\ \gamma \end{pmatrix}$$

## Página 4 — Inversa, triangulación y resolución

$A\vec x = \vec b$, si existe $A^{-1}$, entonces $A^{-1} A \vec x = A^{-1} \vec b \;\Rightarrow\; \vec x = A^{-1} \vec b$ (recordando $A^{-1} A = I$).

Calcular $A^{-1}$ por Gauss-Jordan partiendo de $[A \mid I]$:

$$\left(\begin{array}{ccc|ccc} 1 & 2 & 1 & 1 & 0 & 0 \\ -3 & -4 & -5 & 0 & 1 & 0 \\ 2 & -1 & 1 & 0 & 0 & 1 \end{array}\right) \xrightarrow[F_3 - 2F_1]{F_2 + 3F_1} \left(\begin{array}{ccc|ccc} 1 & 2 & 1 & 1 & 0 & 0 \\ 0 & 2 & -2 & 3 & 1 & 0 \\ 0 & -3 & -1 & -2 & 0 & 1 \end{array}\right) \xrightarrow{F_3 + \tfrac{3}{2}F_2} \cdots$$

> ⚠️ El profesor abandona el cálculo de la inversa y prefiere triangular el sistema directamente.

**Triangulando el sistema** $A\vec x = \vec b$:
$$\begin{pmatrix} \lambda_1 & 0 & 0 \\ 0 & \lambda_2 & 0 \\ 0 & 0 & \lambda_3 \end{pmatrix}\begin{pmatrix} \alpha \\ \beta \\ \gamma \end{pmatrix} = \begin{pmatrix} 2 \\ -5 \\ 1 \end{pmatrix}$$

(Notación: forma diagonal de referencia; en la práctica triangula superior.)

$$\left(\begin{array}{ccc|c} 1 & 2 & 1 & 2 \\ -3 & -4 & -5 & -5 \\ 2 & -1 & 1 & 1 \end{array}\right) \xrightarrow[F_3 - 2F_1]{F_2 + 3F_1} \left(\begin{array}{ccc|c} 1 & 2 & 1 & 2 \\ 0 & 2 & -2 & 1 \\ 0 & -3 & -1 & -3 \end{array}\right) \xrightarrow{F_3 + \tfrac{3}{2}F_2} \left(\begin{array}{ccc|c} 1 & 2 & 1 & 2 \\ 0 & 2 & -2 & 1 \\ 0 & 0 & -6 & -\tfrac{3}{2} \end{array}\right)$$

$$\begin{cases} \alpha + 2\beta + \gamma = 2 \\ 2\beta - 2\gamma = 1 \\ -6\gamma = -\tfrac{3}{2} \end{cases} \;\Rightarrow\; \gamma = \tfrac{1}{4}$$

Sustitución regresiva:
$$\begin{cases} \alpha + 2\beta + \tfrac{1}{4} = 2 \\ 2\beta - \tfrac{1}{2} = 1 \;\Rightarrow\; \beta = (1 + \tfrac{1}{2})/2 = \tfrac{3}{4} \end{cases}$$

## Página 5 — Ejercicio: $A^2 = A$ con $A \in \mathbb{R}^{2\times 2}$

**Ejercicio.** $A \in \mathbb{R}^{2\times 2}$, $A^2 = A$. Hallar todas las matrices que cumplen esta condición (matrices **idempotentes**).

$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}, \qquad A^2 = A \cdot A = \begin{pmatrix} a^2 + bc & ab + bd \\ ca + dc & cb + d^2 \end{pmatrix} = A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$$

Sistema:
$$\begin{cases} a^2 + bc = a \\ b(a + d) = b \\ c(a + d) = c \\ d^2 + bc = d \end{cases}$$

Reorganizando:
$$\begin{cases} a^2 + bc = a \\ b(a + d - 1) = 0 \\ c(a + d - 1) = 0 \\ d^2 + bc = d \end{cases}$$

**Caso 1: $b = 0 \land c = 0$.**
$$\begin{cases} a^2 = a \;\Rightarrow\; a(a - 1) = 0 \\ d^2 = d \;\Rightarrow\; d(d - 1) = 0 \end{cases}$$

Soluciones:
| $a$ | $b$ | $c$ | $d$ |
|----|----|----|----|
| 0  | 0  | 0  | 0  |
| 1  | 0  | 0  | 1  |
| 0  | 0  | 0  | 1  |
| 1  | 0  | 0  | 0  |

Matrices: $\begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix},\; \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix},\; \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix},\; \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}.$

**Caso 2: $a + d - 1 = 0 \;\Rightarrow\; d = 1 - a$.**
$$\begin{cases} a^2 + bc = a \\ (1 - a)^2 + bc = 1 - a \end{cases} \;\Rightarrow\; a^2 - a + bc = 0$$

Desarrollando la segunda: $1 - 2a + a^2 + bc = 1 - a \;\Rightarrow\; a^2 - a + bc = 0$ (idéntica a la primera).

$$\boxed{\;a^2 - a + bc = 0\;}$$

## Página 6 — Cierre del caso 2

$$\boxed{\;a^2 - a + bc = 0\;} \;\Leftrightarrow\; a(a - 1) + bc = 0$$

La familia de soluciones es
$$A = \begin{pmatrix} a & b \\ c & 1 - a \end{pmatrix} \quad \text{con } a^2 - a + bc = 0.$$

> Esto define una variedad 2-paramétrica de matrices idempotentes (con $\operatorname{tr}(A) = 1$), junto con los 4 casos diagonales del Caso 1 (de los cuales $I$ y $\mathbf{0}$ son las idempotentes triviales, y los otros dos también satisfacen $\operatorname{tr}(A) = 1$ ó $0$).
