---
tags: [teoria, unidad-II, determinantes, formas-multilineales, laplace, sarrus]
fuente: raw/Teoricas/Slides/MNA_Unidad_II_Espacios_Vectoriales_P_III_v2.pdf
unidad: II
---

# Determinantes

## Funciones Multilineales Alternadas

**Notación.** Sea $A \in \mathbb{K}^{n \times n}$. Si $A_1, \dots, A_n$ son sus columnas, se notará $A = (A_1, \dots, A_n)$.

> **Definición.** Una forma multilineal alternada es una función $f : \mathbb{K}^{n \times n} \to \mathbb{K}$ que cumple que para cada $1 \leq i \leq n$:
>
> i) $f(A_1, \dots, A_i + B_i, \dots, A_n) = f(A_1, \dots, A_i, \dots, A_n) + f(A_1, \dots, B_i, \dots, A_n)$
>
> ii) $f(A_1, \dots, \lambda \, A_i, \dots, A_n) = \lambda \, f(A_1, \dots, A_n) \quad \forall \, \lambda \in \mathbb{K}$
>
> iii) $f(A_1, \dots, A_i, \dots, A_i, \dots, A_n) = 0$

**Observación.** Una forma multilineal alternada se puede definir como una función $f : V^n \to \mathbb{K}$ que cumple i), ii), iii) con $V$ un espacio vectorial sobre $\mathbb{K}$.

### Propiedades de las formas multilineales alternadas

> **Proposición.** Si $f : \mathbb{K}^{n \times n} \to \mathbb{K}$ es una forma multilineal alternada, entonces:
>
> i) $f(A_1, \dots, A_{i-1}, 0, A_{i+1}, \dots, A_n) = 0$
>
> ii) $f(A_1, \dots, A_i, \dots, A_j, \dots, A_n) = -f(A_1, \dots, A_j, \dots, A_i, \dots, A_n)$
>
> iii) $f(A_1, \dots, A_i + \alpha \, A_j, \dots, A_n) = f(A_1, \dots, A_i, \dots, A_n)$
>
> iv) Si $A_i = \displaystyle\sum_{j=1}^{n} \alpha_j \, A_j$, $j \neq i \implies f(A_1, \dots, A_i, \dots, A_n) = 0$

## Definición del Determinante

> **Definición.** Se define el determinante como la única función multilineal alternada $f : \mathbb{K}^{n \times n} \to \mathbb{K}$ que cumple $f(I_n) = 1$.

**Notación.** Al determinante se lo nota como $\det(A)$, $|A|$, $D(A)$, $d(A)$. Cualquiera de estas notaciones se utilizará.

**Ejemplo.**

$$f : \mathbb{R}^{2 \times 2} \to \mathbb{R} : f\begin{pmatrix} x & y \\ z & w \end{pmatrix} = x \, w - y \, z$$

Es un determinante (verificar).

Luego si $A \in \mathbb{R}^{2 \times 2}$:

$$A = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}, \qquad \det(A) = a_{11} \, a_{22} - a_{12} \, a_{21}$$

## Generalización a $\mathbb{K}^{n \times n}$

Con el fin de generalizar el cálculo de determinantes a $\mathbb{K}^{n \times n}$ se darán algunas definiciones que serán de utilidad.

### Menor de un elemento

> **Definición.** Sea $A \in \mathbb{K}^{n \times n}$, $A = (a_{ij})_{ij}$. Se define el menor de un elemento a la matriz $M_{ij} \in \mathbb{K}^{(n-1) \times (n-1)}$ que se obtiene de $A$, eliminando la fila $i$ y la columna $j$.

**Ejemplo.** Para

$$A = \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix}$$

$$M_{11} = \begin{pmatrix} a_{22} & a_{23} \\ a_{32} & a_{33} \end{pmatrix}, \quad M_{12} = \begin{pmatrix} a_{21} & a_{23} \\ a_{31} & a_{33} \end{pmatrix}, \quad M_{13} = \begin{pmatrix} a_{21} & a_{22} \\ a_{31} & a_{32} \end{pmatrix}$$

$$M_{21} = \begin{pmatrix} a_{12} & a_{13} \\ a_{32} & a_{33} \end{pmatrix}, \quad M_{22} = \begin{pmatrix} a_{11} & a_{13} \\ a_{31} & a_{33} \end{pmatrix}, \quad M_{23} = \begin{pmatrix} a_{11} & a_{12} \\ a_{31} & a_{32} \end{pmatrix}$$

$$M_{31} = \begin{pmatrix} a_{12} & a_{13} \\ a_{22} & a_{23} \end{pmatrix}, \quad M_{32} = \begin{pmatrix} a_{11} & a_{13} \\ a_{21} & a_{23} \end{pmatrix}, \quad M_{33} = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}$$

### Cofactor de un elemento

> **Definición.** Sea $A \in \mathbb{K}^{n \times n}$, $A = (a_{ij})_{ij}$. Se define el cofactor del elemento $a_{ij}$ como
> $$A_{ij} = (-1)^{i+j} \, |M_{ij}|$$

### Regla de Laplace

> **Proposición (Regla de Laplace).** Sea $A \in \mathbb{K}^{n \times n}$, $A = (a_{ij})_{ij}$, $A_{ij}$ el cofactor correspondiente al elemento $a_{ij}$. Entonces
> $$\det(A) = \sum_{j=1}^{n} a_{ij} \, A_{ij}$$

> **Nota (Sarrus).** El slide menciona la Regla de Sarrus en el título de la unidad pero no la desarrolla en estas diapositivas. Recordatorio: Sarrus es la regla mnemotécnica para calcular el determinante de una matriz $3 \times 3$ como
> $$\det(A) = a_{11} a_{22} a_{33} + a_{12} a_{23} a_{31} + a_{13} a_{21} a_{32} - a_{13} a_{22} a_{31} - a_{11} a_{23} a_{32} - a_{12} a_{21} a_{33}$$

---

## Ver también

- [[03-matrices]] — matriz, menor, cofactor en el contexto general
- [[02-vectores-cn-rn]] — columnas de una matriz como vectores
- [[01-numeros-complejos]] — cuerpo base $\mathbb{C}$
