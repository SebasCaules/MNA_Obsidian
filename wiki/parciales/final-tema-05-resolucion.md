---
tags: [final, resolucion, transformaciones-lineales, nucleo-imagen, diagonalizacion, autovalores, fourier-series, diferencias-finitas, ecuacion-calor, neumann, transformada-fourier]
fuente: raw/Practicas/Modelos_Examenes/MNA_Final_Tema_V.pdf
tipo: final
tema: 5
tiene_resolucion: true
---

# Examen Final de Métodos Numéricos Avanzados — Tema V (Resolución)

Enunciado original sin resolver en [[final-tema-05]]. Referencias de método: [[../guias/guia-08-fourier-series]], [[../resueltos/resueltos-fourier]].

## Ejercicio 1

Dada la TL $T : \mathbb{R}^3 \to \mathbb{R}^3 : T(x, y, z) = (2x,\ x + y - z,\ 2z + y)$.

a) Hallar el Núcleo y la Imagen.
b) Decidir si es o no diagonalizable en $\mathbb{R}$.

### Resolución

Las columnas de $M_{EE}(T)$ son las imágenes de la base canónica:

$$T(e_1) = T(1,0,0) = (2,1,0),\quad T(e_2) = T(0,1,0) = (0,1,1),\quad T(e_3) = T(0,0,1) = (0,-1,2).$$

$$M_{EE}(T) = A = \begin{pmatrix} 2 & 0 & 0 \\ 1 & 1 & -1 \\ 0 & 1 & 2 \end{pmatrix}.$$

**a) Núcleo e Imagen.** Calculamos el determinante desarrollando por la primera fila:

$$\det A = 2\cdot\begin{vmatrix} 1 & -1 \\ 1 & 2 \end{vmatrix} = 2\,(2 - (-1)) = 2\cdot 3 = 6 \ne 0.$$

Como $\det A = 6 \ne 0$, la matriz es inversible, así que $T$ es un **isomorfismo**. Por lo tanto:

$$\boxed{N(T) = \{(0,0,0)\}\quad (\dim N(T) = 0), \qquad \text{Im}(T) = \mathbb{R}^3\quad (\dim \text{Im}(T) = 3).}$$

(Consistente con el teorema de la dimensión: $\dim N(T) + \dim \text{Im}(T) = 0 + 3 = 3 = \dim \mathbb{R}^3$.)

**b) ¿Diagonalizable en $\mathbb{R}$?** Polinomio característico con la convención de la cátedra $p_A(\lambda) = \det(\lambda I - A)$:

$$\lambda I - A = \begin{pmatrix} \lambda - 2 & 0 & 0 \\ -1 & \lambda - 1 & 1 \\ 0 & -1 & \lambda - 2 \end{pmatrix}.$$

Desarrollando por la primera fila (solo el primer elemento es no nulo):

$$p_A(\lambda) = (\lambda - 2)\begin{vmatrix} \lambda - 1 & 1 \\ -1 & \lambda - 2 \end{vmatrix} = (\lambda - 2)\big[(\lambda-1)(\lambda-2) + 1\big].$$

$$(\lambda-1)(\lambda-2) + 1 = \lambda^2 - 3\lambda + 2 + 1 = \lambda^2 - 3\lambda + 3.$$

$$\boxed{p_A(\lambda) = (\lambda - 2)\,(\lambda^2 - 3\lambda + 3).}$$

El factor lineal da el autovalor real $\lambda = 2$. Para el factor cuadrático calculamos el discriminante:

$$\Delta = (-3)^2 - 4\cdot 1\cdot 3 = 9 - 12 = -3 < 0,$$

así que $\lambda^2 - 3\lambda + 3$ tiene raíces **complejas conjugadas** $\lambda = \tfrac{3}{2} \pm \tfrac{\sqrt 3}{2}\,i$, **no reales**.

Sobre $\mathbb{R}$ el polinomio característico no se factoriza completamente en factores lineales (solo hay un autovalor real, $\lambda = 2$, con $m_a = 1$). Como el polinomio característico no se escinde en $\mathbb{R}$, **$T$ no es diagonalizable en $\mathbb{R}$**.

$$\boxed{T \text{ NO es diagonalizable en } \mathbb{R}.}$$

> **Punto sutil.** El único autovalor real $\lambda = 2$ es simple ($m_a = m_g = 1$), así que el problema no está en una multiplicidad geométrica chica: está en que faltan autovalores reales. Sobre $\mathbb{C}$ sí sería diagonalizable (tres autovalores distintos: $2$, $\tfrac32 + \tfrac{\sqrt3}{2}i$, $\tfrac32 - \tfrac{\sqrt3}{2}i$). La pregunta dice explícitamente "en $\mathbb{R}$", y ahí la respuesta es negativa.

**Verificación numérica** (numpy). `np.linalg.det(A) = 6.0`, `matrix_rank(A) = 3` (confirma $N(T)=\{0\}$, $\text{Im}(T)=\mathbb{R}^3$). `np.linalg.eig(A)` devuelve autovalores $\{2,\ 1.5 + 0.8660\,i,\ 1.5 - 0.8660\,i\}$ y `sympy.factor` da $p_A(\lambda) = (\lambda-2)(\lambda^2 - 3\lambda + 3)$. Solo uno es real $\Rightarrow$ no diagonalizable en $\mathbb{R}$. ✓

## Ejercicio 2

a) Hallar el desarrollo en serie de Fourier de $f : [0, 1] \to \mathbb{R} : f(x) = 1 - x^2$, con $f(x) = f(x + 1)$ (período $T = 1$).
b) Indicar a qué converge la serie en $x = 0$ y $x = \tfrac{1}{2}$.

### Resolución

**a) Coeficientes.** Con $T = 1$, $\tfrac{2\pi n}{T} = 2\pi n$. Usamos la convención de la cátedra:

$$f(x) = a_0 + \sum_{n=1}^{\infty} a_n\cos(2\pi n x) + \sum_{n=1}^{\infty} b_n\sin(2\pi n x),$$

$$a_0 = \frac{1}{T}\int_0^1 f\,dx,\qquad a_n = \frac{2}{T}\int_0^1 f\cos(2\pi n x)\,dx,\qquad b_n = \frac{2}{T}\int_0^1 f\sin(2\pi n x)\,dx.$$

**Término constante** $a_0$ (valor medio, NO dividido por 2):

$$a_0 = \int_0^1 (1 - x^2)\,dx = \Big[x - \tfrac{x^3}{3}\Big]_0^1 = 1 - \tfrac13 = \boxed{\tfrac{2}{3}}.$$

**Coeficientes coseno** $a_n = 2\displaystyle\int_0^1 (1-x^2)\cos(2\pi n x)\,dx$. Separamos:

$$a_n = 2\underbrace{\int_0^1 \cos(2\pi n x)\,dx}_{=\,0} - 2\int_0^1 x^2\cos(2\pi n x)\,dx.$$

La primera integral es $0$ (un período completo del coseno). Para la segunda, integrando dos veces por partes con $\omega_n = 2\pi n$:

$$\int_0^1 x^2\cos(\omega_n x)\,dx = \left[\frac{x^2\sin(\omega_n x)}{\omega_n} + \frac{2x\cos(\omega_n x)}{\omega_n^2} - \frac{2\sin(\omega_n x)}{\omega_n^3}\right]_0^1.$$

En $x=1$: $\sin(2\pi n) = 0$ y $\cos(2\pi n) = 1$, en $x=0$ todo se anula salvo el término $\tfrac{2x\cos}{\omega_n^2}$ que da $0$. Queda solo el término del medio:

$$\int_0^1 x^2\cos(\omega_n x)\,dx = \frac{2\cdot 1\cdot 1}{\omega_n^2} = \frac{2}{(2\pi n)^2} = \frac{1}{2\pi^2 n^2}.$$

$$a_n = -2\cdot \frac{1}{2\pi^2 n^2} = \boxed{-\frac{1}{\pi^2 n^2}}.$$

**Coeficientes seno** $b_n = 2\displaystyle\int_0^1 (1-x^2)\sin(2\pi n x)\,dx$. Separamos:

$$b_n = 2\underbrace{\int_0^1 \sin(2\pi n x)\,dx}_{=\,0} - 2\int_0^1 x^2\sin(\omega_n x)\,dx.$$

Otra vez la primera integral es $0$. Integrando por partes la segunda:

$$\int_0^1 x^2\sin(\omega_n x)\,dx = \left[-\frac{x^2\cos(\omega_n x)}{\omega_n} + \frac{2x\sin(\omega_n x)}{\omega_n^2} + \frac{2\cos(\omega_n x)}{\omega_n^3}\right]_0^1.$$

En $x=1$ ($\cos(2\pi n)=1$, $\sin(2\pi n)=0$): $-\tfrac{1}{\omega_n} + \tfrac{2}{\omega_n^3}$. En $x=0$: $+\tfrac{2}{\omega_n^3}$. Restando:

$$\int_0^1 x^2\sin(\omega_n x)\,dx = -\frac{1}{\omega_n} + \frac{2}{\omega_n^3} - \frac{2}{\omega_n^3} = -\frac{1}{\omega_n} = -\frac{1}{2\pi n}.$$

$$b_n = -2\cdot\left(-\frac{1}{2\pi n}\right) = \boxed{\frac{1}{\pi n}}.$$

> **Punto sutil (signos).** El $b_n$ NO se anula: aunque $f(x)=1-x^2$ es par como función "limpia", al periodizarla con período $1$ sobre $[0,1]$ la extensión periódica **no** tiene simetría par respecto del origen, así que aparecen senos. Conviene cuidar los signos: $\int_0^1 \sin = \int_0^1 \cos = 0$ matan la parte del "$1$", y el resto viene de $-x^2$.

**Serie resultante:**

$$\boxed{f(x) = \frac{2}{3} - \frac{1}{\pi^2}\sum_{n=1}^{\infty}\frac{\cos(2\pi n x)}{n^2} + \frac{1}{\pi}\sum_{n=1}^{\infty}\frac{\sin(2\pi n x)}{n}.}$$

**b) Convergencia (criterio de Dirichlet).** La extensión periódica empalma $f(1^-) = 1 - 1^2 = 0$ con $f(0^+) = 1 - 0 = 1$, así que en los enteros (en particular $x=0$) hay un **salto**.

- En $x = 0$ (punto de discontinuidad por salto): la serie converge al promedio de los límites laterales,
$$S(0) = \frac{f(0^+) + f(1^-)}{2} = \frac{1 + 0}{2} = \boxed{\tfrac{1}{2}}.$$
- En $x = \tfrac{1}{2}$ (punto interior, $f$ es continua ahí): la serie converge al valor de la función,
$$S\!\left(\tfrac{1}{2}\right) = f\!\left(\tfrac{1}{2}\right) = 1 - \tfrac{1}{4} = \boxed{\tfrac{3}{4}}.$$

**Verificación numérica.** Integración numérica (`scipy.quad`) da $a_0 = 0.66667 = \tfrac23$, $a_1 = -0.101321 = -\tfrac{1}{\pi^2}$, $b_1 = 0.318310 = \tfrac{1}{\pi}$, $a_2 = -\tfrac{1}{4\pi^2}$, $b_2 = \tfrac{1}{2\pi}$ (coinciden para $n=1,\dots,4$). Sumas parciales: con $N=5000$ términos $S(0) \to 0.50002 \approx \tfrac12$, $S(0.5) \to 0.75000 = \tfrac34$, y en un punto de continuidad cualquiera $S(0.25) \to 0.93747 \approx f(0.25) = \tfrac{15}{16}$. ✓

## Ejercicio 3

Dada la ecuación del calor $\dfrac{\partial u}{\partial t} = \dfrac{\partial^2 u}{\partial x^2}$, desarrollar un esquema de diferencias finitas **implícito** con 4 nodos internos para:

a) $u(0, t) = u(1, t) = 0$ (Dirichlet homogéneo) y $u(x, 0) = \operatorname{sen}(x)$.
b) $u_x(0, t) = u_x(1, t) = 0$ (Neumann en ambos bordes) y $u(x, 0) = |x|$.

### Resolución

**Malla.** Dominio $x \in [0,1]$ con 4 nodos internos $\Rightarrow$ $h = \tfrac{1}{5} = 0.2$, nodos $x_0 = 0,\ x_1 = 0.2,\ x_2 = 0.4,\ x_3 = 0.6,\ x_4 = 0.8,\ x_5 = 1$. Notación $u_i^k \approx u(x_i, t_k)$, paso temporal $\Delta t$.

**Discretización (Euler implícito / hacia atrás en tiempo).** Evaluando $u_{xx}$ en el nivel $k+1$:

$$\frac{u_i^{k+1} - u_i^k}{\Delta t} = \frac{u_{i-1}^{k+1} - 2u_i^{k+1} + u_{i+1}^{k+1}}{h^2}.$$

Con $r = \dfrac{\Delta t}{h^2}$, reordenando para dejar las incógnitas (nivel $k+1$) a la izquierda:

$$-r\,u_{i-1}^{k+1} + (1 + 2r)\,u_i^{k+1} - r\,u_{i+1}^{k+1} = u_i^k.$$

#### a) Dirichlet homogéneo

Los bordes son **datos conocidos**: $u_0^{k+1} = u_5^{k+1} = 0$. Al ser nulos, no aportan nada al lado derecho. Las incógnitas son los 4 nodos internos $u_1, u_2, u_3, u_4$. Escribiendo la ecuación para $i = 1,2,3,4$ (y borrando los términos de borde nulos) se obtiene un sistema tridiagonal $4\times 4$:

$$M\,\mathbf{u}^{k+1} = \mathbf{u}^k,\qquad
M = \begin{pmatrix}
1+2r & -r & 0 & 0 \\
-r & 1+2r & -r & 0 \\
0 & -r & 1+2r & -r \\
0 & 0 & -r & 1+2r
\end{pmatrix},\qquad
\mathbf{u}^{k+1} = \begin{pmatrix} u_1^{k+1} \\ u_2^{k+1} \\ u_3^{k+1} \\ u_4^{k+1} \end{pmatrix}.$$

El lado derecho es $\mathbf{u}^k = (u_1^k, u_2^k, u_3^k, u_4^k)^T$ (la solución del paso anterior). El **vector de condición inicial** $u_i^0 = \operatorname{sen}(x_i)$ con $x_i = 0.2,\dots,0.8$:

$$\mathbf{u}^0 = \begin{pmatrix} \operatorname{sen}(0.2) \\ \operatorname{sen}(0.4) \\ \operatorname{sen}(0.6) \\ \operatorname{sen}(0.8) \end{pmatrix} \approx \begin{pmatrix} 0.19867 \\ 0.38942 \\ 0.56464 \\ 0.71736 \end{pmatrix}.$$

> **Atención al argumento.** La condición inicial es $\operatorname{sen}(x)$ en **radianes** del valor $x_i$, no $\operatorname{sen}(\pi x_i)$. Se evalúa directamente en $x_i \in \{0.2, 0.4, 0.6, 0.8\}$. Además los datos de borde de Dirichlet ($u_0^0 = u_5^0 = 0$) son compatibles: $\operatorname{sen}(0) = 0$ en $x_0$, y aunque $\operatorname{sen}(1) \approx 0.841 \ne 0$ en $x_5$, la condición de borde $u(1,t)=0$ tiene prioridad para $t > 0$ (basta tomar $u_5^k = 0$).

Cada paso: se resuelve $M\,\mathbf{u}^{k+1} = \mathbf{u}^k$.

#### b) Neumann en ambos bordes

Ahora $u_x(0,t) = u_x(1,t) = 0$. La clave: con Neumann **los nodos de borde son incógnitas** (no hay valor prescrito de $u$). Para cerrar el esquema en $x_0$ y $x_5$ se usan **nodos fantasma** y se discretiza la derivada con diferencias centradas:

- En $x_0$: $u_x(0,t) \approx \dfrac{u_1^{k+1} - u_{-1}^{k+1}}{2h} = 0 \Rightarrow u_{-1}^{k+1} = u_1^{k+1}$.
- En $x_5$: $u_x(1,t) \approx \dfrac{u_6^{k+1} - u_4^{k+1}}{2h} = 0 \Rightarrow u_6^{k+1} = u_4^{k+1}$.

Aplicando la ecuación general en el nodo $i=0$ (que incluye el fantasma $u_{-1}$) y sustituyendo $u_{-1}^{k+1} = u_1^{k+1}$:

$$-r\,u_{-1}^{k+1} + (1+2r)u_0^{k+1} - r\,u_1^{k+1} = u_0^k \;\Longrightarrow\; (1+2r)u_0^{k+1} - 2r\,u_1^{k+1} = u_0^k.$$

Análogamente en $i=5$ con $u_6^{k+1} = u_4^{k+1}$:

$$(1+2r)u_5^{k+1} - 2r\,u_4^{k+1} = u_5^k.$$

Las incógnitas pasan a ser **los 6 nodos** $u_0, u_1, u_2, u_3, u_4, u_5$. El sistema es $6\times 6$:

$$M\,\mathbf{u}^{k+1} = \mathbf{u}^k,\qquad
M = \begin{pmatrix}
1+2r & -2r & 0 & 0 & 0 & 0 \\
-r & 1+2r & -r & 0 & 0 & 0 \\
0 & -r & 1+2r & -r & 0 & 0 \\
0 & 0 & -r & 1+2r & -r & 0 \\
0 & 0 & 0 & -r & 1+2r & -r \\
0 & 0 & 0 & 0 & -2r & 1+2r
\end{pmatrix}.$$

Notar el $-2r$ (no $-r$) en la primera y última fila: es la huella del nodo fantasma. La matriz es simétrica pero **deja de ser de Toeplitz** en los extremos. El lado derecho es $\mathbf{u}^k = (u_0^k,\dots,u_5^k)^T$, y el **vector de condición inicial** sale de $u(x,0) = |x|$; como en $[0,1]$ se tiene $|x| = x$, resulta $u_i^0 = x_i$:

$$\mathbf{u}^0 = \begin{pmatrix} |x_0| \\ |x_1| \\ |x_2| \\ |x_3| \\ |x_4| \\ |x_5| \end{pmatrix} = \begin{pmatrix} 0 \\ 0.2 \\ 0.4 \\ 0.6 \\ 0.8 \\ 1.0 \end{pmatrix}.$$

> **Puntos sutiles.** (1) Con Neumann en **ambos** bordes el sistema crece a $6\times 6$ (no $4\times 4$): los dos extremos son incógnitas. (2) $|x| = x$ en todo $[0,1]$ porque ahí $x \ge 0$ — el valor absoluto no introduce ningún quiebre en el dominio. (3) Físicamente Neumann homogéneo en ambos bordes = bordes aislados (flujo nulo), así que la "masa" total $\sum_i u_i$ debería conservarse en el tiempo.

**Verificación numérica.** Con $r=1$ y un paso implícito: $\det M_a = 55 \ne 0$ y $\det M_b = 275 \ne 0$ (ambos sistemas bien planteados, $M$ es diagonalmente dominante). Para (b) la suma se conserva: $\sum u_i^0 = 3.0$ y tras un paso $\sum u_i^1 = 3.0$ (consistente con borde aislado / Neumann homogéneo). Los vectores CI computados coinciden con los reportados: $\mathbf u^0_{(a)} = (0.19867, 0.38942, 0.56464, 0.71736)$, $\mathbf u^0_{(b)} = (0, 0.2, 0.4, 0.6, 0.8, 1.0)$. ✓

## Ejercicio 4

Hallar la Transformada de Fourier de $f(t) = e^{-|t - 1|}$ si $0 \le t \le 1$, y $f(t) = 0$ en otro caso.

### Resolución

**Simplificación del soporte.** En el intervalo $[0,1]$ se tiene $t \le 1$, luego $t - 1 \le 0$ y por lo tanto $|t - 1| = 1 - t$. Entonces, dentro del soporte:

$$f(t) = e^{-(1 - t)} = e^{t - 1},\qquad 0 \le t \le 1.$$

> **Punto sutil.** El valor absoluto se "abre" usando el signo de $t-1$ en el dominio dado. Como solo integramos sobre $[0,1]$ (soporte compacto), no hace falta partir en casos: ahí siempre es $1-t \ge 0$.

**Definición (convención de la cátedra)** $\hat f(\omega) = \displaystyle\int_{-\infty}^{\infty} f(t)\,e^{-i\omega t}\,dt$. Como $f$ se anula fuera de $[0,1]$, integramos solo sobre el soporte:

$$\hat f(\omega) = \int_0^1 e^{t-1}\,e^{-i\omega t}\,dt = e^{-1}\int_0^1 e^{(1 - i\omega)t}\,dt.$$

Resolviendo la integral (con $1 - i\omega \ne 0$, es decir $\omega$ finito):

$$\int_0^1 e^{(1 - i\omega)t}\,dt = \left.\frac{e^{(1-i\omega)t}}{1 - i\omega}\right|_0^1 = \frac{e^{1 - i\omega} - 1}{1 - i\omega}.$$

Por lo tanto:

$$\boxed{\hat f(\omega) = e^{-1}\,\frac{e^{1 - i\omega} - 1}{1 - i\omega} = \frac{e^{-i\omega} - e^{-1}}{1 - i\omega},}$$

donde la última igualdad usa $e^{-1}e^{1 - i\omega} = e^{-i\omega}$.

**Caso $\omega = 0$.** La fórmula tiene la forma $\tfrac{0}{0}$ en apariencia, pero se obtiene directo de la integral:

$$\hat f(0) = \int_0^1 e^{t-1}\,dt = e^{-1}\big[e^t\big]_0^1 = e^{-1}(e - 1) = 1 - e^{-1} \approx 0.63212.$$

(Coincide con tomar el límite $\omega \to 0$ de la fórmula por L'Hôpital.)

**Parte real e imaginaria** (multiplicando numerador y denominador por el conjugado $1 + i\omega$, y usando $e^{-i\omega} = \cos\omega - i\sin\omega$):

$$\operatorname{Re}\hat f(\omega) = \frac{e^{-1}\big(\omega\sin\omega + \cos\omega - e^{-1}\big)}{1 + \omega^2}\cdot e,\quad\text{equivalentemente}\quad \operatorname{Re}\hat f(\omega) = \frac{\cos\omega + \omega\sin\omega - e^{-1}}{1 + \omega^2},$$

$$\operatorname{Im}\hat f(\omega) = \frac{-\sin\omega + \omega\cos\omega - \omega\, e^{-1}}{1 + \omega^2}.$$

**Verificación numérica.** Para $\omega \in \{0.5, 1, 2, 3, -1.5\}$ la fórmula cerrada coincide con la integral numérica (`scipy.quad`) en parte real e imaginaria a $\sim 10^{-8}$; p.ej. $\hat f(1) = 0.50695 - 0.33452\,i$, $\hat f(2) = 0.20691 - 0.49547\,i$. En $\omega = 0$ ambas dan $1 - e^{-1} = 0.63212$. También se verificó la equivalencia de las dos formas $e^{-1}\tfrac{e^{1-i\omega}-1}{1-i\omega} = \tfrac{e^{-i\omega}-e^{-1}}{1-i\omega}$. ✓
