---
tags: [parcial, ip, resolucion, transformaciones-lineales, diagonalizacion, nucleo-imagen]
fuente: raw/Practicas/Modelos_Examenes/MNA_IP_Tema_I_Resolucion.pdf
tipo: ip
tema: 1
tiene_resolucion: true
---

# Primer Parcial de Métodos Numéricos Avanzados — Tema I (Resolución)

## Ejercicio 1

Dada la Transformación Lineal $T : \mathbb{R}^3 \to \mathbb{R}^3 : T(x, y, z) = (2x - y + z,\ x + y - z,\ z + y - x)$

a) Hallar el Núcleo y la Imagen
b) Hallar $(x, y, z)$, si existe, de modo que $T(x, y, z) = (1, 1, -2)$

### Resolución

**a)** Para hallar el núcleo se hace $T(x, y, z) = 0$, lo que implica resolver el sistema de ecuaciones

$$2x - y + z = 0,\quad x + y - z = 0,\quad z + y - x = 0$$

De la segunda ecuación $z = x + y$. Reemplazando en la primera:

$$2x - y + x + y = 0 \implies x = 0 \implies y = z \implies y = 0 \implies z = 0$$

Finalmente $N(T) = \{(0, 0, 0)\}$. Luego por el Teorema de la dimensión $R(T) = \mathbb{R}^3$.

**b)** En este caso hay que resolver el sistema

$$2x - y + z = 1,\quad x + y - z = 1,\quad z + y - x = -2$$

De la segunda ecuación se tiene que $z = x + y - 1$. Reemplazando en la primera queda

$$2x - y + x + y = 2 \implies x = 2/3 \implies z = y - 1/3$$

Reemplazando en la tercera se tiene $y - 1/3 + y - 2/3 = -2 \implies y = -1/2 \implies z = -5/6$.

Luego el valor buscado es $\left(\dfrac{2}{3}, -\dfrac{1}{2}, -\dfrac{5}{6}\right)$.

## Ejercicio 2

Sea $F : \mathbb{R}^3 \to \mathbb{R}^3$ una transformación lineal tal que

$$M(F)_{EE} = \begin{pmatrix} 1 & 0 & 1 \\ 0 & k & 1 \\ 0 & 9 & k \end{pmatrix}$$

a) Hallar todos los valores de $k$ para los cuales $F$ es diagonalizable.
b) Para $k = 3$ hallar una base $B$ de $\mathbb{R}^3$ tal que $M(F)_{BB}$ sea diagonal y dar la expresión de $M(F)_{BB}$.

### Resolución

Se rebautiza $A = M(F)_{EE}$. Luego

$$A_\lambda = \begin{pmatrix} \lambda - 1 & 0 & -1 \\ 0 & \lambda - k & -1 \\ 0 & -9 & \lambda - k \end{pmatrix},\quad p_A(\lambda) = \begin{vmatrix} \lambda - 1 & 0 & -1 \\ 0 & \lambda - k & -1 \\ 0 & -9 & \lambda - k \end{vmatrix} = (\lambda - 1)\left[(\lambda - k)^2 - 9\right]$$

$$p_A(\lambda) = (\lambda - 1)[\lambda - (k + 3)][\lambda - (k - 3)]$$

Claramente $k + 3 \ne k - 3$. Se analizarán casos:

**i)** Si $k + 3 \ne 1$ y $k - 3 \ne 1$, o sea $k \ne -2$ y $k \ne 4$, es diagonalizable.

**ii)** Si $k = -2$ se tiene

$$p_A(\lambda) = (\lambda - 1)^2(\lambda + 5),\quad A_1 = \begin{pmatrix} 0 & 0 & -1 \\ 0 & 3 & -1 \\ 0 & -9 & 3 \end{pmatrix} \implies z = 0,\ y = 0$$

Luego hay un solo autovector $v_1 = (1, 0, 0)$. No es diagonalizable.

**iii)** Si $k = 4$ queda

$$p_A(\lambda) = (\lambda - 1)^2(\lambda - 7),\quad A_1 = \begin{pmatrix} 0 & 0 & -1 \\ 0 & -3 & -1 \\ 0 & -9 & -3 \end{pmatrix} \implies z = 0,\ y = 0$$

Luego hay un solo autovector $v_1 = (1, 0, 0)$. No es diagonalizable.

Finalmente sólo será diagonalizable si $k \in \mathbb{R} - \{-2, 4\}$.

**b)** Si $k = 3$ se tiene

$$A_\lambda = \begin{pmatrix} \lambda - 1 & 0 & -1 \\ 0 & \lambda - 3 & -1 \\ 0 & -9 & \lambda - 3 \end{pmatrix} \implies p_A(\lambda) = (\lambda - 1)[(\lambda - 3)^2 - 9] \implies p_A(\lambda) = \lambda(\lambda - 1)(\lambda - 6)$$

Para $\lambda = 0$:

$$A_0 = \begin{pmatrix} -1 & 0 & -1 \\ 0 & -3 & -1 \\ 0 & -9 & -3 \end{pmatrix} \implies z = -3y,\ x = 3y \implies v_0 = (3, 1, -3)$$

Para $\lambda = 1$:

$$A_1 = \begin{pmatrix} 0 & 0 & -1 \\ 0 & -2 & -1 \\ 0 & -9 & -2 \end{pmatrix} \implies z = y = 0 \implies v_1 = (1, 0, 0)$$

Para $\lambda = 6$:

$$A_6 = \begin{pmatrix} 5 & 0 & -1 \\ 0 & 3 & -1 \\ 0 & -9 & 3 \end{pmatrix} \implies z = 3y = 5x \implies v_6 = (3, 5, 15)$$

$$B = \{(3, 1, -3),\ (1, 0, 0),\ (3, 5, 15)\},\quad M(T)_{BB} = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 6 \end{pmatrix}$$

## Ejercicio 3

Considere la matriz

$$A = \begin{pmatrix} 0.92 & 1.44 \\ 1.44 & 0.08 \end{pmatrix}$$

a) Realizar la descomposición en valores singulares.
b) Realizar la factorización QR.

### Resolución

Observación útil: $A$ es **simétrica** ($A = A^T$). Sus autovalores son

$$p_A(\lambda) = \det(\lambda I - A) = (\lambda - 0.92)(\lambda - 0.08) - 1.44^2 = \lambda^2 - \lambda - 2 = (\lambda - 2)(\lambda + 1),$$

es decir $\lambda = 2$ y $\lambda = -1$. Esto no se usa directamente para la SVD (que necesita $A^TA$), pero sí explica por qué los valores singulares resultarán "lindos": $|\det A| = |2 \cdot (-1)| = 2$.

#### a) Descomposición en valores singulares $A = U\Sigma V^T$

**Paso 1 — autovalores de $A^TA$.** Como $A$ es simétrica, $A^TA = A^2$:

$$A^TA = \begin{pmatrix} 0.92 & 1.44 \\ 1.44 & 0.08 \end{pmatrix}\begin{pmatrix} 0.92 & 1.44 \\ 1.44 & 0.08 \end{pmatrix} = \begin{pmatrix} 2.92 & 1.44 \\ 1.44 & 2.08 \end{pmatrix}.$$

$$p_{A^TA}(\lambda) = (\lambda - 2.92)(\lambda - 2.08) - 1.44^2 = \lambda^2 - 5\lambda + 4 = (\lambda - 4)(\lambda - 1).$$

Luego $\lambda_1 = 4$, $\lambda_2 = 1$, y los **valores singulares** (raíces, en orden decreciente) son

$$\boxed{\sigma_1 = \sqrt{4} = 2, \qquad \sigma_2 = \sqrt{1} = 1.}$$

(Coincide con $|\lambda_i(A)| = \{2, 1\}$, propio de una matriz simétrica.)

**Paso 2 — autovectores de $A^TA$ → columnas de $V$.**

Para $\lambda_1 = 4$: $(A^TA - 4I)X = 0$,

$$\begin{pmatrix} -1.08 & 1.44 \\ 1.44 & -1.92 \end{pmatrix}X = 0 \implies -1.08\,x + 1.44\,y = 0 \implies y = \tfrac{3}{4}x \implies \tilde v_1 = (4, 3).$$

$\lVert \tilde v_1\rVert = 5$, de donde $v_1 = \left(\tfrac{4}{5}, \tfrac{3}{5}\right) = (0.8,\ 0.6)$.

Para $\lambda_2 = 1$: $(A^TA - I)X = 0$,

$$\begin{pmatrix} 1.92 & 1.44 \\ 1.44 & 1.08 \end{pmatrix}X = 0 \implies 1.92\,x + 1.44\,y = 0 \implies y = -\tfrac{4}{3}x \implies \tilde v_2 = (3, -4).$$

$\lVert \tilde v_2\rVert = 5$, de donde $v_2 = \left(\tfrac{3}{5}, -\tfrac{4}{5}\right) = (0.6,\ -0.8)$. (Verificamos $v_1 \perp v_2$: $0.8\cdot0.6 + 0.6\cdot(-0.8) = 0$ ✓.)

$$V = \begin{pmatrix} 0.8 & 0.6 \\ 0.6 & -0.8 \end{pmatrix}.$$

**Paso 3 — columnas de $U$** mediante $u_i = \dfrac{A v_i}{\sigma_i}$:

$$u_1 = \frac{1}{2}\begin{pmatrix} 0.92 & 1.44 \\ 1.44 & 0.08 \end{pmatrix}\begin{pmatrix} 0.8 \\ 0.6 \end{pmatrix} = \frac{1}{2}\begin{pmatrix} 1.6 \\ 1.2 \end{pmatrix} = \begin{pmatrix} 0.8 \\ 0.6 \end{pmatrix},$$

$$u_2 = \frac{1}{1}\begin{pmatrix} 0.92 & 1.44 \\ 1.44 & 0.08 \end{pmatrix}\begin{pmatrix} 0.6 \\ -0.8 \end{pmatrix} = \begin{pmatrix} -0.6 \\ 0.8 \end{pmatrix}.$$

Como $A$ es $2\times 2$ de rango completo, $U$ ya queda completa. Entonces

$$\boxed{U = \begin{pmatrix} 0.8 & -0.6 \\ 0.6 & 0.8 \end{pmatrix}, \quad \Sigma = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}, \quad V = \begin{pmatrix} 0.8 & 0.6 \\ 0.6 & -0.8 \end{pmatrix}.}$$

**Verificación.** $V^TV = I$, $U^TU = I$ (columnas ortonormales) y

$$U\Sigma V^T = \begin{pmatrix} 0.8 & -0.6 \\ 0.6 & 0.8 \end{pmatrix}\begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 0.8 & 0.6 \\ 0.6 & -0.8 \end{pmatrix} = \begin{pmatrix} 0.92 & 1.44 \\ 1.44 & 0.08 \end{pmatrix} = A. \quad ✓$$

#### b) Factorización QR ($A = QR$ por Gram–Schmidt)

Tomamos las columnas $a_1 = (0.92,\ 1.44)$, $a_2 = (1.44,\ 0.08)$.

**Columna 1.** $u_1 = a_1$, con

$$\lVert u_1\rVert = \sqrt{0.92^2 + 1.44^2} = \sqrt{2.92} = \frac{\sqrt{73}}{5} \approx 1.7088 \quad (= r_{11}),$$

$$v_1 = \frac{u_1}{\lVert u_1\rVert} = \frac{1}{\sqrt{73}/5}(0.92,\ 1.44) = \frac{1}{5\sqrt{73}}(23,\ 36) \approx (0.5384,\ 0.8427).$$

**Columna 2.** Coeficiente de proyección:

$$r_{12} = \langle a_2, v_1\rangle = \frac{1}{5\sqrt{73}}\big(23\cdot 1.44 + 36\cdot 0.08\big) = \frac{36}{5\sqrt{73}} \approx 0.8427.$$

$$u_2 = a_2 - r_{12}\,v_1 = (1.44,\ 0.08) - 0.8427\,(0.5384,\ 0.8427) = (0.9863,\ -0.6301).$$

Para la norma conviene usar la identidad de un $2\times2$, $r_{22} = \lVert u_2\rVert = \dfrac{|\det A|}{r_{11}}$ con $\det A = 0.92\cdot 0.08 - 1.44^2 = -2$:

$$r_{22} = \frac{|{-2}|}{\sqrt{73}/5} = \frac{10}{\sqrt{73}} \approx 1.1704,$$

$$v_2 = \frac{u_2}{r_{22}} = \frac{1}{5\sqrt{73}}(36,\ -23) \approx (0.8427,\ -0.5384).$$

Resultado:

$$\boxed{Q = \frac{1}{5\sqrt{73}}\begin{pmatrix} 23 & 36 \\ 36 & -23 \end{pmatrix} \approx \begin{pmatrix} 0.5384 & 0.8427 \\ 0.8427 & -0.5384 \end{pmatrix}, \quad R = \begin{pmatrix} \tfrac{\sqrt{73}}{5} & \tfrac{36}{5\sqrt{73}} \\[2pt] 0 & \tfrac{10}{\sqrt{73}} \end{pmatrix} \approx \begin{pmatrix} 1.7088 & 0.8427 \\ 0 & 1.1704 \end{pmatrix}.}$$

**Verificación.** $Q^TQ = I$ ✓ y

$$QR \approx \begin{pmatrix} 0.5384 & 0.8427 \\ 0.8427 & -0.5384 \end{pmatrix}\begin{pmatrix} 1.7088 & 0.8427 \\ 0 & 1.1704 \end{pmatrix} = \begin{pmatrix} 0.92 & 1.44 \\ 1.44 & 0.08 \end{pmatrix} = A. \quad ✓$$

## Ejercicio 4

Dado el siguiente conjunto de datos

| x | y |
|---|---|
| $0$ | $+0.97$ |
| $\pi/4$ | $+1.42$ |
| $\pi$ | $-1.04$ |

Usando cuadrados mínimos, realice el ajuste de los datos experimentales a la ecuación $y(x) = a \cos(x) + b \sin(x)$ utilizando descomposición QR.

### Resolución

**Planteo.** El modelo $y(x) = a\cos x + b\sin x$ es **lineal en los parámetros** $a, b$. Imponer que pase por los tres puntos da el sistema (sobredeterminado) $A X = \mathbf b$, con $X = (a, b)^T$, matriz de diseño $A$ cuyas columnas son $\cos x_i$ y $\sin x_i$, y $\mathbf b$ los valores $y_i$:

$$A = \begin{pmatrix} \cos 0 & \sin 0 \\ \cos\tfrac{\pi}{4} & \sin\tfrac{\pi}{4} \\ \cos\pi & \sin\pi \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ \tfrac{\sqrt2}{2} & \tfrac{\sqrt2}{2} \\ -1 & 0 \end{pmatrix}, \qquad \mathbf b = \begin{pmatrix} 0.97 \\ 1.42 \\ -1.04 \end{pmatrix}.$$

Como hay 3 ecuaciones y 2 incógnitas, el sistema en general es incompatible; buscamos la solución de **cuadrados mínimos** (la que minimiza $\lVert AX - \mathbf b\rVert$). El método estable es: factorizar $A = QR$ y resolver el sistema triangular $R X = Q^T\mathbf b$.

**Paso 1 — QR de $A$ por Gram–Schmidt.** Columnas $a_1 = (1, \tfrac{\sqrt2}{2}, -1)$, $a_2 = (0, \tfrac{\sqrt2}{2}, 0)$.

$$u_1 = a_1, \quad \lVert u_1\rVert = \sqrt{1 + \tfrac12 + 1} = \sqrt{\tfrac52} = \frac{\sqrt{10}}{2} \approx 1.5811 \quad (= r_{11}),$$

$$v_1 = \frac{u_1}{\lVert u_1\rVert} = \sqrt{\tfrac25}\left(1,\ \tfrac{\sqrt2}{2},\ -1\right) = \left(\tfrac{\sqrt{10}}{5},\ \tfrac{\sqrt5}{5},\ -\tfrac{\sqrt{10}}{5}\right) \approx (0.6325,\ 0.4472,\ -0.6325).$$

$$r_{12} = \langle a_2, v_1\rangle = \tfrac{\sqrt2}{2}\cdot\tfrac{\sqrt5}{5} = \frac{\sqrt{10}}{10} \approx 0.3162,$$

$$u_2 = a_2 - r_{12}\,v_1 \approx (0,\ 0.7071,\ 0) - 0.3162\,(0.6325,\ 0.4472,\ -0.6325) = (-0.2,\ 0.5657,\ 0.2),$$

$$r_{22} = \lVert u_2\rVert = \frac{\sqrt{10}}{5} \approx 0.6325, \quad v_2 = \frac{u_2}{r_{22}} = \left(-\tfrac{\sqrt{10}}{10},\ \tfrac{2\sqrt5}{5},\ \tfrac{\sqrt{10}}{10}\right) \approx (-0.3162,\ 0.8944,\ 0.3162).$$

$$Q = \begin{pmatrix} 0.6325 & -0.3162 \\ 0.4472 & 0.8944 \\ -0.6325 & 0.3162 \end{pmatrix}, \qquad R = \begin{pmatrix} \tfrac{\sqrt{10}}{2} & \tfrac{\sqrt{10}}{10} \\[2pt] 0 & \tfrac{\sqrt{10}}{5} \end{pmatrix} \approx \begin{pmatrix} 1.5811 & 0.3162 \\ 0 & 0.6325 \end{pmatrix}.$$

(Verificación: $Q^TQ = I$ y $QR = A$ ✓.)

**Paso 2 — resolver $RX = Q^T\mathbf b$.** Con $\mathbf b = (0.97,\ 1.42,\ -1.04)$:

$$Q^T\mathbf b = \begin{pmatrix} v_1\cdot\mathbf b \\ v_2\cdot\mathbf b \end{pmatrix} \approx \begin{pmatrix} 1.9063 \\ 0.6345 \end{pmatrix}.$$

El sistema triangular $\begin{pmatrix} 1.5811 & 0.3162 \\ 0 & 0.6325\end{pmatrix}\begin{pmatrix} a \\ b\end{pmatrix} = \begin{pmatrix} 1.9063 \\ 0.6345\end{pmatrix}$ se resuelve por sustitución hacia atrás:

$$b = \frac{0.6345}{0.6325} \approx 1.0032, \qquad a = \frac{1.9063 - 0.3162\,b}{1.5811} = \frac{201}{200} = 1.005.$$

(Valores exactos: $a = \tfrac{201}{200} = 1.005$ y $b = \tfrac{71\sqrt2}{50} - \tfrac{201}{200} \approx 1.00318$.)

$$\boxed{a = 1.005, \qquad b \approx 1.0032 \quad\Longrightarrow\quad y(x) \approx 1.005\,\cos x + 1.0032\,\sin x.}$$

**Norma del residuo.** El vector de residuos es

$$AX - \mathbf b \approx (0.035,\ 0,\ 0.035), \qquad \lVert AX - \mathbf b\rVert = \frac{7\sqrt2}{200} \approx 0.0495.$$

Es pequeño, de modo que el ajuste es muy bueno (los datos provienen casi de $\cos x + \sin x$).

**Verificación numérica** (`numpy.linalg.lstsq`): devuelve exactamente $(a, b) = (1.005,\ 1.00318)$ con la misma norma de residuo $0.0495$ ✓.

## Ejercicio 5

Sea $H = \langle x^2 + 2x - 1,\ x^2 + x + a^2 - 4,\ x^2 - 2x + 3 \rangle \subset P_2$. Determinar todos los valores de $a$ si existen para que $\dim(H) = 2$ y $x^2 + a - 1 \in H$.

### Resolución

Trabajamos en **coordenadas respecto de la base canónica** $\{1, x, x^2\}$, anotando cada polinomio como $(\text{coef. de }1,\ \text{coef. de }x,\ \text{coef. de }x^2)$:

$$p_1 = x^2 + 2x - 1 \;\leftrightarrow\; (-1,\ 2,\ 1),$$
$$p_2 = x^2 + x + a^2 - 4 \;\leftrightarrow\; (a^2 - 4,\ 1,\ 1),$$
$$p_3 = x^2 - 2x + 3 \;\leftrightarrow\; (3,\ -2,\ 1).$$

#### Condición 1: $\dim(H) = 2$

$H$ está generado por tres vectores en un espacio de dimensión 3. Que $\dim H = 2$ significa que los tres generadores son **linealmente dependientes** (no generan todo $P_2$) pero no todos colineales. Armamos la matriz cuyas columnas son las coordenadas y pedimos determinante nulo:

$$M = \begin{pmatrix} -1 & a^2 - 4 & 3 \\ 2 & 1 & -2 \\ 1 & 1 & 1 \end{pmatrix}, \qquad \det M = 16 - 4a^2.$$

$$\det M = 0 \iff a^2 = 4 \iff a = 2 \;\text{ ó }\; a = -2.$$

Para cualquier otro $a$, $\det M \ne 0$ y los tres generadores son LI, con lo cual $\dim H = 3$. En **ambos** candidatos $a = \pm 2$ se tiene $\operatorname{rg}(M) = 2$ (las columnas no son proporcionales entre sí: p.ej. $p_1, p_3$ son LI), de modo que efectivamente $\dim H = 2$. Notar que como sólo aparece $a^2 - 4$, en los dos casos $p_2 = (0, 1, 1) = x^2 + x$ es **el mismo** polinomio.

Hasta acá, $\dim H = 2$ se cumple para $a \in \{-2,\ 2\}$.

#### Condición 2: $x^2 + a - 1 \in H$

El vector a testear es $q = x^2 + a - 1 \leftrightarrow (a - 1,\ 0,\ 1)$. Como base de $H$ podemos tomar $\{p_1, p_3\}$ (LI). $q \in H$ si y sólo si $q$ es combinación lineal de $p_1, p_3$, lo que equivale a $\operatorname{rg}[\,p_1\ p_3\ q\,] = \operatorname{rg}[\,p_1\ p_3\,] = 2$.

**Caso $a = 2$:** $q = x^2 + 1 \leftrightarrow (1,\ 0,\ 1)$. Resolvemos $q = c_1 p_1 + c_2 p_3$:

$$\begin{cases} -c_1 + 3c_2 = 1 \\ 2c_1 - 2c_2 = 0 \\ c_1 + c_2 = 1 \end{cases} \implies c_1 = c_2 = \tfrac12.$$

En efecto $\tfrac12(-1,2,1) + \tfrac12(3,-2,1) = (1,0,1)$ ✓. Luego $q \in H$. (Coherentemente, también $p_2 = \tfrac34 p_1 + \tfrac14 p_3$, confirmando $\dim H = 2$.)

**Caso $a = -2$:** $q = x^2 - 3 \leftrightarrow (-3,\ 0,\ 1)$. El sistema $q = c_1 p_1 + c_2 p_3$ queda

$$\begin{cases} -c_1 + 3c_2 = -3 \\ 2c_1 - 2c_2 = 0 \\ c_1 + c_2 = 1 \end{cases}.$$

De la segunda $c_1 = c_2$; de la tercera $c_1 = c_2 = \tfrac12$; pero entonces la primera daría $-\tfrac12 + \tfrac32 = 1 \ne -3$. **Incompatible** $\Rightarrow q \notin H$. (Numéricamente, $\operatorname{rg}[\,p_1\ p_3\ q\,] = 3 \ne 2$.)

#### Conclusión

$$\boxed{a = 2 \text{ es el único valor: } \dim(H) = 2 \;\text{ y }\; x^2 + a - 1 = x^2 + 1 \in H.}$$

(El valor $a = -2$ satisface $\dim H = 2$ pero falla la condición de pertenencia.)
