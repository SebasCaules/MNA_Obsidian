---
tags: [resueltos, pseudoinversa, svd]
fuente: raw/Practicas/Ejercicios_Resueltos/Ejercicios_Algebra_Lineal_Resueltos_Pseudoinversa.pdf
unidad: VII
---

# Ejercicios Resueltos — Pseudoinversa

Ver enunciado relacionado en [[../guias/guia-07-svd-mmcc]] (Ejercicio 2 y 3).

## Ejercicio 1

Hallar la pseudoinversa de la siguiente matriz por SVD:

$$A = \begin{pmatrix} 3 & 2 & 2 \\ 2 & 3 & -2 \end{pmatrix}$$

### Resolución

Se buscan matrices ortogonales $U$ y $V$ tales que $A = U\Sigma V^T$ con $\Sigma$ diagonal en el sentido visto ya que no será cuadrada.

Se hace $A^T A$:

$$A^T A = \begin{pmatrix} 3 & 2 \\ 2 & 3 \\ 2 & -2 \end{pmatrix} \begin{pmatrix} 3 & 2 & 2 \\ 2 & 3 & -2 \end{pmatrix} = \begin{pmatrix} 13 & 12 & 2 \\ 12 & 13 & -2 \\ 2 & -2 & 8 \end{pmatrix}$$

Polinomio característico:

$$p_{A^T A}(\lambda) = \begin{vmatrix} \lambda - 13 & -12 & -2 \\ -12 & \lambda - 13 & 2 \\ -2 & 2 & \lambda - 8 \end{vmatrix} = \lambda^3 - 34\lambda^2 + 225\lambda = \lambda(\lambda - 9)(\lambda - 25)$$

Luego $\Sigma = \begin{pmatrix} 5 & 0 & 0 \\ 0 & 3 & 0 \end{pmatrix}$. Además $A^T A = V\,\Sigma^T \Sigma\, V^T$. Para hallar $V$ se hace:

**Si $\lambda = 0$:**

$$(A^T A)_0 = \begin{pmatrix} -13 & -12 & -2 \\ -12 & -13 & 2 \\ -2 & 2 & -8 \end{pmatrix}$$

$-25x - 25y = 0 \Rightarrow x + y = 0 \Rightarrow y = -x$; y $-4x - 8z = 0 \Rightarrow x = -2z \Rightarrow y = 2z$. Luego $\tilde{v}_0 = (-2, 2, 1)$ y $\|\tilde{v}_0\| = 3 \Rightarrow v_0 = \left(-\tfrac{2}{3}, \tfrac{2}{3}, \tfrac{1}{3}\right)$.

**Si $\lambda = 9$:**

$$(A^T A)_9 = \begin{pmatrix} -4 & -12 & -2 \\ -12 & -4 & 2 \\ -2 & 2 & 1 \end{pmatrix}$$

$y = -x$, $z = 4x \Rightarrow \tilde{v}_1 = (1, -1, 4)$, $\|\tilde{v}_1\| = 3\sqrt{2} \Rightarrow v_1 = \left(\tfrac{1}{3\sqrt{2}}, -\tfrac{1}{3\sqrt{2}}, \tfrac{4}{3\sqrt{2}}\right)$.

**Si $\lambda = 25$:**

$$(A^T A)_{25} = \begin{pmatrix} 12 & -12 & -2 \\ -12 & 12 & 2 \\ -2 & 2 & 17 \end{pmatrix}$$

$z = 6x - 6y$ y $17z = 2x - 2y \Rightarrow x = y \Rightarrow z = 0$. Luego $\tilde{v}_2 = (1, 1, 0)$ y $\|\tilde{v}_2\| = \sqrt{2} \Rightarrow v_2 = \left(\tfrac{1}{\sqrt{2}}, \tfrac{1}{\sqrt{2}}, 0\right)$.

Luego la matriz $V$ es:

$$V = \begin{pmatrix} \tfrac{1}{\sqrt{2}} & \tfrac{1}{3\sqrt{2}} & -\tfrac{2}{3} \\ \tfrac{1}{\sqrt{2}} & -\tfrac{1}{3\sqrt{2}} & \tfrac{2}{3} \\ 0 & \tfrac{4}{3\sqrt{2}} & \tfrac{1}{3} \end{pmatrix}$$

Ahora $AV = U\Sigma$. Por las dimensiones es claro que $U$ es de $2 \times 2$. Luego se hace:

$$\begin{pmatrix} 3 & 2 & 2 \\ 2 & 3 & -2 \end{pmatrix} \begin{pmatrix} \tfrac{1}{\sqrt{2}} & \tfrac{1}{3\sqrt{2}} & -\tfrac{2}{3} \\ \tfrac{1}{\sqrt{2}} & -\tfrac{1}{3\sqrt{2}} & \tfrac{2}{3} \\ 0 & \tfrac{4}{3\sqrt{2}} & \tfrac{1}{3} \end{pmatrix} = \begin{pmatrix} \tfrac{5}{\sqrt{2}} & \tfrac{3}{\sqrt{2}} & 0 \\ \tfrac{5}{\sqrt{2}} & -\tfrac{3}{\sqrt{2}} & 0 \end{pmatrix}$$

Igualando con $\begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} 5 & 0 & 0 \\ 0 & 3 & 0 \end{pmatrix} = \begin{pmatrix} 5a & 3b & 0 \\ 5c & 3d & 0 \end{pmatrix}$:

$$U = \begin{pmatrix} \tfrac{1}{\sqrt{2}} & \tfrac{1}{\sqrt{2}} \\ \tfrac{1}{\sqrt{2}} & -\tfrac{1}{\sqrt{2}} \end{pmatrix}$$

Luego $A^\dagger = V\,\Sigma^{-1}\, U^T$. En este caso:

$$\Sigma^{-1} = \begin{pmatrix} \tfrac{1}{5} & 0 \\ 0 & \tfrac{1}{3} \\ 0 & 0 \end{pmatrix}$$

(Notación: $\Sigma^{-1}$ aquí refiere a la pseudoinversa $\Sigma^\dagger$ del rectangular $\Sigma$ del SVD.)
