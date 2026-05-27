---
tags: [teoria, unidad-II, vectores, producto-interno, normas]
fuente: raw/Teoricas/Slides/MNA_Unidad_II_Espacios_Vectoriales_P_I_v1.pdf
unidad: II
---

# Vectores en $\mathbb{C}^n$ y $\mathbb{R}^n$

## Introducción

### Vectores

**Observación Previa.** Se hará referencia a un cuerpo mediante $\mathbb{K}$ pero en este curso $\mathbb{K} = \mathbb{R}$ o $\mathbb{K} = \mathbb{C}$.

> **Definición.** Un vector en $\mathbb{K}^n$ con $n \in \mathbb{N}$ es una $n$-upla de la forma
> $$v = (v_1, v_2, \dots, v_n)$$
> con $v_i \in \mathbb{K}$.

**Ejemplos:**

$$v = (-5, 8, 1, 4), \qquad v = (1 + i, \, -3 i, \, 8 - 4 i)$$

**Observación.** Cuando $v \in \mathbb{R}^n$ y $n = 1, 2, 3$, se dice que el vector es geométrico. Se dedicará una parte de la presentación a los vectores geométricos.

### Igualdad de vectores

> **Definición.** Sean $v, u \in \mathbb{K}^n$, $v = (v_1, v_2, \dots, v_n)$, $u = (u_1, u_2, \dots, u_n)$. Entonces
> $$u = v \iff u_i = v_i, \quad 1 \leq i \leq n$$

### Adición de vectores

> **Definición.** Sean $v, u \in \mathbb{K}^n$, $v = (v_1, v_2, \dots, v_n)$, $u = (u_1, u_2, \dots, u_n)$. Se define la adición entre $u$ y $v$ al vector
> $$w = (w_1, w_2, \dots, w_n), \quad w_i = u_i + v_i, \quad 1 \leq i \leq n$$
> a $w$ se lo llama vector suma de $u$ con $v$.

**Observación.** La adición es una operación o ley de composición interna, esto es, una aplicación

$$f : \mathbb{K}^n \times \mathbb{K}^n \to \mathbb{K}^n : f(u, v) = u + v$$

### Multiplicación por un escalar

> **Definición.** Sea $v \in \mathbb{K}^n$, $v = (v_1, v_2, \dots, v_n)$ y $\lambda \in \mathbb{K}$. Se define la multiplicación de $v$ por $\lambda$ al vector
> $$w = (w_1, w_2, \dots, w_n), \quad w_i = \lambda \, v_i, \quad 1 \leq i \leq n$$

**Observación.** La multiplicación por un escalar es una acción o ley de composición externa, esto es, una aplicación

$$f : \mathbb{K} \times \mathbb{K}^n \to \mathbb{K}^n : f(\lambda, v) = \lambda \cdot v$$

## Producto Interno

> **Definición.** Sean $u, v \in \mathbb{K}^n$, $u = (u_1, u_2, \dots, u_n)$ y $v = (v_1, v_2, \dots, v_n)$, se define el producto interior entre $u$ y $v$ como
> $$\langle u, v \rangle = \sum_{k=1}^{n} u_i \, v_i$$

> **Nota.** El slide usa $u_i v_i$ (sin conjugación) tanto para $\mathbb{R}^n$ como $\mathbb{C}^n$. En $\mathbb{C}^n$ lo usual es $\sum u_i \overline{v_i}$; transcripción literal del slide.

### Propiedades del producto interno

i) **Simetría:** $\forall \, u, v \in \mathbb{K}^n: \langle u, v \rangle = \langle v, u \rangle$
ii) **Bilinealidad:**
   - ii.i) $\forall \, u, v, w \in \mathbb{K}^n$:
     $$\langle u + w, v \rangle = \langle u, v \rangle + \langle w, v \rangle \quad y \quad \langle u, v + w \rangle = \langle u, v \rangle + \langle u, w \rangle$$
   - ii.ii) $\forall \, u, v \in \mathbb{K}^n, \, \alpha, \beta \in \mathbb{K}$:
     $$\langle \alpha \, u, v \rangle = \alpha \, \langle u, v \rangle \quad y \quad \langle u, \beta \, v \rangle = \beta \, \langle u, v \rangle$$
iii) **Positividad:** $\forall \, u \in \mathbb{K}^n: \langle u, u \rangle \geq 0$

### Desigualdad de Cauchy-Bunyakovsky-Schwarz

> **Proposición.**
> $$\forall \, u, v \in \mathbb{K}^n: |\langle u, v \rangle|^2 \leq |\langle u, u \rangle|^2 \, |\langle v, v \rangle|^2$$

> **Nota.** El slide transcribe la desigualdad con exponentes $2$ a ambos lados; la forma habitual de C-B-S es $|\langle u, v\rangle|^2 \leq \langle u, u\rangle \, \langle v, v\rangle$. Se mantiene aquí la versión literal del slide.

## Norma de un vector

> **Definición.** Una norma en $\mathbb{K}^n$ es una función $N : \mathbb{K}^n \to \mathbb{K}$ que cumple
> i) $N(v) \geq 0$ y $N(v) = 0 \iff v = 0$
> ii) $N(\lambda \, v) = |\lambda| \, N(v) \quad \forall \, \lambda \in \mathbb{K}$
> iii) $N(u + v) \leq N(u) + N(v) \quad \forall \, u, v \in \mathbb{K}^n$

### Norma Usual o Euclidiana

> **Definición.** Se define la norma usual o euclidiana en $\mathbb{K}^n$ como
> $$\| u \| = \sqrt{\langle u, u \rangle}$$

A esta norma la rebautizamos como $\| u \|_2$.

Se dice entonces que $\mathbb{K}^n$ es un espacio normado. Las normas son de mucha utilidad para definir aspectos geométricos y son también utilizadas en Análisis Matemático.

## Ángulo entre Vectores

> **Definición.** Se define el ángulo entre $u$ y $v$, $\alpha_{uv}$, al ángulo que cumple
> $$\cos(\alpha_{uv}) = \frac{\langle u, v \rangle}{\| u \|_2 \, \| v \|_2}, \qquad 0 \leq \alpha_{uv} \leq \pi$$

## Paralelismo y Perpendicularidad

> **Definiciones.**
> i) Se dice que $u, v \in \mathbb{K}^n$ son paralelos $u \parallel v$ si existe $k \in \mathbb{K}: v = k \cdot u$.
> ii) Se dice que $u, v \in \mathbb{K}^n$ son perpendiculares $u \perp v$ si son no nulos y $\langle u, v \rangle = 0$.

**Observación.** En lo que se dijo hasta ahora hay un nivel de abstracción podría decirse intermedio. Si pensamos lo mismo en vectores geométricos se puede dar una interpretación geométrica concreta.

## Otras Normas

En muchas situaciones es conveniente trabajar con otras normas además de la usual, se presentarán en esta sección algunas normas de utilidad. Sea $v \in \mathbb{K}^n: v = (v_1, \dots, v_n)$.

i) **Norma 1:** Se define esta norma como
$$\| v \|_1 = \sum_{i=1}^{n} |v_i|$$

ii) **Norma $p$ con $p > 1$:** Se define esta norma como
$$\| v \|_p = \left( \sum_{i=1}^{n} |v_i|^p \right)^{1/p}$$

iii) **Norma Infinito:** Se define esta norma como
$$\| v \|_\infty = \max\{ |v_i| : 1 \leq i \leq n \}$$

---

## Ver también

- [[01-numeros-complejos]] — números complejos (cuerpo base $\mathbb{C}$)
- [[03-matrices]] — generalización a arreglos $n \times m$
- [[04-determinantes]] — formas multilineales alternadas
