---
tags: [parcial, ip, resolucion, transformaciones-lineales, nucleo-imagen, svd, qr, cuadrados-minimos]
fuente: raw/Practicas/Modelos_Examenes/MNA_IP_Tema_II.pdf
tipo: ip
tema: 2
tiene_resolucion: true
---

# Primer Parcial de Métodos Numéricos Avanzados — Tema II (Resolución)

## Ejercicio 1

Dada la Transformación Lineal $T : \mathbb{R}^3 \to \mathbb{R}^3 : T(x, y, z) = (x - y + z,\ x + 3y - z,\ z + y - 2x)$

a) Hallar el Núcleo y la Imagen.
b) Hallar $(x, y, z)$, si existe, de modo que $T(x, y, z) = (2, 2, -2)$.

### Resolución

Armamos la matriz en base canónica $M_{EE}(T)$ poniendo como columna $j$ el vector $T(e_j)$:

$$T(e_1) = T(1,0,0) = (1,\ 1,\ -2),\quad T(e_2) = T(0,1,0) = (-1,\ 3,\ 1),\quad T(e_3) = T(0,0,1) = (1,\ -1,\ 1).$$

$$A = M_{EE}(T) = \begin{pmatrix} 1 & -1 & 1 \\ 1 & 3 & -1 \\ -2 & 1 & 1 \end{pmatrix}$$

**a) Núcleo.** Resolvemos $AX = 0$ por Gauss. Hacemos $F_2 \leftarrow F_2 - F_1$ y $F_3 \leftarrow F_3 + 2F_1$:

$$\begin{pmatrix} 1 & -1 & 1 \\ 1 & 3 & -1 \\ -2 & 1 & 1 \end{pmatrix} \longrightarrow \begin{pmatrix} 1 & -1 & 1 \\ 0 & 4 & -2 \\ 0 & -1 & 3 \end{pmatrix}.$$

Ahora $F_3 \leftarrow F_3 + \tfrac14 F_2$:

$$\longrightarrow \begin{pmatrix} 1 & -1 & 1 \\ 0 & 4 & -2 \\ 0 & 0 & \tfrac52 \end{pmatrix}.$$

Hay **tres pivotes** ($1,\ 4,\ \tfrac52$), de modo que $\operatorname{rg}(A) = 3$. De la última fila $\tfrac52 z = 0 \Rightarrow z = 0$, luego $4y = 0 \Rightarrow y = 0$, y finalmente $x = 0$. Por lo tanto

$$\boxed{N(T) = \{(0,0,0)\}.}$$

Equivalentemente, $\det(A) = 10 \ne 0$ confirma que el único elemento del núcleo es el nulo. Por el **Teorema de la dimensión**,

$$\dim N(T) + \dim \operatorname{Im}(T) = 3 \implies \dim \operatorname{Im}(T) = 3,$$

así que las tres columnas son pivote y

$$\boxed{\operatorname{Im}(T) = \mathbb{R}^3.}$$

$T$ es entonces inyectiva ($N(T)=\{0\}$), sobreyectiva ($\operatorname{rg}(A)=3=\dim\mathbb{R}^3$) y por ser cuadrada con $\det\neq0$, un **isomorfismo**.

**b) Antiimagen de $(2,2,-2)$.** Como $T$ es biyectiva, la solución existe y es única. Resolvemos $AX = (2,2,-2)^T$. Aplicamos las mismas operaciones de fila al vector ampliado $b = (2,2,-2)$:

$$\left(\begin{array}{ccc|c} 1 & -1 & 1 & 2 \\ 1 & 3 & -1 & 2 \\ -2 & 1 & 1 & -2 \end{array}\right) \xrightarrow{\substack{F_2 - F_1 \\ F_3 + 2F_1}} \left(\begin{array}{ccc|c} 1 & -1 & 1 & 2 \\ 0 & 4 & -2 & 0 \\ 0 & -1 & 3 & 2 \end{array}\right) \xrightarrow{F_3 + \tfrac14 F_2} \left(\begin{array}{ccc|c} 1 & -1 & 1 & 2 \\ 0 & 4 & -2 & 0 \\ 0 & 0 & \tfrac52 & 2 \end{array}\right).$$

Hacia atrás:

$$\tfrac52 z = 2 \implies z = \tfrac45, \qquad 4y - 2z = 0 \implies y = \tfrac{z}{2} = \tfrac25, \qquad x - y + z = 2 \implies x = 2 + \tfrac25 - \tfrac45 = \tfrac85.$$

$$\boxed{(x,y,z) = \left(\tfrac85,\ \tfrac25,\ \tfrac45\right) = (1.6,\ 0.4,\ 0.8).}$$

> **Verificación numérica.** $\det(A) = 10$, $\operatorname{rg}(A) = 3$ (confirmado por `numpy.linalg.matrix_rank`). Resolviendo $AX = (2,2,-2)$ con `numpy.linalg.solve` da $X = (1.6,\ 0.4,\ 0.8)$ y $A\,X = (2,\ 2,\ -2)$ exacto; la solución por la regla de Cramer con fracciones es $\left(\tfrac85, \tfrac25, \tfrac45\right)$.

## Ejercicio 2

Considere la matriz

$$A = \begin{pmatrix} 0.55 & 1.1 \\ 1.1 & 0.8 \end{pmatrix}$$

a) Realizar la descomposición en valores singulares (SVD).
b) Realizar la factorización QR.

### Resolución

**a) SVD $A = U\Sigma V^T$.** Como $A$ es $2\times2$, $V$ sale de los autovectores de $A^TA$ ($A$ es simétrica, pero igual seguimos la receta general). Calculamos

$$A^TA = \begin{pmatrix} 0.55 & 1.1 \\ 1.1 & 0.8 \end{pmatrix}\begin{pmatrix} 0.55 & 1.1 \\ 1.1 & 0.8 \end{pmatrix} = \begin{pmatrix} 1.5125 & 1.485 \\ 1.485 & 1.85 \end{pmatrix}.$$

Polinomio característico $p(\lambda) = \lambda^2 - \operatorname{tr}\lambda + \det$ con $\operatorname{tr}(A^TA) = 3.3625$ y $\det(A^TA) = 1.5125\cdot1.85 - 1.485^2 = 0.5929$:

$$p(\lambda) = \lambda^2 - 3.3625\,\lambda + 0.5929 = 0 \implies \lambda = \frac{3.3625 \pm \sqrt{3.3625^2 - 4(0.5929)}}{2} = \frac{3.3625 \pm \sqrt{8.9348}}{2}.$$

Como $\sqrt{8.9348} \approx 2.9891$:

$$\lambda_1 \approx 3.1758, \qquad \lambda_2 \approx 0.1867.$$

Los valores singulares (raíces, en orden decreciente) son

$$\sigma_1 = \sqrt{\lambda_1} \approx 1.7821, \qquad \sigma_2 = \sqrt{\lambda_2} \approx 0.4321.$$

**Autovectores de $A^TA$** (columnas de $V$). Para $\lambda_1$, de $(1.5125 - \lambda_1)x + 1.485\,y = 0$ se obtiene $\tfrac{y}{x} = \tfrac{\lambda_1 - 1.5125}{1.485} \approx 1.1201$, así que $\tilde v_1 \approx (1,\ 1.1201)$; normalizando,

$$v_1 \approx (0.6660,\ 0.7460).$$

Para $\lambda_2$ resulta $\tfrac{y}{x} \approx -0.8928$, $\tilde v_2 \approx (1,\ -0.8928)$ (también es $v_1$ rotado $90^\circ$, por ortogonalidad), normalizando:

$$v_2 \approx (-0.7460,\ 0.6660).$$

$$V \approx \begin{pmatrix} 0.6660 & -0.7460 \\ 0.7460 & 0.6660 \end{pmatrix}.$$

Las columnas de $U$ con $\sigma_i > 0$ salen de $u_i = \dfrac{A v_i}{\sigma_i}$:

$$u_1 = \frac{A v_1}{\sigma_1} \approx (0.6660,\ 0.7460), \qquad u_2 = \frac{A v_2}{\sigma_2} \approx (0.7460,\ -0.6660).$$

$$\boxed{\;U \approx \begin{pmatrix} 0.6660 & 0.7460 \\ 0.7460 & -0.6660 \end{pmatrix},\quad \Sigma \approx \begin{pmatrix} 1.7821 & 0 \\ 0 & 0.4321 \end{pmatrix},\quad V \approx \begin{pmatrix} 0.6660 & -0.7460 \\ 0.7460 & 0.6660 \end{pmatrix}.}$$

> **Verificación numérica.** $U\Sigma V^T = \begin{pmatrix}0.55 & 1.1\\ 1.1 & 0.8\end{pmatrix} = A$ (coincide a $10^{-8}$) y $U^TU = I$, $V^TV = I$. `numpy.linalg.svd` devuelve los mismos $\sigma = (1.7821,\ 0.4321)$ (los signos de las columnas de $U,V$ pueden diferir globalmente, lo cual es admisible).

**b) Factorización QR (Gram–Schmidt).** Columnas de $A$: $a_1 = (0.55,\ 1.1)$, $a_2 = (1.1,\ 0.8)$. Notar que $a_1 = 0.55\,(1,\ 2)$.

$$u_1 = a_1, \qquad r_{11} = \lVert u_1 \rVert = \sqrt{0.55^2 + 1.1^2} = \sqrt{1.5125} = 0.55\sqrt5 \approx 1.2298,$$

$$v_1 = \frac{u_1}{r_{11}} = \frac{1}{\sqrt5}(1,\ 2) \approx (0.4472,\ 0.8944).$$

Proyección de $a_2$ sobre $v_1$:

$$r_{12} = \langle a_2, v_1\rangle = \frac{1.1 + 1.6}{\sqrt5} = \frac{2.7}{\sqrt5} \approx 1.2075,$$

$$u_2 = a_2 - r_{12}\,v_1 = (1.1,\ 0.8) - 1.2075\,(0.4472,\ 0.8944) = (0.56,\ -0.28),$$

$$r_{22} = \lVert u_2 \rVert = \frac{1.4}{\sqrt5} \approx 0.6261, \qquad v_2 = \frac{u_2}{r_{22}} = \frac{1}{\sqrt5}(2,\ -1) \approx (0.8944,\ -0.4472).$$

$$\boxed{\;Q = \frac{1}{\sqrt5}\begin{pmatrix} 1 & 2 \\ 2 & -1 \end{pmatrix} \approx \begin{pmatrix} 0.4472 & 0.8944 \\ 0.8944 & -0.4472 \end{pmatrix},\quad R = \begin{pmatrix} 1.2298 & 1.2075 \\ 0 & 0.6261 \end{pmatrix}.}$$

> **Verificación numérica.** $QR = \begin{pmatrix}0.55 & 1.1\\ 1.1 & 0.8\end{pmatrix} = A$ y $Q^TQ = I$ (coinciden a $10^{-8}$). `numpy.linalg.qr` da el mismo $Q$ y $R$ salvo el signo global de columna que `numpy` elige (diagonal negativa); la versión de Gram–Schmidt aquí tiene $R_{ii} > 0$, como pide la receta.

## Ejercicio 3

Dado el siguiente conjunto de datos

| $x$ | $y$ |
|---|---|
| $0$ | $0.78$ |
| $1$ | $1.9$ |
| $2$ | $6.7$ |

Usando cuadrados mínimos, ajuste los datos al modelo $y(x) = a\,x^2 + b$ utilizando descomposición QR. Dé $a$, $b$ y la norma del residuo.

### Resolución

El modelo es lineal en los parámetros $(a,b)$. La matriz de diseño tiene como columnas $(x_i^2,\ 1)$:

$$A = \begin{pmatrix} x_1^2 & 1 \\ x_2^2 & 1 \\ x_3^2 & 1 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & 1 \\ 4 & 1 \end{pmatrix}, \qquad b = \begin{pmatrix} 0.78 \\ 1.9 \\ 6.7 \end{pmatrix}, \qquad X = \begin{pmatrix} a \\ b \end{pmatrix}.$$

Buscamos $X$ que minimice $\lVert AX - b\rVert$. Con QR ($A = QR$), el sistema normal se reduce a $R\,X = Q^Tb$.

**Gram–Schmidt sobre las columnas de $A$.** $a_1 = (0,\ 1,\ 4)$, $a_2 = (1,\ 1,\ 1)$.

$$r_{11} = \lVert a_1\rVert = \sqrt{0 + 1 + 16} = \sqrt{17} \approx 4.1231, \qquad v_1 = \frac{1}{\sqrt{17}}(0,\ 1,\ 4) \approx (0,\ 0.2425,\ 0.9701).$$

$$r_{12} = \langle a_2, v_1\rangle = \frac{0 + 1 + 4}{\sqrt{17}} = \frac{5}{\sqrt{17}} \approx 1.2127,$$

$$u_2 = a_2 - r_{12}v_1 = (1,\ 1,\ 1) - \tfrac{5}{17}(0,\ 1,\ 4) = \left(1,\ \tfrac{12}{17},\ -\tfrac{3}{17}\right),$$

$$r_{22} = \lVert u_2\rVert = \sqrt{1 + \tfrac{144}{289} + \tfrac{9}{289}} = \sqrt{\tfrac{442}{289}} = \frac{\sqrt{442}}{17} \approx 1.2367,$$

$$v_2 = \frac{u_2}{r_{22}} \approx (0.8086,\ 0.5708,\ -0.1427).$$

$$Q \approx \begin{pmatrix} 0 & 0.8086 \\ 0.2425 & 0.5708 \\ 0.9701 & -0.1427 \end{pmatrix}, \qquad R = \begin{pmatrix} \sqrt{17} & \tfrac{5}{\sqrt{17}} \\ 0 & \tfrac{\sqrt{442}}{17} \end{pmatrix} \approx \begin{pmatrix} 4.1231 & 1.2127 \\ 0 & 1.2367 \end{pmatrix}.$$

**Resolver $R\,X = Q^Tb$.** Con $b = (0.78,\ 1.9,\ 6.7)$:

$$Q^Tb \approx \begin{pmatrix} 0\cdot0.78 + 0.2425\cdot1.9 + 0.9701\cdot6.7 \\ 0.8086\cdot0.78 + 0.5708\cdot1.9 + (-0.1427)\cdot6.7 \end{pmatrix} \approx \begin{pmatrix} 6.9608 \\ 0.7591 \end{pmatrix}.$$

Sustitución hacia atrás en $R\,X = Q^Tb$:

$$r_{22}\,b = 0.7591 \implies b = \frac{0.7591}{1.2367} \approx 0.6138, \qquad r_{11}\,a + r_{12}\,b = 6.9608 \implies a = \frac{6.9608 - 1.2127\cdot0.6138}{4.1231} \approx 1.5077.$$

Por las ecuaciones normales exactas $A^TA\,X = A^Tb$, con $A^TA = \begin{pmatrix}17 & 5\\ 5 & 3\end{pmatrix}$ (det $=26$) y $A^Tb = (28.7,\ 9.38)$, se obtiene la solución racional

$$\boxed{a = \frac{98}{65} \approx 1.5077, \qquad b = \frac{399}{650} \approx 0.6138.}$$

**Norma del residuo.** El vector de residuos $r = AX - b$ vale

$$r = \left(-\tfrac{54}{325},\ \tfrac{72}{325},\ -\tfrac{18}{325}\right) \approx (-0.1662,\ 0.2215,\ -0.0554),$$

$$\lVert r\rVert = \sqrt{\tfrac{648}{8125}} \approx \boxed{0.2824.}$$

Es decir, el ajuste por cuadrados mínimos es $y(x) \approx 1.5077\,x^2 + 0.6138$, con residuo $\approx 0.2824$.

> **Verificación numérica.** `numpy.linalg.qr` reproduce $A = QR$ con $Q^TQ = I$; resolviendo $RX = Q^Tb$ se obtiene $(a,b) = (1.50769\ldots,\ 0.61384\ldots)$. `numpy.linalg.lstsq(A,b)` da exactamente el mismo $(a,b)$ y norma de residuo $0.28241$. El cálculo exacto con fracciones confirma $a=\tfrac{98}{65}$, $b=\tfrac{399}{650}$, $\lVert r\rVert^2 = \tfrac{648}{8125}$. (Atención al término $\sum x_i^2 y_i = 1\cdot1.9 + 4\cdot6.7 = 28.7$, fácil de equivocar.)
