---
tags: [parcial, iip, resolucion, fourier, serie-trigonometrica, transformada-fourier, diferencias-finitas, ecuacion-onda, neumann, dirichlet]
fuente: raw/Practicas/Modelos_Examenes/MNA_IIP_Tema_V.pdf
tipo: iip
tema: 5
tiene_resolucion: true
---

# Segundo Parcial de Métodos Numéricos Avanzados — Tema V (Resolución)

Enunciado original en [[iip-tema-05]]. Referencias: [[../guias/guia-08-fourier-series]], [[../resueltos/resueltos-fourier]], [[../guias/guia-09-tf]].

---

## Ejercicio 1

Sea la función $x(t) = \cos(t)$ en el intervalo $\left(-\dfrac{\pi}{4}, \dfrac{\pi}{4}\right)$, con $x(t) = x\!\left(t + \tfrac{\pi}{2}\right)$ (período $T = \tfrac{\pi}{2}$).

a) Hallar la Serie Trigonométrica de Fourier de $x(t)$.
b) Usando el desarrollo hallado en a), hallar el desarrollo de $y(t) = x'(t)$.

### Resolución

**a)** El período es $T = \tfrac{\pi}{2}$, de modo que la frecuencia fundamental es

$$\omega_0 = \frac{2\pi}{T} = \frac{2\pi}{\pi/2} = 4 .$$

La función $\cos(t)$ es **par** y el intervalo $\left(-\tfrac\pi4,\tfrac\pi4\right)$ es simétrico respecto del origen, por lo que la extensión periódica es par. En consecuencia **todos los coeficientes $b_n$ se anulan** y la serie tiene solo cosenos:

$$x(t) = a_0 + \sum_{n=1}^{\infty} a_n \cos(4n\,t).$$

**Valor medio $a_0$** (recordar: $a_0$ es el valor medio, sin dividir por 2):

$$a_0 = \frac{1}{T}\int_{-\pi/4}^{\pi/4}\cos t\,dt = \frac{2}{\pi}\Big[\sin t\Big]_{-\pi/4}^{\pi/4} = \frac{2}{\pi}\cdot 2\sin\!\frac{\pi}{4} = \frac{4}{\pi}\cdot\frac{\sqrt2}{2}.$$

$$\boxed{\,a_0 = \frac{2\sqrt2}{\pi} \approx 0{.}9003\,}$$

**Coeficientes $a_n$:**

$$a_n = \frac{2}{T}\int_{-\pi/4}^{\pi/4}\cos t\,\cos(4n\,t)\,dt = \frac{4}{\pi}\int_{-\pi/4}^{\pi/4}\cos t\,\cos(4n\,t)\,dt.$$

Usamos la identidad de producto a suma $\cos\alpha\cos\beta = \tfrac12\big[\cos(\alpha+\beta)+\cos(\alpha-\beta)\big]$:

$$\cos t\,\cos(4n\,t) = \tfrac12\big[\cos((4n+1)t) + \cos((4n-1)t)\big].$$

Integrando ($\int_{-\pi/4}^{\pi/4}\cos(k t)\,dt = \tfrac{2}{k}\sin\tfrac{k\pi}{4}$):

$$a_n = \frac{4}{\pi}\cdot\frac12\left[\frac{2}{4n+1}\sin\frac{(4n+1)\pi}{4} + \frac{2}{4n-1}\sin\frac{(4n-1)\pi}{4}\right].$$

Ahora usamos que $\sin\!\big(n\pi \pm \tfrac{\pi}{4}\big) = \pm(-1)^n\sin\tfrac{\pi}{4} = \pm(-1)^n\tfrac{1}{\sqrt2}$:

$$\sin\frac{(4n+1)\pi}{4} = \sin\!\Big(n\pi+\tfrac{\pi}{4}\Big) = \frac{(-1)^n}{\sqrt2}, \qquad
\sin\frac{(4n-1)\pi}{4} = \sin\!\Big(n\pi-\tfrac{\pi}{4}\Big) = -\frac{(-1)^n}{\sqrt2}.$$

Sustituyendo:

$$a_n = \frac{4}{\pi}\cdot\frac{1}{\sqrt2}\,(-1)^n\left[\frac{1}{4n+1} - \frac{1}{4n-1}\right]
= \frac{4}{\pi}\cdot\frac{(-1)^n}{\sqrt2}\cdot\frac{-2}{16n^2-1}.$$

Simplificando ($\tfrac{4}{\sqrt2}=2\sqrt2$ y absorbiendo el signo en $(-1)^{n+1}$):

$$\boxed{\,a_n = \frac{4\sqrt2\,(-1)^{n+1}}{\pi\,(16n^2-1)}\,}$$

**Serie trigonométrica:**

$$\boxed{\;x(t) = \frac{2\sqrt2}{\pi} + \frac{4\sqrt2}{\pi}\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{16n^2-1}\cos(4n\,t)\;}$$

Primeros coeficientes (verificados numéricamente): $a_1 = \tfrac{4\sqrt2}{15\pi}\approx 0{.}12004$, $a_2 \approx -0{.}02858$, $a_3 \approx 0{.}01259$.

> **Punto sutil (convergencia).** En los bordes del intervalo la función es **continua**: $x\!\left(\tfrac\pi4^-\right)=\cos\tfrac\pi4=\tfrac{1}{\sqrt2}$ y, por periodicidad par, $x\!\left(\tfrac\pi4^+\right)=\cos\!\left(-\tfrac\pi4\right)=\tfrac{1}{\sqrt2}$ también. No hay salto: por Dirichlet la serie converge a $x(t)$ en todo punto (incluidos los bordes). La suma parcial con $N=10$ armónicos ya aproxima $\cos t$ con error $<5\times10^{-3}$ en el interior.

**b)** Como $x(t)$ es continua y de derivada acotada a trozos, podemos **derivar término a término**. Derivando $\cos(4n\,t)\to -4n\sin(4n\,t)$:

$$y(t) = x'(t) = \sum_{n=1}^{\infty} a_n\cdot\big(-4n\big)\sin(4n\,t) = -\sum_{n=1}^{\infty} 4n\,a_n\,\sin(4n\,t).$$

Esta ya es una serie de **solo senos** (impar), coherente con que $y(t)=x'(t)$ es impar. Llamando $b_n^{(y)} = -4n\,a_n$:

$$b_n^{(y)} = -4n\cdot\frac{4\sqrt2\,(-1)^{n+1}}{\pi\,(16n^2-1)} = \frac{16\sqrt2\,n\,(-1)^{n}}{\pi\,(16n^2-1)}.$$

$$\boxed{\;y(t) = x'(t) = \frac{16\sqrt2}{\pi}\sum_{n=1}^{\infty}\frac{(-1)^{n}\,n}{16n^2-1}\,\sin(4n\,t)\;}$$

Esta es la serie de Fourier de $y(t) = -\sin(t)$ sobre $\left(-\tfrac\pi4,\tfrac\pi4\right)$, ya que en el interior $x'(t)=\big(\cos t\big)'=-\sin t$.

Primeros coeficientes: $b_1^{(y)}\approx -0{.}48017$, $b_2^{(y)}\approx 0{.}22865$, $b_3^{(y)}\approx -0{.}15110$.

> **Punto sutil (Gibbs).** A diferencia de $x(t)$, la derivada $y(t)=-\sin t$ **sí tiene salto** en los bordes ($-\sin\tfrac\pi4=-\tfrac1{\sqrt2}$ contra $-\sin(-\tfrac\pi4)=+\tfrac1{\sqrt2}$). Por eso la serie derivada converge mucho más lento (fenómeno de Gibbs en el salto): se verificó que estos coeficientes coinciden exactamente con los obtenidos integrando directamente $b_n^{(y)}=\tfrac4\pi\int_{-\pi/4}^{\pi/4}(-\sin t)\sin(4n t)\,dt$.

---

## Ejercicio 2

Dada la función $x(t) = e^{-2|t|}$, hallar su Transformada de Fourier.

### Resolución

Por definición (convención de la cátedra $\hat x(\omega) = \int_{-\infty}^{\infty} x(t)\,e^{-i\omega t}\,dt$), y separando el valor absoluto en los dos semiejes:

$$\hat x(\omega) = \int_{-\infty}^{0} e^{2t}\,e^{-i\omega t}\,dt + \int_{0}^{\infty} e^{-2t}\,e^{-i\omega t}\,dt.$$

**Segunda integral** (decae para $t\to+\infty$):

$$\int_{0}^{\infty} e^{-2t}e^{-i\omega t}\,dt = \int_{0}^{\infty} e^{-(2+i\omega)t}\,dt = \left.\frac{e^{-(2+i\omega)t}}{-(2+i\omega)}\right|_{0}^{\infty} = \frac{1}{2+i\omega}.$$

**Primera integral** (decae para $t\to-\infty$):

$$\int_{-\infty}^{0} e^{2t}e^{-i\omega t}\,dt = \int_{-\infty}^{0} e^{(2-i\omega)t}\,dt = \left.\frac{e^{(2-i\omega)t}}{2-i\omega}\right|_{-\infty}^{0} = \frac{1}{2-i\omega}.$$

Sumando y poniendo común denominador:

$$\hat x(\omega) = \frac{1}{2+i\omega} + \frac{1}{2-i\omega} = \frac{(2-i\omega)+(2+i\omega)}{(2+i\omega)(2-i\omega)} = \frac{4}{4+\omega^2}.$$

$$\boxed{\;\hat x(\omega) = \frac{4}{4+\omega^2}\;}$$

El resultado es **real y par** (como debe ser, ya que $x(t)=e^{-2|t|}$ es real y par). Generalizando: $\mathcal{F}\{e^{-a|t|}\} = \dfrac{2a}{a^2+\omega^2}$ (lorentziana), aquí con $a=2$.

> **Verificación.** Integrando numéricamente se obtuvo $\hat x(0)=1$, $\hat x(1)=0{.}8$, $\hat x(2)=0{.}5$, $\hat x(3)\approx0{.}30769$, todos con parte imaginaria nula, coincidiendo con $\tfrac{4}{4+\omega^2}$.

---

## Ejercicio 3

Dada la ecuación de onda $\dfrac{\partial^2 u}{\partial t^2} = \dfrac{\partial^2 u}{\partial x^2}$ (velocidad $c=1$), desarrollar un esquema de **diferencias finitas implícito con 4 nodos internos**.

### Esquema general (común a ambos incisos)

Dominio $x\in[0,1]$ con $h = \tfrac{1}{5} = 0{.}2$, nodos

$$x_0=0,\; x_1=0{.}2,\; x_2=0{.}4,\; x_3=0{.}6,\; x_4=0{.}8,\; x_5=1 \quad(\text{4 internos } x_1,\dots,x_4).$$

Notación $u_i^k \approx u(x_i, t_k)$. La onda es de **segundo orden en el tiempo**, así que el esquema usa **tres niveles temporales** ($k-1$, $k$, $k+1$). Discretizamos:

$$u_{tt} \approx \frac{u_i^{k+1} - 2u_i^{k} + u_i^{k-1}}{\Delta t^2}, \qquad
u_{xx} \approx \frac{u_{i-1}^{k+1} - 2u_i^{k+1} + u_{i+1}^{k+1}}{h^2}\;\;(\text{implícito: en el nivel } k+1).$$

Igualando $u_{tt}=u_{xx}$ y definiendo $r = \dfrac{\Delta t^2}{h^2}$, se pasa todo lo del nivel $k+1$ al lado izquierdo:

$$\boxed{\;-r\,u_{i-1}^{k+1} + (1+2r)\,u_i^{k+1} - r\,u_{i+1}^{k+1} = 2u_i^{k} - u_i^{k-1}\;}$$

Tomamos $\Delta t = h = 0{.}2$, de modo que $r = \dfrac{\Delta t^2}{h^2} = 1$, lo que da coeficientes limpios: $1+2r = 3$ en la diagonal y $-r=-1$ fuera de ella.

**Arranque (primer paso).** Para $k=0$ aparece el nivel ficticio $u_i^{-1}$. Se elimina con la condición inicial de velocidad usando la diferencia $u_t(x_i,0) \approx \dfrac{u_i^{1}-u_i^{-1}}{2\Delta t}$, o equivalentemente (lo que usamos aquí) la aproximación hacia atrás $u_i^{-1} = u_i^{0} - \Delta t\,u_t(x_i,0)$.

---

### a) Dirichlet homogéneo: $u(0,t)=u(1,t)=0$, $u(x,0)=\sin x$, $u_t(x,0)=0$

Como ambos bordes son **Dirichlet homogéneos** ($u_0^k=u_5^k=0$), las incógnitas son solo los 4 nodos internos $x_1,\dots,x_4$, y los términos de borde **desaparecen** del lado derecho.

**Condición inicial** $u_i^0 = \sin(x_i)$:

$$\mathbf{u}^0 = \begin{pmatrix}\sin 0{.}2\\ \sin 0{.}4\\ \sin 0{.}6\\ \sin 0{.}8\end{pmatrix}
= \begin{pmatrix}0{.}198669\\ 0{.}389418\\ 0{.}564642\\ 0{.}717356\end{pmatrix}.$$

**Nivel ficticio.** Como $u_t(x,0)=0$:

$$u_i^{-1} = u_i^0 - \Delta t\cdot 0 = u_i^0 \;\Longrightarrow\; \mathbf{u}^{-1}=\mathbf{u}^0.$$

**Sistema** $M\,\mathbf{u}^{k+1} = \mathbf{b}^k$, con la matriz tridiagonal $4\times4$ (con $r=1$):

$$M = \begin{pmatrix}
1+2r & -r & 0 & 0\\
-r & 1+2r & -r & 0\\
0 & -r & 1+2r & -r\\
0 & 0 & -r & 1+2r
\end{pmatrix}
= \begin{pmatrix}
3 & -1 & 0 & 0\\
-1 & 3 & -1 & 0\\
0 & -1 & 3 & -1\\
0 & 0 & -1 & 3
\end{pmatrix},$$

y vector RHS por nodo interno $i=1,\dots,4$:

$$b_i^k = 2u_i^k - u_i^{k-1}.$$

**Primer paso** ($k=0$, despejar $\mathbf{u}^1$): como $\mathbf{u}^{-1}=\mathbf{u}^0$, queda $\mathbf{b}^0 = 2\mathbf{u}^0-\mathbf{u}^0=\mathbf{u}^0$:

$$\mathbf{b}^0 = \begin{pmatrix}0{.}198669\\ 0{.}389418\\ 0{.}564642\\ 0{.}717356\end{pmatrix},
\qquad
\mathbf{u}^1 = M^{-1}\mathbf{b}^0 = \begin{pmatrix}0{.}176340\\ 0{.}330350\\ 0{.}425292\\ 0{.}380883\end{pmatrix}.$$

Para los pasos siguientes ($k\ge1$) se itera $M\mathbf{u}^{k+1} = 2\mathbf{u}^k - \mathbf{u}^{k-1}$. El esquema es **incondicionalmente estable** (implícito): la solución se mantiene acotada (oscila amortiguada numéricamente hacia $0$, como corresponde a la onda con bordes fijos).

---

### b) Neumann + Dirichlet: $u_x(0,t)=0$, $u(1,t)=0$, $u(x,0)=\cos x$, $u_t(x,0)=x$

Ahora el borde izquierdo es **Neumann** ($u_x(0,t)=0$) y el derecho **Dirichlet homogéneo** ($u(1,t)=0$).

**Neumann en $x_0$ con nodo fantasma.** Discretizando $u_x(0,t)\approx\dfrac{u_1^{k+1}-u_{-1}^{k+1}}{2h}=0$ resulta $u_{-1}^{k+1}=u_1^{k+1}$. El nodo de borde $x_0$ pasa a ser **incógnita**, con la ecuación del esquema en $i=0$:

$$-r\,u_{-1}^{k+1} + (1+2r)u_0^{k+1} - r\,u_1^{k+1} = 2u_0^k - u_0^{k-1}.$$

Sustituyendo $u_{-1}^{k+1}=u_1^{k+1}$ se fusionan los dos términos en $u_1$:

$$(1+2r)\,u_0^{k+1} - 2r\,u_1^{k+1} = 2u_0^k - u_0^{k-1}.$$

Esto cambia la **primera fila** (coeficiente $-2r$ en vez de $-r$) y **agranda el sistema a $5\times5$** (incógnitas $x_0,x_1,x_2,x_3,x_4$; el nodo $x_5=1$ sigue siendo Dirichlet conocido $=0$, por lo que su contribución en la fila de $x_4$ desaparece).

**Condición inicial** $u_i^0=\cos(x_i)$ en $x_0,\dots,x_4$:

$$\mathbf{u}^0 = \begin{pmatrix}\cos 0\\ \cos 0{.}2\\ \cos 0{.}4\\ \cos 0{.}6\\ \cos 0{.}8\end{pmatrix}
= \begin{pmatrix}1{.}000000\\ 0{.}980067\\ 0{.}921061\\ 0{.}825336\\ 0{.}696707\end{pmatrix}.$$

**Nivel ficticio** con $u_t(x,0)=x$ (¡aquí la velocidad inicial NO es cero!):

$$u_i^{-1} = u_i^0 - \Delta t\cdot x_i,$$

$$\mathbf{u}^{-1} = \begin{pmatrix}1{.}000000 - 0{.}2(0)\\ 0{.}980067 - 0{.}2(0{.}2)\\ 0{.}921061 - 0{.}2(0{.}4)\\ 0{.}825336 - 0{.}2(0{.}6)\\ 0{.}696707 - 0{.}2(0{.}8)\end{pmatrix}
= \begin{pmatrix}1{.}000000\\ 0{.}940067\\ 0{.}841061\\ 0{.}705336\\ 0{.}536707\end{pmatrix}.$$

**Sistema** $M_b\,\mathbf{u}^{k+1}=\mathbf{b}^k$, con la matriz $5\times5$ (primera fila modificada por Neumann; con $r=1$):

$$M_b = \begin{pmatrix}
1+2r & -2r & 0 & 0 & 0\\
-r & 1+2r & -r & 0 & 0\\
0 & -r & 1+2r & -r & 0\\
0 & 0 & -r & 1+2r & -r\\
0 & 0 & 0 & -r & 1+2r
\end{pmatrix}
= \begin{pmatrix}
3 & -2 & 0 & 0 & 0\\
-1 & 3 & -1 & 0 & 0\\
0 & -1 & 3 & -1 & 0\\
0 & 0 & -1 & 3 & -1\\
0 & 0 & 0 & -1 & 3
\end{pmatrix}.$$

> **Punto sutil.** $M_b$ deja de ser **simétrica** por la fila de Neumann ($-2$ en la posición $(1,2)$ frente a $-1$ en $(2,1)$). La última fila (nodo $x_4$) tiene solo $-1$ a la izquierda porque su vecino derecho $x_5$ es Dirichlet $=0$ y se va al RHS (donde aporta $0$).

Vector RHS por nodo $i=0,\dots,4$: $\;b_i^k = 2u_i^k - u_i^{k-1}$.

**Primer paso** ($k=0$): $\mathbf{b}^0 = 2\mathbf{u}^0 - \mathbf{u}^{-1}$:

$$\mathbf{b}^0 = \begin{pmatrix}1{.}000000\\ 1{.}020067\\ 1{.}001061\\ 0{.}945336\\ 0{.}856707\end{pmatrix},
\qquad
\mathbf{u}^1 = M_b^{-1}\mathbf{b}^0 = \begin{pmatrix}0{.}985733\\ 0{.}978600\\ 0{.}930000\\ 0{.}810339\\ 0{.}555682\end{pmatrix}.$$

Pasos siguientes: iterar $M_b\,\mathbf{u}^{k+1} = 2\mathbf{u}^k - \mathbf{u}^{k-1}$. El recuperado $u^1$ es coherente: en el extremo Neumann el valor casi no cambia (derivada espacial nula) y hacia el extremo Dirichlet la solución cae a $0$.

---

## Resumen de cajas

| Resultado | Valor |
|---|---|
| Ej 1a — $a_0$ | $\dfrac{2\sqrt2}{\pi}$ |
| Ej 1a — $a_n$ | $\dfrac{4\sqrt2\,(-1)^{n+1}}{\pi(16n^2-1)}$ (serie de cosenos) |
| Ej 1b — $y=x'$ | $\dfrac{16\sqrt2}{\pi}\displaystyle\sum_{n\ge1}\dfrac{(-1)^n n}{16n^2-1}\sin(4n t)$ (serie de $-\sin t$) |
| Ej 2 — $\hat x(\omega)$ | $\dfrac{4}{4+\omega^2}$ |
| Ej 3a — $M$ | tridiagonal $4\times4$, diagonal $1+2r=3$, off $-r=-1$ |
| Ej 3b — $M_b$ | $5\times5$, fila Neumann $[3,-2,0,0,0]$, no simétrica |
