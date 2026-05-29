---
tags: [final, resolucion, transformaciones-lineales, diagonalizacion, fourier-series, fourier-transform, diferencias-finitas, edo]
fuente: raw/Practicas/Modelos_Examenes/MNA_Final_Tema_III.pdf
tipo: final
tema: 3
tiene_resolucion: true
---

# Final de Métodos Numéricos Avanzados — Tema III (Resolución)

## Ejercicio 1

Sea la Transformación Lineal $T : \mathbb{R}^3 \to \mathbb{R}^3 : T(x, y, z) = (x + 3y,\ x + y - z,\ z - x - y)$.

a) Hallar la matriz asociada $M_{BB}(T)$ con $B = \{(0, 0, 1),\ (1, 0, 0),\ (1, -1, 0)\}$.

b) ¿Es $T$ diagonalizable en $\mathbb{R}$?

### Resolución

**Matriz en base canónica.** La columna $j$ de $M_{EE}(T)$ es $T(e_j)$ escrito en coordenadas canónicas:

$$T(1,0,0) = (1,\ 1,\ -1),\quad T(0,1,0) = (3,\ 1,\ -1),\quad T(0,0,1) = (0,\ -1,\ 1),$$

$$M_{EE}(T) = \begin{pmatrix} 1 & 3 & 0 \\ 1 & 1 & -1 \\ -1 & -1 & 1 \end{pmatrix}.$$

**a) Cambio de base.** La matriz de paso $P$ tiene por columnas los vectores de $B$ expresados en la base canónica:

$$P = \big(b_1 \mid b_2 \mid b_3\big) = \begin{pmatrix} 0 & 1 & 1 \\ 0 & 0 & -1 \\ 1 & 0 & 0 \end{pmatrix},\qquad \det P = -1 \ne 0.$$

Entonces $M_{BB}(T) = P^{-1}\,M_{EE}(T)\,P$. Conviene calcular columna por columna usando que **la columna $j$ de $M_{BB}$ es $[T(b_j)]_B = P^{-1}\,T(b_j)$**:

$$T(b_1) = T(0,0,1) = (0,\ -1,\ 1) \;\Rightarrow\; [T(b_1)]_B = (1,\ -1,\ 1),$$
$$T(b_2) = T(1,0,0) = (1,\ 1,\ -1) \;\Rightarrow\; [T(b_2)]_B = (-1,\ 2,\ -1),$$
$$T(b_3) = T(1,-1,0) = (-2,\ 0,\ 0) \;\Rightarrow\; [T(b_3)]_B = (0,\ -2,\ 0).$$

(Por ejemplo, para $b_3$: resolver $x_1 b_1 + x_2 b_2 + x_3 b_3 = (-2,0,0)$ da $x_3 = 0$ desde la 2ª coord., $x_1 = 0$ desde la 3ª coord. y $x_2 = -2$ desde la 1ª.) Apilando las columnas:

$$\boxed{M_{BB}(T) = \begin{pmatrix} 1 & -1 & 0 \\ -1 & 2 & -2 \\ 1 & -1 & 0 \end{pmatrix}.}$$

**Verificación.** $P^{-1} M_{EE} P$ reproduce exactamente esta matriz ✓ (chequeado con numpy).

**b) Diagonalizabilidad.** La diagonalizabilidad es una propiedad de $T$, independiente de la base, así que basta estudiar los autovalores de $M_{EE}$ (que son los mismos que los de $M_{BB}$, por ser matrices semejantes). El polinomio característico es

$$p(\lambda) = \det\!\big(\lambda I - M_{EE}\big) = \lambda^3 - 3\lambda^2 - \lambda = \lambda\,(\lambda^2 - 3\lambda - 1).$$

(El término independiente es $-\det M_{EE} = 0$, y el coeficiente de $\lambda^2$ es $-\operatorname{tr} M_{EE} = -3$.) Las raíces son

$$\lambda_1 = 0,\qquad \lambda_{2,3} = \frac{3 \pm \sqrt{13}}{2} \approx \{\,3.3028,\ -0.3028\,\}.$$

Como $\sqrt{13}\in\mathbb{R}$, los **tres autovalores son reales y distintos**. Una matriz $3\times3$ con tres autovalores reales distintos tiene tres autovectores LI ($m_g = m_a = 1$ para cada uno), de modo que es diagonalizable sobre $\mathbb{R}$.

$$\boxed{T \text{ es diagonalizable en }\mathbb{R}\text{, con autovalores } 0,\ \tfrac{3-\sqrt{13}}{2},\ \tfrac{3+\sqrt{13}}{2}.}$$

**Verificación.** numpy/sympy confirman $\operatorname{spec}(M_{EE}) = \operatorname{spec}(M_{BB}) = \{0,\ \tfrac{3\pm\sqrt{13}}{2}\}$ y `is_diagonalizable() == True` ✓.

## Ejercicio 2

a) Hallar la serie de Fourier de $f(x) = x - x^2$ en $[0, 1]$, extendida periódicamente con $f(x) = f(x + 1)$ (período $T = 1$).

b) ¿A qué valor converge la serie en $x = 0$ y en $x = 1/2$?

### Resolución

Con $T = 1$, la frecuencia fundamental es $\tfrac{2\pi}{T} = 2\pi$ y la serie es

$$f(x) = a_0 + \sum_{n=1}^{\infty} a_n \cos(2\pi n x) + \sum_{n=1}^{\infty} b_n \sin(2\pi n x).$$

**a) Coeficientes.**

**Valor medio** ($a_0$ es directamente el promedio, sin dividir por 2):

$$a_0 = \int_0^1 (x - x^2)\,dx = \left[\frac{x^2}{2} - \frac{x^3}{3}\right]_0^1 = \frac{1}{2} - \frac{1}{3} = \boxed{\frac{1}{6}}.$$

**Coeficientes coseno:**

$$a_n = 2\int_0^1 (x - x^2)\cos(2\pi n x)\,dx.$$

Integrando por partes dos veces (los términos de borde se cancelan porque $\sin(2\pi n) = \sin 0 = 0$, y queda solo la contribución de $\cos(2\pi n) = 1$):

$$a_n = -\frac{1}{\pi^2 n^2}.$$

**Coeficientes seno:** $b_n = 0$ para todo $n$. La razón es de **simetría**: en $[0,1]$ la parábola $f(x) = x - x^2 = \tfrac14 - (x-\tfrac12)^2$ es simétrica respecto del eje $x = \tfrac12$, es decir $f(\tfrac12 + u) = f(\tfrac12 - u)$. Esto la hace **par alrededor del centro del período**, lo que anula la parte senoidal:

$$b_n = 2\int_0^1 (x - x^2)\sin(2\pi n x)\,dx = 0.$$

$$\boxed{f(x) = \frac{1}{6} - \frac{1}{\pi^2}\sum_{n=1}^{\infty} \frac{\cos(2\pi n x)}{n^2}.}$$

**Verificación.** La integración simbólica (sympy) confirma $a_0 = \tfrac16$, $a_n = -\tfrac{1}{\pi^2 n^2}$ y $b_n = 0$ para $n = 1, 2, 3, 4, \dots$ ✓. La suma parcial con $N = 2000$ armónicos reproduce $f$ en puntos interiores (p.ej. en $x = 0.25$ da $0.18750 = \tfrac{3}{16}$) ✓.

**b) Convergencia puntual (criterio de Dirichlet).** $f$ es continua y $C^1$ a trozos.

- **En $x = 0$** (que coincide con $x = 1$ por periodicidad): los límites laterales son $f(0^+) = 0$ y $f(1^-) = 1 - 1 = 0$. **Coinciden**, así que la extensión periódica es **continua** en $x = 0$ y la serie converge a

$$\boxed{f(0) = 0.}$$

  Esto da, evaluando la serie en $x = 0$, la identidad $\tfrac16 - \tfrac{1}{\pi^2}\sum \tfrac{1}{n^2} = 0$, es decir $\sum_{n\ge1}\tfrac1{n^2} = \tfrac{\pi^2}{6}$ (consistente ✓).

- **En $x = \tfrac12$**: $f$ es continua ahí, $f(\tfrac12) = \tfrac12 - \tfrac14 = \tfrac14$. La serie converge a

$$\boxed{f\!\left(\tfrac12\right) = \frac14.}$$

  (Equivalentemente, $\cos(\pi n) = (-1)^n$ da $\tfrac16 - \tfrac1{\pi^2}\sum\tfrac{(-1)^n}{n^2} = \tfrac16 + \tfrac1{12} = \tfrac14$, usando $\sum\tfrac{(-1)^n}{n^2} = -\tfrac{\pi^2}{12}$.)

**Verificación.** La suma parcial evaluada da $\to 0$ en $x = 0$ (residuo $\sim 10^{-4}$ con $N=2000$, decae como $1/N$) y exactamente $0.25$ en $x = 1/2$ ✓.

## Ejercicio 3

Dada la EDO $\dfrac{d^2 x}{dt^2} + \dfrac{dx}{dt} + 3x = \cos(t^2 + 1)$, con $x(0) = x'(0) = 0$.

a) Escribirla como sistema de primer orden.

b) Plantear un esquema implícito de diferencias finitas, indicando cómo se cargan las condiciones iniciales.

### Resolución

**a) Reducción a sistema de primer orden.** Definimos $x_1 = x$ y $x_2 = \dot x$. Entonces $\dot x_1 = x_2$ y, despejando de la EDO ($\ddot x = -\dot x - 3x + \cos(t^2+1)$):

$$\boxed{\begin{cases} \dot x_1 = x_2, \\[2pt] \dot x_2 = \cos(t^2 + 1) - x_2 - 3x_1, \end{cases}} \qquad x_1(0) = 0,\quad x_2(0) = 0.$$

En forma vectorial $\dot{\mathbf x} = M\,\mathbf x + \mathbf f(t)$ con

$$\mathbf x = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix},\qquad M = \begin{pmatrix} 0 & 1 \\ -3 & -1 \end{pmatrix},\qquad \mathbf f(t) = \begin{pmatrix} 0 \\ \cos(t^2 + 1) \end{pmatrix}.$$

(La parte homogénea es lineal con coeficientes constantes; el forzado $\cos(t^2+1)$ depende explícitamente de $t$ y va en $\mathbf f$.)

**b) Esquema implícito (Euler hacia atrás).** Con paso temporal $\Delta t$ y nodos $t_k = k\,\Delta t$, aproximamos la derivada por la diferencia hacia atrás y evaluamos el lado derecho en el **nuevo** instante $t_{k+1}$ (lo que vuelve el esquema implícito):

$$\frac{\mathbf x^{k+1} - \mathbf x^k}{\Delta t} = M\,\mathbf x^{k+1} + \mathbf f^{k+1},\qquad \mathbf f^{k+1} = \begin{pmatrix} 0 \\ \cos(t_{k+1}^2 + 1) \end{pmatrix}.$$

Reagrupando los términos en $\mathbf x^{k+1}$ al lado izquierdo:

$$\boxed{\big(I - \Delta t\,M\big)\,\mathbf x^{k+1} = \mathbf x^k + \Delta t\,\mathbf f^{k+1}.}$$

Como el sistema es **lineal**, en cada paso se resuelve un sistema $2\times2$ con la misma matriz:

$$I - \Delta t\,M = \begin{pmatrix} 1 & -\Delta t \\ 3\,\Delta t & 1 + \Delta t \end{pmatrix},\qquad \det\!\big(I - \Delta t\,M\big) = 1 + \Delta t + 3\,\Delta t^2 > 0\ \ \forall\,\Delta t.$$

El determinante nunca se anula, así que la matriz es **siempre invertible** y el esquema está bien planteado (incondicionalmente resoluble; además es A-estable por ser Euler implícito). Despejando:

$$\mathbf x^{k+1} = \big(I - \Delta t\,M\big)^{-1}\big(\mathbf x^k + \Delta t\,\mathbf f^{k+1}\big).$$

**Condiciones iniciales.** Se cargan directamente en el vector de arranque a partir de $x(0)=x'(0)=0$:

$$\mathbf x^0 = \begin{pmatrix} x_1^0 \\ x_2^0 \end{pmatrix} = \begin{pmatrix} x(0) \\ x'(0) \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}.$$

Luego se itera $k = 0, 1, 2, \dots$ resolviendo el sistema lineal anterior en cada paso.

**Verificación.** Implementado el esquema con $\Delta t = 10^{-3}$ y comparado contra un integrador de referencia (`scipy.integrate.solve_ivp`, RK45): en $t = 1$ da $x \approx 0.0984$ vs. $0.0986$ de referencia, y en $t = 3$ da $x \approx -0.00256$ vs. $-0.00266$ ✓. La discrepancia es la esperada para un método de orden 1 y disminuye al refinar $\Delta t$.

## Ejercicio 4

Hallar la Transformada de Fourier de $f(t) = t - t^2$ si $0 \le t \le 1$, y $0$ en otro caso.

### Resolución

La función tiene **soporte compacto** $[0,1]$, así que la integral se reduce a ese intervalo. Con la convención $\hat f(\omega) = \int_{-\infty}^{\infty} f(t)\,e^{-i\omega t}\,dt$:

$$\hat f(\omega) = \int_0^1 (t - t^2)\,e^{-i\omega t}\,dt.$$

**Integración por partes** (dos veces, con $u = t - t^2$ y $dv = e^{-i\omega t}dt$). Conviene usar $\displaystyle\int t^m e^{-i\omega t}dt$ y evaluar los bordes notando que en $t = 0$ y $t = 1$ el factor polinómico $t - t^2$ se anula, lo que simplifica los términos de frontera del primer paso. Separando en parte real e imaginaria, el resultado es

$$\boxed{\hat f(\omega) = \frac{2\sin\omega - \omega\,(1 + \cos\omega)}{\omega^3} \;+\; i\,\frac{\omega\sin\omega + 2\cos\omega - 2}{\omega^3}}\qquad (\omega \ne 0).$$

Equivalentemente, en forma compacta $\hat f(\omega) = \dfrac{2i\,(1 - e^{-i\omega}) - \omega\,(1 + e^{-i\omega})}{\omega^3}$.

**Valor en $\omega = 0$.** El caso $\omega = 0$ es la integral del área, $\hat f(0) = \int_0^1 (t - t^2)\,dt = \tfrac16$. Tomando el límite de la fórmula anterior (Taylor de $\sin,\cos$ a tercer orden) se recupera

$$\lim_{\omega\to0}\operatorname{Re}\hat f(\omega) = \frac16,\qquad \lim_{\omega\to0}\operatorname{Im}\hat f(\omega) = 0 \quad\Longrightarrow\quad \boxed{\hat f(0) = \frac16,}$$

como debe ser. (El polinomio en el numerador anula sus términos hasta orden $\omega^3$, dejando un cociente finito.)

**Verificación.** La integración simbólica (sympy) da exactamente esta $\operatorname{Re}/\operatorname{Im}$, y la integración numérica (`scipy.quad`) coincide en varios valores: $\hat f(1) \approx 0.14264 - 0.07792\,i$, $\hat f(2) \approx 0.08136 - 0.12671\,i$, $\hat f(\pi) \approx -0.12901\,i$, y $\hat f(0) = 0.16667 = \tfrac16$ ✓.
