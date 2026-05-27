---
tags: [teoria, unidad-II, matrices, operaciones-matriciales, transpuesta]
fuente: raw/Teoricas/Slides/MNA_Unidad_II_Espacios_Vectoriales_P_II_v1.pdf
unidad: II
---

# Matrices

## Introducción

### Definición de matriz

> **Definición.** Una matriz $A$ es un arreglo de la forma
> $$A = \begin{pmatrix} a_{11} & a_{12} & \dots & a_{1m} \\ a_{21} & a_{22} & \dots & a_{2m} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \dots & a_{nm} \end{pmatrix}$$
> con $a_{ij} \in \mathbb{K}$, $1 \leq i \leq n$ y $1 \leq j \leq m$.

Como notación abreviada se escribe $A \in \mathbb{K}^{n \times m}$, $A = (a_{ij})_{ij}$.

En una definición más formal, puede decirse que una matriz es una aplicación

$$m : I_n \times I_m \to \mathbb{K} : m(i, j) = a_{ij}$$

Donde $I_h = \{1, \dots, h\}$ se lo llama $h$-ésimo intervalo natural.

### Vectores fila y columna

Es de observar que un vector es un caso particular de matriz cuando $n$ o $m$ sea igual a $1$. Por ejemplo:

$$F_k = (a_{k1}, \dots, a_{km}), \qquad C_k = \begin{pmatrix} a_{1k} \\ a_{2k} \\ \vdots \\ a_{nk} \end{pmatrix}$$

A $F_k$ y $C_k$ se los llama vector fila $k$-ésima y vector columna $k$-ésima respectivamente. Formalmente un vector es una función $v : I_n \to \mathbb{K} : v(i) = v_i$.

### Igualdad de Matrices

> **Definición.** Sean $A, B \in \mathbb{K}^{n \times m}$, $A = (a_{ij})_{ij}$, $B = (b_{ij})_{ij}$. Se dice que
> $$A = B \iff a_{ij} = b_{ij}, \quad 1 \leq i \leq n, \quad 1 \leq j \leq m$$

## Adición de Matrices

> **Definición.** Sean $A, B \in \mathbb{K}^{n \times m}$, $A = (a_{ij})_{ij}$ y $B = (b_{ij})_{ij}$. Se define
> $$A + B = (a_{ij} + b_{ij})_{ij}$$

### Propiedades de la adición

i) **Asociatividad:**
$$\forall \, A, B, C \in \mathbb{K}^{n \times m} : A + (B + C) = (A + B) + C$$

ii) **Existencia de Elemento Neutro:**
$$\exists \, N \in \mathbb{K}^{n \times m} : \forall \, A \in \mathbb{K}^{n \times m} \; A + N = N + A = A$$
**Observación y Notación:** A la matriz $N$ se la llama Matriz Nula y se la nota como $N = 0_{\mathbb{K}^{n \times m}}$.

iii) **Existencia de Inverso Aditivo:**
$$\forall \, A \in \mathbb{K}^{n \times m}, \; \exists \, -A \in \mathbb{K}^{n \times m} : A + (-A) = -A + A = N$$
**Observación:** Si $A = (a_{ij})_{ij}$ entonces $-A = (-a_{ij})_{ij}$.

iv) **Conmutatividad:**
$$\forall \, A, B \in \mathbb{K}^{n \times m} : A + B = B + A$$

## Multiplicación de una matriz por un escalar

> **Definición.** Sea $A \in \mathbb{K}^{n \times m}$, $A = (a_{ij})_{ij}$ y $\lambda \in \mathbb{K}$. Se define la multiplicación de $A$ por $\lambda$ como
> $$\lambda \, A = (\lambda \, a_{ij})_{ij}$$

### Propiedades

i) **Distributividad con la suma de Matrices:**
$$\forall \, A, B \in \mathbb{K}^{n \times m}, \lambda \in \mathbb{K} : \lambda \, (A + B) = \lambda \, A + \lambda \, B$$

ii) **Distributividad con la suma de Escalares:**
$$\forall \, \lambda, \mu \in \mathbb{K}, A \in \mathbb{K}^{n \times m} : (\lambda + \mu) \, A = \lambda \, A + \mu \, A$$

iii) **Asociatividad Mixta:**
$$\forall \, \lambda, \mu \in \mathbb{K}, A \in \mathbb{K}^{n \times m} : (\lambda \, \mu) \, A = \lambda \, (\mu \, A)$$

iv) **Unitariedad:**
$$\forall \, v \in \mathbb{K}^{n \times m} : 1 \cdot v = v$$
Donde $1 \in \mathbb{K}$.

### Matrices Cuadradas

> **Definición.** Si $A \in \mathbb{K}^{n \times n}$ se la denomina matriz cuadrada.

## Multiplicación de Matrices

> **Definición.** Sean $A \in \mathbb{K}^{m \times n}$ y $B \in \mathbb{K}^{n \times p}$, $A = (a_{ij})_{ij}$, $B = (b_{ij})_{ij}$. Se define la matriz $C = A \cdot B$, $C = (c_{ij})_{ij}$ con
> $$c_{ij} = \sum_{k=1}^{n} a_{ik} \, b_{kj}$$

Si se escribe a las matrices $A$ y $B$ como

$$A = \begin{pmatrix} F^A_1 \\ F^A_2 \\ \vdots \\ F^A_n \end{pmatrix} \quad \wedge \quad B = (C^B_1, \dots, C^B_n)$$

Donde $F^A_i$ es la $i$-ésima fila de $A$ y $C^B_j$ la $j$-ésima columna de $B$. Se puede decir que $c_{ij} = \langle F^A_i, C^B_j \rangle$.

**Ejemplo:** Se desea multiplicar las matrices

$$A = \begin{pmatrix} 1 & -3 & 3 \\ 4 & -2 & 6 \end{pmatrix}, \qquad B = \begin{pmatrix} 7 & -1 \\ 3 & 5 \\ 1 & 9 \end{pmatrix}$$

$$AB = \begin{pmatrix} 1 \cdot 7 + (-3) \cdot 3 + 3 \cdot 1 & 1 \cdot (-1) + (-3) \cdot 5 + 3 \cdot 9 \\ 4 \cdot 7 + (-2) \cdot 3 + 6 \cdot 1 & 4 \cdot (-1) + (-2) \cdot 5 + 6 \cdot 9 \end{pmatrix}$$

Finalmente

$$A B = \begin{pmatrix} 1 & 11 \\ 28 & 40 \end{pmatrix}$$

### Observaciones

i) Puede existir $A B$ pero no $B A$.
ii) Si existen $A B$ y $B A$ en general $A B \neq B A$.
iii) Si $A, B \in \mathbb{K}^{n \times n}$, existen $A B$ y $B A$.

### Algunas propiedades

i) **Asociatividad:**
$$\forall \, A \in \mathbb{K}^{n \times m}, B \in \mathbb{K}^{m \times p}, C \in \mathbb{K}^{p \times q} : A \, (B \, C) = (A \, B) \, C$$
ii) **Distributividad:**
$$\forall \, A \in \mathbb{K}^{n \times m}, B, C \in \mathbb{K}^{m \times p} : A \, (B + C) = A \, B + A \, C$$

## Potenciación

Sea $A \in \mathbb{K}^{n \times n}$ y $m \in \mathbb{N}$, se define $A^m = A \, A \, A \dots A$ ($m$ veces).

### Propiedades

i) $\forall \, A \in \mathbb{K}^{n \times n}, p, q \in \mathbb{N} : A^p \, A^q = A^{p+q}$.
ii) $\forall \, A \in \mathbb{K}^{n \times n}, p, q \in \mathbb{N} : (A^p)^q = A^{p \, q}$.

## Matriz Transpuesta

> **Definición.** Sea $A \in \mathbb{K}^{n \times m}$, $A = (a_{ij})_{ij}$. Se define la matriz transpuesta de $A$ como
> $$A^T = (a_{ji})_{ij}$$

### Propiedades

i) $\forall \, A \in \mathbb{K}^{n \times m} : (A^T)^T = A$.
ii) $\forall \, A, B \in \mathbb{K}^{n \times m} : (A + B)^T = A^T + B^T$.
iii) $\forall \, A \in \mathbb{K}^{n \times m}, \lambda \in \mathbb{K} : (\lambda \, A)^T = \lambda \, A^T$.
iv) $\forall \, A \in \mathbb{K}^{n \times m}, B \in \mathbb{K}^{m \times n} : (A \, B)^T = B^T \, A^T$.

**Ejemplo:**

$$A = \begin{pmatrix} -2 & 3 & 5 \\ 1 & 2 & 0 \\ 3 & -5 & 7 \end{pmatrix} \iff A^T = \begin{pmatrix} -2 & 1 & 3 \\ 3 & 2 & -5 \\ 5 & 0 & 7 \end{pmatrix}$$

## Matriz Identidad

> **Definición.** Se define la matriz identidad $I \in \mathbb{K}^{n \times n}$ como $I = (a_{ij})_{ij}$ donde $a_{ij} = 0$ si $i \neq j$ y $a_{ii} = 1$.

**Notación:** A la matriz identidad se la denota como $I$ o como $I_n$ para indicar su dimensión.

**Propiedad:** $\forall \, A \in \mathbb{K}^{n \times n} : A \, I_n = I_n \, A = A$.

## Matriz Inversa

> **Definición.** Sea $A \in \mathbb{K}^{n \times n}$, se dice que $A$ es invertible si existe $B \in \mathbb{K}^{n \times n}$ tal que $A \, B = B \, A = I_n$. A la matriz $B$ se la llama matriz inversa de $A$ y se la nota como $B = A^{-1}$.

**Observación.** Si bien el concepto de matriz inversa se ha definido para matrices cuadradas, se verá en otro apartado que se puede generalizar a otros casos.

### Propiedades

Sea $A, B \in \mathbb{K}^{n \times n}$, si existen $A^{-1}, B^{-1} \in \mathbb{K}^{n \times n}$ entonces:

i) $A^{-1}$ es única.
ii) $(A^{-1})^{-1} = A$.
iii) $\forall \, \lambda \in \mathbb{K} - \{0_{\mathbb{K}}\} : (\lambda \, A)^{-1} = \dfrac{1}{\lambda} \, A^{-1}$.
iv) $(A \, B)^{-1} = B^{-1} \, A^{-1}$.

> **Nota.** El slide escribe $(A B)^{-1} = B^{-1} B^{-1}$ — es una errata; la forma correcta es $B^{-1} A^{-1}$.

## Matrices con nombre propio

En esta sección se presentarán una clasificación de las matrices según algunas propiedades o características que las destacan. Sea $A \in \mathbb{K}^{n \times n}$.

i) **Matriz Simétrica:** $A$ es simétrica si $A = A^T$. Si $A = (a_{ij})_{ij}$ es simétrica es claro que $a_{ij} = a_{ji}$.

ii) **Matriz Antisimétrica:** $A = (a_{ij})_{ij}$ es antisimétrica si $A = -A^T$. Si $A$ es antisimétrica es claro que $a_{ij} = -a_{ji}$ y consecuentemente $a_{ii} = 0$.

iii) **Matriz Triangular:**
   - iii.i) **Triangular Superior:** $A = (a_{ij})_{ij}$ es triangular superior si $a_{ij} = 0 \;\; \forall \, i > j$.
   - iii.ii) **Triangular Inferior:** $A = (a_{ij})_{ij}$ es triangular inferior si $a_{ij} = 0 \;\; \forall \, i < j$.

iv) **Matriz Diagonal:** $A = (a_{ij})_{ij}$ es diagonal si $a_{ij} = 0 \;\; \forall \, i \neq j$.

v) **Matriz Escalar:** $A = (a_{ij})_{ij}$ es escalar si existe $k \in \mathbb{K} : A = k \, I_n$.

vi) **Matriz Idempotente:** $A$ es idempotente si $A^2 = A$.
**Observación:** Si $A$ es idempotente entonces $A^n = A \;\; \forall \, n \in \mathbb{N}$.

vii) **Matriz Involutiva:** $A$ es involutiva si $A^2 = I$.
**Observación:** Si $A$ es involutiva entonces $A^{2n} = I$ y $A^{2n+1} = A \;\; \forall \, n \in \mathbb{N}$.

viii) **Matriz Nilpotente:** $A$ es nilpotente si $\exists \, n_0 \in \mathbb{N} : A^n = N \;\; \forall \, n \geq n_0$. Donde $N$ es la matriz nula. A $n_0$ se lo llama índice de nilpotencia.

> **Nota.** El slide tipea "A no se lo llama indice de nilpotencia". Por contexto se interpreta como "$n_0$ se lo llama índice de nilpotencia" (errata en el slide).

ix) **Matriz Ortogonal:** $A$ es ortogonal si $A \, A^T = I_n$ y $A^T \, A = I_n$.

---

## Ver también

- [[01-numeros-complejos]] — cuerpo base $\mathbb{C}$
- [[02-vectores-cn-rn]] — vectores como matriz fila/columna
- [[04-determinantes]] — determinante de una matriz cuadrada
