---
tags: [final, transformaciones-lineales, nucleo-imagen, diagonalizacion, fourier, edo, diferencias-finitas, transformada-fourier]
fuente: raw/Practicas/Modelos_Examenes/MNA_Final_Tema_II.pdf
tipo: final
tema: 2
tiene_resolucion: true
---

# Examen Final de Métodos Numéricos Avanzados — Tema II (Resolución)

Enunciado base en [[final-tema-02]]. Referencias de método: [[../resueltos/resueltos-fourier]], [[../resueltos/resueltos-diagonalizacion]], [[../guias/guia-08-fourier-series]].

## Ejercicio 1

Dada la TL $T : \mathbb{R}^3 \to \mathbb{R}^3 : T(x, y, z) = (2x - y,\ x + y - z,\ z - x - y)$

a) Hallar el Núcleo y la Imagen.
b) Decidir si es o no diagonalizable en $\mathbb{R}$.

### Resolución

La matriz en base canónica (columnas $= T(e_j)$) es

$$M_{EE}(T) = A = \begin{pmatrix} 2 & -1 & 0 \\ 1 & 1 & -1 \\ -1 & -1 & 1 \end{pmatrix}.$$

Calculamos primero el determinante (decide si $T$ es isomorfismo):

$$\det A = 2\,(1\cdot1 - (-1)(-1)) - (-1)\,(1\cdot1 - (-1)(-1)) + 0 = 2\cdot 0 + 1\cdot 0 + 0 = 0.$$

Como $\det A = 0$, $T$ **no** es inyectiva: el núcleo es no trivial.

**a) Núcleo.** Resolvemos $T(x,y,z)=0$, es decir $AX=0$:

$$\begin{cases} 2x - y = 0 \\ x + y - z = 0 \\ -x - y + z = 0 \end{cases}.$$

La tercera ecuación es $-1$ por la segunda, de modo que solo hay dos ecuaciones independientes (consistente con $\operatorname{rg}(A)=2$). De la primera $y = 2x$; sustituyendo en la segunda $z = x + y = 3x$. Tomando $x=1$:

$$\boxed{N(T) = \langle (1,\ 2,\ 3)\rangle,\qquad \dim N(T) = 1.}$$

(Verificación: $T(1,2,3) = (2-2,\ 1+2-3,\ 3-1-2) = (0,0,0)$ ✓.)

**Imagen.** Por el teorema de la dimensión, $\dim \operatorname{Im}(T) = 3 - \dim N(T) = 2$. La imagen es el espacio columna; como las dos primeras columnas $(2,1,-1)$ y $(-1,1,-1)$ son LI,

$$\operatorname{Im}(T) = \langle (2,\ 1,\ -1),\ (-1,\ 1,\ -1)\rangle.$$

Conviene describirla por una ecuación. Observemos que la **segunda y tercera componentes** de $T$ son opuestas para todo $(x,y,z)$:

$$(x+y-z) + (z-x-y) = 0,$$

luego toda imagen $(u,v,w)=T(x,y,z)$ cumple $v + w = 0$. Como es un plano (dim 2) y la imagen tiene dim 2,

$$\boxed{\operatorname{Im}(T) = \{(u,v,w)\in\mathbb{R}^3 : v + w = 0\},\qquad \dim\operatorname{Im}(T)=2.}$$

**b) ¿Diagonalizable en $\mathbb{R}$?** Polinomio característico $p_A(\lambda) = \det(\lambda I - A)$ (convención de la cátedra, coef. líder $+1$):

$$\lambda I - A = \begin{pmatrix} \lambda - 2 & 1 & 0 \\ -1 & \lambda - 1 & 1 \\ 1 & 1 & \lambda - 1 \end{pmatrix}.$$

Desarrollando (sabiendo ya que $\lambda = 0$ es raíz porque $\det A = 0$):

$$p_A(\lambda) = \lambda^3 - 4\lambda^2 + 5\lambda = \lambda\,(\lambda^2 - 4\lambda + 5).$$

El factor cuadrático tiene discriminante $\Delta = 16 - 20 = -4 < 0$, con raíces

$$\lambda = \frac{4 \pm \sqrt{-4}}{2} = 2 \pm i.$$

Así, los autovalores son

$$\boxed{\lambda_1 = 0,\qquad \lambda_{2,3} = 2 \pm i\ \ (\text{complejos conjugados}).}$$

Para ser diagonalizable **en $\mathbb{R}$** se necesitan $3$ autovalores reales (con $m_g=m_a$ en cada uno). Aquí dos autovalores son **complejos no reales**, de modo que $A$ no tiene una base de autovectores en $\mathbb{R}^3$.

$$\boxed{T \text{ NO es diagonalizable en } \mathbb{R}\ \text{(es diagonalizable en } \mathbb{C}\text{, pues los tres autovalores son distintos).}}$$

> Sutileza: el obstáculo aquí **no** es una multiplicidad geométrica deficiente (autovalor repetido), como en otros temas, sino la aparición de autovalores complejos. Sobre $\mathbb{C}$ sí sería diagonalizable porque $0$, $2+i$, $2-i$ son simples.

**Verificación numérica.** `numpy`: $\det A = 0$, $\operatorname{rg}(A)=2$, núcleo $\propto (1,2,3)$; `np.poly(A)` da coeficientes $(1,-4,5,0)$, es decir $\lambda^3-4\lambda^2+5\lambda$, y `eig` devuelve autovalores $\{0,\ 2+i,\ 2-i\}$ ✓.

## Ejercicio 2

a) Hallar el desarrollo en serie de Fourier de la función $f(x) = 1 - x$ con $f(x) = f(x + 1)$ (período $T=1$).
b) Indique a qué converge la serie en $x = 0$ y $x = \dfrac{1}{2}$.

### Resolución

Es la onda "diente de sierra" de período $T=1$: en cada celda $[0,1)$ vale $1-x$, que va de $f(0^+)=1$ a $f(1^-)=0$, y luego salta de vuelta a $1$. La frecuencia fundamental es $\omega_0 = \tfrac{2\pi}{T} = 2\pi$. Usamos la convención de la cátedra:

$$f(x) = a_0 + \sum_{n=1}^{\infty} a_n\cos(2\pi n x) + \sum_{n=1}^{\infty} b_n\sin(2\pi n x),$$

con $a_0 = \tfrac1T\int_T f$ (valor medio), $a_n = \tfrac2T\int_T f\cos(2\pi n x)\,dx$, $b_n = \tfrac2T\int_T f\sin(2\pi n x)\,dx$.

**Término constante (valor medio).**

$$a_0 = \int_0^1 (1-x)\,dx = \left[x - \tfrac{x^2}{2}\right]_0^1 = 1 - \tfrac12 = \frac12.$$

**Coeficientes coseno.** Con $\int_0^1 \cos(2\pi n x)\,dx = 0$ y, por partes, $\int_0^1 x\cos(2\pi n x)\,dx = 0$ (porque $\sin(2\pi n)=0$ y los términos de borde se cancelan):

$$a_n = 2\int_0^1 (1-x)\cos(2\pi n x)\,dx = 0\qquad (n\ge 1).$$

**Coeficientes seno.** Con $\int_0^1 \sin(2\pi n x)\,dx = 0$ y $\displaystyle\int_0^1 x\sin(2\pi n x)\,dx = -\frac{1}{2\pi n}$ (integración por partes; usa $\cos(2\pi n)=1$, $\sin(2\pi n)=0$):

$$b_n = 2\int_0^1 (1-x)\sin(2\pi n x)\,dx = 2\Big(\underbrace{\textstyle\int_0^1\sin(2\pi n x)dx}_{0} - \underbrace{\textstyle\int_0^1 x\sin(2\pi n x)dx}_{-1/(2\pi n)}\Big) = 2\cdot\frac{1}{2\pi n} = \frac{1}{\pi n}.$$

(El signo importa: el aporte de $-x$ es positivo, y da $b_n>0$.)

$$\boxed{f(x) = \frac12 + \sum_{n=1}^{\infty} \frac{1}{\pi n}\,\sin(2\pi n x).}$$

**Verificación numérica.** Integrando con `scipy.quad`: $a_0=0.5$, $a_n\approx 0$ y $b_n = \{0.31831, 0.15915, 0.10610,\dots\}$, que coincide con $\tfrac{1}{\pi n}=\{1/\pi,\ 1/2\pi,\ 1/3\pi,\dots\}$. Simbólicamente (`sympy`, $n$ entero) $a_n=0$, $b_n = \tfrac{1}{\pi n}$ exacto ✓.

**b) Convergencia puntual (Dirichlet).**

- En $x = \tfrac12$ la función es **continua** (estamos en el interior de la celda, $f$ es lineal allí), así que la serie converge al valor de la función:
  $$\boxed{S\!\left(\tfrac12\right) = f\!\left(\tfrac12\right) = 1 - \tfrac12 = \frac12.}$$
  Además, como todos los senos valen $\sin(\pi n)=0$ en $x=\tfrac12$, la serie da directamente $a_0 = \tfrac12$, consistente.

- En $x = 0$ hay un **salto** (extremo de la celda): por la izquierda $f(0^-) = f(1^-) = 0$ y por la derecha $f(0^+) = 1$. La serie converge al **promedio**:
  $$\boxed{S(0) = \tfrac12\big(f(0^+) + f(0^-)\big) = \tfrac12(1 + 0) = \frac12.}$$
  (También coincide con $a_0=\tfrac12$, ya que $\sin(0)=0$.)

**Verificación numérica.** Las sumas parciales $S_N$ con $N=10,100,1000,5000$ dan $S(0)\to 0.5$ y $S(\tfrac12)\to 0.5$ ✓ (en $x=0$ persiste el overshoot de Gibbs alrededor del salto, pero el valor exacto en el punto es $\tfrac12$).

## Ejercicio 3

Considere la EDO

$$\frac{d^2 x}{dt^2} + 2\frac{dx}{dt} + x = e^{-t^2},\qquad x(0) = x'(0).$$

a) Escriba la ecuación como un sistema de orden 1.
b) Plantee un esquema implícito de diferencias finitas. Indique cómo implementa las condiciones iniciales.

### Resolución

**a) Reducción a primer orden.** Definimos las variables de estado

$$x_1 = x,\qquad x_2 = \dot x.$$

Entonces $\dot x_1 = x_2$ y, despejando $\ddot x$ de la EDO ($\ddot x = e^{-t^2} - 2\dot x - x$),

$$\boxed{\begin{cases} \dot x_1 = x_2, \\[2pt] \dot x_2 = e^{-t^2} - 2 x_2 - x_1. \end{cases}}$$

En forma matricial $\dot{\mathbf x} = M\mathbf x + \mathbf f(t)$, con

$$\mathbf x = \begin{pmatrix} x_1 \\ x_2\end{pmatrix},\qquad M = \begin{pmatrix} 0 & 1 \\ -1 & -2 \end{pmatrix},\qquad \mathbf f(t) = \begin{pmatrix} 0 \\ e^{-t^2}\end{pmatrix}.$$

Es un sistema **lineal** (matriz $M$ constante) con un término forzante no lineal en $t$ pero independiente de $\mathbf x$. Esto es clave: el esquema implícito quedará lineal.

**b) Esquema implícito (Euler hacia atrás).** Tomamos paso temporal $\Delta t$ y nodos $t_k = k\,\Delta t$, $\mathbf x^k \approx \mathbf x(t_k)$. Euler implícito aproxima la derivada con la diferencia hacia atrás y evalúa el lado derecho en el nivel **nuevo** $k+1$:

$$\frac{\mathbf x^{k+1} - \mathbf x^{k}}{\Delta t} = M\,\mathbf x^{k+1} + \mathbf f(t_{k+1}).$$

Reagrupando las incógnitas $\mathbf x^{k+1}$ a la izquierda:

$$\boxed{(I - \Delta t\, M)\,\mathbf x^{k+1} = \mathbf x^{k} + \Delta t\,\mathbf f(t_{k+1}),}$$

que en componentes es el sistema lineal $2\times 2$ por paso

$$\begin{pmatrix} 1 & -\Delta t \\ \Delta t & 1 + 2\,\Delta t \end{pmatrix}\begin{pmatrix} x_1^{k+1} \\ x_2^{k+1} \end{pmatrix} = \begin{pmatrix} x_1^{k} \\ x_2^{k} + \Delta t\, e^{-t_{k+1}^2} \end{pmatrix}.$$

El determinante de la matriz del sistema es $\det(I-\Delta t\,M) = (1)(1+2\Delta t) - (-\Delta t)(\Delta t) = 1 + 2\Delta t + \Delta t^2 = (1+\Delta t)^2 > 0$ para todo $\Delta t > 0$, así que el paso siempre tiene solución única (esquema bien definido e incondicionalmente estable para esta EDO disipativa). Cada paso se resuelve, por ejemplo, despejando

$$x_1^{k+1} = \frac{(1+2\Delta t)\,x_1^{k} + \Delta t\,\big(x_2^{k} + \Delta t\,e^{-t_{k+1}^2}\big)}{(1+\Delta t)^2},\qquad x_2^{k+1} = \frac{x_2^{k} + \Delta t\,e^{-t_{k+1}^2} - \Delta t\,x_1^{k}}{(1+\Delta t)^2}.$$

**Condiciones iniciales.** El dato es $x(0) = x'(0)$: el enunciado fija que la posición y la velocidad iniciales **coinciden**, pero no da su valor común. Llamemos $c$ a ese valor (constante dada del problema). Entonces

$$\boxed{x_1^{0} = x(0) = c,\qquad x_2^{0} = x'(0) = c.}$$

Es decir, el vector de arranque es $\mathbf x^0 = (c,\ c)^T$. Con un único vector inicial alcanza para arrancar la recursión de Euler implícito (a diferencia de un esquema de 2 niveles para la onda, aquí solo hace falta $\mathbf x^0$). Si en el examen se diera un valor numérico (p. ej. $c=0$, reposo desde el origen, o $c=1$), simplemente se sustituye. Conocido $\mathbf x^0$, se itera $k=0,1,2,\dots$ resolviendo el sistema $2\times2$ anterior en cada paso.

**Verificación numérica.** Implementé el esquema con $\Delta t = 0.1$ y $c=0$: la matriz $I-\Delta t\,M = \begin{pmatrix}1 & -0.1\\ 0.1 & 1.2\end{pmatrix}$ tiene $\det = 1.21 = (1.1)^2$ ✓; integrando hasta $t=2$ da $x(2)\approx 0.259$, frente a $0.285$ de una solución de referencia (`solve_ivp` RK de alta precisión). La diferencia ($\sim 0.026$) es el error de Euler implícito de orden 1 con paso grueso; al refinar $\Delta t$ converge, confirmando que el planteo es correcto.

## Ejercicio 4

Hallar la Transformada de Fourier de $f(t) = (t-1)^2$ si $0 \le t \le 1$, y $f(t) = 0$ en otro caso.

### Resolución

Convención de la cátedra: $\displaystyle \hat f(\omega) = \int_{-\infty}^{\infty} f(t)\,e^{-i\omega t}\,dt$. Como el soporte es $[0,1]$,

$$\hat f(\omega) = \int_0^1 (t-1)^2\, e^{-i\omega t}\,dt.$$

**Cambio de variable** $s = t-1$ (así $ds=dt$, $t:0\to1 \Rightarrow s:-1\to0$ y $e^{-i\omega t} = e^{-i\omega(s+1)} = e^{-i\omega}e^{-i\omega s}$):

$$\hat f(\omega) = e^{-i\omega}\int_{-1}^{0} s^2\, e^{-i\omega s}\,ds.$$

**Integral por partes dos veces** (o usando $\int s^2 e^{as}ds = e^{as}\big(\tfrac{s^2}{a} - \tfrac{2s}{a^2} + \tfrac{2}{a^3}\big)$ con $a=-i\omega$). Para $\omega \ne 0$:

$$\int_{-1}^0 s^2 e^{-i\omega s}\,ds = \left[e^{-i\omega s}\left(\frac{s^2}{-i\omega} - \frac{2s}{(-i\omega)^2} + \frac{2}{(-i\omega)^3}\right)\right]_{-1}^{0}.$$

Evaluando en $s=0$ y $s=-1$ (con $(-i\omega)^2=-\omega^2$, $(-i\omega)^3 = i\omega^3$) y multiplicando por $e^{-i\omega}$ se obtiene, tras simplificar:

$$\boxed{\hat f(\omega) = -\frac{i}{\omega} + \frac{2}{\omega^2} + \frac{2i}{\omega^3}\left(1 - e^{-i\omega}\right),\qquad \omega \neq 0.}$$

**Caso $\omega = 0$.** La transformada en $\omega=0$ es el área bajo $f$:

$$\hat f(0) = \int_0^1 (t-1)^2\,dt = \left[\frac{(t-1)^3}{3}\right]_0^1 = 0 - \left(-\frac13\right) = \frac13.$$

Es el límite $\lim_{\omega\to0}\hat f(\omega)$ (las singularidades aparentes $1/\omega$, $1/\omega^2$, $1/\omega^3$ se cancelan al desarrollar $1-e^{-i\omega} = i\omega + \tfrac{\omega^2}{2} - \cdots$), de modo que $\hat f$ es de hecho continua en $\omega=0$.

$$\boxed{\hat f(0) = \frac13.}$$

**Verificación numérica.** Comparé la fórmula cerrada contra integración directa de $\int_0^1 (t-1)^2 e^{-i\omega t}dt$ en varios $\omega$:

| $\omega$ | $\hat f(\omega)$ (fórmula = numérico) |
|---|---|
| $0$ | $0.3333$ |
| $0.5$ | $0.3292 - 0.0413\,i$ |
| $1$ | $0.3171 - 0.0806\,i$ |
| $2$ | $0.2727 - 0.1460\,i$ |
| $5$ | $0.0953 - 0.1885\,i$ |
| $-3$ | $0.2118 + 0.1859\,i$ |

La diferencia entre fórmula y cuadratura numérica es $\sim 10^{-16}$ en todos los casos, y `sympy` confirma $\lim_{\omega\to0}\hat f(\omega) = 1/3$ ✓.

---

## Resumen de resultados

| Ej. | Resultado |
|---|---|
| 1a | $N(T)=\langle(1,2,3)\rangle$ (dim 1); $\operatorname{Im}(T)=\{v+w=0\}=\langle(2,1,-1),(-1,1,-1)\rangle$ (dim 2) |
| 1b | Autovalores $0,\ 2\pm i$ → **no** diagonalizable en $\mathbb{R}$ (sí en $\mathbb{C}$) |
| 2a | $f(x)=\tfrac12+\sum_{n\ge1}\tfrac{1}{\pi n}\sin(2\pi n x)$ |
| 2b | $S(0)=\tfrac12$ (promedio del salto); $S(\tfrac12)=\tfrac12$ (continuidad) |
| 3 | $\dot x_1=x_2,\ \dot x_2=e^{-t^2}-2x_2-x_1$; Euler implícito $(I-\Delta t M)\mathbf x^{k+1}=\mathbf x^k+\Delta t\,\mathbf f^{k+1}$; CI $\mathbf x^0=(c,c)$ |
| 4 | $\hat f(\omega)=-\tfrac{i}{\omega}+\tfrac{2}{\omega^2}+\tfrac{2i}{\omega^3}(1-e^{-i\omega})$, $\ \hat f(0)=\tfrac13$ |
