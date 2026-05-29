---
tags: [final, resolucion, transformaciones-lineales, nucleo-imagen, diagonalizacion, autovalores, fourier-series, diferencias-finitas, ecuacion-calor, neumann, dirichlet, transformada-fourier]
fuente: raw/Practicas/Modelos_Examenes/MNA_Final_Tema_VI.pdf
tipo: final
tema: 6
tiene_resolucion: true
---

# Examen Final de Métodos Numéricos Avanzados — Tema VI (Resolución)

Enunciado original sin resolver en [[final-tema-06]]. Referencias de método: [[../guias/guia-08-fourier-series]], [[../resueltos/resueltos-fourier]], [[../guias/guia-09-tf]]. Resolución hermana muy parecida en estructura: [[final-tema-05-resolucion]].

## Ejercicio 1

Dada la TL $T : \mathbb{R}^3 \to \mathbb{R}^3 : T(x, y, z) = (2x - y,\ x + y - z,\ x + 2z + y)$.

a) Hallar el Núcleo y la Imagen.
b) Decidir si es o no diagonalizable en $\mathbb{R}$.

### Resolución

Las columnas de $M_{EE}(T)$ son las imágenes de la base canónica:

$$T(e_1) = T(1,0,0) = (2,1,1),\quad T(e_2) = T(0,1,0) = (-1,1,1),\quad T(e_3) = T(0,0,1) = (0,-1,2).$$

(Leyendo coeficientes: la 1ª componente $2x-y$ aporta $2,-1,0$; la 2ª $x+y-z$ aporta $1,1,-1$; la 3ª $x+y+2z$ aporta $1,1,2$.)

$$M_{EE}(T) = A = \begin{pmatrix} 2 & -1 & 0 \\ 1 & 1 & -1 \\ 1 & 1 & 2 \end{pmatrix}.$$

**a) Núcleo e Imagen.** Calculamos el determinante desarrollando por la primera fila:

$$\det A = 2\begin{vmatrix} 1 & -1 \\ 1 & 2 \end{vmatrix} - (-1)\begin{vmatrix} 1 & -1 \\ 1 & 2 \end{vmatrix} + 0 = 2\,(2+1) + 1\,(2+1) = 6 + 3 = 9 \ne 0.$$

(Con cuidado: $\begin{vmatrix} 1 & -1 \\ 1 & 2 \end{vmatrix} = 1\cdot 2 - (-1)\cdot 1 = 3$ y $\begin{vmatrix} 1 & -1 \\ 1 & 2 \end{vmatrix} = 3$, así que $\det A = 2\cdot 3 + 1\cdot 3 = 9$.)

Como $\det A = 9 \ne 0$, la matriz es inversible, así que $T$ es un **isomorfismo**. Por lo tanto:

$$\boxed{N(T) = \{(0,0,0)\}\quad (\dim N(T) = 0), \qquad \text{Im}(T) = \mathbb{R}^3\quad (\dim \text{Im}(T) = 3).}$$

(Consistente con el teorema de la dimensión: $\dim N(T) + \dim \text{Im}(T) = 0 + 3 = 3 = \dim \mathbb{R}^3$. Como $\text{rg}(A)=3$ las tres columnas son base de la imagen.)

**b) ¿Diagonalizable en $\mathbb{R}$?** Polinomio característico con la convención de la cátedra $p_A(\lambda) = \det(\lambda I - A)$:

$$\lambda I - A = \begin{pmatrix} \lambda - 2 & 1 & 0 \\ -1 & \lambda - 1 & 1 \\ -1 & -1 & \lambda - 2 \end{pmatrix}.$$

Desarrollando por la primera fila:

$$p_A(\lambda) = (\lambda-2)\begin{vmatrix} \lambda-1 & 1 \\ -1 & \lambda-2 \end{vmatrix} - 1\begin{vmatrix} -1 & 1 \\ -1 & \lambda-2 \end{vmatrix} + 0.$$

Los dos menores:

$$\begin{vmatrix} \lambda-1 & 1 \\ -1 & \lambda-2 \end{vmatrix} = (\lambda-1)(\lambda-2) + 1 = \lambda^2 - 3\lambda + 3,$$
$$\begin{vmatrix} -1 & 1 \\ -1 & \lambda-2 \end{vmatrix} = -(\lambda-2) + 1 = 3 - \lambda.$$

Entonces:

$$p_A(\lambda) = (\lambda-2)(\lambda^2 - 3\lambda + 3) - (3 - \lambda) = (\lambda^3 - 5\lambda^2 + 9\lambda - 6) + (\lambda - 3),$$

$$\boxed{p_A(\lambda) = \lambda^3 - 5\lambda^2 + 10\lambda - 9.}$$

**Búsqueda de raíces racionales.** Por el teorema de la raíz racional, las candidatas (divisores de $9$) son $\pm1, \pm3, \pm9$. Evaluando: $p_A(1) = 1 - 5 + 10 - 9 = -3$, $p_A(3) = 27 - 45 + 30 - 9 = 3$, $p_A(9) = 405$, y todos los demás dan distinto de cero. **No hay raíces racionales** "lindas".

**¿Cuántas raíces reales?** Estudiamos la monotonía con la derivada:

$$p_A'(\lambda) = 3\lambda^2 - 10\lambda + 10,\qquad \Delta = (-10)^2 - 4\cdot 3\cdot 10 = 100 - 120 = -20 < 0.$$

Como el discriminante de $p_A'$ es negativo y su coeficiente líder es positivo, $p_A'(\lambda) > 0$ para todo $\lambda$: el polinomio característico es **estrictamente creciente**, así que tiene **exactamente una raíz real**. Por el cambio de signo $p_A(2) = 8 - 20 + 20 - 9 = -1 < 0$ y $p_A(3) = 3 > 0$, esa raíz real está en $(2,3)$ (numéricamente $\lambda_1 \approx 2.3926$).

Como un polinomio cúbico real con una sola raíz real tiene las otras dos **complejas conjugadas no reales** ($\lambda_{2,3} \approx 1.3037 \pm 1.4359\,i$), el polinomio característico **no se escinde sobre $\mathbb{R}$**: faltan autovalores reales para poder diagonalizar.

$$\boxed{T \text{ NO es diagonalizable en } \mathbb{R}.}$$

> **Punto sutil.** No conviene perder tiempo buscando $P$ y $D$: el bloqueo no está en una multiplicidad geométrica chica (el único $\lambda$ real es simple), sino en que faltan autovalores reales. El argumento de la derivada ($p_A' > 0 \Rightarrow$ una sola raíz real) es la vía limpia para decidirlo **sin** calcular la raíz cúbica explícita (que es irracional y fea). Sobre $\mathbb{C}$ sí habría tres autovalores distintos y $T$ sería diagonalizable; la consigna pide "en $\mathbb{R}$", y ahí la respuesta es negativa.

**Verificación numérica** (numpy/sympy). `np.linalg.det(A) = 9.0`, `matrix_rank(A) = 3` (confirma $N(T)=\{0\}$, $\text{Im}(T)=\mathbb{R}^3$). `sympy.expand((lam*I - A).det())` da $\lambda^3 - 5\lambda^2 + 10\lambda - 9$ y `sympy.factor` no lo factoriza (irreducible sobre $\mathbb{Q}$). `np.linalg.eig(A)` devuelve $\{2.3926,\ 1.3037 + 1.4359\,i,\ 1.3037 - 1.4359\,i\}$ — un solo autovalor real. Además $\operatorname{disc}(p_A) = -87 < 0$ confirma una raíz real y dos complejas. ✓

## Ejercicio 2

a) Hallar el desarrollo en serie de Fourier de $f : [0, 1] \to \mathbb{R} : f(x) = 1 - x$, con $f(x) = f(x + 1)$ (período $T = 1$).
b) Indicar a qué converge la serie en $x = 0$ y $x = \tfrac{1}{2}$.

### Resolución

**a) Coeficientes.** Con $T = 1$ se tiene $\tfrac{2\pi n}{T} = 2\pi n$. Convención de la cátedra:

$$f(x) = a_0 + \sum_{n=1}^{\infty} a_n\cos(2\pi n x) + \sum_{n=1}^{\infty} b_n\sin(2\pi n x),$$

$$a_0 = \frac{1}{T}\int_0^1 f\,dx,\qquad a_n = \frac{2}{T}\int_0^1 f\cos(2\pi n x)\,dx,\qquad b_n = \frac{2}{T}\int_0^1 f\sin(2\pi n x)\,dx.$$

**Término constante** $a_0$ (valor medio, NO dividido por 2):

$$a_0 = \int_0^1 (1 - x)\,dx = \Big[x - \tfrac{x^2}{2}\Big]_0^1 = 1 - \tfrac12 = \boxed{\tfrac{1}{2}}.$$

**Coeficientes coseno** $a_n = 2\displaystyle\int_0^1 (1-x)\cos(2\pi n x)\,dx$. Separamos con $\omega_n = 2\pi n$:

$$a_n = 2\underbrace{\int_0^1 \cos(\omega_n x)\,dx}_{=\,0} - 2\int_0^1 x\cos(\omega_n x)\,dx.$$

La primera integral es $0$ (período completo del coseno). Para la segunda, por partes ($u=x$, $dv=\cos(\omega_n x)\,dx$):

$$\int_0^1 x\cos(\omega_n x)\,dx = \left[\frac{x\sin(\omega_n x)}{\omega_n} + \frac{\cos(\omega_n x)}{\omega_n^2}\right]_0^1 = \frac{\sin(2\pi n)}{\omega_n} + \frac{\cos(2\pi n) - 1}{\omega_n^2}.$$

Como $\sin(2\pi n) = 0$ y $\cos(2\pi n) = 1$, esta integral vale $0$. Por lo tanto:

$$\boxed{a_n = 0\quad (n\ge 1).}$$

**Coeficientes seno** $b_n = 2\displaystyle\int_0^1 (1-x)\sin(\omega_n x)\,dx$. Separamos:

$$b_n = 2\underbrace{\int_0^1 \sin(\omega_n x)\,dx}_{=\,0} - 2\int_0^1 x\sin(\omega_n x)\,dx.$$

Otra vez la primera integral es $0$. Por partes la segunda ($u=x$, $dv=\sin(\omega_n x)\,dx$):

$$\int_0^1 x\sin(\omega_n x)\,dx = \left[-\frac{x\cos(\omega_n x)}{\omega_n} + \frac{\sin(\omega_n x)}{\omega_n^2}\right]_0^1 = -\frac{\cos(2\pi n)}{\omega_n} + \frac{\sin(2\pi n)}{\omega_n^2} = -\frac{1}{\omega_n}.$$

Entonces:

$$b_n = -2\left(-\frac{1}{\omega_n}\right) = \frac{2}{2\pi n} = \boxed{\frac{1}{\pi n}.}$$

> **Punto sutil (por qué desaparecen los cosenos).** Al periodizar $f(x)=1-x$ con período $1$, la extensión es la clásica "diente de sierra" centrada en su valor medio $\tfrac12$. La parte $g(x) = f(x) - \tfrac12 = \tfrac12 - x$ es **impar** respecto del centro del intervalo, lo que mata todos los $a_n$ y deja solo senos. El término constante $a_0 = \tfrac12$ es justamente ese valor medio.

**Serie resultante:**

$$\boxed{f(x) = \frac{1}{2} + \frac{1}{\pi}\sum_{n=1}^{\infty}\frac{\sin(2\pi n x)}{n}.}$$

**b) Convergencia (criterio de Dirichlet).** La extensión periódica empalma $f(1^-) = 1 - 1 = 0$ con $f(0^+) = 1 - 0 = 1$, así que en los enteros (en particular $x=0$) hay un **salto**.

- En $x = 0$ (discontinuidad por salto): la serie converge al promedio de los límites laterales,
$$S(0) = \frac{f(0^+) + f(1^-)}{2} = \frac{1 + 0}{2} = \boxed{\tfrac{1}{2}}.$$
  (También se ve directo: todos los $\sin(2\pi n\cdot 0)=0$, así que la suma vale el término constante $a_0 = \tfrac12$.)
- En $x = \tfrac{1}{2}$ (punto interior, $f$ continua ahí): la serie converge al valor de la función,
$$S\!\left(\tfrac{1}{2}\right) = f\!\left(\tfrac{1}{2}\right) = 1 - \tfrac{1}{2} = \boxed{\tfrac{1}{2}}.$$
  (También directo: $\sin(2\pi n\cdot\tfrac12) = \sin(\pi n) = 0$ para todo $n$, así que la suma vale $a_0 = \tfrac12$.)

> **Coincidencia (no confundir).** En este problema $S(0) = S(\tfrac12) = \tfrac12$, pero por **razones distintas**: en $x=0$ es el promedio de un salto; en $x=\tfrac12$ es el valor (continuo) de la función, que justo también vale $\tfrac12$. No es que la serie no distinga los puntos.

**Verificación numérica.** Integración numérica (`scipy.quad`) da $a_0 = 0.5$, $a_n \approx 0$ y $b_n = \tfrac{1}{\pi n}$ para $n=1,\dots,5$ (p.ej. $b_1 = 0.318310 = \tfrac1\pi$, $b_2 = 0.159155 = \tfrac{1}{2\pi}$). Sumas parciales con $N=20000$: $S(0) \to 0.5$, $S(0.5) \to 0.5$, y en un punto de continuidad de control $S(0.25) \to 0.74999 \approx f(0.25) = \tfrac34$. ✓

## Ejercicio 3

Dada la ecuación del calor $\dfrac{\partial u}{\partial t} = \dfrac{\partial^2 u}{\partial x^2}$, desarrollar un esquema de diferencias finitas **implícito** con 4 nodos internos para:

a) $u(0, t) = u(1, t) = 0$ (Dirichlet homogéneo) y $u(x, 0) = e^{-x}\operatorname{sen}(x)$.
b) $u_x(0, t) = u(1, t) = 0$ (mixto: Neumann en $x=0$, Dirichlet en $x=1$) y $u(x, 0) = x^2$.

### Resolución

**Malla.** Dominio $x \in [0,1]$ con 4 nodos internos $\Rightarrow$ $h = \tfrac{1}{5} = 0.2$, nodos $x_0 = 0,\ x_1 = 0.2,\ x_2 = 0.4,\ x_3 = 0.6,\ x_4 = 0.8,\ x_5 = 1$. Notación $u_i^k \approx u(x_i, t_k)$, paso temporal $\Delta t$.

**Discretización (Euler implícito / hacia atrás en tiempo).** Evaluando $u_{xx}$ en el nivel $k+1$:

$$\frac{u_i^{k+1} - u_i^k}{\Delta t} = \frac{u_{i-1}^{k+1} - 2u_i^{k+1} + u_{i+1}^{k+1}}{h^2}.$$

Con $r = \dfrac{\Delta t}{h^2}$, reordenando para dejar las incógnitas (nivel $k+1$) a la izquierda:

$$\boxed{-r\,u_{i-1}^{k+1} + (1 + 2r)\,u_i^{k+1} - r\,u_{i+1}^{k+1} = u_i^k.}$$

#### a) Dirichlet homogéneo en ambos bordes

Los bordes son **datos conocidos**: $u_0^{k+1} = u_5^{k+1} = 0$. Al ser nulos, no aportan nada al lado derecho. Las incógnitas son los 4 nodos internos $u_1, u_2, u_3, u_4$. Escribiendo la ecuación para $i = 1,2,3,4$ (y borrando los términos de borde nulos) se obtiene un sistema tridiagonal $4\times 4$:

$$M\,\mathbf{u}^{k+1} = \mathbf{u}^k,\qquad
M = \begin{pmatrix}
1+2r & -r & 0 & 0 \\
-r & 1+2r & -r & 0 \\
0 & -r & 1+2r & -r \\
0 & 0 & -r & 1+2r
\end{pmatrix},\qquad
\mathbf{u}^{k+1} = \begin{pmatrix} u_1^{k+1} \\ u_2^{k+1} \\ u_3^{k+1} \\ u_4^{k+1} \end{pmatrix}.$$

El lado derecho es $\mathbf{b}^k = \mathbf{u}^k = (u_1^k, u_2^k, u_3^k, u_4^k)^T$ (la solución del paso anterior). El **vector de condición inicial** sale de $u(x,0) = e^{-x}\operatorname{sen}(x)$ evaluado en $x_i = 0.2,\dots,0.8$:

$$\mathbf{u}^0 = \begin{pmatrix} e^{-0.2}\operatorname{sen}(0.2) \\ e^{-0.4}\operatorname{sen}(0.4) \\ e^{-0.6}\operatorname{sen}(0.6) \\ e^{-0.8}\operatorname{sen}(0.8) \end{pmatrix} \approx \begin{pmatrix} 0.162657 \\ 0.261035 \\ 0.309882 \\ 0.322329 \end{pmatrix}.$$

> **Atención al argumento.** El seno está en **radianes** del propio $x_i$ (no $\operatorname{sen}(\pi x_i)$), y hay un factor $e^{-x_i}$ que conviene no olvidar. En $x_0 = 0$ la CI vale $e^0\operatorname{sen}(0)=0$, compatible con el borde de Dirichlet; en $x_5=1$ la condición de borde $u(1,t)=0$ prevalece para $t>0$.

Cada paso temporal: se resuelve el sistema $M\,\mathbf{u}^{k+1} = \mathbf{u}^k$.

#### b) Mixto: Neumann en $x=0$, Dirichlet en $x=1$

Ahora $u_x(0,t) = 0$ (Neumann) y $u(1,t) = 0$ (Dirichlet homogéneo). Tratamos cada borde por separado:

- **Borde derecho $x_5=1$ (Dirichlet):** $u_5^{k+1} = 0$ es **dato conocido** → no es incógnita y, por ser nulo, no aporta al lado derecho.
- **Borde izquierdo $x_0=0$ (Neumann):** no hay valor prescrito de $u$, así que $u_0$ **pasa a ser incógnita**. Para cerrar el esquema se usa un **nodo fantasma** $u_{-1}$ y diferencia centrada:
$$u_x(0,t) \approx \frac{u_1^{k+1} - u_{-1}^{k+1}}{2h} = 0 \;\Longrightarrow\; u_{-1}^{k+1} = u_1^{k+1}.$$

Aplicando la ecuación general en el nodo $i=0$ (que incluye el fantasma $u_{-1}$) y sustituyendo $u_{-1}^{k+1} = u_1^{k+1}$:

$$-r\,u_{-1}^{k+1} + (1+2r)u_0^{k+1} - r\,u_1^{k+1} = u_0^k \;\Longrightarrow\; (1+2r)u_0^{k+1} - 2r\,u_1^{k+1} = u_0^k.$$

Las incógnitas pasan a ser **los 5 nodos** $u_0, u_1, u_2, u_3, u_4$ (entra $u_0$ por Neumann, sale $u_5$ por Dirichlet). El sistema es $5\times 5$:

$$M\,\mathbf{u}^{k+1} = \mathbf{u}^k,\qquad
M = \begin{pmatrix}
1+2r & -2r & 0 & 0 & 0 \\
-r & 1+2r & -r & 0 & 0 \\
0 & -r & 1+2r & -r & 0 \\
0 & 0 & -r & 1+2r & -r \\
0 & 0 & 0 & -r & 1+2r
\end{pmatrix},\qquad
\mathbf{u}^{k+1} = \begin{pmatrix} u_0^{k+1} \\ u_1^{k+1} \\ u_2^{k+1} \\ u_3^{k+1} \\ u_4^{k+1} \end{pmatrix}.$$

Detalles de las filas extremas:
- **Primera fila** (nodo $x_0$, Neumann): $(1+2r)u_0^{k+1} - 2r\,u_1^{k+1} = u_0^k$. El $-2r$ (no $-r$) es la huella del nodo fantasma.
- **Última fila** (nodo $x_4$): la ecuación natural sería $-r\,u_3^{k+1} + (1+2r)u_4^{k+1} - r\,u_5^{k+1} = u_4^k$; como $u_5^{k+1}=0$ (Dirichlet), ese término desaparece y queda $-r\,u_3^{k+1} + (1+2r)u_4^{k+1} = u_4^k$. Por eso la última fila es una fila tridiagonal "normal", **no** lleva $-2r$.

El lado derecho es $\mathbf{b}^k = \mathbf{u}^k = (u_0^k, u_1^k, u_2^k, u_3^k, u_4^k)^T$. El **vector de condición inicial** sale de $u(x,0) = x^2$; como $x_i^2$ con $x_i = 0, 0.2, 0.4, 0.6, 0.8$:

$$\mathbf{u}^0 = \begin{pmatrix} 0^2 \\ 0.2^2 \\ 0.4^2 \\ 0.6^2 \\ 0.8^2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0.04 \\ 0.16 \\ 0.36 \\ 0.64 \end{pmatrix}.$$

(El nodo $x_5 = 1$ tendría CI $1^2 = 1$, pero queda fuera del sistema porque la condición de borde $u(1,t)=0$ lo fija en $0$ para $t>0$.)

> **Puntos sutiles.** (1) Con **un** borde Neumann y otro Dirichlet, el sistema es $5\times 5$: respecto del caso Dirichlet–Dirichlet ($4\times4$) entra el nodo $x_0$ como incógnita, pero $x_5$ sigue saliendo por Dirichlet. (No es $6\times6$ como sería con Neumann en ambos bordes.) (2) La asimetría de las filas extremas (primera con $-2r$, última con $-r$) refleja que cada borde tiene una condición distinta. (3) La CI $x^2$ en $x_0=0$ da $0$, compatible con $u_x(0,0)=2x\big|_{0}=0$ (la propia parábola satisface la condición de Neumann en el origen, un dato consistente).

**Verificación numérica.** Con $r=1$ y un paso implícito: $\det M_a = 55 \ne 0$ (caso a, $4\times4$) y $\det M_b = 123 \ne 0$ (caso b, $5\times5$); ambas matrices son diagonalmente dominantes por filas, así que los sistemas están bien planteados y son resolubles. Los vectores CI computados coinciden con los reportados: $\mathbf u^0_{(a)} = (0.162657, 0.261035, 0.309882, 0.322329)$, $\mathbf u^0_{(b)} = (0, 0.04, 0.16, 0.36, 0.64)$. ✓

## Ejercicio 4

Hallar la Transformada de Fourier de $f(t) = e^{-2|t| + 1}$ si $0 \le t \le 1$, y $f(t) = 0$ en otro caso.

### Resolución

**Simplificación del soporte.** En el intervalo $[0,1]$ se tiene $t \ge 0$, luego $|t| = t$ y por lo tanto, dentro del soporte:

$$f(t) = e^{-2t + 1} = e^{1 - 2t},\qquad 0 \le t \le 1.$$

> **Punto sutil.** El valor absoluto se evalúa con el signo de $t$ en el dominio dado: como solo integramos sobre $[0,1]$ (soporte compacto) y ahí $t \ge 0$, simplemente $|t| = t$. No hace falta partir en casos.

**Definición (convención de la cátedra)** $\hat f(\omega) = \displaystyle\int_{-\infty}^{\infty} f(t)\,e^{-i\omega t}\,dt$. Como $f$ se anula fuera de $[0,1]$, integramos solo sobre el soporte:

$$\hat f(\omega) = \int_0^1 e^{1 - 2t}\,e^{-i\omega t}\,dt = e\int_0^1 e^{-(2 + i\omega)t}\,dt.$$

Resolviendo la integral (con $2 + i\omega \ne 0$, lo cual siempre vale porque la parte real es $2$):

$$\int_0^1 e^{-(2+i\omega)t}\,dt = \left.\frac{e^{-(2+i\omega)t}}{-(2+i\omega)}\right|_0^1 = \frac{1 - e^{-(2+i\omega)}}{2 + i\omega}.$$

Por lo tanto:

$$\boxed{\hat f(\omega) = e\,\frac{1 - e^{-(2 + i\omega)}}{2 + i\omega} = \frac{e - e^{-1}\,e^{-i\omega}}{2 + i\omega},}$$

donde la última igualdad usa $e\cdot e^{-(2+i\omega)} = e^{-1}e^{-i\omega}$.

**Caso $\omega = 0$.** No hay indeterminación (el denominador $2+i\omega$ no se anula); evaluamos directo:

$$\hat f(0) = e\,\frac{1 - e^{-2}}{2} = \frac{e - e^{-1}}{2} \approx 1.17520.$$

(Coincide con integrar $\displaystyle\int_0^1 e^{1-2t}\,dt = e\big[-\tfrac12 e^{-2t}\big]_0^1 = \tfrac{e}{2}(1 - e^{-2})$.)

**Parte real e imaginaria** (racionalizando: multiplicar numerador y denominador por el conjugado $2 - i\omega$, y usando $e^{-i\omega} = \cos\omega - i\sin\omega$):

$$\operatorname{Re}\hat f(\omega) = \frac{e^{-1}\big(\omega\sin\omega - 2\cos\omega + 2e^{2}\big)}{\omega^2 + 4},$$

$$\operatorname{Im}\hat f(\omega) = \frac{e^{-1}\big(\omega\cos\omega + 2\sin\omega - \omega\, e^{2}\big)}{\omega^2 + 4}.$$

(Chequeo de consistencia en $\omega=0$: $\operatorname{Re}\hat f(0) = \dfrac{e^{-1}(-2 + 2e^2)}{4} = \dfrac{e - e^{-1}}{2}$ y $\operatorname{Im}\hat f(0) = 0$. ✓)

**Verificación numérica.** Para $\omega \in \{0, 0.5, 1, 2, 3, -1.5\}$ la fórmula cerrada coincide con la integral numérica (`scipy.quad`) en parte real e imaginaria a $\sim 10^{-16}$; p.ej. $\hat f(1) = 1.06972 - 0.38008\,i$, $\hat f(2) = 0.80147 - 0.63422\,i$, $\hat f(-1.5) = 0.94959 + 0.52872\,i$. En $\omega = 0$ ambas dan $\tfrac{e - e^{-1}}{2} = 1.17520$. También se verificó (sympy) que las fórmulas de $\operatorname{Re}\hat f$ y $\operatorname{Im}\hat f$ son la expansión exacta de la forma cerrada. ✓
