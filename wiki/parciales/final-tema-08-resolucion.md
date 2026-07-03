---
tags: [final, transformaciones-lineales, nucleo, fourier, svd]
fuente: raw/Practicas/Modelos_Examenes/MNA_Final_Tema_VIII.pdf
tipo: final
tema: 8
tiene_resolucion: true
---

# Examen Final de Métodos Numéricos Avanzados — Tema VIII (Resolución)

Enunciado sin resolver en [[final-tema-08]].

## Ejercicio 1

Dada la TL $T : \mathbb{R}^3 \to \mathbb{R}^3 : T(x, y, z) = \big(2x + 8y + k z,\ -x - 4y,\ (k + 3) x + 12 y + 2 k z\big)$

a) Hallar todos los valores de $k \in \mathbb{R}$ tales que $\dim(R(T)) = 1$.
b) Para $k = 0$, hallar una base y la dimensión de $N(T)$.

### Resolución

La matriz de $T$ en base canónica (columnas $= T(e_j)$, o equivalentemente filas $=$ las tres componentes) es

$$M_{EE}(T) = A = \begin{pmatrix} 2 & 8 & k \\ -1 & -4 & 0 \\ k+3 & 12 & 2k \end{pmatrix}.$$

Recordemos que $\dim R(T) = \operatorname{rg}(A)$ y, por el teorema de la dimensión, $\dim N(T) + \dim R(T) = 3$.

#### a) $\dim(R(T)) = 1 \iff \operatorname{rg}(A) = 1$

**Primero, ¿cuándo baja el rango de 3?** Calculamos el determinante:

$$\det A = 2\big[(-4)(2k) - 0\cdot 12\big] - 8\big[(-1)(2k) - 0\cdot(k+3)\big] + k\big[(-1)\cdot 12 - (-4)(k+3)\big]$$
$$= 2(-8k) - 8(-2k) + k(4k) = -16k + 16k + 4k^2 = 4k^2.$$

Luego $\det A = 4k^2 = 0 \iff k = 0$. Para todo $k \ne 0$ se tiene $\det A \ne 0$, es decir $\operatorname{rg}(A) = 3$ (TL inversible, $\dim R(T) = 3$). Por lo tanto el rango sólo puede bajar en $k = 0$.

**Rango exactamente 1.** Que $\operatorname{rg}(A) = 1$ exige que **todos** los menores $2\times 2$ se anulen (no sólo el determinante $3\times 3$). Los menores $2\times 2$ de $A$ son, salvo signo, múltiplos de $k$ (por ejemplo $\det\begin{pmatrix}2&8\\-1&-4\end{pmatrix} = 0$ siempre, pero $\det\begin{pmatrix}8&k\\-4&0\end{pmatrix} = 4k$, $\det\begin{pmatrix}2&k\\-1&0\end{pmatrix} = k$, etc.). Todos se anulan simultáneamente **sólo si $k = 0$**.

En $k = 0$:

$$A = \begin{pmatrix} 2 & 8 & 0 \\ -1 & -4 & 0 \\ 3 & 12 & 0 \end{pmatrix}.$$

Las tres filas son proporcionales a $(1, 4, 0)$ (la fila 1 es $2(1,4,0)$, la fila 2 es $-(1,4,0)$, la fila 3 es $3(1,4,0)$), de modo que $\operatorname{rg}(A) = 1$. (Equivalentemente, las columnas son proporcionales: $\text{col}_2 = 4\,\text{col}_1$ y $\text{col}_3 = 0$.)

$$\boxed{\dim R(T) = 1 \iff k = 0.}$$

> Observación: para ningún $k$ ocurre $\operatorname{rg}(A) = 2$; el rango es $3$ si $k \ne 0$ y $1$ si $k = 0$. No hay valor intermedio.

#### b) Base y dimensión de $N(T)$ para $k = 0$

Resolvemos $AX = 0$ con $A = \begin{pmatrix} 2 & 8 & 0 \\ -1 & -4 & 0 \\ 3 & 12 & 0 \end{pmatrix}$. Como $\operatorname{rg}(A) = 1$, las tres ecuaciones se reducen a una sola. Tomando la fila más simple $(1,4,0)$:

$$x + 4y = 0 \implies x = -4y,$$

mientras que $z$ no aparece, luego $z$ es **libre**. La solución general es

$$X = (x, y, z) = (-4y,\ y,\ z) = y\,(-4, 1, 0) + z\,(0, 0, 1).$$

$$\boxed{N(T) = \operatorname{gen}\{(-4, 1, 0),\ (0, 0, 1)\}, \qquad \dim N(T) = 2.}$$

**Verificación (teorema de la dimensión).** $\dim N(T) + \dim R(T) = 2 + 1 = 3 = \dim \mathbb{R}^3$ ✓. Además $T(-4,1,0) = (2(-4)+8,\, -(-4)-4,\, 12) \cdot[\text{con }k=0] = (0,0,0)$ ✓ y $T(0,0,1) = (0\cdot 1,\, 0,\, 0) = (0,0,0)$ ✓.

## Ejercicio 2

a) Hallar el desarrollo en serie de Fourier de $f : [0, 1] \to \mathbb{R} : f(x) = 1 - x^2$, extendida de modo que $f(x) = f(x + 1)$ para todo $x \in \mathbb{R}$ (período $T = 1$).
b) Indicar a qué converge la serie en $x = 0$ y $x = \dfrac{1}{2}$.

### Resolución

#### a) Coeficientes de Fourier

Usamos la convención de la cátedra con período $T = 1$ (frecuencia $\tfrac{2\pi n}{T} = 2\pi n$):

$$f(x) = a_0 + \sum_{n=1}^{\infty} a_n \cos(2\pi n x) + \sum_{n=1}^{\infty} b_n \sin(2\pi n x),$$

$$a_0 = \int_0^1 f(x)\,dx,\qquad a_n = 2\int_0^1 f(x)\cos(2\pi n x)\,dx,\qquad b_n = 2\int_0^1 f(x)\sin(2\pi n x)\,dx.$$

(Recordar: $a_0$ es el **valor medio**, sin dividir por 2. Como integramos sobre $[0,1]$ y no sobre un intervalo simétrico, la función **no** tiene paridad definida, así que en general aparecen tanto $a_n$ como $b_n$.)

**Término constante $a_0$:**

$$a_0 = \int_0^1 (1 - x^2)\,dx = \left[x - \frac{x^3}{3}\right]_0^1 = 1 - \frac{1}{3} = \boxed{\frac{2}{3}}.$$

**Coeficientes $a_n$.** Necesitamos $\displaystyle\int_0^1 (1-x^2)\cos(2\pi n x)\,dx$. El término $\int_0^1 \cos(2\pi n x)\,dx = 0$, así que sólo sobrevive la parte con $x^2$. Integrando por partes dos veces (con $\int_0^1 x^2\cos(2\pi n x)\,dx = \tfrac{1}{2\pi^2 n^2}$, ya que los términos de borde con $\sin(2\pi n)$ se anulan y queda el del $\cos(2\pi n) = 1$):

$$a_n = 2\int_0^1 (1 - x^2)\cos(2\pi n x)\,dx = -2\cdot\frac{1}{2\pi^2 n^2} = \boxed{-\frac{1}{\pi^2 n^2}}.$$

**Coeficientes $b_n$.** Para $\displaystyle\int_0^1 (1-x^2)\sin(2\pi n x)\,dx$: el término constante da $\int_0^1 \sin(2\pi n x)\,dx = 0$, y por partes $\int_0^1 x^2 \sin(2\pi n x)\,dx = -\tfrac{1}{2\pi n}$. Luego

$$b_n = 2\int_0^1 (1 - x^2)\sin(2\pi n x)\,dx = -2\cdot\left(-\frac{1}{2\pi n}\right) = \boxed{\frac{1}{\pi n}}.$$

(Verificado por integración simbólica: $a_0 = \tfrac23$, $a_n = -\tfrac{1}{\pi^2 n^2}$, $b_n = \tfrac{1}{\pi n}$ exactos.)

**Serie de Fourier:**

$$\boxed{\,f(x) \sim \frac{2}{3} - \frac{1}{\pi^2}\sum_{n=1}^{\infty} \frac{\cos(2\pi n x)}{n^2} + \frac{1}{\pi}\sum_{n=1}^{\infty} \frac{\sin(2\pi n x)}{n}.\,}$$

#### b) Convergencia en $x = 0$ y $x = 1/2$

Por el teorema de Dirichlet, la serie converge en cada punto al valor de $f$ si es continuo, y al **promedio de los límites laterales** $\tfrac12\big(f(x^+) + f(x^-)\big)$ en un salto. Hay que mirar la **extensión periódica** de $f(x) = 1 - x^2$ tomada en $[0,1)$.

**En $x = 0$ (y en todo entero).** Es un punto de **discontinuidad de salto**: viniendo por la derecha, $f(0^+) = 1 - 0^2 = 1$; viniendo por la izquierda usamos el final del período anterior, $f(0^-) = f(1^-) = 1 - 1^2 = 0$. La serie converge al promedio:

$$\boxed{S(0) = \frac{f(0^+) + f(0^-)}{2} = \frac{1 + 0}{2} = \frac{1}{2}.}$$

**En $x = 1/2$.** Es un punto **interior de continuidad** ($f$ es polinómica y continua en $(0,1)$), así que la serie converge al propio valor de la función:

$$\boxed{S\!\left(\tfrac12\right) = f\!\left(\tfrac12\right) = 1 - \left(\tfrac12\right)^2 = \frac{3}{4}.}$$

**Verificación numérica** (sumas parciales hasta $N = 5000$): $S(0) \to 0.50002$ y $S(1/2) \to 0.75000$, confirmando $\tfrac12$ y $\tfrac34$ respectivamente. (En $x=0$ la convergencia es lenta, $\sim 1/N$, propia de un salto.)

## Ejercicio 3

Hallar una factorización SVD para $A = \begin{pmatrix} 1 & -3 & 2 \\ 5 & 2 & 0 \end{pmatrix}$.

### Resolución

Buscamos $A = U\Sigma V^T$ con $U$ ($2\times 2$) y $V$ ($3\times 3$) ortogonales y $\Sigma$ ($2\times 3$) "diagonal" con los valores singulares.

**Estrategia.** Como $A$ es $2\times 3$, conviene trabajar con $AA^T$ (matriz $2\times 2$) en lugar de $A^TA$ (que sería $3\times 3$): sus autovalores no nulos son los mismos. Obtenemos $U$ de $AA^T$, luego $v_i = \dfrac{A^T u_i}{\sigma_i}$, y completamos $V$ con una base de $N(A)$.

#### Paso 1 — autovalores de $AA^T$

$$AA^T = \begin{pmatrix} 1 & -3 & 2 \\ 5 & 2 & 0 \end{pmatrix}\begin{pmatrix} 1 & 5 \\ -3 & 2 \\ 2 & 0 \end{pmatrix} = \begin{pmatrix} 1+9+4 & 5-6+0 \\ 5-6+0 & 25+4+0 \end{pmatrix} = \begin{pmatrix} 14 & -1 \\ -1 & 29 \end{pmatrix}.$$

Polinomio característico:

$$p_{AA^T}(\lambda) = \det(\lambda I - AA^T) = (\lambda - 14)(\lambda - 29) - (-1)^2 = \lambda^2 - 43\lambda + 405.$$

Las raíces (no son "lindas") son

$$\lambda_{1,2} = \frac{43 \pm \sqrt{43^2 - 4\cdot 405}}{2} = \frac{43 \pm \sqrt{1849 - 1620}}{2} = \frac{43 \pm \sqrt{229}}{2}.$$

Numéricamente $\lambda_1 = \tfrac{43 + \sqrt{229}}{2} \approx 29.0664$ y $\lambda_2 = \tfrac{43 - \sqrt{229}}{2} \approx 13.9336$. Los **valores singulares** (raíces, en orden decreciente) son

$$\boxed{\sigma_1 = \sqrt{\frac{43 + \sqrt{229}}{2}} \approx 5.3913, \qquad \sigma_2 = \sqrt{\frac{43 - \sqrt{229}}{2}} \approx 3.7328.}$$

> Chequeo rápido: $\lambda_1\lambda_2 = 405$ ($=\det(AA^T)$) y $\lambda_1 + \lambda_2 = 43$ ($=\operatorname{tr}(AA^T)$) ✓. Además $\sigma_1\sigma_2 = \sqrt{405} = 9\sqrt5 \approx 20.12$.

#### Paso 2 — autovectores de $AA^T$ → columnas de $U$

Para cada $\lambda_i$ resolvemos $(AA^T - \lambda_i I)u = 0$. La primera fila de $AA^T - \lambda I$ es $(14-\lambda,\ -1)$, de donde $(14-\lambda)x - y = 0 \Rightarrow y = (14-\lambda)x$. Tomando $x = 2$ obtenemos las direcciones

$$\tilde u_1 = \big(2,\ 2(14-\lambda_1)\big) = (2,\ -15 - \sqrt{229}), \qquad \tilde u_2 = (2,\ -15 + \sqrt{229}),$$

ya que $14 - \lambda_1 = \tfrac{28 - 43 - \sqrt{229}}{2} = \tfrac{-15 - \sqrt{229}}{2}$ (análogo para $\lambda_2$ con $+\sqrt{229}$). Normalizando ($\lVert\tilde u_1\rVert^2 = 458 + 30\sqrt{229}$, $\lVert\tilde u_2\rVert^2 = 458 - 30\sqrt{229}$):

$$u_1 = \frac{\tilde u_1}{\lVert\tilde u_1\rVert} \approx \begin{pmatrix} 0.0662 \\ -0.9978 \end{pmatrix}, \qquad u_2 = \frac{\tilde u_2}{\lVert\tilde u_2\rVert} \approx \begin{pmatrix} 0.9978 \\ 0.0662 \end{pmatrix}.$$

$$U = \big(u_1 \mid u_2\big) \approx \begin{pmatrix} 0.0662 & 0.9978 \\ -0.9978 & 0.0662 \end{pmatrix}.$$

(Se verifica $u_1 \perp u_2$ y $\lVert u_i\rVert = 1$.)

#### Paso 3 — columnas de $V$ mediante $v_i = \dfrac{A^T u_i}{\sigma_i}$

$$v_1 = \frac{1}{\sigma_1}A^T u_1 = \frac{1}{5.3913}\begin{pmatrix} 1 & 5 \\ -3 & 2 \\ 2 & 0 \end{pmatrix}\begin{pmatrix} 0.0662 \\ -0.9978 \end{pmatrix} \approx \begin{pmatrix} -0.9131 \\ -0.4070 \\ 0.0246 \end{pmatrix},$$

$$v_2 = \frac{1}{\sigma_2}A^T u_2 = \frac{1}{3.7328}\begin{pmatrix} 1 & 5 \\ -3 & 2 \\ 2 & 0 \end{pmatrix}\begin{pmatrix} 0.9978 \\ 0.0662 \end{pmatrix} \approx \begin{pmatrix} 0.3560 \\ -0.7664 \\ 0.5346 \end{pmatrix}.$$

Como $A$ tiene rango $2$ y $V$ debe ser $3\times 3$, falta una tercera columna $v_3$: una base ortonormal de $N(A)$ (el espacio de los valores singulares nulos). Resolvemos $AX = 0$:

$$\begin{cases} x - 3y + 2z = 0 \\ 5x + 2y = 0 \end{cases} \implies x = -\tfrac{2}{5}y, \quad z = \tfrac{3y - x}{2} = \tfrac{17}{10}y.$$

Tomando $y = 10$: $\tilde v_3 = (-4,\ 10,\ 17)$, con $\lVert\tilde v_3\rVert = \sqrt{16 + 100 + 289} = \sqrt{405} = 9\sqrt5$. Normalizando:

$$v_3 = \frac{1}{9\sqrt5}(-4,\ 10,\ 17) \approx \begin{pmatrix} -0.1988 \\ 0.4969 \\ 0.8447 \end{pmatrix}.$$

Finalmente:

$$\boxed{U \approx \begin{pmatrix} 0.0662 & 0.9978 \\ -0.9978 & 0.0662 \end{pmatrix}, \quad \Sigma = \begin{pmatrix} \sigma_1 & 0 & 0 \\ 0 & \sigma_2 & 0 \end{pmatrix} \approx \begin{pmatrix} 5.3913 & 0 & 0 \\ 0 & 3.7328 & 0 \end{pmatrix},}$$

$$\boxed{V \approx \begin{pmatrix} -0.9131 & 0.3560 & -0.1988 \\ -0.4070 & -0.7664 & 0.4969 \\ 0.0246 & 0.5346 & 0.8447 \end{pmatrix}.}$$

**Verificación.** Se comprueba $U^TU = I_2$, $V^TV = I_3$ (columnas ortonormales) y

$$U\Sigma V^T \approx \begin{pmatrix} 1 & -3 & 2 \\ 5 & 2 & 0 \end{pmatrix} = A. \quad ✓$$

(La reconstrucción $U\Sigma V^T = A$ es exacta usando los valores exactos $\sigma_i = \sqrt{(43\pm\sqrt{229})/2}$ y las columnas exactas; los decimales mostrados llevan a $A$ con error $< 10^{-4}$.)
