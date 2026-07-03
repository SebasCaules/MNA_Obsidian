---
tags: [parcial, iip, resolucion, fourier, serie-trigonometrica, transformada-fourier, diferencias-finitas, ecuacion-calor]
fuente: raw/Practicas/Modelos_Examenes/MNA_IIP_Tema_IV.pdf
tipo: iip
tema: 4
tiene_resolucion: true
---

# Segundo Parcial de Métodos Numéricos Avanzados — Tema IV (Resolución)

Ver enunciado en [[iip-tema-04]]. Convenciones de Fourier y diferencias finitas en [[../guias/guia-08-fourier-series]] y [[../resueltos/resueltos-fourier]].

## Ejercicio 1

Sea la función $x(t) = t^2$ en el intervalo $(0, 2\pi)$, con $x(t) = x(t + 2\pi)$ (período $T = 2\pi$).

a) Hallar la Serie Trigonométrica de Fourier de $x(t)$.
b) Usando el desarrollo hallado en a), hallar el desarrollo de $y(t) = x'(t)$.

### Resolución

Con $T = 2\pi$ la frecuencia fundamental es $\omega_0 = \dfrac{2\pi}{T} = 1$, así que los armónicos son $\cos(nt)$ y $\sin(nt)$. Usamos la convención de la cátedra (con $a_0$ = **valor medio**):

$$x(t) = a_0 + \sum_{n=1}^{\infty} a_n\cos(nt) + \sum_{n=1}^{\infty} b_n\sin(nt),\qquad a_0 = \frac{1}{T}\int_0^{2\pi}\!\! x,\quad a_n = \frac{2}{T}\int_0^{2\pi}\!\! x\cos(nt)\,dt,\quad b_n = \frac{2}{T}\int_0^{2\pi}\!\! x\sin(nt)\,dt.$$

**a) Coeficientes.**

**Término medio:**

$$a_0 = \frac{1}{2\pi}\int_0^{2\pi} t^2\,dt = \frac{1}{2\pi}\cdot\frac{t^3}{3}\Big|_0^{2\pi} = \frac{1}{2\pi}\cdot\frac{8\pi^3}{3} = \boxed{\frac{4\pi^2}{3}}\;(\approx 13.1595).$$

**Coeficiente coseno.** Integrando por partes dos veces $\displaystyle\int_0^{2\pi} t^2\cos(nt)\,dt$:

$$\int t^2\cos(nt)\,dt = \frac{t^2\sin(nt)}{n} + \frac{2t\cos(nt)}{n^2} - \frac{2\sin(nt)}{n^3}.$$

Evaluado en $[0, 2\pi]$, los senos se anulan ($\sin(2\pi n) = 0$) y queda sólo el término coseno:

$$\int_0^{2\pi} t^2\cos(nt)\,dt = \frac{2(2\pi)\cos(2\pi n)}{n^2} - 0 = \frac{4\pi}{n^2}.$$

$$a_n = \frac{2}{2\pi}\cdot\frac{4\pi}{n^2} = \boxed{\frac{4}{n^2}}.$$

**Coeficiente seno.** Análogamente $\displaystyle\int t^2\sin(nt)\,dt = -\frac{t^2\cos(nt)}{n} + \frac{2t\sin(nt)}{n^2} + \frac{2\cos(nt)}{n^3}$, y al evaluar en $[0, 2\pi]$ sólo sobrevive el primer término:

$$\int_0^{2\pi} t^2\sin(nt)\,dt = -\frac{(2\pi)^2\cos(2\pi n)}{n} = -\frac{4\pi^2}{n}.$$

$$b_n = \frac{2}{2\pi}\cdot\left(-\frac{4\pi^2}{n}\right) = \boxed{-\frac{4\pi}{n}}.$$

Por lo tanto, la serie trigonométrica es

$$\boxed{\;x(t) \sim \frac{4\pi^2}{3} + \sum_{n=1}^{\infty}\frac{4}{n^2}\cos(nt) - \sum_{n=1}^{\infty}\frac{4\pi}{n}\sin(nt).\;}$$

> **Convergencia (Dirichlet).** En puntos de continuidad la serie converge a $t^2$ (extendida por período). En el borde $t = 0 \equiv 2\pi$ hay un **salto** entre $x(2\pi^-) = 4\pi^2$ y $x(0^+) = 0$; allí la serie converge al promedio $\tfrac12(4\pi^2 + 0) = 2\pi^2$.

*Verificación numérica.* Las integrales simbólicas confirman $a_0 = \tfrac{4\pi^2}{3}$, $a_n = \tfrac{4}{n^2}$, $b_n = -\tfrac{4\pi}{n}$. Sumas parciales: en $t = \pi$ (continuidad) la serie da $9.86960\approx\pi^2$; en $t = 0$ (salto) tiende a $\approx 2\pi^2 = 19.739$ ✓.

**b) Desarrollo de $y(t) = x'(t)$.**

Derivando la serie **término a término** (regla $\frac{d}{dt}[a_n\cos(nt) + b_n\sin(nt)] = -a_n\,n\sin(nt) + b_n\,n\cos(nt)$, y el término constante $a_0$ desaparece):

$$y(t) \sim \sum_{n=1}^{\infty}\big(-a_n\,n\sin(nt) + b_n\,n\cos(nt)\big) = \sum_{n=1}^{\infty}\left(-\frac{4}{n}\sin(nt) - 4\pi\cos(nt)\right).$$

Clásicamente $x'(t) = 2t$ en $(0, 2\pi)$ (período $2\pi$). Comparemos con la serie *directa* de $2t$. Su valor medio es $\alpha_0 = \tfrac{1}{2\pi}\int_0^{2\pi} 2t\,dt = 2\pi$, sus cosenos son $\alpha_n = \tfrac{2}{2\pi}\int_0^{2\pi}2t\cos(nt)\,dt = 0$ y sus senos $\beta_n = \tfrac{2}{2\pi}\int_0^{2\pi}2t\sin(nt)\,dt = -\tfrac{4}{n}$, es decir

$$2t \sim 2\pi - \sum_{n=1}^{\infty}\frac{4}{n}\sin(nt).$$

> **Punto sutil (el detalle que «cierra» el ejercicio).** Los **senos coinciden** ($-\tfrac{4}{n}$ en ambas). El término $-4\pi\sum_n\cos(nt)$ que aparece al derivar **no es despreciable**: la identidad de sumabilidad $\sum_{n\ge1}\cos(nt) = -\tfrac12$ (Abel/Cesàro, para $t\notin 2\pi\mathbb Z$) hace que $-4\pi\cdot(-\tfrac12) = 2\pi$, **exactamente el valor medio que le faltaba a la serie derivada**. Así, la serie derivada término a término representa efectivamente a $x'(t) = 2t$ en el interior. El motivo por el que aparece como serie divergente de cosenos en lugar de una constante $2\pi$ es el **salto** de $x(t)$ en $t = 2\pi$: la derivada en sentido distribucional incluye un tren de deltas $-4\pi^2\sum_k\delta(t - 2\pi k)$, y ese término $-4\pi\sum\cos(nt)$ es justamente su serie de Fourier. Por eso la derivación término a término es lícita salvo en los saltos.

$$\boxed{\;y(t) = x'(t) \sim -4\pi\sum_{n=1}^{\infty}\cos(nt) - \sum_{n=1}^{\infty}\frac{4}{n}\sin(nt)\;\;\equiv\;\; 2\pi - \sum_{n=1}^{\infty}\frac{4}{n}\sin(nt) = 2t\ \text{ en } (0, 2\pi).\;}$$

*Verificación numérica.* Sumando $\beta_n$ contra $2t$ punto a punto en $(0, 2\pi)$ el error es $<10^{-3}$ con $N\sim10^4$ armónicos (Gibbs cerca del salto); y la suma de Abel $\sum r^n\cos(nt)\to -\tfrac12$ al $r\to1^-$ ✓.

## Ejercicio 2

Dada la función $x(t) = t^2$ si $0 \le t \le 2\pi$ y $x(t) = 0$ en otro caso. Hallar su Transformada de Fourier.

### Resolución

Con la convención $\hat x(\omega) = \displaystyle\int_{-\infty}^{\infty} x(t)e^{-i\omega t}\,dt$ y soporte compacto $[0, 2\pi]$:

$$\hat x(\omega) = \int_0^{2\pi} t^2\,e^{-i\omega t}\,dt.$$

**Integración por partes (dos veces).** Una primitiva de $t^2 e^{-i\omega t}$ es

$$\int t^2 e^{-i\omega t}\,dt = e^{-i\omega t}\left(\frac{i\,t^2}{\omega} + \frac{2t}{\omega^2} - \frac{2i}{\omega^3}\right),$$

que se obtiene con $\frac{1}{i\omega} = -\frac{i}{\omega}$, $\frac{1}{(i\omega)^2} = -\frac{1}{\omega^2}$, $\frac{1}{(i\omega)^3} = \frac{i}{\omega^3}$. (Se verifica derivando: $\tfrac{d}{dt}$ de la primitiva da $t^2 e^{-i\omega t}$.) Evaluando en $[0, 2\pi]$:

- En $t = 2\pi$: $\;e^{-2\pi i\omega}\left(\dfrac{i\,(2\pi)^2}{\omega} + \dfrac{2(2\pi)}{\omega^2} - \dfrac{2i}{\omega^3}\right)$.
- En $t = 0$: $\;1\cdot\left(0 + 0 - \dfrac{2i}{\omega^3}\right) = -\dfrac{2i}{\omega^3}$.

Restando ($\omega \ne 0$):

$$\boxed{\;\hat x(\omega) = e^{-2\pi i\omega}\left(\frac{4\pi^2 i}{\omega} + \frac{4\pi}{\omega^2} - \frac{2i}{\omega^3}\right) + \frac{2i}{\omega^3}.\;}$$

En forma compacta equivale a

$$\hat x(\omega) = \frac{2\big(2\pi^2\omega^2\,i + 2\pi\omega + i\,e^{2\pi i\omega} - i\big)\,e^{-2\pi i\omega}}{\omega^3},$$

con partes real e imaginaria (escribiendo $e^{-2\pi i\omega} = \cos(2\pi\omega) - i\sin(2\pi\omega)$):

$$\operatorname{Re}\hat x(\omega) = \frac{2\big(2\pi^2\omega^2\sin(2\pi\omega) + 2\pi\omega\cos(2\pi\omega) - \sin(2\pi\omega)\big)}{\omega^3},$$
$$\operatorname{Im}\hat x(\omega) = \frac{2\big(2\pi^2\omega^2\cos(2\pi\omega) - 2\pi\omega\sin(2\pi\omega) - \cos(2\pi\omega) + 1\big)}{\omega^3}.$$

**Caso $\omega = 0$ (valor en el origen).** Por L'Hôpital o directamente $\hat x(0) = \displaystyle\int_0^{2\pi} t^2\,dt = \boxed{\dfrac{8\pi^3}{3}}\;(\approx 82.6834)$, que es el límite continuo de la expresión anterior.

**Caso $\omega = n$ entero (control con la serie del Ej. 1).** Como $e^{-2\pi i n} = 1$, los términos $\mp\tfrac{2i}{\omega^3}$ se cancelan y queda

$$\hat x(n) = \frac{4\pi^2 i}{n} + \frac{4\pi}{n^2} = \pi\Big(\underbrace{\tfrac{4}{n^2}}_{a_n} + i\,\underbrace{\tfrac{4\pi}{n}}_{-b_n}\Big),$$

coherente con los coeficientes del Ejercicio 1 (la TF en $\omega = n$ codifica $\pi(a_n - i\,b_n)$), lo que sirve de chequeo cruzado.

*Verificación numérica.* La forma cerrada coincide con la integral por cuadratura en $\omega \in \{0.5, 1, 2, 3, -1.5, 5\}$ a $\sim10^{-14}$, y $\hat x(0) = 82.6834$ ✓. (Importó cuidar los signos al reemplazar $\tfrac{1}{(i\omega)^k}$: el término $+\tfrac{2t}{\omega^2}$ lleva signo $+$, no $-$.)

## Ejercicio 3

Dada la ecuación del calor $\dfrac{\partial u}{\partial t} = \dfrac{\partial^2 u}{\partial x^2}$, desarrollar un esquema de diferencias finitas **implícito** con 4 nodos internos para:

a) $u(0, t) = u(1, t) = 0$ (Dirichlet) y $u(x, 0) = \sin(x)$.
b) $u_x(0, t) = u(1, t) = 0$ (mixto: Neumann en $x = 0$, Dirichlet en $x = 1$) y $u(x, 0) = \cos(x)$.

### Resolución

**Malla común.** Dominio $x \in [0, 1]$, $h = \tfrac15 = 0.2$, nodos

$$x_0 = 0,\quad x_1 = 0.2,\quad x_2 = 0.4,\quad x_3 = 0.6,\quad x_4 = 0.8,\quad x_5 = 1,$$

con 4 nodos **internos** $x_1, \dots, x_4$. Notación $u_i^k \approx u(x_i, t_k)$, paso temporal $\Delta t$ y $r = \dfrac{\Delta t}{h^2}$.

**Esquema implícito (Euler hacia atrás en tiempo, central en espacio).** Aproximamos $u_t \approx \dfrac{u_i^{k+1} - u_i^k}{\Delta t}$ y $u_{xx} \approx \dfrac{u_{i-1}^{k+1} - 2u_i^{k+1} + u_{i+1}^{k+1}}{h^2}$. Igualando y multiplicando por $\Delta t$:

$$-r\,u_{i-1}^{k+1} + (1 + 2r)\,u_i^{k+1} - r\,u_{i+1}^{k+1} = u_i^k.$$

El sistema a resolver en cada paso es $M\,\mathbf u^{k+1} = \mathbf b^k$.

#### a) Dirichlet homogéneo

Las incógnitas son los 4 nodos internos $u_1, u_2, u_3, u_4$. Los bordes son **conocidos** y homogéneos, $u_0^{k+1} = u_5^{k+1} = 0$, así que **desaparecen del lado derecho**. Escribiendo la ecuación por nodo:

$$
\begin{aligned}
(1+2r)u_1 - r\,u_2 &= u_1^k & &(\text{el término } -r\,u_0 = 0)\\
-r\,u_1 + (1+2r)u_2 - r\,u_3 &= u_2^k\\
-r\,u_2 + (1+2r)u_3 - r\,u_4 &= u_3^k\\
-r\,u_3 + (1+2r)u_4 &= u_4^k & &(\text{el término } -r\,u_5 = 0)
\end{aligned}
$$

Matriz **tridiagonal** $4\times4$ (simétrica):

$$M = \begin{pmatrix} 1+2r & -r & 0 & 0 \\ -r & 1+2r & -r & 0 \\ 0 & -r & 1+2r & -r \\ 0 & 0 & -r & 1+2r \end{pmatrix},\qquad \mathbf b^k = \begin{pmatrix} u_1^k \\ u_2^k \\ u_3^k \\ u_4^k \end{pmatrix}.$$

**Condición inicial** $u_i^0 = \sin(x_i)$ en los nodos internos $x_i = 0.2, 0.4, 0.6, 0.8$:

$$\mathbf u^0 = \begin{pmatrix} \sin 0.2 \\ \sin 0.4 \\ \sin 0.6 \\ \sin 0.8 \end{pmatrix} = \begin{pmatrix} 0.1987 \\ 0.3894 \\ 0.5646 \\ 0.7174 \end{pmatrix}.$$

El primer paso resuelve $M\,\mathbf u^1 = \mathbf u^0$; en pasos sucesivos $\mathbf b^k = \mathbf u^k$.

*Verificación numérica.* Con $r = 0.5$, resolviendo $M\,\mathbf u^1 = \mathbf u^0$ se obtiene $\mathbf u^1 \approx (0.1908,\ 0.3660,\ 0.4944,\ 0.4823)$ y $\|M\mathbf u^1 - \mathbf u^0\| \approx 10^{-16}$ ✓.

#### b) Mixto: Neumann en $x_0$, Dirichlet en $x_5$

La condición $u_x(0, t) = 0$ **no fija** $u_0$, de modo que $x_0$ pasa a ser **incógnita**. Para escribir $u_{xx}$ en $x_0$ se introduce un **nodo fantasma** $x_{-1} = -h$ y se discretiza la derivada de borde con diferencia central:

$$u_x(0, t) \approx \frac{u_1^{k+1} - u_{-1}^{k+1}}{2h} = 0 \;\Longrightarrow\; u_{-1}^{k+1} = u_1^{k+1}.$$

Sustituyendo en la ecuación general del nodo $x_0$ ($-r\,u_{-1} + (1+2r)u_0 - r\,u_1 = u_0^k$):

$$-r\,u_1 + (1+2r)u_0 - r\,u_1 = u_0^k \;\Longrightarrow\; \boxed{(1+2r)u_0 - 2r\,u_1 = u_0^k}.$$

Esa es la **primera fila** (el factor $-2r$ es la firma del Neumann). Los nodos $x_1, x_2, x_3$ son internos estándar; en $x_4$, el borde Dirichlet $u_5^{k+1} = 0$ desaparece del RHS. Las incógnitas pasan a ser $u_0, u_1, u_2, u_3, u_4$ y el sistema crece a $5\times5$:

$$
\begin{aligned}
(1+2r)u_0 - 2r\,u_1 &= u_0^k & &(\text{Neumann, fantasma } u_{-1}=u_1)\\
-r\,u_0 + (1+2r)u_1 - r\,u_2 &= u_1^k\\
-r\,u_1 + (1+2r)u_2 - r\,u_3 &= u_2^k\\
-r\,u_2 + (1+2r)u_3 - r\,u_4 &= u_3^k\\
-r\,u_3 + (1+2r)u_4 &= u_4^k & &(\text{Dirichlet } u_5 = 0)
\end{aligned}
$$

$$M = \begin{pmatrix} 1+2r & -2r & 0 & 0 & 0 \\ -r & 1+2r & -r & 0 & 0 \\ 0 & -r & 1+2r & -r & 0 \\ 0 & 0 & -r & 1+2r & -r \\ 0 & 0 & 0 & -r & 1+2r \end{pmatrix},\qquad \mathbf b^k = \begin{pmatrix} u_0^k \\ u_1^k \\ u_2^k \\ u_3^k \\ u_4^k \end{pmatrix}.$$

> Notar que esta $M$ **no es simétrica**: la primera fila tiene $-2r$ pero la segunda columna en la fila 0 no se "refleja" en la fila 1 (que tiene $-r$). Es la asimetría típica que introduce el nodo fantasma de Neumann.

**Condición inicial** $u_i^0 = \cos(x_i)$, ahora **incluyendo $x_0 = 0$** (porque es incógnita), en $x_i = 0, 0.2, 0.4, 0.6, 0.8$:

$$\mathbf u^0 = \begin{pmatrix} \cos 0 \\ \cos 0.2 \\ \cos 0.4 \\ \cos 0.6 \\ \cos 0.8 \end{pmatrix} = \begin{pmatrix} 1.0000 \\ 0.9801 \\ 0.9211 \\ 0.8253 \\ 0.6967 \end{pmatrix}.$$

*Verificación numérica.* Con $r = 0.5$, $M\,\mathbf u^1 = \mathbf u^0$ da $\mathbf u^1 \approx (0.9790,\ 0.9580,\ 0.8928,\ 0.7712,\ 0.5411)$ con residuo $\sim10^{-16}$, y la fila Neumann reconstruida ($-r u_1 + (1+2r)u_0 - r u_1$) recupera $u_0^0 = 1$ ✓.

---

> **Resumen de puntos sutiles.**
> 1. **Ej. 1b:** la derivada término a término genera un término divergente $-4\pi\sum\cos(nt)$ que, sumado en sentido Abel/Cesàro, aporta exactamente el valor medio $2\pi$ de $2t$ (es la firma del salto periódico de $t^2$). La serie derivada **sí** representa $x'(t) = 2t$.
> 2. **Ej. 2:** atención a los signos al expandir $\tfrac{1}{(i\omega)^k}$; el coeficiente de $1/\omega^2$ es $+4\pi$. El valor en $\omega = n$ entero reproduce los coeficientes del Ej. 1.
> 3. **Ej. 3b:** el Neumann convierte el borde en incógnita (sistema $5\times5$), su fila lleva $-2r$ y la matriz deja de ser simétrica; la CI debe evaluarse también en $x_0 = 0$.
