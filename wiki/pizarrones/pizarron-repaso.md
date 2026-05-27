---
tags: [pizarron, repaso, transformaciones-lineales, autovalores, diagonalizacion, svd, qr]
fuente: raw/Practicas/Pizarrones/clase_repaso.pdf
tipo: escaneo
---

# Pizarrón — Clase de repaso: TL paramétrica, autovalores/diagonalización, SVD y QR

Repaso integrador: rango/núcleo de una TL paramétrica, autovalores y diagonalización, factorización SVD de una matriz $3 \times 2$ y factorización QR.

## Página 1 — TL paramétrica $T: \mathbb{R}^3 \to \mathbb{R}^3$ y autovalores paramétricos

**Enunciado.** Sea $T : \mathbb{R}^3 \to \mathbb{R}^3$ una transformación lineal tal que su matriz en la base canónica $E$ es
$$M_{EE}(T) = \begin{pmatrix} 0 & k & 1 \\ k & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix}.$$

**a) Hallar $k \in \mathbb{R}$, si existe, tal que $\dim(N(T)) = 1$.**

**Teorema de la dimensión:** $\dim(V) = \dim(N(T)) + \dim(R(T))$.

Con $V = \mathbb{R}^3$: $3 = 1 + \operatorname{rango}(M_{EE}(T)) \;\Rightarrow\; \operatorname{rango}(M_{EE}(T)) = 2$.

Para que el rango sea 2 necesitamos $\det(M_{EE}(T)) = 0$:
$$\det\!\begin{pmatrix} 0 & k & 1 \\ k & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix} = 0 + k + k - (0 + 0 + 0) = k + k = 2k = 0 \;\Rightarrow\; k = 0.$$

$$M(0) = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix} \;\text{(rango 2)}.$$

**b) Para $k = 2$, hallar $R(T)$.**

$$M_{EE}(T) = \begin{pmatrix} 0 & 2 & 1 \\ 2 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix} \;\Rightarrow\; \det(M_{EE}(T)) = 2k = 4 \neq 0 \;\Rightarrow\; \operatorname{rango} = 3.$$

$$\boxed{R(T) = \mathbb{R}^3.}$$

**Ejercicio.** Sea $A = \begin{pmatrix} 3 & 0 & 1 \\ 1 & k & -1 \\ 2 & 0 & 2 \end{pmatrix}$.

**a) Hallar $k$ para que $\lambda = -1$ sea autovalor de $A$.**

$\det(A - \lambda I) = 0$ con $\lambda = -1$:
$$\begin{vmatrix} 3 - (-1) & 0 & 1 \\ 1 & k - (-1) & -1 \\ 2 & 0 & 2 - (-1) \end{vmatrix} = \begin{vmatrix} 4 & 0 & 1 \\ 1 & k + 1 & -1 \\ 2 & 0 & 3 \end{vmatrix} = (k + 1)\,(-1)^{2+2}\begin{vmatrix} 4 & 1 \\ 2 & 3 \end{vmatrix} = (k + 1)\cdot 10 = 0 \;\Rightarrow\; \boxed{k = -1.}$$

## Página 2 — Diagonalización de $A$ para $k = 2$

$$A = \begin{pmatrix} 3 & 0 & 1 \\ 1 & 2 & -1 \\ 2 & 0 & 2 \end{pmatrix} \;\Rightarrow\; A = P D P^{-1}.$$

$$\det(A - \lambda I) = \begin{vmatrix} 3 - \lambda & 0 & 1 \\ 1 & 2 - \lambda & -1 \\ 2 & 0 & 2 - \lambda \end{vmatrix} = (2 - \lambda)\,\begin{vmatrix} 3 - \lambda & 1 \\ 2 & 2 - \lambda \end{vmatrix}$$
$$= (2 - \lambda)\big[(3 - \lambda)(2 - \lambda) - 2\big] = (2 - \lambda)[6 - 3\lambda - 2\lambda + \lambda^2 - 2] = (2 - \lambda)(\lambda^2 - 5\lambda + 4) = (2 - \lambda)(\lambda - 1)(\lambda - 4) = 0.$$

$\lambda_1 = 2$ (MA = 1), $\lambda_2 = 1$ (MA = 1), $\lambda_3 = 4$ (MA = 1).

**Autovectores asociados:** $(A - \lambda I)\vec v = \vec 0$.

**$\lambda_1 = 2$:**
$$\begin{pmatrix} 1 & 0 & 1 \\ 1 & 0 & -1 \\ 2 & 0 & 0 \end{pmatrix}\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \vec 0 \;\Rightarrow\; \begin{cases} x + z = 0 \\ x = 0 \end{cases} \;\Rightarrow\; x = 0, z = 0, y \text{ libre.}$$
$$\vec v_1 = (0, 1, 0).\; MG = 1.$$

**$\lambda_2 = 1$:**
$$\begin{pmatrix} 2 & 0 & 1 \\ 1 & 1 & -1 \\ 2 & 0 & 1 \end{pmatrix}\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \vec 0 \;\Rightarrow\; \begin{cases} 2x + z = 0 \\ x + y - z = 0 \end{cases} \;\Rightarrow\; z = -2x,\; y = z - x = -3x.$$
$$\vec v_2 = (1, -3, -2).\; MG = 1.$$

**$\lambda_3 = 4$:**
$$\begin{pmatrix} -1 & 0 & 1 \\ 1 & -2 & -1 \\ 2 & 0 & -2 \end{pmatrix}\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \vec 0 \;\Rightarrow\; \begin{cases} -x + z = 0 \\ x - 2y - z = 0 \end{cases} \;\Rightarrow\; z = x,\; -2y = 0 \;\Rightarrow\; y = 0.$$
$$\vec v_3 = (1, 0, 1).\; MG = 1.$$

Como $MA = MG$ para los tres autovalores $\Rightarrow$ **$A$ es diagonalizable**.

## Página 3 — Matriz diagonal, matriz de pasaje y arranque de SVD

$$D = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 4 \end{pmatrix}, \quad P = \begin{pmatrix} 0 & 1 & 1 \\ 1 & -3 & 0 \\ 0 & -2 & 1 \end{pmatrix}.$$

**Dada la matriz** $A = \begin{pmatrix} 1 & -1 \\ 0 & 1 \\ 1 & 0 \end{pmatrix}$.

**a) Factorización SVD.** $A = U\,\Sigma\,V^T$ con $U \in \mathbb{R}^{3\times 2}$, $\Sigma \in \mathbb{R}^{2\times 2}$, $V^T \in \mathbb{R}^{2\times 2}$ (forma reducida).

$$A^T A = \begin{pmatrix} 1 & 0 & 1 \\ -1 & 1 & 0 \end{pmatrix}\begin{pmatrix} 1 & -1 \\ 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}.$$

**Autovalores de $A^T A$:** $\det(A^T A - \lambda I) = 0$.
$$\begin{vmatrix} 2 - \lambda & -1 \\ -1 & 2 - \lambda \end{vmatrix} = (2 - \lambda)^2 - 1 = 0 \;\Rightarrow\; (2 - \lambda)^2 = 1 \;\Rightarrow\; 2 - \lambda = \pm 1.$$

$\lambda_1 = 3, \lambda_2 = 1$. Valores singulares: $\sigma_1 = \sqrt{3},\; \sigma_2 = 1$.

$$\Sigma = \begin{pmatrix} \sqrt{3} & 0 \\ 0 & 1 \end{pmatrix}.$$

**Autovectores (matriz $V$).**

**$\lambda = 3$:** $(A^T A - 3I)\vec v = \vec 0$.
$$\begin{pmatrix} -1 & -1 \\ -1 & -1 \end{pmatrix}\binom{x}{y} = \binom{0}{0} \;\Rightarrow\; -x - y = 0 \;\Rightarrow\; y = -x.$$
$$\vec v = \binom{1}{-1}, \quad \|\vec v\| = \sqrt{2} \;\Rightarrow\; \vec v_1 = \tfrac{1}{\sqrt{2}}\binom{1}{-1}.$$

**$\lambda = 1$:** $(A^T A - I)\vec v = \vec 0$.
$$\begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix}\binom{x}{y} = \binom{0}{0} \;\Rightarrow\; x - y = 0 \;\Rightarrow\; x = y.$$
$$\vec v_2 = \tfrac{1}{\sqrt{2}}\binom{1}{1}.$$

$$V = \tfrac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}.$$

## Página 4 — Construcción de $U$ y arranque QR

$$\vec u_i = \tfrac{1}{\sigma_i}\,A\,\vec v_i.$$

$$\vec u_1 = \tfrac{1}{\sqrt{3}}\begin{pmatrix} 1 & -1 \\ 0 & 1 \\ 1 & 0 \end{pmatrix}\cdot \tfrac{1}{\sqrt{2}}\binom{1}{-1} = \tfrac{1}{\sqrt{6}}\binom{2}{-1}{1}.$$

$$\vec u_2 = \tfrac{1}{1}\begin{pmatrix} 1 & -1 \\ 0 & 1 \\ 1 & 0 \end{pmatrix}\cdot \tfrac{1}{\sqrt{2}}\binom{1}{1} = \tfrac{1}{\sqrt{2}}\binom{0}{1}{1}.$$

$$U = \begin{pmatrix} 2/\sqrt{6} & 0 \\ -1/\sqrt{6} & 1/\sqrt{2} \\ 1/\sqrt{6} & 1/\sqrt{2} \end{pmatrix} \quad \text{(forma reducida)}.$$

**Forma larga.** $U \in \mathbb{R}^{3 \times 3}$, $\Sigma \in \mathbb{R}^{3\times 2}$, $V \in \mathbb{R}^{2\times 2}$.

Para hallar $\vec u_3$ hacemos el producto vectorial entre $\vec u_1$ y $\vec u_2$:
$$\vec u_3 = \dfrac{\vec u_1 \times \vec u_2}{\|\vec u_1 \times \vec u_2\|} = \tfrac{1}{\sqrt{3}}\binom{-1}{-1}{1}.$$

(Calculado vía $\vec u_1 \times \vec u_2$ con $\hat i, \hat j, \hat k$.)

$$U = \begin{pmatrix} 2/\sqrt{6} & 0 & -1/\sqrt{3} \\ -1/\sqrt{6} & 1/\sqrt{2} & -1/\sqrt{3} \\ 1/\sqrt{6} & 1/\sqrt{2} & 1/\sqrt{3} \end{pmatrix},\quad \Sigma = \begin{pmatrix} \sqrt{3} & 0 \\ 0 & 1 \\ 0 & 0 \end{pmatrix},\quad V^T = \tfrac{1}{\sqrt{2}}\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}.$$

**b) Factorización QR ($A = QR$).**

$\vec a_1 = (1, 0, 1)^\top$, $\vec a_2 = (-1, 1, 0)^\top$.

**Hallar $Q$:**

$\|\vec a_1\| = \sqrt{2} \;\Rightarrow\; \vec q_1 = \tfrac{1}{\sqrt{2}}\binom{1}{0}{1}$.

Proyectar $\vec a_2$ sobre $\vec q_1$ y restar:
$$\operatorname{Proy}_{\vec q_1}(\vec a_2) = (\vec q_1^T \vec a_2)\,\vec q_1, \quad \vec q_1^T \vec a_2 = -\tfrac{1}{\sqrt{2}}.$$

## Página 5 — Cierre QR

$$\vec p_2 = \vec a_2 - \operatorname{Proy}_{\vec q_1}(\vec a_2) = \binom{-0{,}5}{1}{0{,}5} \;\Rightarrow\; \|\vec p_2\| = \sqrt{3/2}.$$

$$\vec q_2 = \dfrac{\vec p_2}{\|\vec p_2\|} = \tfrac{1}{\sqrt{6}}\binom{-1}{2}{1}.$$

$\vec q_3$ tiene que ser ortogonal a $\vec q_1$ y $\vec q_2$. Hacemos el producto vectorial:
$$\vec q_3 = \vec q_1 \times \vec q_2 = \tfrac{1}{\sqrt{3}}\binom{1}{-1}{1}.$$

$$Q = \begin{pmatrix} 1/\sqrt{2} & -1/\sqrt{6} & 1/\sqrt{3} \\ 0 & 2/\sqrt{6} & -1/\sqrt{3} \\ 1/\sqrt{2} & 1/\sqrt{6} & 1/\sqrt{3} \end{pmatrix},\quad R = Q^T A = \begin{pmatrix} \sqrt{2} & -1/\sqrt{2} \\ 0 & \sqrt{3/2} \\ 0 & 0 \end{pmatrix}.$$

**Nota:** $R_{11} = \|\vec a_1\| = \sqrt{2}$; $R_{12} = \vec q_1^T \vec a_2 = -\tfrac{1}{\sqrt{2}}$; $R_{22} = \|\vec p_2\| = \sqrt{3/2}$.

## Página 6

> ⚠️ Página en blanco.
