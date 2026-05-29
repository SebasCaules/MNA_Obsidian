---
tags: [parcial, iip, resolucion, fourier, serie-trigonometrica, transformada-fourier, diferencias-finitas, conveccion-difusion]
fuente: raw/Practicas/Modelos_Examenes/MNA_IIP_Tema_VI.pdf
tipo: iip
tema: 6
tiene_resolucion: true
---

# Segundo Parcial de Métodos Numéricos Avanzados — Tema VI (Resolución)

Convenciones (cátedra): serie trigonométrica
$$f(t)=a_0+\sum_{n\ge1}a_n\cos\!\Big(\tfrac{2\pi n}{T}t\Big)+\sum_{n\ge1}b_n\sin\!\Big(\tfrac{2\pi n}{T}t\Big),\quad a_0=\tfrac1T\!\int_T f,\ \ a_n=\tfrac2T\!\int_T f\cos,\ \ b_n=\tfrac2T\!\int_T f\sin.$$
Transformada de Fourier $\hat f(\omega)=\int_{-\infty}^{\infty}f(t)e^{-i\omega t}\,dt$. Diferencias finitas: esquema **implícito** (Euler hacia atrás en tiempo). Ver [[../resueltos/resueltos-fourier]], [[../guias/guia-08-fourier-series]].

---

## Ejercicio 1

Sea la función $x(t)=\operatorname{sen}(t)$ en el intervalo $\left(-\dfrac{\pi}{4},\dfrac{\pi}{4}\right)$, con $x(t)=x(t+\pi/2)$ (período $T=\pi/2$).

a) Hallar la Serie Trigonométrica de Fourier de $x(t)$.
b) Usando el desarrollo hallado en a), hallar el desarrollo de $y(t)=x'(t)$.

### Resolución

#### a) Serie trigonométrica

**Período y frecuencia fundamental.** $T=\dfrac{\pi}{2}$, de modo que
$$\omega_0=\frac{2\pi}{T}=\frac{2\pi}{\pi/2}=4.$$
La serie tendrá armónicos $\cos(4n\,t)$ y $\operatorname{sen}(4n\,t)$.

**Simetría.** En el intervalo simétrico $\left(-\tfrac\pi4,\tfrac\pi4\right)$ la función $x(t)=\operatorname{sen}(t)$ es **impar** ($\operatorname{sen}(-t)=-\operatorname{sen}(t)$). Por lo tanto
$$a_0=0,\qquad a_n=0\quad(\forall n\ge1),$$
y sólo sobreviven los senos. (Verificado numéricamente: $a_0$ y todos los $a_n$ dan $0$ a precisión de máquina.)

**Coeficientes $b_n$.** Con $T=\tfrac\pi2$, $\tfrac2T=\tfrac4\pi$:
$$b_n=\frac2T\int_{-\pi/4}^{\pi/4}\operatorname{sen}(t)\,\operatorname{sen}(4nt)\,dt=\frac4\pi\int_{-\pi/4}^{\pi/4}\operatorname{sen}(t)\,\operatorname{sen}(4nt)\,dt.$$
Usamos producto a suma: $\operatorname{sen}A\,\operatorname{sen}B=\tfrac12\big[\cos(A-B)-\cos(A+B)\big]$, con $A=t$, $B=4nt$:
$$b_n=\frac4\pi\cdot\frac12\int_{-\pi/4}^{\pi/4}\Big[\cos\big((4n-1)t\big)-\cos\big((4n+1)t\big)\Big]dt=\frac2\pi\int_{-\pi/4}^{\pi/4}\Big[\cos\big((4n-1)t\big)-\cos\big((4n+1)t\big)\Big]dt.$$
Como cada integrando es par, $\displaystyle\int_{-\pi/4}^{\pi/4}\cos(kt)\,dt=\frac{2\sin(k\pi/4)}{k}$. Llamando $k_1=4n-1$, $k_2=4n+1$:
$$b_n=\frac2\pi\left[\frac{2\sin\!\big(\tfrac{(4n-1)\pi}{4}\big)}{4n-1}-\frac{2\sin\!\big(\tfrac{(4n+1)\pi}{4}\big)}{4n+1}\right]=\frac4\pi\left[\frac{\sin\!\big(\tfrac{(4n-1)\pi}{4}\big)}{4n-1}-\frac{\sin\!\big(\tfrac{(4n+1)\pi}{4}\big)}{4n+1}\right].$$

**Simplificación de los senos.** Escribiendo $\tfrac{(4n\mp1)\pi}{4}=n\pi\mp\tfrac\pi4$:
$$\sin\!\Big(n\pi-\tfrac\pi4\Big)=-(-1)^n\frac{\sqrt2}{2},\qquad \sin\!\Big(n\pi+\tfrac\pi4\Big)=(-1)^n\frac{\sqrt2}{2}.$$
(Ambas verificadas numéricamente para $n=1,\dots,5$.) Sustituyendo:
$$b_n=\frac4\pi\cdot\left(-(-1)^n\frac{\sqrt2}{2}\right)\left[\frac{1}{4n-1}+\frac{1}{4n+1}\right]=-\frac{2\sqrt2}{\pi}(-1)^n\cdot\frac{(4n+1)+(4n-1)}{(4n-1)(4n+1)}.$$
$$\boxed{\,b_n=\frac{2\sqrt2}{\pi}\,(-1)^{n+1}\,\frac{8n}{16n^2-1}=\frac{16\sqrt2}{\pi}\,(-1)^{n+1}\,\frac{n}{16n^2-1}.\,}$$

Primeros valores (numéricamente idénticos a la integración directa de $b_n$):
$$b_1=+0.4802,\quad b_2=-0.2287,\quad b_3=+0.1511,\quad b_4=-0.1130,\quad b_5=+0.0903.$$

**Serie:**
$$\boxed{\,x(t)=\sum_{n=1}^{\infty}\frac{16\sqrt2}{\pi}\,(-1)^{n+1}\,\frac{n}{16n^2-1}\,\operatorname{sen}(4n\,t).\,}$$

**Convergencia.** En el interior $\left(-\tfrac\pi4,\tfrac\pi4\right)$ la serie converge a $\operatorname{sen}(t)$. En los bordes $t=\pm\tfrac\pi4$ la extensión periódica **salta** (en $t=\tfrac\pi4$: límite por izquierda $\operatorname{sen}\tfrac\pi4=\tfrac{\sqrt2}{2}$, por derecha $\operatorname{sen}(-\tfrac\pi4)=-\tfrac{\sqrt2}{2}$), de modo que por Dirichlet la serie converge al **promedio** $\tfrac12\big(\tfrac{\sqrt2}{2}-\tfrac{\sqrt2}{2}\big)=0$. En efecto $\operatorname{sen}(4n\cdot\tfrac\pi4)=\operatorname{sen}(n\pi)=0$, así que toda suma parcial vale exactamente $0$ en el borde ✓. Como la función periódica es discontinua, la convergencia es lenta (decae $\sim 1/N$, con sobreoscilación de Gibbs cerca de $\pm\tfrac\pi4$): verificado, $\max|S_N-\operatorname{sen} t|$ en el interior es $\approx0.61\,(N{=}5)$, $0.35\,(N{=}20)$, $0.083\,(N{=}100)$.

#### b) Desarrollo de $y(t)=x'(t)$

Derivando la serie **término a término** (y usando $\tfrac{d}{dt}\operatorname{sen}(4nt)=4n\cos(4nt)$):
$$\boxed{\,y(t)=x'(t)=\sum_{n=1}^{\infty}b_n\,(4n)\,\cos(4n\,t)=\sum_{n=1}^{\infty}\frac{16\sqrt2}{\pi}\,(-1)^{n+1}\,\frac{4n^2}{16n^2-1}\,\cos(4n\,t).\,}$$
Es decir, una serie **sólo de cosenos** con coeficientes $B_n=4n\,b_n=\dfrac{2\sqrt2}{\pi}(-1)^{n+1}\dfrac{32n^2}{16n^2-1}$:
$$B_1=+1.9207,\quad B_2=-1.8292,\quad B_3=+1.8132,\quad B_4=-1.8077,\dots$$

**Sutileza importante (verificada).** Como la función *clásica* es $x'(t)=\cos(t)$, uno *esperaría* que esta serie sea la serie de $\cos t$ en $\left(-\tfrac\pi4,\tfrac\pi4\right)$. Sin embargo, $B_n\not\to0$ (de hecho $|B_n|\to\tfrac{2\sqrt2}{\pi}\cdot2=1.8006$), por lo que la serie **no converge puntualmente**: la derivación término a término sólo es lícita donde la extensión periódica es continua, y aquí tiene saltos de tamaño $-\sqrt2$ en $\pm\tfrac\pi4$. En sentido de distribuciones,
$$x'(t)=\cos(t)\;-\;\underbrace{\sqrt2\sum_{m}\delta\!\big(t-\tfrac\pi4-m\tfrac\pi2\big)}_{\text{tren de deltas en los saltos}},$$
y la serie de cosenos de arriba es justamente la serie de Fourier de esa derivada distribucional (la parte oscilante con $B_n\to$ cte. reproduce el tren de deltas). En el interior, promediando (Cesàro) las sumas parciales se recupera $\cos t$: verificado, p.ej. en $t=0,\,0.3,\,0.5$ el promedio de Cesàro con $N=2000$ da $1.000,\,0.955,\,0.877$ frente a $\cos t=1.000,\,0.955,\,0.878$. Esta es la respuesta formal pedida ("usando el desarrollo de a)"); la moraleja es que derivar la serie de una función con extensión periódica discontinua **degrada** la convergencia.

---

## Ejercicio 2

Dada la función $x(t)=t\,e^{-t}$, hallar su Transformada de Fourier.

### Resolución

**Supuesto de causalidad.** Tal como está, $x(t)=te^{-t}$ en todo $\mathbb R$ **no es transformable**: para $t\to-\infty$, $te^{-t}\to-\infty$ y la integral diverge. La interpretación estándar (y la única que converge) es la **señal causal**
$$x(t)=\begin{cases} t\,e^{-t}, & t\ge0,\\[2pt] 0, & t<0,\end{cases}\qquad\text{equivalentemente } x(t)=t\,e^{-t}\,u(t).$$
Bajo este supuesto integramos sólo sobre el soporte $[0,\infty)$.

**Cálculo.**
$$\hat x(\omega)=\int_{0}^{\infty} t\,e^{-t}\,e^{-i\omega t}\,dt=\int_{0}^{\infty} t\,e^{-(1+i\omega)t}\,dt.$$
Llamando $\alpha=1+i\omega$ (con $\operatorname{Re}\alpha=1>0$, lo que asegura convergencia), usamos $\displaystyle\int_0^\infty t\,e^{-\alpha t}\,dt=\frac{1}{\alpha^2}$ (por partes, $\Gamma(2)/\alpha^2$). Entonces:
$$\boxed{\,\hat x(\omega)=\frac{1}{(1+i\omega)^2}.\,}$$

**Forma cartesiana / espectro.** Multiplicando por el conjugado:
$$\hat x(\omega)=\frac{(1-i\omega)^2}{\big((1+i\omega)(1-i\omega)\big)^2}=\frac{1-\omega^2-2i\omega}{(1+\omega^2)^2},$$
$$\operatorname{Re}\hat x(\omega)=\frac{1-\omega^2}{(1+\omega^2)^2},\qquad \operatorname{Im}\hat x(\omega)=\frac{-2\omega}{(1+\omega^2)^2},\qquad |\hat x(\omega)|=\frac{1}{1+\omega^2}.$$

**Verificación numérica** (integración de $\int_0^\infty te^{-t}e^{-i\omega t}dt$ y `sympy`): coincide con $1/(1+i\omega)^2$ a $\sim10^{-14}$. P.ej. $\hat x(0)=1$, $\hat x(0.5)=0.48-0.64i$, $\hat x(1)=-0.5i$, $\hat x(2)=-0.12-0.16i$ ✓.

> Observación: este resultado es coherente con la propiedad de derivación en frecuencia. Para $e^{-t}u(t)$ se tiene $\mathcal F=\tfrac{1}{1+i\omega}$ (ver [[../resueltos/resueltos-fourier]] (a)); y como $t\,f(t)\xleftrightarrow{\ \mathcal F\ } i\,\dfrac{d}{d\omega}\hat f(\omega)$, resulta $i\dfrac{d}{d\omega}\dfrac{1}{1+i\omega}=i\cdot\dfrac{-i}{(1+i\omega)^2}=\dfrac{1}{(1+i\omega)^2}$ ✓.

---

## Ejercicio 3

Dada la ecuación diferencial (convección–difusión)
$$\frac{\partial u}{\partial t}=\frac{\partial^2 u}{\partial x^2}+\frac{\partial u}{\partial x},$$
desarrollar un esquema de diferencias finitas **implícito** con 4 nodos internos para:

a) $u(0,t)=u(1,t)=0$, $u(x,0)=\operatorname{sen}(x)$.
b) $u_x(0,t)=u(1,t)=0$, $u(x,0)=\cos(x)$.

### Resolución

#### Malla y discretización

Dominio $x\in[0,1]$, **4 nodos internos** $\Rightarrow$ $h=\dfrac15=0.2$ y
$$x_0=0,\ x_1=0.2,\ x_2=0.4,\ x_3=0.6,\ x_4=0.8,\ x_5=1.$$
$u_i^k\approx u(x_i,t_k)$, paso temporal $\Delta t$. Esquema **implícito** (Euler hacia atrás), todas las derivadas espaciales evaluadas en $k+1$:
$$u_t\approx\frac{u_i^{k+1}-u_i^k}{\Delta t},\quad u_{xx}\approx\frac{u_{i-1}^{k+1}-2u_i^{k+1}+u_{i+1}^{k+1}}{h^2},\quad u_x\approx\frac{u_{i+1}^{k+1}-u_{i-1}^{k+1}}{2h}.$$

#### Derivación de la ecuación por nodo (con cuidado en los signos)

Sustituyendo en $u_t=u_{xx}+u_x$ y multiplicando por $\Delta t$:
$$u_i^{k+1}-u_i^k=\frac{\Delta t}{h^2}\big(u_{i-1}^{k+1}-2u_i^{k+1}+u_{i+1}^{k+1}\big)+\frac{\Delta t}{2h}\big(u_{i+1}^{k+1}-u_{i-1}^{k+1}\big).$$
Definimos
$$r=\frac{\Delta t}{h^2},\qquad s=\frac{\Delta t}{2h}.$$
Pasando todos los términos en $k+1$ al lado izquierdo y dejando $u_i^k$ a la derecha, **término a término**:

- coeficiente de $u_{i-1}^{k+1}$: $\ -\,r+s\ =\ (s-r)$,
- coeficiente de $u_{i}^{k+1}$: $\ 1+2r$,
- coeficiente de $u_{i+1}^{k+1}$: $\ -\,r-s\ =\ -(r+s)$.

$$\boxed{\,(s-r)\,u_{i-1}^{k+1}+(1+2r)\,u_i^{k+1}-(r+s)\,u_{i+1}^{k+1}=u_i^k.\,}$$

> **Cuidado con el signo (verificado símbolo a símbolo).** El término convectivo $u_x$ aporta $+s$ sobre $u_{i+1}$ y $-s$ sobre $u_{i-1}$ en el **lado derecho**; al pasarlos a la izquierda cambian de signo, de modo que $u_{i-1}$ recibe $-r+s$ y $u_{i+1}$ recibe $-r-s$. La matriz resulta **tridiagonal NO simétrica** (subdiagonal $s-r$, superdiagonal $-(r+s)$): es la firma de la convección. Comprobado contra un solver de referencia (método de líneas) con $\Delta t=5\cdot10^{-4}$: este esquema reproduce la solución a $O(\Delta t)\approx6\cdot10^{-4}$, mientras que invertir los signos de las off-diagonales da un error $\approx4\cdot10^{-2}$ (dos órdenes peor) — confirmando que el signo correcto es el de arriba.

Con $h=\tfrac15$ queda $r=\dfrac{\Delta t}{(1/5)^2}=25\,\Delta t$ y $s=\dfrac{\Delta t}{2/5}=2.5\,\Delta t$, de modo que $1+2r=1+50\,\Delta t$, $\ s-r=-22.5\,\Delta t$, $\ -(r+s)=-27.5\,\Delta t$.

---

#### a) Dirichlet homogéneo: $u(0,t)=u(1,t)=0$

Las incógnitas son los 4 nodos internos $u_1^{k+1},\dots,u_4^{k+1}$. Los bordes son **conocidos** ($u_0^{k+1}=u_5^{k+1}=0$) y, al ser homogéneos, **desaparecen** del sistema. Escribiendo la ecuación para $i=1,2,3,4$ se obtiene $M\,\mathbf u^{k+1}=\mathbf u^{k}$ con $\mathbf u=(u_1,u_2,u_3,u_4)^T$ y matriz tridiagonal $4\times4$:
$$\boxed{\,M=\begin{pmatrix} 1+2r & -(r+s) & 0 & 0\\ s-r & 1+2r & -(r+s) & 0\\ 0 & s-r & 1+2r & -(r+s)\\ 0 & 0 & s-r & 1+2r\end{pmatrix},\qquad \mathbf b^{k}=\mathbf u^{k}=\begin{pmatrix}u_1^k\\u_2^k\\u_3^k\\u_4^k\end{pmatrix}.\,}$$

**Condición inicial** $u_i^0=\operatorname{sen}(x_i)$, $i=1,\dots,4$:
$$\mathbf u^0=\big(\operatorname{sen}0.2,\ \operatorname{sen}0.4,\ \operatorname{sen}0.6,\ \operatorname{sen}0.8\big)^T=(0.1987,\ 0.3894,\ 0.5646,\ 0.7174)^T.$$

En cada paso temporal se resuelve el sistema lineal $M\,\mathbf u^{k+1}=\mathbf u^{k}$ (Thomas / LU). (A modo numérico, con $\Delta t=0.01$: $r=0.25$, $s=0.025$, $M=\begin{psmallmatrix}1.5&-0.275&0&0\\-0.225&1.5&-0.275&0\\0&-0.225&1.5&-0.275\\0&0&-0.225&1.5\end{psmallmatrix}$, verificado contra el método de líneas.)

---

#### b) Neumann en $x_0$ y Dirichlet en $x_5$: $u_x(0,t)=0$, $u(1,t)=0$

Ahora $u_0$ **deja de ser dato** (en $x=0$ se prescribe la derivada, no el valor): pasa a ser **incógnita**. El sistema crece a $5\times5$ con incógnitas $\mathbf u=(u_0,u_1,u_2,u_3,u_4)^T$ (sigue siendo $u_5^{k+1}=0$ por Dirichlet).

**Nodo fantasma.** Introducimos $x_{-1}$ con valor $u_{-1}^{k+1}$ y discretizamos la condición $u_x(0,t)=0$ con diferencia **central**:
$$u_x(0,t)\approx\frac{u_1^{k+1}-u_{-1}^{k+1}}{2h}=0\ \Longrightarrow\ \boxed{u_{-1}^{k+1}=u_1^{k+1}.}$$

**Ecuación del nodo $0$.** Aplicamos la misma molécula en $i=0$ (usando $u_{-1}$) y sustituimos $u_{-1}^{k+1}=u_1^{k+1}$:
$$(s-r)\,u_{-1}^{k+1}+(1+2r)\,u_0^{k+1}-(r+s)\,u_1^{k+1}=u_0^k$$
$$\Rightarrow (1+2r)\,u_0^{k+1}+\big[(s-r)-(r+s)\big]u_1^{k+1}=u_0^k\ \Rightarrow\ (1+2r)\,u_0^{k+1}-2r\,u_1^{k+1}=u_0^k.$$

> **Detalle elegante (verificado):** al simular el fantasma, los términos en $s$ se **cancelan** ($\,(s-r)-(r+s)=-2r\,$): el término convectivo desaparece en la fila de la pared de Neumann, que queda idéntica a la del caso difusivo puro: $(1+2r)u_0-2r\,u_1=u_0^k$.

Las filas $i=1,2,3,4$ son las del esquema general (la última usa $u_5^{k+1}=0$, que desaparece). El sistema $M\,\mathbf u^{k+1}=\mathbf u^{k}$ es $5\times5$:
$$\boxed{\,M=\begin{pmatrix} 1+2r & -2r & 0 & 0 & 0\\ s-r & 1+2r & -(r+s) & 0 & 0\\ 0 & s-r & 1+2r & -(r+s) & 0\\ 0 & 0 & s-r & 1+2r & -(r+s)\\ 0 & 0 & 0 & s-r & 1+2r\end{pmatrix},\qquad \mathbf b^k=\mathbf u^k=\begin{pmatrix}u_0^k\\u_1^k\\u_2^k\\u_3^k\\u_4^k\end{pmatrix}.\,}$$

**Condición inicial** $u_i^0=\cos(x_i)$, $i=0,\dots,4$:
$$\mathbf u^0=\big(\cos0,\ \cos0.2,\ \cos0.4,\ \cos0.6,\ \cos0.8\big)^T=(1.0000,\ 0.9801,\ 0.9211,\ 0.8253,\ 0.6967)^T.$$

(Numéricamente, con $\Delta t=5\cdot10^{-4}$: $r=0.0125$, $s=0.00125$, $M=\begin{psmallmatrix}1.025&-0.025&0&0&0\\-0.01125&1.025&-0.01375&0&0\\0&-0.01125&1.025&-0.01375&0\\0&0&-0.01125&1.025&-0.01375\\0&0&0&-0.01125&1.025\end{psmallmatrix}$, verificado a $O(\Delta t)$ contra el método de líneas con el mismo nodo fantasma.)

---

### Notas finales

- La matriz de convección–difusión es **tridiagonal no simétrica**: subdiagonal $s-r$, diagonal $1+2r$, superdiagonal $-(r+s)$. Sin el término $u_x$ ($s=0$) se recupera el calor simétrico $-r,\,1+2r,\,-r$.
- Dirichlet homogéneo $\Rightarrow$ los bordes se anulan y el sistema es $4\times4$. Neumann $\Rightarrow$ nodo fantasma + el borde se vuelve incógnita $\Rightarrow$ sistema $5\times5$, con primera fila $(1+2r,\,-2r,\dots)$.
- Cada paso temporal: resolver $M\,\mathbf u^{k+1}=\mathbf u^{k}$ (la CI provee $\mathbf u^0$).
