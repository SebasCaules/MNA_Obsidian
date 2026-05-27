---
tags: [pizarron, sistemas-parametricos, espacios-vectoriales, subespacios, independencia-lineal, espacio-funciones]
fuente: raw/Practicas/Pizarrones/Clase4 (1).pdf
tipo: escaneo
---

# Pizarrón — Clase 4: Repaso de sistemas paramétricos, espacios vectoriales, subespacios e independencia lineal

Esta clase mezcla cierre del ejercicio 1.10 (compatibilidad de un sistema paramétrico) con la introducción a la teoría de **espacios y subespacios vectoriales** (axiomas, ejemplos, contraejemplos) y un primer ejercicio de independencia lineal.

## Página 1 — Ejercicio 1.10: discusión del sistema

$$\begin{cases} 2x - 4y + 6z = 4 \\ -3x - 2y + 8z = 4 \\ 3y - z = k \end{cases}$$

¿Para qué valores de $k$ el sistema es compatible determinado (única solución)?

$$\begin{pmatrix} -2 & -4 & 6 \\ -3 & -3 & 8 \\ 0 & 3 & -1 \end{pmatrix}\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 4 \\ 4 \\ k \end{pmatrix} \;\Rightarrow\; A\vec x = \vec b$$

Si $A^{-1}$ existe, $\vec x = A^{-1} \vec b$. Cálculo $A^{-1} = \tfrac{1}{\det(A)} \operatorname{Adj}(A)$.

$$\det(A) = -6 - 54 + 0 - (0 - 48 - 12) = 0$$

> No es sistema compatible determinado (sino incompatible o compatible indeterminado).

**(b)** ¿Para qué valores de $k$ es compatible indeterminado?

$$\begin{pmatrix} -2 & -4 & 6 \\ -3 & -3 & 8 \\ 0 & 3 & -1 \end{pmatrix}\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 4 \\ 4 \\ k \end{pmatrix}$$

$$\begin{cases} -2x - 4y + 6z = 4 \quad (1) \\ -3x - 3y + 8z = 4 \quad (2) \\ 3y - z = k \quad (3) \end{cases}$$

Visto en forma de combinación lineal: $x\,\vec a_1 + y\,\vec a_2 + z\,\vec a_3 = \vec b$ con
$$\vec a_1 = \begin{pmatrix} -2 \\ -3 \\ 0 \end{pmatrix},\; \vec a_2 = \begin{pmatrix} -4 \\ -3 \\ 3 \end{pmatrix},\; \vec a_3 = \begin{pmatrix} 6 \\ 8 \\ -1 \end{pmatrix},\; \vec b = \begin{pmatrix} 4 \\ 4 \\ k \end{pmatrix}.$$

De (3): $z = 3y - k$. Reemplazando:
$$\begin{cases} -2x - 4y + 6(3y - k) = 4 \\ -3x - 3y + 8(3y - k) = 4 \end{cases}$$

## Página 2 — Despeje y caso $k = -2$

$$\begin{cases} -2x + 14y = 4 + 6k \\ -3x + 21y = 4 + 8k \end{cases} \;\Rightarrow\; \begin{cases} -x + 7y = 2 + 3k \\ -x + 7y = \tfrac{4 + 8k}{3} \end{cases}$$

Para que sea compatible, las dos ecuaciones deben coincidir:
$$2 + 3k = \tfrac{4 + 8k}{3} \;\Rightarrow\; 6 + 9k = 4 + 8k \;\Rightarrow\; \boxed{k = -2}.$$

**Verificación $k = -2$:**
$$\begin{cases} -2x - 4y + 6z = 4 \\ -3x - 3y + 8z = 4 \\ 3y - z = -2 \;\Rightarrow\; z = 3y + 2 \end{cases} \;\Rightarrow\; \begin{cases} -x - y - 2z = 0 \\ \cdots \end{cases}$$

Reemplazando $z$ en la primera:
$$-x - y - 2(3y + 2) = 0 \;\Rightarrow\; -x - 7y - 4 = 0 \;\Rightarrow\; \boxed{x = -7y - 4} \quad (\text{con signo: } x = -4 - 7y)$$

Equivalentemente, en la transcripción del pizarrón:
$$\vec x = \begin{pmatrix} 4 + 7y \\ y \\ 3y + 2 \end{pmatrix} = \begin{pmatrix} 7y \\ y \\ 3y \end{pmatrix} + \begin{pmatrix} 4 \\ 0 \\ 2 \end{pmatrix} = y\,(7, 1, 3) + (4, 0, 2)^\top.$$

Con $k \neq -2$, el sistema es **incompatible**.

**Sistema homogéneo asociado** ($\vec b = \vec 0$):
$$\begin{cases} -2x - 4y + 6z = 0 \\ -3x - 3y + 8z = 0 \\ 3y - z = 0 \;\Rightarrow\; z = 3y \end{cases} \;\Rightarrow\; \begin{cases} -x - y - 6y = 0 \;\Rightarrow\; x = -7y \end{cases}$$

$$\operatorname{sol}: \vec x_h = \begin{pmatrix} 7y \\ y \\ 3y \end{pmatrix} \quad \text{(con signo según despeje)}.$$

## Página 3 — Ejercicio 3: espacio de funciones $\mathbb{R} \to \mathbb{R}$

**Ejercicio 1) (sección 3).** $V = \{f : \mathbb{R} \to \mathbb{R}\}$. $f$ función. Operaciones:
$$+: (f + g)(x) = f(x) + g(x), \quad \forall x \in \mathbb{R}$$
$$\cdot: (\alpha \cdot f)(x) = \alpha f(x), \quad \forall x \in \mathbb{R}$$

**Verificación de axiomas** con $f, g, h \in V$, $\alpha, b \in \mathbb{R}$:

1. **Asociatividad de la suma:**
$$(f + (g + h))(x) = f(x) + (g + h)(x) = f(x) + g(x) + h(x) = ((f + g) + h)(x).$$

2. **Conmutatividad:**
$$(f + g)(x) = f(x) + g(x) = g(x) + f(x) = (g + f)(x).$$

3. **Elemento neutro $z(x) \equiv 0$** ($z \in V$):
$$(z + f)(x) = z(x) + f(x) = 0 + f(x) = f(x).$$

4. **Opuesto $\bar f(x) = -f(x)$**:
$$(f + \bar f)(x) = f(x) + \bar f(x) = f(x) + (-f(x)) = 0 = z(x).$$

5. **Asociatividad del escalar:** $(a(bf))(x) = a\,(bf)(x) = a\, b\, f(x) = (ab f)(x).$

6. **Neutro multiplicativo:** $(1\cdot f)(x) = 1\cdot f(x) = f(x).$

7. **Distributividad escalar:** $(a(f + g))(x) = a(f + g)(x) = a(f(x) + g(x)) = a f(x) + a g(x) = (af + ag)(x).$

## Página 4 — Cierre del ejercicio 3 y subespacio en $\mathbb{R}^2$

8. **Distributividad vectorial:** $((a + b)f)(x) = (a + b)f(x) = af(x) + bf(x) = (af + bf)(x).$

$$\therefore\; (V, +; \mathbb{R}, \cdot)\; \text{es espacio vectorial.}$$

**Ejercicio 4.a)** $A = \{(x_1, x_2) \in \mathbb{R}^2 \mid x_1 = 0\}$. Ver si $A$ es subespacio de $\mathbb{R}^2$.

**Definición.** Diremos que $(S \subseteq V,\; +; \mathbb{K}, \cdot)$ es subespacio vectorial sobre un cuerpo de escalares $\mathbb{K}$ si:
- $S \neq \emptyset$,
- $\vec s_1, \vec s_2 \in S \;\Rightarrow\; \vec s_1 + \vec s_2 \in S$,
- $\lambda \in \mathbb{K}, \vec s \in S \;\Rightarrow\; \lambda \vec s \in S$.

Para $A$: $\vec 0 = \binom{0}{0} \in S \;\Rightarrow\; S \neq \emptyset$.

Como todos los vectores de $S$ son $\vec s = \binom{0}{\alpha}$ con $\alpha \in \mathbb{R}$, y $\vec 0 \in S$:

Sean $\vec s_1, \vec s_2 \in S$, $\vec s_1 = \binom{0}{\alpha_1}$, $\vec s_2 = \binom{0}{\alpha_2}$ con $\alpha_1, \alpha_2 \in \mathbb{R}$:
$$\vec s(\vec s_1 + \vec s_2) = \binom{0}{\alpha_1} + \binom{0}{\alpha_2} = \binom{0}{\alpha_1 + \alpha_2} = \binom{0}{\alpha_3} \in S$$

$$\vec s_4 = (\lambda \vec s_1) = \lambda \binom{0}{\alpha_1} = \binom{0}{\lambda \alpha_1} = \binom{0}{\alpha_4} \in S, \quad \alpha_4 \in \mathbb{R}$$

$$\therefore\; S\text{ es subespacio vectorial.}$$

> Esquema: $S$ es el eje $x_2$ de $\mathbb{R}^2$ (recta vertical por el origen).

## Página 5 — Ejercicio 5.d / 5.e: $S = \{\alpha i\}$ en $\mathbb{C}$

**5.d)** $V = \mathbb{C}$, $\mathbb{K} = \mathbb{R}$, $S = \{\alpha i \mid \alpha \in \mathbb{R}\}$.

Como los elementos de $S$ son los números complejos $z = \alpha i$:

> Esquema: en el plano complejo, $S$ es el eje imaginario.

Sean $z_1, z_2 \in S$ y $\alpha \in \mathbb{R}$:
- $z_1 = x_1 i,\; z_2 = x_2 i \;\Rightarrow\; |S| \neq \emptyset$.
- $z_3 = z_1 + z_2 = x_1 i + x_2 i = (x_1 + x_2)i$, con $(x_1 + x_2) \in \mathbb{R}$, $\Rightarrow z_3 \in S$. $\checkmark$
- $z_5 = (\lambda z_1) = \lambda z_1 = \lambda x_1 i = (\lambda x_1) i$ con $\lambda x_1 \in \mathbb{R}$, $\Rightarrow z_5 \in S$. $\checkmark$

$$\therefore\; S\text{ es subespacio vectorial de }\mathbb{C}.$$

**5.e)** $V = \mathbb{C}$, $\mathbb{K} = \mathbb{C}$, $S = \{\alpha i \mid \alpha \in \mathbb{R}\}$.

Sean $z_1, z_2 \in S$ y $\alpha \in \mathbb{C}$. $z_1 = x_1 i, z_2 = x_2 i$ con $x_1, x_2 \in \mathbb{R}$.

## Página 6 — 5.e (contraejemplo) y ejercicio 6

$z_3 = z_1 + z_2 = (x_1 + x_2)i$ con $x_1 + x_2 \in \mathbb{R}$. $\Rightarrow z_3 \in S$ $\checkmark$

$z_4 = (\alpha z_1) = \alpha z_1 = (a + ib)\,x_1 i = (a x_1)i - b x_1$ con $-bx_1 \in \mathbb{R}$, $a x_1 \in \mathbb{R}$.

$\Rightarrow z_4 \notin S$ (tiene parte real $\neq 0$).

$$\therefore\; S\text{ NO es subespacio vectorial de }(\mathbb{C}, +; \mathbb{C}, \cdot).$$

**Ejercicio 6.a)** $\left\{ \binom{1}{2}{0}, \binom{1}{1}{1}, \binom{0}{1}{1 - k}\right\}$ — quizá agrupados como vectores de $\mathbb{R}^3$: $\vec s_1 = (1, 2, k)$, $\vec s_2 = (1, 1, 1)$, $\vec s_3 = (0, 1, 1 - k)$. ¿Son LI?

> ⚠️ La notación en el pizarrón muestra los vectores apilados; según el contexto se trata de tres vectores en $\mathbb{R}^3$ con parámetro $k$.

**Independencia lineal.** $c_1 \vec s_1 + c_2 \vec s_2 + \cdots + c_n \vec s_n = \vec 0$ $\;\Rightarrow\;$ $\{\vec s_1, \dots, \vec s_n\}$ son LI $\;\Leftrightarrow\;$ $c_1 = c_2 = \cdots = c_n = 0$.

Aplicado:
$$\alpha \vec s_1 + \beta \vec s_2 + \gamma \vec s_3 = \vec 0$$
$$\alpha\binom{1}{2}{k} + \beta\binom{1}{1}{1} + \gamma\binom{0}{1}{1 - k} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$$
$$\begin{cases} \alpha + \beta + 0\gamma = 0 \\ 2\alpha + \beta + \gamma = 0 \\ k\alpha + \beta + \gamma(1 - k) = 0 \end{cases} \;\Rightarrow\; \underbrace{\begin{pmatrix} 1 & 1 & 0 \\ 2 & 1 & 1 \\ k & 1 & 1 - k \end{pmatrix}}_{A}\,\underbrace{\begin{pmatrix} \alpha \\ \beta \\ \gamma \end{pmatrix}}_{\vec x} = \underbrace{\begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}}_{\vec 0}$$

$A\vec x = \vec 0$ — sistema homogéneo.

## Página 7 — Cierre de 6.a

Si $\det(A) \neq 0$, $A$ es invertible, $\vec x = \vec 0$, $\Rightarrow \alpha = 0, \beta = 0, \gamma = 0$, $\Rightarrow \vec s_1, \vec s_2, \vec s_3$ son LI.

$$\det(A) = \begin{vmatrix} 1 & 1 & 0 \\ 2 & 1 & 1 \\ k & 1 & 1 - k \end{vmatrix} = \big((1 - k) + 0 + k\big) - \big(1 + 2(1 - k)\big) = 1 - k + k - 1 - 2 + 2k = 2k - 2 = 2(k - 1).$$

(La cuenta del pizarrón llega a $-2 + 2k = 2(k - 1)$.)

$\therefore$ Cuando $k \neq 1 \Rightarrow \det(A) \neq 0 \Rightarrow \alpha = 0,\; \beta = 0,\; \gamma = 0 \Rightarrow \{\vec s_1, \vec s_2, \vec s_3\}$ son LI.

Con $k = 1$ no son LI (son **LD**).

**Comprobación $k = 1$:** $\vec s_1 = \binom{1}{2}{1},\; \vec s_2 = \binom{1}{1}{1},\; \vec s_3 = \binom{0}{1}{0}$.

$$\vec s_3 = \vec s_1 - \vec s_2 = \binom{1}{2}{1} - \binom{1}{1}{1} = \binom{0}{1}{0}.\;\checkmark$$
