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

#### a) Descomposición SVD ($A = U\Sigma V^T$)

$A$ es $3\times 2$, así que $\Sigma$ es $3\times 2$, $U$ es $3\times 3$ y $V$ es $2\times 2$. Arrancamos por la matriz chica $A^TA$ (de $2\times2$):

$$A^T A = \begin{pmatrix} 3 & 5 & -2 \\ 1 & -1 & -3 \end{pmatrix}\begin{pmatrix} 3 & 1 \\ 5 & -1 \\ -2 & -3 \end{pmatrix} = \begin{pmatrix} 38 & 4 \\ 4 & 11 \end{pmatrix}$$

**Autovalores de $A^TA$.** Polinomio característico:

$$p(\lambda) = \det(\lambda I - A^TA) = (\lambda-38)(\lambda-11) - 16 = \lambda^2 - 49\lambda + (418-16) = \lambda^2 - 49\lambda + 402.$$

$$\lambda_{1,2} = \frac{49 \pm \sqrt{49^2 - 4\cdot 402}}{2} = \frac{49 \pm \sqrt{2401-1608}}{2} = \frac{49 \pm \sqrt{793}}{2}.$$

Como $\sqrt{793}\approx 28.160$:

$$\boxed{\lambda_1 = \frac{49+\sqrt{793}}{2} \approx 38.580, \qquad \lambda_2 = \frac{49-\sqrt{793}}{2} \approx 10.420.}$$

> **Orden decreciente (clave).** Los valores singulares se ordenan de mayor a menor, así que $\lambda_1$ es el **mayor**. La resolución oficial del PDF dejó los $\sigma$ en orden invertido; lo corregimos para que $\sigma_1 \ge \sigma_2$:
> $$\sigma_1 = \sqrt{\lambda_1} \approx \sqrt{38.580} \approx 6.2113, \qquad \sigma_2 = \sqrt{\lambda_2} \approx \sqrt{10.420} \approx 3.2280.$$

**Vectores singulares derechos $v_i$** (autovectores normalizados de $A^TA$). De $(A^TA - \lambda I)v = 0$, la primera fila da $(38-\lambda)x + 4y = 0$, o sea $v \parallel (4,\ \lambda-38)$.

- Para $\lambda_1 \approx 38.580$: $v_1 \parallel (4,\ 0.5801)$, con norma $\sqrt{16+0.5801^2}\approx 4.0418$, luego
$$v_1 \approx (0.9896,\ 0.1435).$$
- Para $\lambda_2 \approx 10.420$: $v_2 \parallel (4,\ -27.580)$, con norma $\approx 27.869$, luego
$$v_2 \approx (0.1435,\ -0.9896).$$

(Son ortogonales, $v_1\cdot v_2 = 0$, como debe ser por ser $A^TA$ simétrica.)

**Vectores singulares izquierdos** $u_i = \dfrac{1}{\sigma_i}A v_i$ (para $\sigma_i>0$):

$$u_1 = \frac{1}{\sigma_1}A v_1 = \frac{1}{6.2113}\begin{pmatrix} 3 & 1 \\ 5 & -1 \\ -2 & -3 \end{pmatrix}\begin{pmatrix} 0.9896 \\ 0.1435 \end{pmatrix} \approx (0.5011,\ 0.7735,\ -0.3880),$$

$$u_2 = \frac{1}{\sigma_2}A v_2 = \frac{1}{3.2280}\begin{pmatrix} 3 & 1 \\ 5 & -1 \\ -2 & -3 \end{pmatrix}\begin{pmatrix} 0.1435 \\ -0.9896 \end{pmatrix} \approx (-0.1732,\ 0.5289,\ 0.8308).$$

Ambos son unitarios y ortogonales entre sí.

**Tercer vector $u_3$ (completar la base de $U$).** Como $A$ tiene solo $2$ valores singulares no nulos, falta una columna de $U$. Se toma una base ortonormal de $N(A^T)$ (lo que es ortogonal a $u_1,u_2$). Resolviendo $A^T u = 0$:

$$\begin{cases} 3x + 5y - 2z = 0 \\ x - y - 3z = 0 \end{cases} \implies u \parallel (17,\ -7,\ 8).$$

Como $\lVert(17,-7,8)\rVert = \sqrt{17^2+7^2+8^2} = \sqrt{402} \approx 20.050$:

$$u_3 = \frac{1}{\sqrt{402}}(17,\ -7,\ 8) \approx (0.8479,\ -0.3491,\ 0.3990).$$

**Resultado.** Reuniendo todo (valores exactos $\sigma_1=\sqrt{\tfrac{49+\sqrt{793}}{2}}$, $\sigma_2=\sqrt{\tfrac{49-\sqrt{793}}{2}}$):

$$U \approx \begin{pmatrix} 0.5011 & -0.1732 & 0.8479 \\ 0.7735 & 0.5289 & -0.3491 \\ -0.3880 & 0.8308 & 0.3990 \end{pmatrix}, \quad \Sigma \approx \begin{pmatrix} 6.2113 & 0 \\ 0 & 3.2280 \\ 0 & 0 \end{pmatrix}, \quad V \approx \begin{pmatrix} 0.9896 & 0.1435 \\ 0.1435 & -0.9896 \end{pmatrix}.$$

**Verificación** (numérica con numpy): $U\Sigma V^T$ reproduce $A$ con error máximo $\sim 2\times10^{-15}$, y $U^TU = I_3$. ✓

$$U\Sigma V^T = \begin{pmatrix} 3 & 1 \\ 5 & -1 \\ -2 & -3 \end{pmatrix} = A. \checkmark$$

#### b) Factorización QR ($A = QR$, Gram–Schmidt)

Sean las columnas $a_1=(3,5,-2)$, $a_2=(1,-1,-3)$.

**Primera columna.**
$$u_1 = a_1 = (3,5,-2), \qquad \lVert u_1\rVert = \sqrt{9+25+4} = \sqrt{38} \approx 6.1644,$$
$$v_1 = \frac{u_1}{\lVert u_1\rVert} = \frac{1}{\sqrt{38}}(3,5,-2) \approx (0.4867,\ 0.8111,\ -0.3244).$$

Esto fija $r_{11} = \lVert u_1\rVert = \sqrt{38}$.

**Segunda columna.** El coeficiente de proyección es
$$r_{12} = \langle a_2, v_1\rangle = \frac{a_2\cdot a_1}{\sqrt{38}} = \frac{3-5+6}{\sqrt{38}} = \frac{4}{\sqrt{38}} \approx 0.6489.$$

Restamos la proyección:
$$u_2 = a_2 - r_{12}\,v_1 = a_2 - \frac{4}{38}a_1 = (1,-1,-3) - \frac{2}{19}(3,5,-2) = \left(\tfrac{13}{19},\ -\tfrac{29}{19},\ -\tfrac{53}{19}\right) \approx (0.6842,\ -1.5263,\ -2.7895).$$

Su norma (vía $\lVert u_2\rVert^2 = \lVert a_2\rVert^2 - r_{12}^2 = 11 - \tfrac{16}{38} = \tfrac{201}{19}$):
$$r_{22} = \lVert u_2\rVert = \sqrt{\tfrac{201}{19}} \approx 3.2525,$$
$$v_2 = \frac{u_2}{\lVert u_2\rVert} \approx (0.2104,\ -0.4693,\ -0.8576).$$

**Resultado.**

$$Q = (v_1 \mid v_2) \approx \begin{pmatrix} 0.4867 & 0.2104 \\ 0.8111 & -0.4693 \\ -0.3244 & -0.8576 \end{pmatrix}, \qquad R = \begin{pmatrix} \sqrt{38} & \tfrac{4}{\sqrt{38}} \\ 0 & \sqrt{\tfrac{201}{19}} \end{pmatrix} \approx \begin{pmatrix} 6.1644 & 0.6489 \\ 0 & 3.2525 \end{pmatrix}.$$

**Verificación** (numpy): $QR = A$ con error máximo $\sim 10^{-16}$, y $Q^TQ = I_2$. ✓

$$QR = \begin{pmatrix} 3 & 1 \\ 5 & -1 \\ -2 & -3 \end{pmatrix} = A. \checkmark$$
