---
tags: [pizarron, svd, valores-singulares, pseudo-inversa, descomposicion]
fuente: raw/Practicas/Pizarrones/clase_svd.pdf
tipo: escaneo
---

# Pizarrón — Clase de SVD: descomposición en valores singulares y pseudo-inversa

Ejemplos completos de cálculo de SVD para matrices $4 \times 3$, $2 \times 1$ y $2 \times 3$, incluyendo el cálculo de la **pseudo-inversa de Moore-Penrose** $A^+ = V\Sigma^+ U^T$.

## Página 1 — SVD de una matriz $4 \times 3$

Se pide verificar la descomposición en valores singulares (SVD) de la matriz $A$.

$$A\, U\, \Sigma\, V^T \quad \text{(forma: } A = U\Sigma V^T\text{)} \quad \text{con } V^T V = I.$$

Verificar las siguientes SVD (completa y reducida) que se proponen.

$$A\,A^T = A^T A + I \quad \text{(condición consistente con } A^T A = V\Sigma^T \Sigma V^T\text{)}$$
$$U: A A^T \quad ;\quad V: A^T A$$

**Cálculo:**
$$A^T A = \begin{pmatrix} 0 & 4 & 4 & 0 \\ 3 & 1 & 1 & 3 \\ 3 & -1 & -1 & 3 \end{pmatrix}\begin{pmatrix} 0 & 3 & 3 \\ 4 & 1 & -1 \\ 4 & 1 & -1 \\ 0 & 3 & 3 \end{pmatrix} = \begin{pmatrix} 32 & 8 & -8 \\ 8 & 20 & 16 \\ -8 & 16 & 20 \end{pmatrix}.$$

$\det(A^T A - \lambda I) = 0$:
$$\begin{vmatrix} 32 - \lambda & 8 & -8 \\ 8 & 20 - \lambda & 16 \\ -8 & 16 & 20 - \lambda \end{vmatrix} = -\lambda (\lambda - 36)^2 \quad \rightarrow\; \lambda_1 = 36,\; \lambda_2 = 36,\; \lambda_3 = 0.$$

(En el pizarrón se desarrolla y se llega a la factorización $\lambda(\lambda - 36)^2 = 0$.)

Valores singulares: $\sigma_1 = \sqrt{36} = 6,\; \sigma_2 = \sqrt{36} = 6,\; \sigma_3 = 0$.

**Autovectores de $A^T A$ (matriz $V$):**

**$\lambda = 36$:** $(A^T A - 36 I)\vec v = 0$:
$$\begin{pmatrix} -4 & 8 & -8 \\ 8 & -16 & 16 \\ -8 & 16 & -16 \end{pmatrix}\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \vec 0 \;\Rightarrow\; -4x + 8y - 8z = 0 \;\Rightarrow\; x = 2y - 2z.$$

$$(x, y, z) = (2y - 2z, y, z) = y(2, 1, 0) + z(-2, 0, 1)$$

$$\vec v_1 \propto (2, 1, 0), \;\; \vec v_2 \propto (-2, 0, 1)\;\text{(o equivalentes ortogonalizados)}.$$

Norma de $\vec v_1$: $\sqrt{4 + 1 + 0} = \sqrt{5}$; norma de $\vec v_2$: $\sqrt{4 + 0 + 1} = \sqrt{5}$ — el pizarrón normaliza por $\sqrt{9}$ tras ortogonalizar: $\vec v_1 = \tfrac{1}{3}\binom{2}{2}{1}$, $\vec v_2 = \tfrac{1}{3}\binom{2}{-1}{-2}$.

## Página 2 — $V$, $U$, expresión final y caso $A = (1, 3)^T$

$$V = \tfrac{1}{3}\begin{pmatrix} 2 & 2 \\ 2 & -1 \\ 1 & -2 \end{pmatrix} \;\Rightarrow\; V^T = \tfrac{1}{3}\begin{pmatrix} 2 & 2 & 1 \\ 2 & -1 & -2 \end{pmatrix}.$$

$A\vec v_i = \sigma_i\vec u_i \;\Rightarrow\; \vec u_i = \tfrac{1}{\sigma_i}A\vec v_i$.

$$\vec u_1 = \tfrac{1}{6}\begin{pmatrix} 0 & 3 & 3 \\ 4 & 1 & -1 \\ 4 & 1 & -1 \\ 0 & 3 & 3 \end{pmatrix}\cdot \tfrac{1}{3}\binom{2}{2}{1} = \tfrac{1}{2}\binom{1}{1}{1}{1}.$$

$$\vec u_2 = \tfrac{1}{6}\begin{pmatrix} 0 & 3 & 3 \\ 4 & 1 & -1 \\ 4 & 1 & -1 \\ 0 & 3 & 3 \end{pmatrix}\cdot \tfrac{1}{3}\binom{2}{-1}{-2} = \tfrac{1}{2}\binom{-1}{1}{1}{-1}.$$

$$U = \tfrac{1}{2}\begin{pmatrix} 1 & -1 \\ 1 & 1 \\ 1 & 1 \\ 1 & -1 \end{pmatrix}.$$

$$A = U\Sigma V^T = \tfrac{1}{2}\begin{pmatrix} 1 & -1 \\ 1 & 1 \\ 1 & 1 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} 6 & 0 \\ 0 & 6 \end{pmatrix}\tfrac{1}{3}\begin{pmatrix} 2 & 2 & 1 \\ 2 & -1 & -2 \end{pmatrix} \quad \text{(forma reducida)}.$$

**Forma completa:**
$$A = \tfrac{1}{2}\begin{pmatrix} 1 & -1 & 1 & 1 \\ 1 & 1 & -1 & 1 \\ 1 & 1 & 1 & -1 \\ 1 & -1 & -1 & -1 \end{pmatrix}\begin{pmatrix} 6 & 0 & 0 \\ 0 & 6 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}\tfrac{1}{3}\begin{pmatrix} 2 & 2 & 1 \\ 2 & -1 & -2 \\ -1 & 2 & -2 \end{pmatrix}.$$

(Las dos columnas extra de $U$ son ortogonales a $\vec u_1, \vec u_2$ y completan una base: $(1, 0, 0, -1)$ y $(0, 1, -1, 0)$.)

**Encuentre la SVD y la pseudo-inversa de:**

### Matriz $A = \binom{1}{3} \in \mathbb{R}^{2\times 1}$

$$A^T A = (1\;3)\binom{1}{3} = 10 \;\Rightarrow\; \lambda_1 = 10,\; \sigma_1 = \sqrt{10}.$$
$$\Sigma = \binom{\sqrt{10}}{0}.$$

Autovector: $(10 - 10\cdot I)x = 0 \;\Rightarrow\; 0\cdot x = 0$, así $V = (1)$ (matriz $1\times 1$).

## Página 3 — $U$, expresión y matriz $C \in \mathbb{R}^{2\times 3}$

$$\vec u_1 = \tfrac{1}{\sigma_1}\cdot A\cdot \vec v_1 = \tfrac{1}{\sqrt{10}}\binom{1}{3}\cdot 1 = \tfrac{1}{\sqrt{10}}\binom{1}{3}.$$

$$\vec u_2 = \tfrac{1}{\sqrt{10}}\binom{-3}{1} \quad \text{(para que sea ortonormal a } \vec u_1\text{)}.$$

$$U = \tfrac{1}{\sqrt{10}}\begin{pmatrix} 1 & -3 \\ 3 & 1 \end{pmatrix}.$$

$$A = U\Sigma V^T = \tfrac{1}{\sqrt{10}}\begin{pmatrix} 1 & -3 \\ 3 & 1 \end{pmatrix}\binom{\sqrt{10}}{0}\cdot(1).$$

**Pseudo-inversa $A^+$** (Moore-Penrose) con $A \in \mathbb{R}^{m\times n}$:
$$A^+ = V\Sigma^+ U^T = (1)\cdot \big(\tfrac{1}{\sqrt{10}}\;\;0\big)\cdot \tfrac{1}{\sqrt{10}}\begin{pmatrix} 1 & 3 \\ -3 & 1 \end{pmatrix} = \tfrac{1}{10}(1\;\;3).$$

Verificación: $A^+ A = 1$.

### Matriz $C = \begin{pmatrix} 3 & 2 & 2 \\ 2 & 3 & -2 \end{pmatrix} \in \mathbb{R}^{2\times 3}$, $C C^T \in \mathbb{R}^{2\times 2}$.

> Estrategia: como $C C^T$ es $2\times 2$ y $C^T C$ es $3\times 3$, conviene calcular $C C^T$.

$$C C^T = \begin{pmatrix} 3 & 2 & 2 \\ 2 & 3 & -2 \end{pmatrix}\begin{pmatrix} 3 & 2 \\ 2 & 3 \\ 2 & -2 \end{pmatrix} = \begin{pmatrix} 17 & 8 \\ 8 & 17 \end{pmatrix}.$$

$|C C^T - \lambda I| = 0$:
$$\det\!\begin{pmatrix} 17 - \lambda & 8 \\ 8 & 17 - \lambda \end{pmatrix} = (17 - \lambda)^2 - 64 = 0 \;\Rightarrow\; 17 - \lambda = \pm 8.$$

$\lambda_1 = 25 \;\Rightarrow\; \sigma_1 = 5;\; \lambda_2 = 9 \;\Rightarrow\; \sigma_2 = 3$.

$$\Sigma = \begin{pmatrix} 5 & 0 & 0 \\ 0 & 3 & 0 \end{pmatrix}.$$

**Autovectores de $CC^T$:**

**$\lambda_1 = 25$:** $(CC^T - 25 I)\vec u = \vec 0$
$$\begin{pmatrix} -8 & 8 \\ 8 & -8 \end{pmatrix}\vec u = \vec 0 \;\Rightarrow\; \vec u_1 = \tfrac{1}{\sqrt{2}}\binom{1}{1}.$$

## Página 4 — Caso 2×3: cierre SVD y pseudo-inversa

**$\lambda_2 = 9$:** $(CC^T - 9I)\vec u = 0$:
$$\begin{pmatrix} 8 & 8 \\ 8 & 8 \end{pmatrix}\vec u = \vec 0 \;\Rightarrow\; \vec u_2 = \tfrac{1}{\sqrt{2}}\binom{1}{-1}.$$

$$U = \tfrac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}.$$

**Cálculo de $V$:** $\vec v_i = \tfrac{1}{\sigma_i}\,C^T\,\vec u_i$, $V \in \mathbb{R}^{3\times 3}$.

$$\vec v_1 = \tfrac{1}{5}\begin{pmatrix} 3 & 2 \\ 2 & 3 \\ 2 & -2 \end{pmatrix}\cdot \tfrac{1}{\sqrt{2}}\binom{1}{1} = \tfrac{1}{\sqrt{2}}\binom{1}{1}{0}.$$

$$\vec v_2 = \tfrac{1}{3}\begin{pmatrix} 3 & 2 \\ 2 & 3 \\ 2 & -2 \end{pmatrix}\cdot \tfrac{1}{\sqrt{2}}\binom{1}{-1} = \tfrac{1}{3\sqrt{2}}\binom{1}{-1}{4}.$$

Se necesita un $\vec v_3$ ortogonal a $\vec v_1$ y $\vec v_2$ — producto vectorial:
$$\vec v_3 = \vec v_1 \times \vec v_2 = \tfrac{1}{\sqrt{2}}\binom{1}{1}{0} \times \tfrac{1}{3\sqrt{2}}\binom{1}{-1}{4}.$$

Con $\vec v_1 = (1, 1, 0)$ y $\vec v_2 = (1, -1, 4)$ (sin normalizar):
$$\begin{vmatrix} \hat i & \hat j & \hat k \\ 1 & 1 & 0 \\ 1 & -1 & 4 \end{vmatrix} = 4\hat i - 4\hat j - 2\hat k = (4, -4, -2) \;\Rightarrow\; \vec v_3 = \tfrac{1}{6}\cdot 2\,(2, -2, -1) = \tfrac{1}{3}(2, -2, -1).$$

(Norma: $\sqrt{4 + 4 + 1} = 3$.)

$$V = \begin{pmatrix} 1/\sqrt{2} & 1/(3\sqrt{2}) & 2/3 \\ 1/\sqrt{2} & -1/(3\sqrt{2}) & -2/3 \\ 0 & 4/(3\sqrt{2}) & -1/3 \end{pmatrix}.$$

**Pseudo-inversa $C^+$:**
$$\Sigma^+ = \begin{pmatrix} 1/5 & 0 \\ 0 & 1/3 \\ 0 & 0 \end{pmatrix}, \quad U^T = \tfrac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}.$$

$$C^+ = V\Sigma^+ U^T = \tfrac{1}{45}\begin{pmatrix} 7 & 2 \\ 2 & 7 \\ 10 & -10 \end{pmatrix}.$$

## Página 5

> ⚠️ Página en blanco.
