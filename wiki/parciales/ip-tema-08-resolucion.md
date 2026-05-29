---
tags: [parcial, ip, resolucion, autovectores, diagonalizacion, qr, plu, fourier, serie-trigonometrica]
fuente: raw/Practicas/Modelos_Examenes/MNA_IP_Tema_VIII.pdf
tipo: ip
tema: 8
tiene_resolucion: true
---

# Primer Parcial de Métodos Numéricos Avanzados — Tema VIII (Resolución)

Enunciado original sin resolución en [[ip-tema-08]]. Recetas en [[../../study/MNA_Cheatsheet|cheatsheet]]; teoría de series en [[../guias/guia-08-fourier-series]].

## Ejercicio 1

Sea $A = \begin{pmatrix} k & 0 & 0 \\ 2 & -2 & -1 \\ -2 & 5 & 4 \end{pmatrix}$

a) Hallar $k \in \mathbb{R}$ para que $(0, -1, 1)$ sea autovector de $A$.
b) Para los valores hallados en a) decida si $A$ es diagonalizable en $\mathbb{R}$.

### Resolución

**a)** Pedir que $v = (0, -1, 1)$ sea autovector es imponer $Av = \lambda v$ para algún $\lambda \in \mathbb{R}$. Calculamos $Av$:

$$A\begin{pmatrix} 0 \\ -1 \\ 1 \end{pmatrix} = \begin{pmatrix} k\cdot 0 + 0\cdot(-1) + 0\cdot 1 \\ 2\cdot 0 + (-2)(-1) + (-1)\cdot 1 \\ -2\cdot 0 + 5(-1) + 4\cdot 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix}.$$

Comparamos componente a componente con $\lambda v = (0, -\lambda, \lambda)$:

- **Fila 1:** $0 = \lambda\cdot 0 = 0$. Se cumple para todo $\lambda$ y **no impone ninguna condición sobre $k$** (la primera componente del autovector es $0$, así que $k$ nunca aparece).
- **Fila 2:** $1 = -\lambda \implies \lambda = -1$.
- **Fila 3:** $-1 = \lambda \implies \lambda = -1$. Consistente.

Entonces $Av = -v$: el vector $(0,-1,1)$ **es autovector de $A$ con autovalor $\lambda = -1$ para cualquier valor de $k \in \mathbb{R}$**. El parámetro $k$ queda libre.

> **Punto sutil.** Como la primera coordenada del autovector candidato es $0$, multiplica a la única entrada que contiene $k$ (la posición $(1,1)$). Por eso $k$ no interviene y la respuesta del inciso a) es: *todo* $k \in \mathbb{R}$.

**b)** Calculamos el polinomio característico (convención de la cátedra $p_A(\lambda) = \det(\lambda I - A)$, líder $+1$). Como la primera columna de $A$ es $(k, 2, -2)^T$ pero las filas $2$ y $3$ no tocan la primera columna salvo en su propia fila, desarrollamos $\lambda I - A$ por la primera fila:

$$\lambda I - A = \begin{pmatrix} \lambda - k & 0 & 0 \\ -2 & \lambda + 2 & 1 \\ 2 & -5 & \lambda - 4 \end{pmatrix}.$$

$$p_A(\lambda) = (\lambda - k)\begin{vmatrix} \lambda + 2 & 1 \\ -5 & \lambda - 4 \end{vmatrix} = (\lambda - k)\big[(\lambda+2)(\lambda-4) + 5\big] = (\lambda - k)(\lambda^2 - 2\lambda - 3).$$

Factorizando $\lambda^2 - 2\lambda - 3 = (\lambda - 3)(\lambda + 1)$:

$$\boxed{\,p_A(\lambda) = (\lambda - k)(\lambda - 3)(\lambda + 1)\,}$$

Los autovalores son $\lambda \in \{\,-1,\ 3,\ k\,\}$. Esto confirma lo del inciso a): $\lambda = -1$ es autovalor de $A$ **para todo $k$**. Analizamos la diagonalización según $k$ (un autovalor simple siempre aporta $m_g = 1 = m_a$; sólo hay que vigilar las coincidencias).

**Caso general $k \neq -1$ y $k \neq 3$:** los tres autovalores $-1,\,3,\,k$ son distintos. Tres autovalores distintos en $\mathbb{R}^{3}$ $\Rightarrow$ tres autovectores LI $\Rightarrow$ **$A$ es diagonalizable**.

**Caso $k = 3$:** el polinomio queda $p_A(\lambda) = (\lambda - 3)^2(\lambda + 1)$, con $\lambda = 3$ de multiplicidad algebraica $m_a = 2$. Hay que verificar $m_g$. Con $k = 3$:

$$3I - A = \begin{pmatrix} 0 & 0 & 0 \\ -2 & 5 & 1 \\ 2 & -5 & -1 \end{pmatrix}.$$

La fila $3$ es $-1\cdot$ la fila $2$ y la fila $1$ es nula, así que $\operatorname{rg}(3I - A) = 1$ y por el teorema de la dimensión $\dim S_3 = 3 - 1 = 2 = m_a$. Como además $\lambda = -1$ es simple ($m_g = 1$), se cumple $m_g = m_a$ para todos los autovalores $\Rightarrow$ **$A$ es diagonalizable**. (Una base de $S_3$ es $\{(5,2,0),\,(1,0,2)\}$, obtenida de $-2x + 5y + z = 0$.)

**Caso $k = -1$:** ahora $\lambda = -1$ tiene multiplicidad algebraica $m_a = 2$ y $p_A(\lambda) = (\lambda - 3)(\lambda + 1)^2$. Estudiamos $S_{-1} = N(-I - A)$ con $k = -1$:

$$-I - A = \begin{pmatrix} -1 - (-1) & 0 & 0 \\ -2 & -1 + 2 & 1 \\ 2 & -5 & -1 - 4 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 0 \\ -2 & 1 & 1 \\ 2 & -5 & -5 \end{pmatrix}.$$

Escalonando (queremos el rango): $F_3 \leftarrow F_3 + F_2$ da $(0, -4, -4)$, y la fila $1$ es nula. Quedan dos filas LI $(-2,1,1)$ y $(0,-4,-4)$, así que $\operatorname{rg}(-I - A) = 2$ y $\dim S_{-1} = 3 - 2 = 1$. Entonces $m_g = 1 < 2 = m_a$ $\Rightarrow$ **$A$ NO es diagonalizable**. (El único autovector de $S_{-1}$ es, justamente, $(0,-1,1)$ del inciso a): de $-4y - 4z = 0 \Rightarrow z = -y$ y $-2x + y + z = 0 \Rightarrow x = 0$, dando $(0, 1, -1) \parallel (0,-1,1)$.)

**Conclusión.**

$$\boxed{\ A \text{ es diagonalizable en } \mathbb{R} \iff k \neq -1;\quad \text{para } k = -1 \text{ NO es diagonalizable.}\ }$$

*(Verificado con `sympy`: para $k=-1$ se obtiene $m_a=2,\ m_g=1$ en $\lambda=-1$ — no diagonalizable; para $k=3$ se obtiene $m_a=m_g=2$ en $\lambda=3$ — diagonalizable; y $A(0,-1,1)^T = (0,1,-1) = -(0,-1,1)^T$ para todo $k$.)*

## Ejercicio 2

Dada la matriz $A = \begin{pmatrix} 2 & 0 & 2 \\ 0 & 3 & 3 \\ 1 & -1 & 0 \end{pmatrix}$

a) Hallar una factorización $QR$.
b) Hallar una factorización $PLU$.

> **Observación clave (vale para todo el ejercicio).** Las columnas de $A$ cumplen $a_3 = a_1 + a_2$ (en efecto $(2,0,1)+(0,3,-1)=(2,3,0)$). Por lo tanto $\operatorname{rg}(A) = 2$ y $\det A = 0$: $A$ es **singular**. Esto se reflejará en una fila nula de $R$ (QR) y en un pivote $U_{33} = 0$ (LU).

### Resolución de a) — QR por Gram–Schmidt

Trabajamos con las columnas $a_1 = (2,0,1)^T$, $a_2 = (0,3,-1)^T$, $a_3 = (2,3,0)^T$.

**Columna 1.** $u_1 = a_1 = (2,0,1)^T$, con $\lVert u_1\rVert = \sqrt{4+0+1} = \sqrt5$. Entonces

$$v_1 = \frac{u_1}{\lVert u_1\rVert} = \frac{1}{\sqrt5}(2,0,1)^T = \frac{\sqrt5}{5}(2,0,1)^T.$$

Así $R_{11} = \lVert u_1\rVert = \sqrt5$.

**Columna 2.** $R_{12} = \langle a_2, v_1\rangle = \dfrac{1}{\sqrt5}\big(0\cdot2 + 3\cdot0 + (-1)\cdot1\big) = -\dfrac{1}{\sqrt5} = -\dfrac{\sqrt5}{5}$.

$$u_2 = a_2 - R_{12}\,v_1 = (0,3,-1)^T - \Big(-\tfrac{1}{5}\Big)(2,0,1)^T = \Big(\tfrac{2}{5},\,3,\,-\tfrac{4}{5}\Big)^T.$$

$\lVert u_2\rVert^2 = \tfrac{4}{25} + 9 + \tfrac{16}{25} = \tfrac{20}{25} + 9 = \tfrac{49}{5}$, de modo que $\lVert u_2\rVert = \dfrac{7}{\sqrt5} = \dfrac{7\sqrt5}{5}$ ($= R_{22}$). Entonces

$$v_2 = \frac{u_2}{\lVert u_2\rVert} = \frac{\sqrt5}{7}\Big(\tfrac{2}{5},\,3,\,-\tfrac{4}{5}\Big)^T = \Big(\tfrac{2\sqrt5}{35},\,\tfrac{3\sqrt5}{7},\,-\tfrac{4\sqrt5}{35}\Big)^T.$$

**Columna 3.** Como $a_3 = a_1 + a_2$, debe caer enteramente en el espacio generado por $v_1, v_2$, así que la proyección será exacta y $u_3 = 0$. Verifiquémoslo calculando los coeficientes:

$$R_{13} = \langle a_3, v_1\rangle = \tfrac{1}{\sqrt5}(2\cdot2 + 3\cdot0 + 0\cdot1) = \tfrac{4}{\sqrt5} = \tfrac{4\sqrt5}{5},$$

$$R_{23} = \langle a_3, v_2\rangle = \tfrac{2\sqrt5}{35}\cdot2 + \tfrac{3\sqrt5}{7}\cdot3 + \big(-\tfrac{4\sqrt5}{35}\big)\cdot0 = \tfrac{4\sqrt5}{35} + \tfrac{9\sqrt5}{7} = \tfrac{4\sqrt5 + 45\sqrt5}{35} = \tfrac{49\sqrt5}{35} = \tfrac{7\sqrt5}{5}.$$

$$u_3 = a_3 - R_{13}\,v_1 - R_{23}\,v_2 = (0,0,0)^T \quad\Rightarrow\quad R_{33} = 0.$$

Como $u_3 = 0$, la columna $a_3$ no aporta una nueva dirección. Para tener una factorización **completa** con $Q$ ortogonal ($Q^TQ = I$), completamos la base ortonormal de $\mathbb{R}^3$ eligiendo $v_3$ ortonormal a $v_1, v_2$. Tomamos $v_3 \parallel u_1 \times u_2 \propto (2,0,1)\times(\tfrac25,3,-\tfrac45)$, que da la dirección $(-3, 2, 6)$ (norma $\sqrt{9+4+36}=7$):

$$v_3 = \frac{1}{7}(-3,2,6)^T = \Big(-\tfrac{3}{7},\,\tfrac{2}{7},\,\tfrac{6}{7}\Big)^T.$$

**Resultado.** Con $Q = (\,v_1 \mid v_2 \mid v_3\,)$ y $R = Q^T A$:

$$Q = \begin{pmatrix} \dfrac{2\sqrt5}{5} & \dfrac{2\sqrt5}{35} & -\dfrac{3}{7} \\[2mm] 0 & \dfrac{3\sqrt5}{7} & \dfrac{2}{7} \\[2mm] \dfrac{\sqrt5}{5} & -\dfrac{4\sqrt5}{35} & \dfrac{6}{7} \end{pmatrix} \approx \begin{pmatrix} 0.8944 & 0.1278 & -0.4286 \\ 0 & 0.9583 & 0.2857 \\ 0.4472 & -0.2556 & 0.8571 \end{pmatrix},$$

$$R = \begin{pmatrix} \sqrt5 & -\dfrac{\sqrt5}{5} & \dfrac{4\sqrt5}{5} \\[2mm] 0 & \dfrac{7\sqrt5}{5} & \dfrac{7\sqrt5}{5} \\[2mm] 0 & 0 & 0 \end{pmatrix} \approx \begin{pmatrix} 2.2361 & -0.4472 & 1.7889 \\ 0 & 3.1305 & 3.1305 \\ 0 & 0 & 0 \end{pmatrix}.$$

La última fila nula de $R$ refleja $\operatorname{rg}(A) = 2$.

**Verificación.** $Q^TQ = I_3$ y $QR = A$:

$$QR = \begin{pmatrix} 2 & 0 & 2 \\ 0 & 3 & 3 \\ 1 & -1 & 0 \end{pmatrix} = A. \quad\checkmark$$

*(Comprobado numéricamente con `numpy`/`sympy`: $\lVert Q^TQ - I\rVert = 0$, $\lVert QR - A\rVert = 0$, $\det Q = 1$.)*

> **Nota.** Si sólo se pide "una" factorización QR (no necesariamente con $Q$ ortogonal completa), basta dar $v_1, v_2$ y dejar la tercera columna de $Q$ nula con $R_{33}=0$; el producto $QR=A$ se mantiene. Acá completamos $v_3$ para que $Q$ sea ortogonal "de verdad", que es lo habitual en el parcial.

### Resolución de b) — PLU (Doolittle)

Eliminación gaussiana sobre $A$ con el método de Doolittle ($L$ con unos en la diagonal; cada operación $F_i \leftarrow F_i - m_{ij}F_j$ deja $L_{ij} = m_{ij}$).

**Pivote 1:** $A_{11} = 2 \neq 0$, no hace falta permutar. Multiplicadores de la primera columna:

$$m_{21} = \frac{A_{21}}{A_{11}} = \frac{0}{2} = 0, \qquad m_{31} = \frac{A_{31}}{A_{11}} = \frac{1}{2}.$$

$F_2 \leftarrow F_2 - 0\cdot F_1$ (sin cambios), $F_3 \leftarrow F_3 - \tfrac12 F_1$:

$$\begin{pmatrix} 2 & 0 & 2 \\ 0 & 3 & 3 \\ 1 & -1 & 0 \end{pmatrix} \longrightarrow \begin{pmatrix} 2 & 0 & 2 \\ 0 & 3 & 3 \\ 0 & -1 & -1 \end{pmatrix}.$$

**Pivote 2:** $3 \neq 0$, no se permuta. $m_{32} = \dfrac{-1}{3} = -\dfrac13$. $F_3 \leftarrow F_3 - \big(-\tfrac13\big)F_2 = F_3 + \tfrac13 F_2$:

$$\begin{pmatrix} 2 & 0 & 2 \\ 0 & 3 & 3 \\ 0 & -1 & -1 \end{pmatrix} \longrightarrow \begin{pmatrix} 2 & 0 & 2 \\ 0 & 3 & 3 \\ 0 & 0 & 0 \end{pmatrix} = U.$$

El pivote $U_{33} = 0$ aparece **sólo al final** (no es un pivote que haya que usar para eliminar nada debajo), así que **no se requiere pivoteo**: $P = I$.

**Resultado.**

$$P = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix},\qquad L = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ \tfrac12 & -\tfrac13 & 1 \end{pmatrix},\qquad U = \begin{pmatrix} 2 & 0 & 2 \\ 0 & 3 & 3 \\ 0 & 0 & 0 \end{pmatrix}.$$

**Verificación.** $PA = A$ y

$$LU = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ \tfrac12 & -\tfrac13 & 1 \end{pmatrix}\begin{pmatrix} 2 & 0 & 2 \\ 0 & 3 & 3 \\ 0 & 0 & 0 \end{pmatrix} = \begin{pmatrix} 2 & 0 & 2 \\ 0 & 3 & 3 \\ 1 & -1 & 0 \end{pmatrix} = A = PA. \quad\checkmark$$

*(Comprobado numéricamente: $\lVert LU - A\rVert = 0$. El pivoteo parcial de `scipy.linalg.lu` también devuelve $P = I$ acá, porque los pivotes naturales $2$ y $3$ ya son los de mayor módulo en su columna.)*

## Ejercicio 3

Dada la función $f(t) = |\sin(t)|$:

a) Hallar la serie trigonométrica de Fourier.
b) Indicar a qué converge la serie de $f'(t)$ en $t = \pi$.

### Resolución de a)

**Período y simetría.** Aunque $\sin t$ tiene período $2\pi$, el valor absoluto "pliega" la parte negativa: $|\sin(t + \pi)| = |-\sin t| = |\sin t|$, así que el **período fundamental es $T = \pi$**. Además $f$ es **par** ($|\sin(-t)| = |\sin t|$), de modo que **todos los $b_n = 0$**: la serie tiene sólo cosenos.

Con la convención de la cátedra y $T = \pi$, la frecuencia de los armónicos es $\dfrac{2\pi n}{T} = \dfrac{2\pi n}{\pi} = 2n$, es decir aparecen $\cos(2nt)$. En todo el intervalo $[0,\pi]$ vale $\sin t \ge 0$, así que $|\sin t| = \sin t$ ahí.

**Valor medio $a_0$** (recordar: es el promedio, sin dividir por $2$):

$$a_0 = \frac{1}{T}\int_0^{T} f(t)\,dt = \frac{1}{\pi}\int_0^{\pi}\sin t\,dt = \frac{1}{\pi}\big[-\cos t\big]_0^{\pi} = \frac{1}{\pi}\big(1 - (-1)\big) = \frac{2}{\pi}.$$

**Coeficientes $a_n$:**

$$a_n = \frac{2}{T}\int_0^{T} f(t)\cos\!\Big(\tfrac{2\pi n}{T}t\Big)dt = \frac{2}{\pi}\int_0^{\pi}\sin t\,\cos(2nt)\,dt.$$

Usamos producto a suma: $\sin t\cos(2nt) = \tfrac12\big[\sin\big((1+2n)t\big) + \sin\big((1-2n)t\big)\big]$. Entonces

$$a_n = \frac{1}{\pi}\int_0^{\pi}\Big[\sin\big((2n+1)t\big) - \sin\big((2n-1)t\big)\Big]dt = \frac{1}{\pi}\left[-\frac{\cos((2n+1)t)}{2n+1} + \frac{\cos((2n-1)t)}{2n-1}\right]_0^{\pi}.$$

Como $\cos((2n\pm1)\pi) = -1$ (argumento impar $\times \pi$) y $\cos 0 = 1$, la primitiva evaluada entre $0$ y $\pi$ da $\cos((2n\pm1)\pi) - \cos 0 = -1 - 1 = -2$ en cada término:

$$a_n = \frac{1}{\pi}\left[\frac{\cos((2n-1)\pi) - 1}{2n-1} - \frac{\cos((2n+1)\pi) - 1}{2n+1}\right] = \frac{1}{\pi}\left[\frac{-2}{2n-1} - \frac{-2}{2n+1}\right]$$

$$= \frac{2}{\pi}\left[\frac{1}{2n+1} - \frac{1}{2n-1}\right] = \frac{2}{\pi}\cdot\frac{(2n-1) - (2n+1)}{(2n+1)(2n-1)} = \frac{2}{\pi}\cdot\frac{-2}{4n^2 - 1}.$$

$$\boxed{\,a_n = -\frac{4}{\pi(4n^2 - 1)}\,}\qquad (n \ge 1).$$

**Serie trigonométrica de Fourier:**

$$\boxed{\ |\sin t| = \frac{2}{\pi} - \frac{4}{\pi}\sum_{n=1}^{\infty}\frac{\cos(2nt)}{4n^2 - 1}\ }$$

Los primeros coeficientes son $a_1 = -\tfrac{4}{3\pi}$, $a_2 = -\tfrac{4}{15\pi}$, $a_3 = -\tfrac{4}{35\pi}$, $a_4 = -\tfrac{4}{63\pi}$, … Como $f$ es continua en todo $\mathbb{R}$, por Dirichlet la serie converge a $f(t)$ en **todo** punto.

*(Verificado numéricamente: $a_0 = 2/\pi$ por integración exacta; $a_n = -4/[\pi(4n^2-1)]$ coincide término a término con la integral para $n=1,\dots,5$; y la suma parcial $S_{200}(t)$ aproxima $|\sin t|$ a $\sim 10^{-5}$ en $t = 0.3,\,1,\,\pi/2,\,2.5,\,3$.)*

### Resolución de b)

Estudiamos $f'(t)$ alrededor de $t = \pi$. Cerca de ese punto $|\sin t|$ tiene un **pico** (vértice) porque $\sin t$ cambia de signo: $\sin t > 0$ en $(0,\pi)$ y $\sin t < 0$ en $(\pi, 2\pi)$. Entonces:

- En $(0,\pi)$: $f(t) = \sin t \Rightarrow f'(t) = \cos t$, luego $f'(\pi^-) = \cos\pi = -1$.
- En $(\pi, 2\pi)$: $f(t) = -\sin t \Rightarrow f'(t) = -\cos t$, luego $f'(\pi^+) = -\cos\pi = +1$.

Así $f'$ presenta un **salto** (discontinuidad de salto) en $t = \pi$, con límites laterales $-1$ y $+1$. Por el teorema de Dirichlet, la serie de Fourier de $f'$ converge en un salto al **promedio de los límites laterales**:

$$\text{serie de } f'\big|_{t=\pi} \longrightarrow \frac{f'(\pi^-) + f'(\pi^+)}{2} = \frac{-1 + 1}{2}.$$

$$\boxed{\ \text{La serie de } f'(t) \text{ converge a } 0 \text{ en } t = \pi.\ }$$

**Consistencia con la derivación término a término.** Derivando la serie de a):

$$f'(t) \sim \frac{d}{dt}\left[\frac{2}{\pi} - \frac{4}{\pi}\sum_{n\ge1}\frac{\cos(2nt)}{4n^2-1}\right] = \frac{8}{\pi}\sum_{n=1}^{\infty}\frac{n}{4n^2 - 1}\sin(2nt).$$

En $t = \pi$: $\sin(2n\pi) = 0$ para todo $n$, así que **cada término se anula** y la suma vale $0$, en perfecto acuerdo con el promedio de los saltos.

*(Verificado numéricamente: $f'(\pi^-) = -1$, $f'(\pi^+) = +1$, promedio $0$; la suma parcial de $\tfrac{8}{\pi}\sum \tfrac{n}{4n^2-1}\sin(2nt)$ en $t=\pi$ da $\sim 10^{-13}$, y en un punto de continuidad como $t=1$ tiende a $\cos 1 \approx 0.5403$.)*

---

## Resumen de resultados

| Ej. | Resultado |
|-----|-----------|
| 1a  | $(0,-1,1)$ es autovector con $\lambda = -1$ para **todo** $k \in \mathbb{R}$ |
| 1b  | Diagonalizable $\iff k \neq -1$ (en $k=-1$: $\lambda=-1$ tiene $m_a=2,\ m_g=1$) |
| 2a  | $A = QR$ con $R_{33}=0$ ($\operatorname{rg} A = 2$); $R_{11}=\sqrt5,\ R_{22}=\tfrac{7\sqrt5}{5}$ |
| 2b  | $A = LU$ con $P=I$, $L_{31}=\tfrac12,\ L_{32}=-\tfrac13$, $U_{33}=0$ |
| 3a  | $\displaystyle |\sin t| = \frac{2}{\pi} - \frac{4}{\pi}\sum_{n\ge1}\frac{\cos(2nt)}{4n^2-1}$ |
| 3b  | La serie de $f'$ converge a $0$ en $t=\pi$ (promedio de $-1$ y $+1$) |

Relacionados: [[ip-tema-08]] · [[../guias/guia-08-fourier-series]] · [[../resueltos/resueltos-fourier]] · [[patrones]]
