---
tags: [pizarron, subespacios, polinomios, bases, producto-interno, proyeccion-ortogonal, l2]
fuente: raw/Practicas/Pizarrones/clase_5.pdf
tipo: escaneo
---

# Pizarrón — Clase 5: Subespacios en $\mathbb{R}^{n\times n}$ y $\mathbb{P}_2$, bases, producto interno, proyección y $L^2$

Cierre del bloque de subespacios + arranque de producto interno: ángulo entre vectores, proyección ortogonal, vector error y ortogonalidad de $\cos(kx), \sin(nx)$ en $L^2([0, 2\pi])$.

## Página 1 — 5c, 6b, 11b

**Ejercicio 5c.** Sea $V = \mathbb{R}^{2\times 2}$, $\mathbb{K} = \mathbb{R}$, $S = \{A \in \mathbb{R}^{2\times 2} \mid A \text{ es singular}\}$. ¿Es $S$ un subespacio?

- $\vec 0 \in S$ (la matriz nula tiene determinante 0). $\checkmark$
- $\forall u, v \in S \;\Rightarrow\; u + v \in S$ ?
- $\forall \vec s \in S,\; \lambda \in \mathbb{K} \;\Rightarrow\; \lambda \vec s \in S$ ?

**Contraejemplo (suma):** Tomar
$$A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \;\Rightarrow\; \det(A) = 0 \;\Rightarrow\; A \in S$$
$$B = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} \;\Rightarrow\; \det(B) = 0 \;\Rightarrow\; B \in S$$
$$A + B = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I \;\Rightarrow\; \det(I) = 1 \neq 0$$

$$\therefore\; \text{como lo pruebo no se cumple, NO es subespacio.}$$

**Ejercicio 6b.** $V = \mathbb{P}_2$ (polinomios de grado $\leq 2$), $S = \{p \in \mathbb{P}_2 \mid a_0 - a_1 + a_2 = 0 \;\land\; 2a_2 - a_0 = 0\}$.

$p(x) = a_2 x^2 + a_1 x + a_0$.

De la 2ª restricción: $a_0 = 2a_2$.
Sustituyendo en la 1ª: $2a_2 - a_1 + a_2 = 0 \;\Rightarrow\; a_1 = 3a_2$.

$$p(x) = a_2 x^2 + 3a_2 x + 2a_2 = a_2(x^2 + 3x + 2)$$

$S = \operatorname{gen}\{x^2 + 3x + 2\}$ $\Rightarrow$ $S$ es subespacio vectorial de dimensión 1.

**Ejercicio 11b.** Completa a una base de $\mathbb{R}_3[x]$ el conjunto linealmente independiente $S = \{x^3 - 2x + 1,\; x^3 + 3x\}$.

$\mathbb{R}_3[x]$ tiene $\dim = 4$. La base canónica es $B_c = \{1, x, x^2, x^3\}$.

Vectores de $S$ en coordenadas $(a_0, a_1, a_2, a_3)$:
$$p_1(x) = 1 - 2x + 0 x^2 + x^3 = (1, -2, 0, 1)$$

## Página 2 — Completar a base y verificar LI con determinante

$$p_2(x) = 0 + 3x + 0 x^2 + x^3 = (0, 3, 0, 1)$$
$$p_3(x) = x^2 = (0, 0, 1, 0)$$
$$p_4(x) = 1 = (1, 0, 0, 0)$$

(Se agregan $x^2$ y $1$ de la base canónica.)

Armamos la matriz con los 4 vectores como filas:
$$M = \begin{pmatrix} 1 & 0 & 0 & 1 \\ -2 & 3 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 1 & 1 & 0 & 0 \end{pmatrix}$$

Desarrollo por la columna 3 (sólo un elemento no nulo, $M_{33} = 1$):
$$\det(M) = 1 \cdot (-1)^{3+3}\,\begin{vmatrix} 1 & 0 & 1 \\ -2 & 3 & 0 \\ 1 & 1 & 0 \end{vmatrix} = 1 \cdot (-1)^{1+3}\begin{vmatrix} -2 & 3 \\ 1 & 1 \end{vmatrix} = (-2 - 3) = -5.$$

$\det(M) \neq 0 \Rightarrow$ los 4 vectores son LI.

$$\boxed{B = \{x^3 - 2x + 1,\; x^3 + 3x,\; x^2,\; 1\}}$$

## Página 3 — Producto interno: norma, ángulo, proyección

**Ejercicio 1 (b y c).** Para $\vec x_1 = (1, -1)^\top$ y $\vec y_1 = (-1, 1)^\top$, calcular ángulo y proyección de $\vec x_1$ sobre $\vec y_1$.

**a)** $|\langle \vec x_1, \vec y_1 \rangle| \leq \|\vec x_1\|\,\|\vec y_1\|$ (Cauchy-Schwarz).

$$\langle \vec x_1, \vec y_1\rangle = 1\cdot(-1) + (-1)\cdot 1 = -2$$
$$\|\vec x_1\| = \sqrt{1^2 + (-1)^2} = \sqrt{2}, \quad \|\vec y_1\| = \sqrt{(-1)^2 + 1^2} = \sqrt{2}$$
$$|-2| \leq \sqrt{2}\cdot\sqrt{2} \;\Rightarrow\; 2 \leq 2. \;\checkmark$$

**b)** $\cos \hat\theta = \dfrac{\langle \vec x_1, \vec y_1\rangle}{\|\vec x_1\|\,\|\vec y_1\|} = \dfrac{-2}{\sqrt{2}\cdot\sqrt{2}} = -1 \;\Rightarrow\; \hat\theta = \pi$ (vectores antiparalelos).

**c)** $\operatorname{Proy}_{\vec y_1}(\vec x_1) = \dfrac{\langle \vec x_1, \vec y_1\rangle}{\|\vec y_1\|^2}\,\vec y_1 = \dfrac{-2}{(\sqrt{2})^2}\binom{-1}{1} = -1\binom{-1}{1} = \binom{1}{-1} = \vec x_1.$

> Esquema en el pizarrón: $\vec x_1$ y $\vec y_1$ apuntan en direcciones opuestas a $\pm 45°$ (cuadrantes II y IV); $\hat\theta = \pi$.

**Segundo caso.** $\vec x = \binom{3}{1}$, $\vec y = \binom{2}{3}$.

**a)** $\langle \vec x, \vec y\rangle = 3\cdot 2 + 1\cdot 3 = 9$. $\|\vec x\| = \sqrt{9 + 1} = \sqrt{10} \approx 3{,}16$. $\|\vec y\| = \sqrt{4 + 9} = \sqrt{13} \approx 3{,}60$. Verifica $9 \leq 3{,}16 \cdot 3{,}60$. $\checkmark$

**b)** $\cos\hat\theta = \dfrac{9}{\sqrt{10}\cdot\sqrt{13}} \approx 0{,}79 \;\Rightarrow\; \hat\theta \approx 37{,}8°$.

**c)** $\operatorname{Proy}_{\vec y}(\vec x) = \dfrac{\langle \vec x, \vec y\rangle}{\|\vec y\|^2}\,\vec y = \dfrac{9}{13}\binom{2}{3} = \binom{18/13}{27/13} \approx \binom{1{,}38}{2{,}07}$.

## Página 4 — Minimizar $\|b - \alpha a\|^2$, vector error perpendicular a $a$

> Esquema: en $\mathbb{R}^2$, vectores $\vec x = (3, 1)$, $\vec y = (2, 3)$; el vector $\operatorname{Proy}_{\vec y}(\vec x)$ se dibuja sobre $\vec y$, formando ángulo $\hat\theta \approx 37{,}8°$ entre $\vec x$ e $\vec y$.

**Ejercicio 3.** Sean $\vec a$ y $\vec b$ vectores en $\mathbb{R}^2$. $\alpha \in \mathbb{R}$.

**a)** Encuentra el valor de $\alpha$ que minimiza $f(\alpha) = \|\vec b - \alpha \vec a\|^2$.

Recordando $\|\vec v\|^2 = \langle \vec v, \vec v\rangle$:
$$f(\alpha) = \langle \vec b - \alpha\vec a,\; \vec b - \alpha\vec a\rangle$$
$$f(\alpha) = \langle \vec b, \vec b\rangle - \langle \vec b, \alpha\vec a\rangle - \langle \alpha\vec a, \vec b\rangle + \langle \alpha\vec a, \alpha\vec a\rangle$$
$$f(\alpha) = \|\vec b\|^2 - 2\alpha\langle \vec b, \vec a\rangle + \alpha^2\|\vec a\|^2$$

Minimizando: $f'(\alpha) = -2\langle \vec b, \vec a\rangle + 2\alpha\|\vec a\|^2 = 0 \;\Rightarrow\;$
$$\boxed{\;\alpha^* = \dfrac{\langle \vec b, \vec a\rangle}{\|\vec a\|^2}\;}$$

**b)** Demuestra que el vector error $\vec e = \vec b - \alpha^* \vec a$ es perpendicular a $\vec a$.

$$\langle \vec e, \vec a\rangle = 0\;?$$
$$\langle \vec b - \alpha^*\vec a,\; \vec a\rangle = \langle \vec b, \vec a\rangle - \alpha^*\langle \vec a, \vec a\rangle = \langle \vec b, \vec a\rangle - \dfrac{\langle \vec b, \vec a\rangle}{\|\vec a\|^2}\cdot\|\vec a\|^2 = 0.\;\checkmark$$

## Página 5 — Producto interno en $L^2([0, 2\pi])$: ortogonalidad de $\cos(kx)$ y $\sin(nx)$

**Ejercicio 5.** Determinar el producto interno en $L^2([0, 2\pi])$ entre $f_k(x) = \cos(kx)$ y $g_n(x) = \sin(nx)$ para $k, n \in \mathbb{N}_0$.

**Definición.**
$$\langle f, g\rangle = \int_a^b f(x)\,g(x)\,dx.$$

$$\langle f_k(x), g_n(x)\rangle = \int_0^{2\pi} \cos(kx)\,\sin(nx)\,dx$$

Identidad producto-suma:
$$\cos(A)\,\sin(B) = \tfrac{1}{2}\big[\sin(A + B) - \sin(A - B)\big].$$

$$\langle f_k, g_n\rangle = \tfrac{1}{2}\int_0^{2\pi}\!\big[\sin((k + n)x) - \sin((k - n)x)\big]\,dx$$

La integral del seno en un período completo (o múltiplos) es 0. Como $k, n$ enteros, ambos integrandos cumplen.

$$\boxed{\;\langle f_k(x), g_n(x)\rangle = 0.\;}$$

(Ortogonalidad entre cosenos y senos de cualquier frecuencia entera — base del desarrollo de Fourier.)
