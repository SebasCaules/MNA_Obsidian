---
tags: [final, resolucion, transformaciones-lineales, clasificacion, diagonalizacion, sistemas-lineales, svd, plu]
fuente: raw/Practicas/Modelos_Examenes/MNA_Final_Tema_XIV.pdf
tipo: final
tema: 14
tiene_resolucion: true
---

# Final de Métodos Numéricos Avanzados — Tema XIV (Resolución)

## Ejercicio 1

Sea la Transformación Lineal $T : P_2 \to \mathbb{R}^3 : T(a + b x + c x^2) = (a + b,\ a + b + c,\ b - c)$.

a) Hallar la matriz asociada en las bases canónicas respectivas ($\{1, x, x^2\}$ en $P_2$ y $\{e_1, e_2, e_3\}$ en $\mathbb{R}^3$).

b) Clasificarla.

### Resolución

**a) Matriz en bases canónicas.** La columna $j$ de la matriz es la imagen del $j$-ésimo vector de la base de $P_2$, escrita en coordenadas de la base canónica de $\mathbb{R}^3$. Evaluamos $T$ en $1$, $x$, $x^2$ (es decir, en los polinomios $a=1$; $b=1$; $c=1$, todo lo demás nulo):

$$T(1) = T(1 + 0x + 0x^2) = (1 + 0,\ 1 + 0 + 0,\ 0 - 0) = (1,\ 1,\ 0),$$
$$T(x) = T(0 + 1x + 0x^2) = (0 + 1,\ 0 + 1 + 0,\ 1 - 0) = (1,\ 1,\ 1),$$
$$T(x^2) = T(0 + 0x + 1x^2) = (0 + 0,\ 0 + 0 + 1,\ 0 - 1) = (0,\ 1,\ -1).$$

Apilando estas imágenes como columnas:

$$\boxed{M = M_{EE}(T) = \big[\,[T(1)]_E \mid [T(x)]_E \mid [T(x^2)]_E\,\big] = \begin{pmatrix} 1 & 1 & 0 \\ 1 & 1 & 1 \\ 0 & 1 & -1 \end{pmatrix}.}$$

**b) Clasificación.** $T : P_2 \to \mathbb{R}^3$ va de un espacio de dimensión $3$ a otro de dimensión $3$, y su matriz $M$ es **cuadrada** $3\times3$. Calculamos su determinante desarrollando por la primera columna:

$$\det M = 1\cdot\det\begin{pmatrix}1 & 1\\ 1 & -1\end{pmatrix} - 1\cdot\det\begin{pmatrix}1 & 0\\ 1 & -1\end{pmatrix} + 0 = 1\cdot(-1-1) - 1\cdot(-1-0) = -2 + 1 = -1.$$

Como $\det M = -1 \ne 0$, la matriz es **inversible**, por lo que $M$ tiene rango $3$. De aquí se deduce todo:

- **Inyectiva:** $N(T) = N(M) = \{0\}$ (el único $X$ con $MX=0$ es el nulo, porque $M$ es inversible), o equivalentemente $\dim N(T) = 3 - \operatorname{rg}(M) = 0$. ✔
- **Sobreyectiva:** $\dim \operatorname{Im}(T) = \operatorname{rg}(M) = 3 = \dim \mathbb{R}^3$, así que $\operatorname{Im}(T) = \mathbb{R}^3$. ✔ (Coherente con el teorema de la dimensión: $\dim N(T) + \dim \operatorname{Im}(T) = 0 + 3 = 3 = \dim P_2$.)
- **Biyectiva:** al ser inyectiva y sobreyectiva, $T$ es **biyectiva**.

$$\boxed{T \text{ es un isomorfismo (inyectiva, sobreyectiva y biyectiva), pues } \det M = -1 \ne 0.}$$

**Verificación.** numpy/sympy dan $\det M = -1$, $\operatorname{rg}(M) = 3$, núcleo trivial (nullspace vacío) y RREF $= I_3$ ✔.

## Ejercicio 2

Dada la matriz

$$A = \begin{pmatrix} 2 & k - 2 & 0 \\ 0 & 3 & k - 1 \\ 0 & 0 & 3 \end{pmatrix},\qquad k \in \mathbb{R}.$$

a) Hallar $k$, si existe, para que $A$ sea diagonalizable en $\mathbb{R}$.

b) Para $k = 2$, resolver el sistema $A^T A\, X = 0$.

### Resolución

**a) Diagonalizabilidad.** Por ser $A$ **triangular superior**, sus autovalores son los elementos de la diagonal:

$$\lambda = 2 \ (\text{simple}),\qquad \lambda = 3 \ (\text{doble}),$$

con multiplicidades **algebraicas** $m_a(2) = 1$ y $m_a(3) = 2$. (Esto no depende de $k$.) Una matriz es diagonalizable en $\mathbb{R}$ $\iff$ para todo autovalor $m_g = m_a$. El autovalor simple $\lambda=2$ cumple siempre $m_g(2) = 1 = m_a(2)$. El problema está en $\lambda = 3$: hace falta

$$m_g(3) = \dim N(A - 3I) = 2 \iff \operatorname{rg}(A - 3I) = 3 - 2 = 1.$$

Calculamos:

$$A - 3I = \begin{pmatrix} -1 & k - 2 & 0 \\ 0 & 0 & k - 1 \\ 0 & 0 & 0 \end{pmatrix}.$$

La primera fila $(-1,\ k-2,\ 0)$ nunca es nula (su primera entrada es $-1$), así que aporta siempre **un** pivote. El rango será exactamente $1$ solo si la segunda fila se anula, es decir si su único elemento no trivial es cero:

$$k - 1 = 0 \iff k = 1.$$

Si $k \ne 1$, la segunda fila $(0,0,k-1)$ es no nula e independiente de la primera, dando $\operatorname{rg}(A-3I) = 2$, luego $m_g(3) = 1 < 2 = m_a(3)$ y $A$ **no** es diagonalizable. (Notar que el término $k-2$ de la posición $(1,2)$ es irrelevante para el rango: la primera fila ya tiene su pivote en la columna $1$.)

$$\boxed{A \text{ es diagonalizable en } \mathbb{R} \iff k = 1.}$$

Para $k = 1$: $A - 3I = \begin{pmatrix} -1 & -1 & 0\\ 0 & 0 & 0\\ 0 & 0 & 0\end{pmatrix}$ tiene rango $1$, luego $m_g(3) = 2$, y junto con $m_g(2) = 1$ se obtienen $3$ autovectores LI. ✔

**Verificación.** sympy: `is_diagonalizable()` devuelve `True` únicamente para $k = 1$ (y `False` para $k = 0, 2, 3, -5, \dots$). Para $k=1$ los autoespacios son $S_2 = \langle(1,0,0)\rangle$ y $S_3 = \langle(-1,1,0),\,(0,0,1)\rangle$ ✔.

**b) Sistema $A^T A\, X = 0$ con $k = 2$.** Sustituyendo $k = 2$:

$$A = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 3 & 1 \\ 0 & 0 & 3 \end{pmatrix},\qquad \det A = 2\cdot 3 \cdot 3 = 18 \ne 0$$

(determinante de una triangular = producto de la diagonal). Como $\det A = 18 \ne 0$, $A$ es **inversible**, y por lo tanto

$$\det(A^T A) = \det(A^T)\det(A) = (\det A)^2 = 18^2 = 324 \ne 0,$$

así que $A^T A$ **también es inversible**. La única solución de un sistema homogéneo con matriz inversible es la trivial:

$$\boxed{X = (0,\ 0,\ 0)^T \quad (\text{solución única}).}$$

Otra manera de verlo, más conceptual: $A^T A$ es siempre **simétrica y semidefinida positiva**, y es **definida positiva** exactamente cuando $A$ tiene núcleo trivial (columnas LI). Aquí, explícitamente,

$$A^T A = \begin{pmatrix} 4 & 0 & 0 \\ 0 & 9 & 3 \\ 0 & 3 & 10 \end{pmatrix},$$

cuyos menores principales líderes son $4 > 0$, $\det\begin{pmatrix}4&0\\0&9\end{pmatrix}=36 > 0$ y $\det(A^TA) = 324 > 0$: por el criterio de Sylvester $A^TA$ es **definida positiva**, en particular inversible, y de nuevo $X = 0$. (Además, para cualquier $X$ vale $X^T A^T A X = \lVert AX\rVert^2 = 0 \iff AX = 0 \iff X = 0$, por ser $A$ inyectiva.)

**Verificación.** sympy: $\det A = 18$, $A^TA = \begin{pmatrix}4&0&0\\0&9&3\\0&3&10\end{pmatrix}$, $\det(A^TA)=324$, nullspace vacío, simétrica y con menores líderes $4,36,324>0$ ✔.

## Ejercicio 3

Dada la matriz $A = \begin{pmatrix} 0 & -1 \\ -1 & -1 \\ 1 & 1 \end{pmatrix}$ (de $3\times2$):

a) Hallar su factorización $SVD$ **completa** (no se tendrá en cuenta la reducida).

b) Hallar la factorización $PLU$ de la matriz $A A^T$ ($3\times3$).

### Resolución

**a) SVD completa $A = U\Sigma V^T$.** Para $A$ de $3\times2$, la SVD completa tiene $U$ de $3\times3$, $\Sigma$ de $3\times2$ y $V$ de $2\times2$, ambas $U,V$ ortogonales.

**Paso 1 — autovalores de $A^T A$ (matriz $2\times2$).**

$$A^T A = \begin{pmatrix} 0 & -1 & 1 \\ -1 & -1 & 1 \end{pmatrix}\begin{pmatrix} 0 & -1 \\ -1 & -1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 2 \\ 2 & 3 \end{pmatrix}.$$

Polinomio característico (usando $\operatorname{tr} = 5$, $\det = 2$):

$$p(\lambda) = \lambda^2 - 5\lambda + 2 = 0 \;\Rightarrow\; \lambda = \frac{5 \pm \sqrt{25 - 8}}{2} = \frac{5 \pm \sqrt{17}}{2}.$$

Ordenados de mayor a menor:

$$\lambda_1 = \frac{5 + \sqrt{17}}{2} \approx 4.5616,\qquad \lambda_2 = \frac{5 - \sqrt{17}}{2} \approx 0.4384.$$

**Paso 2 — valores singulares** ($\sigma_i = \sqrt{\lambda_i}$, decrecientes):

$$\sigma_1 = \sqrt{\tfrac{5+\sqrt{17}}{2}} \approx 2.1358,\qquad \sigma_2 = \sqrt{\tfrac{5-\sqrt{17}}{2}} \approx 0.6622.$$

(Chequeo: $\sigma_1 \sigma_2 = \sqrt{\lambda_1\lambda_2} = \sqrt{\det(A^TA)} = \sqrt{2}$ ✔.) Ambos son no nulos, así que $A$ tiene rango $2$ (columnas LI).

**Paso 3 — autovectores de $A^T A$ → columnas de $V$.** Para cada $\lambda_i$ resolvemos $(A^TA - \lambda_i I)v = 0$. La primera fila da $(2 - \lambda)v_x + 2 v_y = 0$, de donde un autovector sin normalizar es $v = (2,\ \lambda - 2)$:

- $\lambda_1$: $\tilde v_1 = \big(2,\ \tfrac{1+\sqrt{17}}{2}\big)$, con $\lVert\tilde v_1\rVert = \tfrac12\sqrt{34 + 2\sqrt{17}} \approx 3.2499$. Normalizando:
$$v_1 = \frac{\tilde v_1}{\lVert\tilde v_1\rVert} \approx (0.6154,\ 0.7882).$$
- $\lambda_2$: $\tilde v_2 = \big(2,\ \tfrac{1-\sqrt{17}}{2}\big)$, con $\lVert\tilde v_2\rVert = \tfrac12\sqrt{34 - 2\sqrt{17}} \approx 2.5374$. Normalizando:
$$v_2 = \frac{\tilde v_2}{\lVert\tilde v_2\rVert} \approx (0.7882,\ -0.6154).$$

(Como $A^TA$ es simétrica con autovalores distintos, $v_1 \perp v_2$ automáticamente: $v_1\cdot v_2 = 0$ ✔.) Entonces

$$V = (v_1 \mid v_2) \approx \begin{pmatrix} 0.6154 & 0.7882 \\ 0.7882 & -0.6154 \end{pmatrix}.$$

**Paso 4 — columnas de $U$ asociadas a $\sigma_i > 0$:** $u_i = \dfrac{1}{\sigma_i}A v_i$.

$$u_1 = \frac{1}{\sigma_1}A v_1 \approx \frac{1}{2.1358}\begin{pmatrix} -0.7882 \\ -1.4036 \\ 1.4036 \end{pmatrix} \approx \begin{pmatrix} -0.3690 \\ -0.6572 \\ 0.6572 \end{pmatrix},$$

$$u_2 = \frac{1}{\sigma_2}A v_2 \approx \frac{1}{0.6622}\begin{pmatrix} 0.6154 \\ -0.1728 \\ 0.1728 \end{pmatrix} \approx \begin{pmatrix} 0.9294 \\ -0.2610 \\ 0.2610 \end{pmatrix}.$$

Ambos quedan unitarios y ortogonales ($u_1\cdot u_2 = 0$).

**Paso 5 — completar $U$ con $N(A^T)$.** Como $A$ es $3\times2$ de rango $2$, falta una tercera columna $u_3$, base ortonormal de $N(A^T) = \operatorname{Im}(A)^\perp$. Resolviendo $A^T u = 0$:

$$A^T = \begin{pmatrix} 0 & -1 & 1 \\ -1 & -1 & 1 \end{pmatrix},\quad A^T u = 0 \;\Rightarrow\; \begin{cases} -u_2 + u_3 = 0 \\ -u_1 - u_2 + u_3 = 0 \end{cases} \Rightarrow u_2 = u_3,\ u_1 = 0.$$

Un generador es $(0,1,1)$; normalizado:

$$u_3 = \tfrac{1}{\sqrt2}(0,\ 1,\ 1) \approx (0,\ 0.7071,\ 0.7071).$$

**Resultado (SVD completa):**

$$\boxed{
U \approx \begin{pmatrix} -0.3690 & 0.9294 & 0 \\ -0.6572 & -0.2610 & 0.7071 \\ 0.6572 & 0.2610 & 0.7071 \end{pmatrix},\quad
\Sigma = \begin{pmatrix} \sigma_1 & 0 \\ 0 & \sigma_2 \\ 0 & 0 \end{pmatrix} \approx \begin{pmatrix} 2.1358 & 0 \\ 0 & 0.6622 \\ 0 & 0 \end{pmatrix},\quad
V \approx \begin{pmatrix} 0.6154 & 0.7882 \\ 0.7882 & -0.6154 \end{pmatrix}.}
$$

con $\sigma_1 = \sqrt{\tfrac{5+\sqrt{17}}{2}}$, $\sigma_2 = \sqrt{\tfrac{5-\sqrt{17}}{2}}$. La tercera fila de $\Sigma$ (toda nula) es lo que hace falta para que $U\Sigma V^T$ tenga las dimensiones $3\times2$ de $A$.

> **Nota sobre signos.** La SVD no es única: se puede cambiar el signo de un par $(v_i, u_i)$ simultáneamente. Por eso una herramienta de cómputo puede mostrar columnas con el signo opuesto; lo único que importa es que $A v_i = \sigma_i u_i$ con $v_i, u_i$ unitarios.

**Verificación.** Con sympy, usando las formas exactas $v_i$, $u_i = Av_i/\sigma_i$ y $u_3 = (0,1,1)/\sqrt2$, se obtiene $U\Sigma V^T = A$ **exactamente** (simplificación simbólica a $0$), $U^TU = I_3$ y $V^TV = I_2$ ✔. numpy `np.linalg.svd(A, full_matrices=True)` reproduce los mismos $\sigma$ y los mismos subespacios (con un signo global opuesto en $U,V$) ✔.

**b) Factorización $PLU$ de $A A^T$.** Primero la matriz:

$$A A^T = \begin{pmatrix} 0 & -1 \\ -1 & -1 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} 0 & -1 & 1 \\ -1 & -1 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 1 & -1 \\ 1 & 2 & -2 \\ -1 & -2 & 2 \end{pmatrix}.$$

Es $3\times3$, simétrica, de **rango $2$** (es $A$ por $A^T$, ambas de rango $2$), por lo tanto **singular** ($\det = 0$). Aplicamos eliminación gaussiana (Doolittle): el pivote $(1,1) = 1 \ne 0$, así que **no hace falta permutar** ($P = I$).

**Columna 1.** Multiplicadores $m_{21} = \tfrac{1}{1} = 1$, $m_{31} = \tfrac{-1}{1} = -1$.
$$F_2 \leftarrow F_2 - 1\cdot F_1,\qquad F_3 \leftarrow F_3 - (-1)\cdot F_1 = F_3 + F_1:$$
$$\begin{pmatrix} 1 & 1 & -1 \\ 0 & 1 & -1 \\ 0 & -1 & 1 \end{pmatrix}.$$

**Columna 2.** Pivote $(2,2) = 1 \ne 0$. Multiplicador $m_{32} = \tfrac{-1}{1} = -1$.
$$F_3 \leftarrow F_3 - (-1)\cdot F_2 = F_3 + F_2 \;\Rightarrow\; \begin{pmatrix} 1 & 1 & -1 \\ 0 & 1 & -1 \\ 0 & 0 & 0 \end{pmatrix} = U.$$

El cero final $U_{33} = 0$ refleja la singularidad de $AA^T$ (rango $2$), pero **no obligó a pivotear**, porque apareció recién al terminar la eliminación. Reuniendo los multiplicadores en $L$ (unos en la diagonal):

$$\boxed{P = I_3 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix},\quad L = \begin{pmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ -1 & -1 & 1 \end{pmatrix},\quad U = \begin{pmatrix} 1 & 1 & -1 \\ 0 & 1 & -1 \\ 0 & 0 & 0 \end{pmatrix}.}$$

Como $P = I$, se trata de una factorización $LU$ directa: $A A^T = LU$.

**Verificación.** sympy/numpy: $L U = A A^T$ exactamente; `scipy.linalg.lu(AA^T)` (pivoteo parcial) devuelve la **misma** $P = I$, $L$ y $U$ ✔, confirmando que no era necesario permutar.
