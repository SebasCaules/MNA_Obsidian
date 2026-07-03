---
tags: [parcial, ip, resolucion, autovectores, diagonalizacion, transformaciones-lineales, antiimagen, nucleo-imagen, fourier, serie-trigonometrica, convergencia]
fuente: raw/Practicas/Modelos_Examenes/MNA_IP_Tema_VII.pdf
tipo: ip
tema: 7
tiene_resolucion: true
---

# Primer Parcial de Métodos Numéricos Avanzados — Tema VII (Resolución)

Enunciado original sin desarrollo en [[ip-tema-07]]. Recetas relacionadas: diagonalización en [[ip-tema-01-resolucion]] y [[ip-tema-05-resolucion]]; antiimagen y núcleo/imagen en [[ip-tema-01-resolucion]]; series de Fourier en [[../guias/guia-08-fourier-series]] y [[../resueltos/resueltos-fourier]].

## Ejercicio 1

Sea $A = \begin{pmatrix} 1 & 0 & b \\ 1 & 1 & 0 \\ 1 & 1 & a \end{pmatrix}$.

a) Hallar $a, b \in \mathbb{R}$ para que $(0, -1, 1)$ sea autovector de $A$.
b) Para los valores hallados en a), decida si $A$ es diagonalizable en $\mathbb{R}$.

### Resolución

**a)** Que $v = (0, -1, 1)$ sea autovector significa que existe $\lambda \in \mathbb{R}$ con $Av = \lambda v$. Calculamos $Av$:

$$A\begin{pmatrix} 0 \\ -1 \\ 1 \end{pmatrix} = \begin{pmatrix} 1\cdot 0 + 0\cdot(-1) + b\cdot 1 \\ 1\cdot 0 + 1\cdot(-1) + 0\cdot 1 \\ 1\cdot 0 + 1\cdot(-1) + a\cdot 1 \end{pmatrix} = \begin{pmatrix} b \\ -1 \\ a - 1 \end{pmatrix}$$

Imponemos $Av = \lambda v = (0,\ -\lambda,\ \lambda)$, igualando componente a componente:

$$\begin{cases} b = 0 \\ -1 = -\lambda \\ a - 1 = \lambda \end{cases} \implies \lambda = 1,\quad b = 0,\quad a = \lambda + 1 = 2$$

$$\boxed{a = 2,\quad b = 0,\quad \text{con autovalor asociado } \lambda = 1}$$

Verificación directa: con $a=2,\ b=0$, $\ A(0,-1,1)^T = (0, -1, 1)^T = 1\cdot(0,-1,1)^T$. ✓

**b)** Para los valores hallados la matriz es

$$A = \begin{pmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 1 & 2 \end{pmatrix}$$

Calculamos el polinomio característico $p_A(\lambda) = \det(\lambda I - A)$:

$$\lambda I - A = \begin{pmatrix} \lambda - 1 & 0 & 0 \\ -1 & \lambda - 1 & 0 \\ -1 & -1 & \lambda - 2 \end{pmatrix}$$

La matriz es triangular inferior, así que el determinante es el producto de la diagonal:

$$p_A(\lambda) = (\lambda - 1)(\lambda - 1)(\lambda - 2) = (\lambda - 1)^2(\lambda - 2)$$

Los autovalores son $\lambda_1 = 1$ con multiplicidad algebraica $m_a = 2$ y $\lambda_2 = 2$ con $m_a = 1$.

$A$ es diagonalizable en $\mathbb{R}$ $\iff$ para todo autovalor $m_g = m_a$. El único candidato a fallar es $\lambda = 1$ (el repetido). Calculamos su multiplicidad geométrica $m_g = \dim S_1 = \dim N(1\cdot I - A)$:

$$1\cdot I - A = \begin{pmatrix} 0 & 0 & 0 \\ -1 & 0 & 0 \\ -1 & -1 & -1 \end{pmatrix} \xrightarrow{\text{Gauss}} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{pmatrix}$$

Esta matriz tiene rango $2$, así que su núcleo tiene dimensión $3 - 2 = 1$. De la forma escalonada: $x = 0$ y $y = -z$, luego

$$S_1 = \langle (0, -1, 1) \rangle,\qquad m_g(\lambda=1) = 1$$

(es justamente el autovector del item a). Como $m_g(1) = 1 \ne 2 = m_a(1)$:

$$\boxed{A \text{ NO es diagonalizable en } \mathbb{R}}$$

> **Verificación numérica (numpy/sympy).** $p_A(\lambda) = \lambda^3 - 4\lambda^2 + 5\lambda - 2 = (\lambda-1)^2(\lambda-2)$; `np.linalg.eig` devuelve autovalores $\{1, 1, 2\}$. El núcleo de $(I - A)$ tiene dimensión $1$ con base $(0,-1,1)$, confirmando $m_g(1) = 1 < m_a(1) = 2$.

## Ejercicio 2

Sea $T : \mathbb{R}^3 \to \mathbb{R}^3$ una Transformación Lineal cuya matriz asociada es

$$M(T)_{EB} = \begin{pmatrix} 2 & 0 & 2 \\ 0 & 3 & 3 \\ 1 & -1 & 0 \end{pmatrix}$$

con $E$ la base canónica de $\mathbb{R}^3$ y $B = \{(0, 1, -1),\ (0, 0, 1),\ (1, 1, 0)\}$.

a) Hallar todos los $v \in \mathbb{R}^3$, si existen, de modo que $T(v) = (0, 2, 1)$.
b) Hallar $\dim(N(T))$.

### Resolución

**Convención.** $M_{EB}$ recibe coordenadas **en la base $B$** del dominio y devuelve el resultado **en la base canónica** del codominio:

$$M_{EB}\,[v]_B = T(v) \quad (\text{en coordenadas canónicas}).$$

**a)** Como $(0,2,1)$ ya está en canónica, debemos resolver el sistema $M_{EB}\,[v]_B = (0, 2, 1)$ para las coordenadas $[v]_B = (x_1, x_2, x_3)$:

$$\begin{pmatrix} 2 & 0 & 2 \\ 0 & 3 & 3 \\ 1 & -1 & 0 \end{pmatrix}\begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} 0 \\ 2 \\ 1 \end{pmatrix}$$

Primero notamos que el sistema **no** es directamente inversible: $\det(M_{EB}) = 0$ (las columnas son linealmente dependientes, $\text{rg}(M_{EB}) = 2$). Hay que analizar la **compatibilidad** reduciendo la matriz ampliada:

$$\left(\begin{array}{ccc|c} 2 & 0 & 2 & 0 \\ 0 & 3 & 3 & 2 \\ 1 & -1 & 0 & 1 \end{array}\right) \xrightarrow{\text{Gauss-Jordan}} \left(\begin{array}{ccc|c} 1 & 0 & 1 & 0 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{array}\right)$$

La última fila es $0\,x_1 + 0\,x_2 + 0\,x_3 = 1$, que es **imposible**. El sistema es **incompatible**.

Equivalentemente, $(0,2,1) \notin \text{Im}(T)$: la imagen es el plano generado por las columnas pivote de $M_{EB}$,

$$\text{Im}(T) = \langle (2, 0, 1),\ (0, 3, -1) \rangle,$$

cuyo vector normal es $(2,0,1) \times (0,3,-1) = (-3, 2, 6)$. Como $(-3, 2, 6)\cdot(0, 2, 1) = 0 + 4 + 6 = 10 \ne 0$, el punto $(0,2,1)$ no pertenece al plano imagen.

$$\boxed{\text{No existe } v \in \mathbb{R}^3 \text{ tal que } T(v) = (0, 2, 1)}$$

**b)** Por el teorema de la dimensión, $\dim N(T) + \dim \text{Im}(T) = \dim(\text{dominio}) = 3$. Como $\dim \text{Im}(T) = \text{rg}(M_{EB}) = 2$:

$$\boxed{\dim N(T) = 3 - 2 = 1}$$

A modo de chequeo explícito, $N(T)$ corresponde a $M_{EB}\,[v]_B = 0$, es decir $[v]_B \in N(M_{EB}) = \langle (-1, -1, 1) \rangle$. Reconstruyendo en canónica:

$$v = -1\cdot(0,1,-1) - 1\cdot(0,0,1) + 1\cdot(1,1,0) = (1, 0, 0),\qquad N(T) = \langle (1, 0, 0) \rangle.$$

> **Verificación numérica (sympy).** $\text{rg}(M_{EB}) = 2$, $\det = 0$. La RREF de la ampliada da una fila $[0\ 0\ 0\,|\,1]$ → sistema sin solución, confirmando (a). $N(M_{EB}) = \langle(-1,-1,1)\rangle$ y la reconstrucción da $v=(1,0,0)$ con $T(v)=M_{EB}[v]_B = (0,0,0)$, confirmando $\dim N(T) = 1$.

## Ejercicio 3

Dada la función $f(t) = |\cos(t)|$:

a) Hallar la serie trigonométrica de Fourier.
b) Indicar a qué converge la serie de $f'(t)$ en $t = \dfrac{\pi}{2}$.

### Resolución

**a)** Aunque $\cos(t)$ tiene período $2\pi$, al tomar valor absoluto $f(t) = |\cos t|$ el período se reduce a

$$T = \pi,$$

porque $|\cos(t + \pi)| = |-\cos t| = |\cos t|$. Conviene además observar que $f$ es **par** ($f(-t) = f(t)$), de modo que **todos los $b_n = 0$** y la serie tiene solo cosenos.

La frecuencia fundamental es $\dfrac{2\pi}{T} = \dfrac{2\pi}{\pi} = 2$, así que los armónicos son $\cos(2n\,t)$. Sobre un período centrado $\left[-\tfrac{\pi}{2}, \tfrac{\pi}{2}\right]$ se tiene $\cos t \ge 0$, luego $|\cos t| = \cos t$ ahí.

**Valor medio** $a_0$ (recordar: en la convención de la cátedra $a_0$ es el valor medio, **sin** dividir por 2):

$$a_0 = \frac{1}{T}\int_{-\pi/2}^{\pi/2} \cos t\,dt = \frac{1}{\pi}\big[\sin t\big]_{-\pi/2}^{\pi/2} = \frac{1}{\pi}(1 - (-1)) = \frac{2}{\pi}$$

**Coeficientes $a_n$** ($n \ge 1$):

$$a_n = \frac{2}{T}\int_{-\pi/2}^{\pi/2} \cos t \cos(2n\,t)\,dt = \frac{2}{\pi}\int_{-\pi/2}^{\pi/2} \cos t \cos(2n\,t)\,dt$$

Usando producto a suma $\cos\alpha\cos\beta = \tfrac12[\cos(\alpha-\beta) + \cos(\alpha+\beta)]$:

$$a_n = \frac{1}{\pi}\int_{-\pi/2}^{\pi/2}\Big[\cos\big((2n-1)t\big) + \cos\big((2n+1)t\big)\Big]dt$$

$$= \frac{1}{\pi}\left[\frac{\sin((2n-1)t)}{2n-1} + \frac{\sin((2n+1)t)}{2n+1}\right]_{-\pi/2}^{\pi/2} = \frac{2}{\pi}\left[\frac{\sin\!\big((2n-1)\tfrac{\pi}{2}\big)}{2n-1} + \frac{\sin\!\big((2n+1)\tfrac{\pi}{2}\big)}{2n+1}\right]$$

Ahora $(2n\pm 1)$ es impar, y $\sin\!\big((2k+1)\tfrac{\pi}{2}\big) = (-1)^{k}$. Para el primer término $2n-1 = 2(n-1)+1$ da $(-1)^{n-1}$; para el segundo $2n+1 = 2n+1$ da $(-1)^{n}$:

$$a_n = \frac{2}{\pi}\left[\frac{(-1)^{n-1}}{2n-1} + \frac{(-1)^{n}}{2n+1}\right] = \frac{2}{\pi}(-1)^{n-1}\left[\frac{1}{2n-1} - \frac{1}{2n+1}\right] = \frac{2}{\pi}(-1)^{n-1}\cdot\frac{2}{(2n-1)(2n+1)}$$

Como $(2n-1)(2n+1) = 4n^2 - 1$ y $(-1)^{n-1} = (-1)^{n+1}$:

$$\boxed{a_0 = \frac{2}{\pi},\qquad a_n = \frac{4}{\pi}\,\frac{(-1)^{n+1}}{4n^2 - 1}\quad (n \ge 1),\qquad b_n = 0}$$

Por lo tanto la serie trigonométrica de Fourier es

$$\boxed{\,|\cos t| = \frac{2}{\pi} + \frac{4}{\pi}\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{4n^2 - 1}\cos(2n\,t)\,}$$

Los primeros términos: $\displaystyle |\cos t| = \frac{2}{\pi} + \frac{4}{3\pi}\cos(2t) - \frac{4}{15\pi}\cos(4t) + \frac{4}{35\pi}\cos(6t) - \cdots$

Como $f$ es continua en todo punto, por el teorema de Dirichlet la serie converge a $f(t)$ para todo $t$.

> **Verificación numérica (sympy/numpy).** Integrando simbólicamente: $a_0 = 2/\pi$ y $a_n = \dfrac{4(-1)^{n+1}}{\pi(4n^2-1)}$ (coincide término a término con la fórmula cerrada para $n=1,\dots,5$). Las sumas parciales convergen a $|\cos t|$: el máximo error sobre una muestra cae de $4.8\cdot10^{-2}$ ($N=5$) a $1.1\cdot10^{-3}$ ($N=100$); la convergencia es lenta ($\sim 1/N$) cerca de los picos $t = k\pi$, donde $f$ tiene un punto anguloso (vértice).

**b)** La derivada de $f(t) = |\cos t|$ tiene un **salto** (discontinuidad de salto) en $t = \tfrac{\pi}{2}$, porque ahí $\cos t$ cambia de signo. Explícitamente, en un entorno de $\tfrac{\pi}{2}$:

- Para $t < \tfrac{\pi}{2}$ (con $t$ cercano), $\cos t > 0 \implies f(t) = \cos t \implies f'(t) = -\sin t$.
- Para $t > \tfrac{\pi}{2}$ (con $t$ cercano), $\cos t < 0 \implies f(t) = -\cos t \implies f'(t) = \sin t$.

Evaluando los límites laterales en $t = \tfrac{\pi}{2}$:

$$f'\!\left(\tfrac{\pi}{2}^{-}\right) = -\sin\!\tfrac{\pi}{2} = -1,\qquad f'\!\left(\tfrac{\pi}{2}^{+}\right) = \sin\!\tfrac{\pi}{2} = +1$$

En un punto de salto, la serie de Fourier (de $f'$) converge al **promedio de los límites laterales** (Dirichlet):

$$\frac{1}{2}\Big(f'\!\left(\tfrac{\pi}{2}^{-}\right) + f'\!\left(\tfrac{\pi}{2}^{+}\right)\Big) = \frac{1}{2}\big(-1 + 1\big) = 0$$

$$\boxed{\text{La serie de } f'(t) \text{ converge a } 0 \text{ en } t = \tfrac{\pi}{2}}$$

> **Verificación numérica.** Los límites laterales numéricos de la derivada dan $f'(\pi/2^-) \approx -1.000000$ y $f'(\pi/2^+) \approx +1.000000$, promedio $0$. Además, derivando la serie término a término ($f'(t) \approx \sum_{n\ge1} -\tfrac{8n}{\pi}\tfrac{(-1)^{n+1}}{4n^2-1}\sin(2nt)$) y evaluando en $t=\pi/2$, las sumas parciales dan exactamente $0$ (todos los $\sin(2n\cdot\tfrac{\pi}{2}) = \sin(n\pi) = 0$), del orden de $10^{-14}$ a máquina, en concordancia con el promedio de Dirichlet.
