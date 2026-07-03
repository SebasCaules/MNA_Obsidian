---
tags: [final, resolucion, transformaciones-lineales, nucleo-imagen, diagonalizacion, fourier, diferencias-finitas, ecuacion-calor, transformada-fourier]
fuente: raw/Practicas/Modelos_Examenes/MNA_Final_Tema_XI(1).pdf
tipo: final
tema: 11
tiene_resolucion: true
---

# Examen Final de Métodos Numéricos Avanzados — Tema XI, variante (Resolución)

> Nota: hay dos archivos rotulados "Tema XI". Esta resolución corresponde a la **variante**, el segundo archivo (`MNA_Final_Tema_XI(1).pdf`). El enunciado del otro Tema XI está en [[final-tema-11]] (y su resolución en [[final-tema-11-resolucion]]); el enunciado de esta variante, en [[final-tema-11-alt]].

## Ejercicio 1

Dada la Transformación Lineal $T : \mathbb{R}^3 \to \mathbb{R}^3 : T(x, y, z) = (-y + z,\ x + y,\ x + z)$

a) Hallar el Núcleo y la Imagen.
b) Decidir si es o no diagonalizable en $\mathbb{R}$.

### Resolución

La matriz de $T$ en base canónica tiene por columnas $T(e_1), T(e_2), T(e_3)$:

$$T(e_1)=T(1,0,0)=(0,1,1),\quad T(e_2)=T(0,1,0)=(-1,1,0),\quad T(e_3)=T(0,0,1)=(1,0,1),$$

$$A = M_{EE}(T) = \begin{pmatrix} 0 & -1 & 1 \\ 1 & 1 & 0 \\ 1 & 0 & 1 \end{pmatrix}.$$

Calculamos el determinante (desarrollando por la primera fila):

$$\det A = 0\cdot\begin{vmatrix}1&0\\0&1\end{vmatrix} -(-1)\begin{vmatrix}1&0\\1&1\end{vmatrix} + 1\cdot\begin{vmatrix}1&1\\1&0\end{vmatrix} = 0 + 1\cdot(1) + 1\cdot(-1) = 0.$$

Como $\det A = 0$, $T$ **no es inyectiva** ($N(T)\ne\{0\}$) y por lo tanto tampoco es un isomorfismo.

#### a) Núcleo e Imagen

**Núcleo.** Resolvemos $AX=0$ por Gauss:

$$\begin{pmatrix} 0 & -1 & 1 \\ 1 & 1 & 0 \\ 1 & 0 & 1 \end{pmatrix}\!\!\begin{pmatrix}x\\y\\z\end{pmatrix}=0 \;\xrightarrow{\text{escalonando}}\; \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & -1 \\ 0 & 0 & 0 \end{pmatrix}.$$

La forma escalonada reducida da las ecuaciones $x = -z$ y $y = z$, con $z$ libre. Tomando $z=1$:

$$\boxed{N(T) = \big\langle (-1,\ 1,\ 1)\big\rangle,\qquad \dim N(T)=1.}$$

**Imagen.** Por el teorema de la dimensión, $\dim\text{Im}(T) = \dim\mathbb{R}^3 - \dim N(T) = 3-1 = 2 = \operatorname{rg}(A)$. La imagen está generada por las **columnas pivote** de $A$ (columnas 1 y 2):

$$\text{Im}(T) = \big\langle (0,1,1),\ (-1,1,0)\big\rangle.$$

Como es un plano por el origen en $\mathbb{R}^3$, conviene darlo también por su ecuación. Si $(x,y,z)\in\text{Im}(T)$ entonces existe $(r,s,t)$ con $x=-s+t$, $y=r+s$, $z=r+t$; eliminando $r,s,t$ se ve que $z = x+y$ (basta restar: $y - x = (r+s)-(-s+t)=r+2s-t$… o directamente $\det$ de la matriz ampliada $[(0,1,1)\,|\,(-1,1,0)\,|\,(x,y,z)]=0$). El resultado es

$$\boxed{\text{Im}(T) = \big\langle (0,1,1),\ (-1,1,0)\big\rangle = \{(x,y,z): -x-y+z=0\},\qquad \dim\text{Im}(T)=2.}$$

(Verificación: el vector normal del plano es $(0,1,1)\times(-1,1,0)=(-1,-1,1)$, de donde $-x-y+z=0$ ✓.)

#### b) ¿Es diagonalizable en $\mathbb{R}$?

Polinomio característico con la convención de cátedra $p_A(\lambda)=\det(\lambda I - A)$:

$$\lambda I - A = \begin{pmatrix} \lambda & 1 & -1 \\ -1 & \lambda-1 & 0 \\ -1 & 0 & \lambda-1 \end{pmatrix},$$

$$p_A(\lambda) = \lambda^3 - 2\lambda^2 + \lambda = \lambda\,(\lambda-1)^2.$$

Los autovalores son $\lambda_1 = 0$ (multiplicidad algebraica $m_a=1$) y $\lambda_2 = 1$ (multiplicidad algebraica $m_a=2$). Todos reales, así que el problema de diagonalizar en $\mathbb{R}$ se reduce a verificar $m_g=m_a$ en cada autovalor.

- **$\lambda=0$:** al ser $m_a=1$ automáticamente $m_g=1$. (Su autoespacio es $S_0=N(A)=\langle(-1,1,1)\rangle$.)

- **$\lambda=1$:** $S_1 = N(I-A)$, con

$$I - A = \begin{pmatrix} 1 & 1 & -1 \\ -1 & 0 & 0 \\ -1 & 0 & 0 \end{pmatrix}\;\xrightarrow{\text{escalonando}}\;\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & -1 \\ 0 & 0 & 0 \end{pmatrix}.$$

El rango es 2, luego $\dim S_1 = 3-2 = 1$. Es decir $m_g(\lambda=1) = 1 < 2 = m_a(\lambda=1)$.

Como falla la igualdad de multiplicidades en $\lambda=1$:

$$\boxed{T \text{ NO es diagonalizable en } \mathbb{R}\ \ (\text{para }\lambda=1:\ m_g=1\neq m_a=2).}$$

**Verificación numérica** (`numpy.linalg.eigvals`): autovalores $\{0,\,1,\,1\}$; `sympy` confirma `is_diagonalizable() = False` y el autoespacio de $\lambda=1$ tiene dimensión 1.

## Ejercicio 2

a) Hallar el desarrollo en serie de Fourier de $f : [0, 1] \to \mathbb{R} : f(x) = 1 - x^2$, con $f(x) = f(x + 1)$ (período $T=1$).
b) Indicar a qué converge la serie en $x = 0$ y $x = \tfrac{1}{2}$.

### Resolución

#### a) Coeficientes de Fourier

Usamos la convención de cátedra para período $T=1$ (de modo que $\tfrac{2\pi n}{T}=2\pi n$):

$$f(x) = a_0 + \sum_{n\ge1} a_n\cos(2\pi n x) + \sum_{n\ge1} b_n\sin(2\pi n x),$$

con $a_0=\int_0^1 f$ (valor medio), $a_n=2\int_0^1 f\cos(2\pi n x)\,dx$, $b_n=2\int_0^1 f\sin(2\pi n x)\,dx$.

**Término constante** (valor medio):

$$a_0 = \int_0^1 (1-x^2)\,dx = \Big[x-\tfrac{x^3}{3}\Big]_0^1 = 1-\tfrac13 = \boxed{\tfrac23}.$$

**Coeficientes de coseno.** Conviene recordar que sobre un período entero $\int_0^1 \cos(2\pi n x)\,dx = 0$ y $\int_0^1 x\cos(2\pi n x)\,dx = 0$ (pues $\cos(2\pi n)=1$, $\sin(2\pi n)=0$). Solo sobrevive el término en $x^2$:

$$a_n = 2\int_0^1 (1-x^2)\cos(2\pi n x)\,dx = -2\int_0^1 x^2\cos(2\pi n x)\,dx.$$

Integrando por partes dos veces y evaluando con $\cos(2\pi n)=1,\ \sin(2\pi n)=0$:

$$\int_0^1 x^2\cos(2\pi n x)\,dx = \frac{2\cos(2\pi n)}{(2\pi n)^2} = \frac{2}{4\pi^2 n^2} = \frac{1}{2\pi^2 n^2},$$

$$\boxed{a_n = -2\cdot\frac{1}{2\pi^2 n^2} = -\frac{1}{\pi^2 n^2}.}$$

**Coeficientes de seno.** Igual que antes, $\int_0^1 \sin(2\pi n x)\,dx=0$, y los términos en $x$ y $x^2$ aportan:

$$b_n = 2\int_0^1 (1-x^2)\sin(2\pi n x)\,dx.$$

Operando ($\int_0^1 x\sin(2\pi n x)\,dx = -\tfrac{1}{2\pi n}$ y $\int_0^1 x^2\sin(2\pi n x)\,dx = -\tfrac{1}{2\pi n}$, con $\cos(2\pi n)=1$):

$$b_n = 2\Big(0 - \big(-\tfrac{1}{2\pi n}\big)\Big)\ \text{(de }x^2\text{ y la cte se cancelan salvo un }\tfrac{1}{2\pi n}) = \boxed{\frac{1}{\pi n}.}$$

Resultado de la serie:

$$\boxed{\,f(x) = \frac23 - \frac{1}{\pi^2}\sum_{n\ge1}\frac{\cos(2\pi n x)}{n^2} + \frac{1}{\pi}\sum_{n\ge1}\frac{\sin(2\pi n x)}{n}.\,}$$

**Verificación** (integración simbólica con `sympy`): $a_0=\tfrac23$; para $n=1,2,3,4$ se obtiene $a_n=-\tfrac{1}{\pi^2},-\tfrac{1}{4\pi^2},-\tfrac{1}{9\pi^2},-\tfrac{1}{16\pi^2}$ y $b_n=\tfrac1\pi,\tfrac{1}{2\pi},\tfrac{1}{3\pi},\tfrac{1}{4\pi}$, exactamente los patrones $a_n=-\tfrac{1}{\pi^2 n^2}$, $b_n=\tfrac{1}{\pi n}$ ✓.

#### b) Convergencia puntual (Dirichlet)

La extensión periódica de $f(x)=1-x^2$ es **continua dentro** de cada intervalo $(0,1)$, pero tiene un **salto en los enteros** $x=0,1,2,\dots$ porque $f(0^+)=1$ mientras que el final del período anterior vale $f(1^-)=1-1^2=0$.

- **En $x=0$** (punto de salto). Por el teorema de Dirichlet la serie converge al promedio de los límites laterales:

$$S(0) = \frac{f(0^+) + f(1^-)}{2} = \frac{1 + 0}{2} = \boxed{\tfrac12}.$$

- **En $x=\tfrac12$** (punto interior de continuidad). La serie converge al valor de la función:

$$S(\tfrac12) = f(\tfrac12) = 1 - (\tfrac12)^2 = 1 - \tfrac14 = \boxed{\tfrac34}.$$

**Verificación numérica** (sumas parciales): con $N=5000$ armónicos, $S(0)\approx 0.50002\to\tfrac12$ y $S(\tfrac12)\approx 0.75000\to\tfrac34$; en un interior cualquiera (p.ej. $x=0.3$) la suma da $0.90994\approx 1-0.09=0.91=f(0.3)$ ✓.

## Ejercicio 3

Dada la ecuación del calor $\dfrac{\partial u}{\partial t} = \dfrac{\partial^2 u}{\partial x^2}$ en $x\in[0,1]$:

a) Desarrollar un esquema de diferencias finitas **implícito** con 4 nodos internos si $u(0,t)=u(1,t)=0$ y $u(x,0)=x e^{-x}$.
b) Ídem si $u_x(0,t)=u_x(1,t)=0$ (Neumann en **ambos** bordes) y $u(x,0)=x+1$.

### Resolución

**Malla común.** Con 4 nodos internos tomamos $h=\tfrac15=0.2$ y nodos

$$x_0=0,\quad x_1=0.2,\quad x_2=0.4,\quad x_3=0.6,\quad x_4=0.8,\quad x_5=1.$$

**Esquema implícito (Euler hacia atrás en el tiempo).** Aproximamos en el nivel $k+1$:

$$\frac{u_i^{k+1}-u_i^{k}}{\Delta t} = \frac{u_{i-1}^{k+1}-2u_i^{k+1}+u_{i+1}^{k+1}}{h^2}.$$

Definiendo $r=\dfrac{\Delta t}{h^2}$ y agrupando, la ecuación de cada nodo interior es

$$\boxed{-r\,u_{i-1}^{k+1} + (1+2r)\,u_i^{k+1} - r\,u_{i+1}^{k+1} = u_i^{k}.}$$

El esquema es incondicionalmente estable; en cada paso temporal se **resuelve un sistema lineal** $M\,\mathbf u^{k+1}=\mathbf b^k$.

#### a) Dirichlet homogéneo

Las incógnitas son los **4 nodos internos** $u_1,u_2,u_3,u_4$. Los bordes son conocidos: $u_0^{k+1}=u_5^{k+1}=0$, y como son **homogéneos** desaparecen del lado derecho (no aportan al RHS). Escribiendo la ecuación nodo a nodo:

$$
\begin{aligned}
i=1:&\quad (1+2r)u_1^{k+1} - r\,u_2^{k+1} &= u_1^k \quad (\text{el término }-r\,u_0^{k+1}=0)\\
i=2:&\quad -r\,u_1^{k+1} + (1+2r)u_2^{k+1} - r\,u_3^{k+1} &= u_2^k\\
i=3:&\quad -r\,u_2^{k+1} + (1+2r)u_3^{k+1} - r\,u_4^{k+1} &= u_3^k\\
i=4:&\quad -r\,u_3^{k+1} + (1+2r)u_4^{k+1} &= u_4^k \quad (\text{el término }-r\,u_5^{k+1}=0)
\end{aligned}
$$

En forma matricial $M\,\mathbf u^{k+1}=\mathbf u^{k}$ con $M$ tridiagonal $4\times4$:

$$\boxed{
M = \begin{pmatrix}
1+2r & -r & 0 & 0\\
-r & 1+2r & -r & 0\\
0 & -r & 1+2r & -r\\
0 & 0 & -r & 1+2r
\end{pmatrix},\qquad
\mathbf u^{k+1}=\begin{pmatrix}u_1^{k+1}\\u_2^{k+1}\\u_3^{k+1}\\u_4^{k+1}\end{pmatrix},\qquad
\mathbf b^k = \mathbf u^k.}
$$

**Condición inicial** $u_i^0 = x_i\,e^{-x_i}$ en los nodos internos:

$$\boxed{
\mathbf u^0 = \begin{pmatrix} u_1^0\\u_2^0\\u_3^0\\u_4^0\end{pmatrix}
= \begin{pmatrix} 0.2\,e^{-0.2}\\ 0.4\,e^{-0.4}\\ 0.6\,e^{-0.6}\\ 0.8\,e^{-0.8}\end{pmatrix}
\approx \begin{pmatrix} 0.16375\\ 0.26813\\ 0.32929\\ 0.35946 \end{pmatrix}.}
$$

(Coherente con los Dirichlet: $u_0^0=0\cdot e^0=0$ y $u_5^0=1\cdot e^{-1}\approx0.3679$, pero el borde derecho se fuerza a $0$ por la condición de contorno.)

#### b) Neumann en ambos bordes

Con $u_x=0$ en $x=0$ y en $x=1$ **los dos nodos de borde pasan a ser incógnitas**. Se introducen **nodos fantasma** y se discretiza la condición de Neumann por diferencia centrada:

- En $x_0=0$: $u_x\approx\dfrac{u_1^{k+1}-u_{-1}^{k+1}}{2h}=0 \Rightarrow u_{-1}^{k+1}=u_1^{k+1}$.
- En $x_5=1$: $u_x\approx\dfrac{u_6^{k+1}-u_4^{k+1}}{2h}=0 \Rightarrow u_6^{k+1}=u_4^{k+1}$.

Aplicando la ecuación general del nodo en $i=0$ y reemplazando $u_{-1}^{k+1}=u_1^{k+1}$:

$$-r\,u_{-1}^{k+1}+(1+2r)u_0^{k+1}-r\,u_1^{k+1}=u_0^k \;\Rightarrow\; (1+2r)u_0^{k+1}-2r\,u_1^{k+1}=u_0^k.$$

Análogamente en $i=5$ con $u_6^{k+1}=u_4^{k+1}$:

$$(1+2r)u_5^{k+1}-2r\,u_4^{k+1}=u_5^k.$$

Ahora hay **6 incógnitas** $u_0,\dots,u_5$ y el sistema es $6\times6$. La matriz es tridiagonal salvo que la primera y la última fila tienen $-2r$ en lugar de $-r$:

$$\boxed{
M = \begin{pmatrix}
1+2r & -2r & 0 & 0 & 0 & 0\\
-r & 1+2r & -r & 0 & 0 & 0\\
0 & -r & 1+2r & -r & 0 & 0\\
0 & 0 & -r & 1+2r & -r & 0\\
0 & 0 & 0 & -r & 1+2r & -r\\
0 & 0 & 0 & 0 & -2r & 1+2r
\end{pmatrix},\qquad
\mathbf u^{k+1}=\begin{pmatrix}u_0^{k+1}\\u_1^{k+1}\\u_2^{k+1}\\u_3^{k+1}\\u_4^{k+1}\\u_5^{k+1}\end{pmatrix},\qquad
\mathbf b^k=\mathbf u^k.}
$$

**Condición inicial** $u_i^0 = x_i+1$ en los 6 nodos $x_i=0,0.2,0.4,0.6,0.8,1$:

$$\boxed{
\mathbf u^0=\big(u_0^0,u_1^0,u_2^0,u_3^0,u_4^0,u_5^0\big)^T=(1,\ 1.2,\ 1.4,\ 1.6,\ 1.8,\ 2)^T.}
$$

> Observaciones útiles para el examen:
> - La condición de **Dirichlet homogénea** (parte a) achica el sistema a $4\times4$ porque los bordes son datos $=0$; si fueran Dirichlet **no** homogéneos pasarían al RHS como $+r\,g$.
> - La condición de **Neumann** (parte b) agranda el sistema a $6\times6$ porque convierte ambos bordes en incógnitas; el efecto del nodo fantasma es duplicar el coeficiente fuera de la diagonal ($-2r$) en la primera y última fila.
> - La matriz de (a) es simétrica; la de (b) **no** es simétrica (las filas de borde rompen la simetría), aunque sigue siendo de diagonal dominante e invertible para todo $r>0$.

**Verificación** (`sympy`): las dos matrices y los vectores de condición inicial se reprodujeron exactamente con la construcción anterior; en particular $u_5^0(\text{a})=e^{-1}\approx0.36788$ y $u^0(\text{b})=(1,1.2,1.4,1.6,1.8,2)$ ✓.

## Ejercicio 4

Hallar la Transformada de Fourier de $f(t) = e^{-a|t|}$ si $0\le t\le1$ ($a>0$), y $f(t)=0$ en otro caso.

### Resolución

**Lectura del enunciado.** El soporte de $f$ es $[0,1]$. En ese intervalo $t\ge0$, de modo que $|t|=t$ y por lo tanto $f(t)=e^{-at}$ sobre $[0,1]$ (y $0$ fuera). Usamos la convención de cátedra

$$\hat f(\omega) = \int_{-\infty}^{\infty} f(t)\,e^{-i\omega t}\,dt = \int_0^1 e^{-at}\,e^{-i\omega t}\,dt.$$

**Cálculo.** Agrupando exponentes:

$$\hat f(\omega) = \int_0^1 e^{-(a+i\omega)t}\,dt = \left.\frac{e^{-(a+i\omega)t}}{-(a+i\omega)}\right|_0^1 = \frac{1 - e^{-(a+i\omega)}}{a+i\omega}.$$

$$\boxed{\ \hat f(\omega) = \frac{1 - e^{-(a+i\omega)}}{a+i\omega} = \frac{1 - e^{-a}\big(\cos\omega - i\sin\omega\big)}{a+i\omega}.\ }$$

Como la integral es sobre un dominio **acotado**, converge para todo $\omega$ y todo $a>0$ (no hace falta pedir nada extra, a diferencia del caso de soporte infinito $e^{-at}u(t)$, donde sí se necesita $a>0$ para que converja en $+\infty$).

**Parte real e imaginaria.** Racionalizando (multiplicando por el conjugado $a-i\omega$, denominador $a^2+\omega^2$):

$$\operatorname{Re}\hat f(\omega) = \frac{a - e^{-a}\big(a\cos\omega - \omega\sin\omega\big)}{a^2+\omega^2},\qquad
\operatorname{Im}\hat f(\omega) = \frac{-\omega + e^{-a}\big(\omega\cos\omega + a\sin\omega\big)}{a^2+\omega^2}.$$

**Verificación numérica** (con $a=1$, integración directa de $\int_0^1 e^{-t}e^{-i\omega t}\,dt$ vía `scipy.quad` frente a la fórmula cerrada):

| $\omega$ | numérico | fórmula cerrada |
|---|---|---|
| $0$ | $0.63212$ | $0.63212\;(=1-e^{-1})$ |
| $1$ | $0.55540 - 0.24584\,i$ | $0.55540 - 0.24584\,i$ |
| $2.5$ | $0.25450 - 0.41609\,i$ | $0.25450 - 0.41609\,i$ |
| $5$ | $-0.03339 - 0.18581\,i$ | $-0.03339 - 0.18581\,i$ |

Coincidencia exacta ✓. (En $\omega=0$ la transformada vale el área $\int_0^1 e^{-at}\,dt=\tfrac{1-e^{-a}}{a}$, que para $a=1$ es $1-e^{-1}\approx0.63212$.)

---

### Enlaces

- Enunciado de esta variante: [[final-tema-11-alt]]
- Otro Tema XI: [[final-tema-11]] · [[final-tema-11-resolucion]]
- Teoría de apoyo: [[guia-08-fourier-series]] · [[resueltos-fourier]] · diferencias finitas / ecuación del calor.
