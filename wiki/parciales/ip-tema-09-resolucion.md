---
tags: [parcial, ip, resolucion, transformaciones-lineales, autovalores, diagonalizacion, svd, qr]
fuente: raw/Practicas/Modelos_Examenes/MNA_IP_Tema_IX_Resolucion.pdf
tipo: ip
tema: 9
tiene_resolucion: true
---

# Parcial de Métodos Numéricos Avanzados — Tema IX (Resolución)

## Ejercicio 1

Sea $T : \mathbb{R}^3 \to \mathbb{R}^3$ una transformación lineal tal que

$$M_{EE}(T) = \begin{pmatrix} 0 & k & 1 \\ k & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix}$$

a) Hallar $k \in \mathbb{R}$, si existe, tal que $\dim(N(T)) = 1$.
b) Para $k = 2$ hallar $R(T)$.

### Resolución

**a)** Se halla el determinante de $M_{EE}(T)$ y se iguala a cero:

$$\begin{vmatrix} 0 & k & 1 \\ k & 0 & 1 \\ 1 & 1 & 0 \end{vmatrix} = 0 \implies -k(-1) + k = 0 \implies 2k = 0 \implies k = 0$$

Reemplazando se tiene $M_{EE}(T) = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix}$. Es claro que $M_{EE}(T)$ tiene rango 2, luego cumple lo pedido.

**b)** Si $k = 2$ se tiene $M_{EE}(T) = \begin{pmatrix} 0 & 2 & 1 \\ 2 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix}$. Como $k \ne 0$, $T$ es inyectiva y sobreyectiva, luego $R(T) = \mathbb{R}^3$.

## Ejercicio 2

Sea $A = \begin{pmatrix} 3 & 0 & 1 \\ 1 & k & -1 \\ 2 & 0 & 2 \end{pmatrix}$

a) Hallar $k \in \mathbb{R}$ para que $\lambda = -1$ sea autovalor de $A$.
b) Para $k = 2$, diagonalice la matriz.

### Resolución

**a)** Se calcula el polinomio característico de $A$:

$$p_A(\lambda) = \begin{vmatrix} \lambda - 3 & 0 & -1 \\ -1 & \lambda - k & 1 \\ -2 & 0 & \lambda - 2 \end{vmatrix} = (\lambda - 3)(\lambda - k)(\lambda - 2) - 2(\lambda - k)$$

$$p_A(\lambda) = (\lambda - k)(\lambda^2 - 5\lambda + 4)$$

Se busca que $p_A(-1) = 0 \implies 10(-1 - k) = 0 \implies k = -1$.

**b)** Si $k = 2$ queda $p_A(\lambda) = (\lambda - 2)(\lambda - 1)(\lambda - 4)$. Se buscan los autovectores:

Para $\lambda = 2$:

$$A_2 = \begin{pmatrix} -1 & 0 & -1 \\ -1 & 0 & 1 \\ -2 & 0 & 0 \end{pmatrix} \implies -2x = 0 \implies x = 0 \implies z = 0 \implies v_2 = (0, 1, 0)$$

Para $\lambda = 1$:

$$A_1 = \begin{pmatrix} -2 & 0 & -1 \\ -1 & -1 & 1 \\ -2 & 0 & -1 \end{pmatrix}$$

$-2x - z = 0 \implies z = -2x$. $-x - y - 2x = 0 \implies y = -3x \implies v_1 = (1, -3, -2)$.

Para $\lambda = 4$:

$$A_4 = \begin{pmatrix} 1 & 0 & -1 \\ -1 & 2 & 1 \\ -2 & 0 & 2 \end{pmatrix}$$

$x = z \implies 2y = 0 \implies v_4 = (1, 0, 1)$.

## Ejercicio 3

Dada la Matriz $A = \begin{pmatrix} 3 & 1 \\ 5 & -1 \\ -2 & -3 \end{pmatrix}$

a) Hallar su descomposición $SVD$.
b) Hallar su factorización $QR$.

### Resolución

**a)** Se comienza haciendo

$$A^T A = \begin{pmatrix} 38 & 4 \\ 4 & 11 \end{pmatrix}$$

Los autovalores son $\lambda_1 = 10.42$ y $\lambda_2 = 38.58 \implies \sigma_1 = 3.22,\ \sigma_2 = 6.2113$.

*(El PDF de resolución se corta acá.)*
