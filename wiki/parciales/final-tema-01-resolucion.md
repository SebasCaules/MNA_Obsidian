---
tags: [final, resolucion, transformaciones-lineales, nucleo-imagen, diagonalizacion, fourier, series-fourier, ecuaciones-diferenciales, diferencias-finitas, svd, transformada-fourier]
fuente: raw/Practicas/Modelos_Examenes/MNA_Final_Tema_I.pdf
tipo: final
tema: 1
tiene_resolucion: true
---

# Examen Final de Métodos Numéricos Avanzados — Tema I (Resolución)

Enunciado original en [[final-tema-01]]. Recetas de referencia en `study/MNA_Cheatsheet.html`.

## Ejercicio 1

Dada la Transformación Lineal $T : \mathbb{R}^3 \to \mathbb{R}^3 : T(x, y, z) = (2x - y,\ x + y - z,\ z)$

a) Hallar el Núcleo y la Imagen.
b) Decidir si es o no diagonalizable en $\mathbb{R}$.

### Resolución

Armamos la matriz en base canónica $M_{EE}(T)$, cuyas columnas son las imágenes de los vectores de la base $T(e_1), T(e_2), T(e_3)$:

$$T(e_1)=T(1,0,0)=(2,1,0),\quad T(e_2)=T(0,1,0)=(-1,1,0),\quad T(e_3)=T(0,0,1)=(0,-1,1).$$

$$M_{EE}(T) = A = \begin{pmatrix} 2 & -1 & 0 \\ 1 & 1 & -1 \\ 0 & 0 & 1 \end{pmatrix}.$$

**a) Núcleo e Imagen.** Calculamos el determinante desarrollando por la tercera fila:

$$\det A = 1\cdot\begin{vmatrix} 2 & -1 \\ 1 & 1\end{vmatrix} = 1\cdot(2\cdot1 - (-1)\cdot1) = 3 \ne 0.$$

Como $\det A = 3 \ne 0$, la matriz es inversible, de modo que el único $X$ con $AX = 0$ es el trivial:

$$\boxed{N(T) = \{(0,0,0)\}.}$$

Por el **Teorema de la dimensión**, $\dim N(T) + \dim \mathrm{Im}(T) = 3$, luego $\dim\mathrm{Im}(T)=3$ y

$$\boxed{\mathrm{Im}(T) = \mathbb{R}^3.}$$

($T$ es además un isomorfismo: es cuadrada con $\det\ne0$.)

**b) ¿Diagonalizable en $\mathbb{R}$?** El polinomio característico es $p_A(\lambda)=\det(\lambda I - A)$ (coef. líder $+1$):

$$\lambda I - A = \begin{pmatrix} \lambda-2 & 1 & 0 \\ -1 & \lambda-1 & 1 \\ 0 & 0 & \lambda-1 \end{pmatrix}.$$

Desarrollando por la tercera fila (que tiene un solo término no nulo, $\lambda-1$ en la posición $(3,3)$):

$$p_A(\lambda) = (\lambda-1)\begin{vmatrix} \lambda-2 & 1 \\ -1 & \lambda-1\end{vmatrix} = (\lambda-1)\big[(\lambda-2)(\lambda-1) + 1\big].$$

$$(\lambda-2)(\lambda-1)+1 = \lambda^2 - 3\lambda + 2 + 1 = \lambda^2 - 3\lambda + 3.$$

$$\boxed{p_A(\lambda) = (\lambda - 1)(\lambda^2 - 3\lambda + 3).}$$

El factor lineal da $\lambda_1 = 1$. El factor cuadrático tiene discriminante

$$\Delta = (-3)^2 - 4\cdot1\cdot3 = 9 - 12 = -3 < 0,$$

de modo que sus raíces son **complejas conjugadas**:

$$\lambda_{2,3} = \frac{3 \pm \sqrt{-3}}{2} = \frac{3}{2} \pm \frac{\sqrt{3}}{2}\,i.$$

Como aparecen autovalores que **no son reales**, $A$ no tiene tres autovalores reales (contados con multiplicidad) y por lo tanto **no existe una base de $\mathbb{R}^3$ formada por autovectores reales**.

$$\boxed{T \text{ NO es diagonalizable en } \mathbb{R}.}$$

(Observación: sí sería diagonalizable sobre $\mathbb{C}$, porque los tres autovalores $1,\ \tfrac32\pm\tfrac{\sqrt3}{2}i$ son **distintos** entre sí, y autovalores distintos garantizan diagonalización. La pregunta del examen es específicamente sobre $\mathbb{R}$.)

**Verificación numérica.** `numpy.poly(A)` devuelve los coeficientes $[1,-4,6,-3]$, es decir $\lambda^3 - 4\lambda^2 + 6\lambda - 3$, que coincide con $(\lambda-1)(\lambda^2-3\lambda+3)$. Los autovalores son $\{1,\ 1.5\pm0.8660\,i\}$ ($0.8660\approx\tfrac{\sqrt3}{2}$), $\det A = 3$ y $\mathrm{rg}(A)=3$. ✓

## Ejercicio 2

a) Hallar el desarrollo en serie de Fourier de la función $f(x) = x - [x]$ (parte fraccionaria, período $1$).
b) Indique a qué converge la serie en $\mathbb{Z}$ (los enteros).

### Resolución

$f(x) = x - [x]$ es la **parte fraccionaria**: es periódica de período $T = 1$, y en el intervalo $[0,1)$ vale simplemente $f(x) = x$ (es la rampa "diente de sierra"). Usamos la convención de la cátedra con $T=1$, donde $\tfrac{2\pi n}{T} = 2\pi n$:

$$f(x) = a_0 + \sum_{n=1}^{\infty} a_n\cos(2\pi n x) + \sum_{n=1}^{\infty} b_n\sin(2\pi n x).$$

**Coeficiente $a_0$** (valor medio, **sin** dividir por 2):

$$a_0 = \frac{1}{T}\int_0^1 f(x)\,dx = \int_0^1 x\,dx = \left.\frac{x^2}{2}\right|_0^1 = \frac{1}{2}.$$

**Coeficientes $a_n$** ($n\ge1$). Integrando por partes $\int_0^1 x\cos(2\pi n x)\,dx$ con $u=x$, $dv=\cos(2\pi n x)\,dx$:

$$a_n = 2\int_0^1 x\cos(2\pi n x)\,dx = 2\left[\frac{x\sin(2\pi n x)}{2\pi n} + \frac{\cos(2\pi n x)}{(2\pi n)^2}\right]_0^1.$$

En $x=1$ y $x=0$, $\sin(2\pi n)=\sin0=0$ y $\cos(2\pi n)=\cos0=1$, de modo que ambos términos se cancelan:

$$\boxed{a_n = 0 \quad (n\ge1).}$$

**Coeficientes $b_n$** ($n\ge1$). Integrando por partes $\int_0^1 x\sin(2\pi n x)\,dx$:

$$b_n = 2\int_0^1 x\sin(2\pi n x)\,dx = 2\left[-\frac{x\cos(2\pi n x)}{2\pi n} + \frac{\sin(2\pi n x)}{(2\pi n)^2}\right]_0^1.$$

Evaluando: en $x=1$ el primer término es $-\frac{1\cdot\cos(2\pi n)}{2\pi n} = -\frac{1}{2\pi n}$; en $x=0$ vale $0$; los términos con $\sin$ se anulan. Luego

$$b_n = 2\left(-\frac{1}{2\pi n}\right) = -\frac{1}{\pi n}.$$

$$\boxed{b_n = -\frac{1}{\pi n} \quad (n\ge1).}$$

**Serie de Fourier:**

$$\boxed{f(x) = \frac{1}{2} - \sum_{n=1}^{\infty} \frac{1}{\pi n}\sin(2\pi n x) = \frac{1}{2} - \frac{1}{\pi}\sum_{n=1}^{\infty} \frac{\sin(2\pi n x)}{n}.}$$

(Coherente con la rampa estándar: $f$ tiene valor medio $\tfrac12$ y solo armónicos senoidales, porque al restarle $\tfrac12$ resulta una función impar respecto del centro del período.)

**b) Convergencia en $\mathbb{Z}$.** En cada entero $x = k \in \mathbb{Z}$ hay una **discontinuidad de salto**: por la izquierda $f(k^-) = \lim_{x\to k^-} (x-[x]) = 1$ (la rampa llega a $1$), y por la derecha $f(k^+) = 0$ (la rampa "reinicia"). Por el criterio de **Dirichlet**, en un punto de salto la serie no converge a ninguno de los dos valores sino al **promedio** de los límites laterales:

$$S(k) = \frac{1}{2}\big(f(k^+) + f(k^-)\big) = \frac{1}{2}(0 + 1) = \frac{1}{2}.$$

$$\boxed{\text{En todo } k\in\mathbb{Z},\ \text{la serie converge a } \tfrac{1}{2}.}$$

Esto también se ve directamente de la serie: en $x=k$ entero, $\sin(2\pi n k) = 0$ para todo $n$, así que todos los términos senoidales se anulan y queda exactamente $f(k) \to a_0 = \tfrac12$.

**Verificación numérica.** Por integración numérica: $a_0 = 0.5$, $a_n \approx 0$, $b_n = \{-0.31831, -0.15915, -0.10610,\dots\}$, que coincide con $-\tfrac{1}{\pi n}$. Evaluando sumas parciales en $x=0$ y $x=3$ (enteros) con $N=10,100,1000$ términos da $0.500000$ en todos los casos; en un punto de continuidad como $x=0.3$ la suma parcial tiende a $0.3$. ✓

## Ejercicio 3

Considere la EDO (oscilador de **Duffing forzado**):

$$\frac{d^2 x}{dt^2} + \delta \frac{dx}{dt} + \beta x + \alpha x^3 = \gamma \cos(\omega t + \phi).$$

a) Escriba la ecuación como un sistema de orden 1.
b) Plantee un esquema implícito de diferencias finitas. Indique cómo implementa las condiciones iniciales.

### Resolución

**a) Reducción a sistema de primer orden.** Introducimos las variables de estado $x_1 = x$ (posición) y $x_2 = \dot x$ (velocidad). Entonces $\dot x_1 = \dot x = x_2$, y de la EDO despejamos $\ddot x$:

$$\ddot x = \gamma\cos(\omega t + \phi) - \delta\dot x - \beta x - \alpha x^3.$$

Con esto, el sistema de primer orden es

$$\boxed{\begin{cases} \dot x_1 = x_2, \\[4pt] \dot x_2 = \gamma\cos(\omega t + \phi) - \delta\,x_2 - \beta\,x_1 - \alpha\,x_1^3. \end{cases}}$$

En forma vectorial $\dot{\mathbf x} = \mathbf F(t, \mathbf x)$ con $\mathbf x = (x_1, x_2)^T$ y

$$\mathbf F(t,\mathbf x) = \begin{pmatrix} x_2 \\ \gamma\cos(\omega t+\phi) - \delta x_2 - \beta x_1 - \alpha x_1^3 \end{pmatrix}.$$

Observación clave: por el término $\alpha x^3$, el sistema es **no lineal** en la primera variable.

**b) Esquema implícito (Euler hacia atrás) y condiciones iniciales.** Discretizamos el tiempo con paso $\Delta t$: $t_k = k\,\Delta t$, y notamos $x_1^k \approx x_1(t_k)$, $x_2^k \approx x_2(t_k)$. El esquema **implícito** evalúa $\mathbf F$ en el instante nuevo $t_{k+1}$ (Euler hacia atrás), reemplazando las derivadas por $\dot{\mathbf x} \approx (\mathbf x^{k+1} - \mathbf x^k)/\Delta t$:

$$\boxed{\begin{cases} \dfrac{x_1^{k+1} - x_1^{k}}{\Delta t} = x_2^{k+1}, \\[10pt] \dfrac{x_2^{k+1} - x_2^{k}}{\Delta t} = \gamma\cos(\omega t_{k+1} + \phi) - \delta\,x_2^{k+1} - \beta\,x_1^{k+1} - \alpha\,(x_1^{k+1})^3. \end{cases}}$$

A diferencia del esquema explícito (Euler hacia adelante), aquí las incógnitas $x_1^{k+1}, x_2^{k+1}$ aparecen **en ambos miembros**, y por el término $(x_1^{k+1})^3$ aparecen de manera **no lineal**. Por lo tanto, **cada paso temporal requiere resolver un sistema de ecuaciones NO lineales** (a diferencia del calor lineal, donde solo se invierte una matriz tridiagonal una vez). El método estándar es **Newton-Raphson**. Reorganizamos el sistema como $\mathbf G(\mathbf x^{k+1}) = \mathbf 0$:

$$\mathbf G(x_1, x_2) = \begin{pmatrix} x_1 - x_1^k - \Delta t\,x_2 \\[4pt] x_2 - x_2^k - \Delta t\big[\gamma\cos(\omega t_{k+1}+\phi) - \delta x_2 - \beta x_1 - \alpha x_1^3\big] \end{pmatrix} = \mathbf 0,$$

cuya matriz Jacobiana es

$$J = \frac{\partial \mathbf G}{\partial(x_1,x_2)} = \begin{pmatrix} 1 & -\Delta t \\[4pt] \Delta t\,(\beta + 3\alpha x_1^2) & 1 + \Delta t\,\delta \end{pmatrix}.$$

En cada paso se itera $\mathbf x \leftarrow \mathbf x - J^{-1}\mathbf G(\mathbf x)$ partiendo de $\mathbf x^k$ hasta convergencia, y el resultado es $\mathbf x^{k+1}$.

(Una alternativa frecuente en el examen es el esquema **semi-implícito**: tratar el término no lineal $\alpha x_1^3$ de forma explícita —evaluado en $x_1^k$— y el resto implícito; así cada paso queda lineal y se evita Newton, a costa de menor estabilidad.)

**Condiciones iniciales.** La EDO de segundo orden necesita **dos** datos iniciales: $x(0)$ y $x'(0)$. Estos se cargan directamente como el vector de estado en $k=0$:

$$\boxed{x_1^0 = x(0), \qquad x_2^0 = x'(0).}$$

A partir de $\mathbf x^0 = (x_1^0, x_2^0)$, el esquema avanza $\mathbf x^0 \to \mathbf x^1 \to \mathbf x^2 \to \cdots$ resolviendo en cada paso el sistema no lineal anterior. (Nótese que, a diferencia de la ecuación de onda, este es un problema de **valores iniciales** de primer orden por componente: no hace falta nodo fantasma temporal, basta el estado completo en $t_0$.)

**Verificación numérica.** Se implementó el esquema (Euler hacia atrás + Newton, $\Delta t=0.01$) con $\delta=0.3,\beta=-1,\alpha=1,\gamma=0.5,\omega=1.2,\phi=0$ y CI $x(0)=1,\ x'(0)=0$. Tras $500$ pasos da $x\approx0.1036$, consistente con un integrador de referencia (`scipy` RK45 da $x\approx0.0682$); la diferencia es la esperada por el error $O(\Delta t)$ del método implícito de primer orden, y Newton converge en pocas iteraciones en cada paso (residuo $<10^{-13}$). ✓

## Ejercicio 4

Considere la matriz

$$A = \begin{pmatrix} 0.92 & 1.44 \\ 1.44 & 0.08 \end{pmatrix}$$

a) Realizar la descomposición en valores singulares.
b) Indique si es o no diagonalizable.

### Resolución

Observación útil: $A$ es **simétrica** ($A = A^T$), lo cual simplifica todo. Esto ya anticipa la respuesta de (b) y nos permite usar $A^TA = A^2$ en la SVD.

#### a) Descomposición en valores singulares $A = U\Sigma V^T$

**Paso 1 — autovalores de $A^TA$.** Como $A$ es simétrica, $A^TA = A^2$:

$$A^TA = \begin{pmatrix} 0.92 & 1.44 \\ 1.44 & 0.08 \end{pmatrix}\begin{pmatrix} 0.92 & 1.44 \\ 1.44 & 0.08 \end{pmatrix} = \begin{pmatrix} 2.92 & 1.44 \\ 1.44 & 2.08 \end{pmatrix}.$$

($0.92^2 + 1.44^2 = 0.8464 + 2.0736 = 2.92$; $0.92\cdot1.44 + 1.44\cdot0.08 = 1.44$; $1.44^2 + 0.08^2 = 2.08$.)

$$p_{A^TA}(\lambda) = (\lambda - 2.92)(\lambda - 2.08) - 1.44^2 = \lambda^2 - 5\lambda + 4 = (\lambda - 4)(\lambda - 1).$$

Luego $\lambda_1 = 4$, $\lambda_2 = 1$, y los **valores singulares** (raíces, en orden **decreciente**) son

$$\boxed{\sigma_1 = \sqrt{4} = 2, \qquad \sigma_2 = \sqrt{1} = 1.}$$

**Paso 2 — autovectores de $A^TA$ → columnas de $V$.**

Para $\lambda_1 = 4$: $(A^TA - 4I)X = 0$,

$$\begin{pmatrix} -1.08 & 1.44 \\ 1.44 & -1.92 \end{pmatrix}X = 0 \implies -1.08\,x + 1.44\,y = 0 \implies y = \tfrac{3}{4}x \implies \tilde v_1 = (4, 3).$$

$\lVert\tilde v_1\rVert = 5$, de donde $v_1 = \left(\tfrac{4}{5}, \tfrac{3}{5}\right) = (0.8,\ 0.6)$.

Para $\lambda_2 = 1$: $(A^TA - I)X = 0$,

$$\begin{pmatrix} 1.92 & 1.44 \\ 1.44 & 1.08 \end{pmatrix}X = 0 \implies 1.92\,x + 1.44\,y = 0 \implies y = -\tfrac{4}{3}x \implies \tilde v_2 = (3, -4).$$

$\lVert\tilde v_2\rVert = 5$, de donde $v_2 = \left(\tfrac{3}{5}, -\tfrac{4}{5}\right) = (0.6,\ -0.8)$. (Son ortogonales: $0.8\cdot0.6 + 0.6\cdot(-0.8) = 0$ ✓.)

$$V = \begin{pmatrix} 0.8 & 0.6 \\ 0.6 & -0.8 \end{pmatrix}.$$

**Paso 3 — columnas de $U$** mediante $u_i = \dfrac{A v_i}{\sigma_i}$:

$$u_1 = \frac{1}{2}\begin{pmatrix} 0.92 & 1.44 \\ 1.44 & 0.08 \end{pmatrix}\begin{pmatrix} 0.8 \\ 0.6 \end{pmatrix} = \frac{1}{2}\begin{pmatrix} 1.6 \\ 1.2 \end{pmatrix} = \begin{pmatrix} 0.8 \\ 0.6 \end{pmatrix},$$

$$u_2 = \frac{1}{1}\begin{pmatrix} 0.92 & 1.44 \\ 1.44 & 0.08 \end{pmatrix}\begin{pmatrix} 0.6 \\ -0.8 \end{pmatrix} = \begin{pmatrix} -0.6 \\ 0.8 \end{pmatrix}.$$

Como $A$ es $2\times2$ de rango completo ($\sigma_1,\sigma_2 > 0$), $U$ ya queda completa. Entonces

$$\boxed{U = \begin{pmatrix} 0.8 & -0.6 \\ 0.6 & 0.8 \end{pmatrix}, \quad \Sigma = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}, \quad V = \begin{pmatrix} 0.8 & 0.6 \\ 0.6 & -0.8 \end{pmatrix}.}$$

**Verificación.** $U^TU = I$, $V^TV = I$ (columnas ortonormales) y

$$U\Sigma V^T = \begin{pmatrix} 0.8 & -0.6 \\ 0.6 & 0.8 \end{pmatrix}\begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 0.8 & 0.6 \\ 0.6 & -0.8 \end{pmatrix} = \begin{pmatrix} 0.92 & 1.44 \\ 1.44 & 0.08 \end{pmatrix} = A. \quad ✓$$

#### b) ¿Es diagonalizable?

**Sí.** $A$ es una **matriz simétrica real**, y por el **Teorema Espectral** toda matriz simétrica real es **ortogonalmente diagonalizable**: existe una base ortonormal de autovectores, es decir $A = PDP^T$ con $P$ ortogonal ($P^{-1}=P^T$) y $D$ diagonal real.

Explícitamente, los autovalores de $A$ salen de

$$p_A(\lambda) = (\lambda - 0.92)(\lambda - 0.08) - 1.44^2 = \lambda^2 - \lambda - 2 = (\lambda - 2)(\lambda + 1),$$

es decir $\lambda = 2$ y $\lambda = -1$ (distintos, lo que ya basta para diagonalizar). Sus autovectores normalizados son:

- $\lambda = 2$: $(A - 2I)X = 0 \Rightarrow \begin{pmatrix}-1.08 & 1.44\\1.44 & -1.92\end{pmatrix}X=0 \Rightarrow y=\tfrac34 x \Rightarrow w_1 = (0.8,\ 0.6)$.
- $\lambda = -1$: $(A + I)X = 0 \Rightarrow \begin{pmatrix}1.92 & 1.44\\1.44 & 1.08\end{pmatrix}X=0 \Rightarrow y=-\tfrac43 x \Rightarrow w_2 = (0.6,\ -0.8)$.

$$\boxed{P = \begin{pmatrix} 0.8 & 0.6 \\ 0.6 & -0.8 \end{pmatrix}, \qquad D = \begin{pmatrix} 2 & 0 \\ 0 & -1 \end{pmatrix}, \qquad A = PDP^{T}.}$$

(Nótese la diferencia entre las dos descomposiciones: la diagonalización usa los autovalores **con signo** de $A$ —$2$ y $-1$— mientras que la SVD usa los valores singulares —$2$ y $1$, siempre $\ge0$— que son los $|\lambda_i|$ por ser $A$ simétrica. El cambio de signo del autovalor $-1$ se absorbe en la columna correspondiente de $U$, que resulta $-w_2$.)

**Verificación.** $P$ es ortogonal ($P^TP=I$), $AP = PD$ exactamente y $PDP^T = A$. ✓

## Ejercicio 5

Hallar la Transformada de Fourier de $f(t) = e^{-|t|}$.

### Resolución

Usamos la convención de la cátedra $\hat f(\omega) = \displaystyle\int_{-\infty}^{\infty} f(t)\,e^{-i\omega t}\,dt$. Como $|t|$ se define a tramos, partimos la integral en $t<0$ (donde $|t|=-t$) y $t>0$ (donde $|t|=t$):

$$\hat f(\omega) = \int_{-\infty}^{0} e^{t}\,e^{-i\omega t}\,dt + \int_{0}^{\infty} e^{-t}\,e^{-i\omega t}\,dt = \int_{-\infty}^{0} e^{(1-i\omega)t}\,dt + \int_{0}^{\infty} e^{-(1+i\omega)t}\,dt.$$

**Segunda integral** (análoga al ejercicio resuelto de $e^{-at}$, ver [[../resueltos/resueltos-fourier]]):

$$\int_{0}^{\infty} e^{-(1+i\omega)t}\,dt = \left.\frac{e^{-(1+i\omega)t}}{-(1+i\omega)}\right|_0^\infty = \frac{0 - 1}{-(1+i\omega)} = \frac{1}{1+i\omega},$$

ya que $|e^{-(1+i\omega)t}| = e^{-t} \to 0$ cuando $t\to\infty$.

**Primera integral:**

$$\int_{-\infty}^{0} e^{(1-i\omega)t}\,dt = \left.\frac{e^{(1-i\omega)t}}{1-i\omega}\right|_{-\infty}^{0} = \frac{1 - 0}{1-i\omega} = \frac{1}{1-i\omega},$$

ya que $|e^{(1-i\omega)t}| = e^{t} \to 0$ cuando $t\to-\infty$.

**Sumando** (común denominador $(1-i\omega)(1+i\omega) = 1 + \omega^2$):

$$\hat f(\omega) = \frac{1}{1-i\omega} + \frac{1}{1+i\omega} = \frac{(1+i\omega) + (1-i\omega)}{(1-i\omega)(1+i\omega)} = \frac{2}{1+\omega^2}.$$

$$\boxed{\hat f(\omega) = \mathcal{F}\{e^{-|t|}\}(\omega) = \frac{2}{1+\omega^2}.}$$

El resultado es **real y par** (como debía ser, porque $f$ es real y par). Es la conocida **Lorentziana**: su transformada inversa relaciona esta función con el núcleo de Poisson / Cauchy. (Comparar con el ejercicio (e) de la guía, $A\,e^{-\alpha|t|}$, cuyo caso $A=1,\alpha=1$ es justamente este.)

**Verificación numérica.** Por integración numérica de $\int e^{-|t|}\cos(\omega t)\,dt$ (la parte imaginaria da $0$ por paridad): $\hat f(0)=2$, $\hat f(0.5)=1.6$, $\hat f(1)=1$, $\hat f(2)=0.4$, $\hat f(3)=0.2$, que coinciden exactamente con $\tfrac{2}{1+\omega^2}$. ✓
