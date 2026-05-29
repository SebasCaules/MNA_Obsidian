---
tags: [final, resolucion, transformaciones-lineales, matriz-asociada, cambio-base, qr, gram-schmidt, diferencias-finitas, ecuacion-calor, neumann, dirichlet, transformada-fourier, pulso-triangular]
fuente: raw/Practicas/Modelos_Examenes/MNA_Final_Tema_X.pdf
tipo: final
tema: 10
tiene_resolucion: true
---

# Examen Final de Métodos Numéricos Avanzados — Tema X (Resolución)

Enunciado original sin resolver en [[final-tema-10]]. Referencias de método: [[../clases/clase-2026-04-23]] (matriz asociada, cambio de base), [[../clases/clase-2026-05-07]] (QR por Gram–Schmidt), [[../guias/guia-09-tf]], [[../resueltos/resueltos-fourier]] y la resolución hermana [[final-tema-05-resolucion]] (mismo combo TL + calor + TF).

## Ejercicio 1

Dada la TL $T : \mathbb{R}^3 \to \mathbb{R}^3 : T(x, y, z) = (2x + y - z,\ x + 3y - z,\ z - y)$.

a) Hallar la matriz asociada $M_{BB}$ con $B = \{(0, 0, 1),\ (1, 0, 0),\ (1, -1, 0)\}$.
b) Hallar la descomposición $QR$ de $M_{BB}$.

### Resolución

**a) Matriz asociada $M_{BB}$.**

Primero la matriz en base canónica $M_{EE}(T)$, cuyas columnas son las imágenes de los versores:

$$T(e_1) = T(1,0,0) = (2,1,0),\quad T(e_2) = T(0,1,0) = (1,3,-1),\quad T(e_3) = T(0,0,1) = (-1,-1,1),$$

$$M_{EE}(T) = \begin{pmatrix} 2 & 1 & -1 \\ 1 & 3 & -1 \\ 0 & -1 & 1 \end{pmatrix}.$$

Para pasar a la base $B = \{b_1, b_2, b_3\}$ con $b_1 = (0,0,1)$, $b_2 = (1,0,0)$, $b_3 = (1,-1,0)$, armamos la **matriz de cambio de base** $P$ cuyas columnas son los $b_j$ escritos en canónica:

$$P = \big(b_1 \mid b_2 \mid b_3\big) = \begin{pmatrix} 0 & 1 & 1 \\ 0 & 0 & -1 \\ 1 & 0 & 0 \end{pmatrix},\qquad \det P = -1 \ne 0\ (\text{base válida}).$$

$P$ recibe coordenadas en $B$ y devuelve coordenadas canónicas; $P^{-1}$ hace lo inverso. La matriz asociada en $B$ es la conjugación

$$\boxed{M_{BB} = P^{-1}\,M_{EE}\,P.}$$

Invertimos $P$ (es una permutación con un $-1$; sale directo):

$$P^{-1} = \begin{pmatrix} 0 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & -1 & 0 \end{pmatrix}.$$

**Cálculo columna por columna** (cada columna $j$ es $[T(b_j)]_B$, lo más seguro para no equivocarse):

- $T(b_1) = T(0,0,1) = (-1,-1,1)$. Lo escribimos en $B$: buscamos $\alpha,\beta,\gamma$ con $\alpha b_1 + \beta b_2 + \gamma b_3 = (-1,-1,1)$, o sea $(\beta+\gamma,\ -\gamma,\ \alpha) = (-1,-1,1)$. De la 2ª coord $\gamma = 1$; de la 3ª $\alpha = 1$; de la 1ª $\beta = -1-\gamma = -2$. Columna $[T(b_1)]_B = (1,-2,1)^T$.
- $T(b_2) = T(1,0,0) = (2,1,0)$. $(\beta+\gamma,-\gamma,\alpha) = (2,1,0)$: $\gamma = -1$, $\alpha = 0$, $\beta = 2-\gamma = 3$. Columna $(0,3,-1)^T$.
- $T(b_3) = T(1,-1,0) = (2\cdot1 + (-1) - 0,\ 1 + 3(-1) - 0,\ 0 - (-1)) = (1,-2,1)$. $(\beta+\gamma,-\gamma,\alpha) = (1,-2,1)$: $\gamma = 2$, $\alpha = 1$, $\beta = 1-\gamma = -1$. Columna $(1,-1,2)^T$.

$$\boxed{M_{BB} = \begin{pmatrix} 1 & 0 & 1 \\ -2 & 3 & -1 \\ 1 & -1 & 2 \end{pmatrix}.}$$

(Coincide con $P^{-1}M_{EE}P$; tiene $\det M_{BB} = 4 = \det M_{EE}$, como debe ser bajo cambio de base.)

> **Punto sutil.** Conviene calcular cada columna como $[T(b_j)]_B$ y no confundir con $M_{EB}$ (que devolvería coordenadas canónicas). Como $T$ va de $\mathbb{R}^3$ a $\mathbb{R}^3$ y usamos **la misma** base $B$ en dominio y codominio, ambas conjugaciones por $P$ son necesarias: $M_{BB} = P^{-1}M_{EE}P$, no solo $P^{-1}M_{EE}$.

**Verificación numérica** (numpy). $P^{-1}M_{EE}P$ da exactamente $\begin{pmatrix}1&0&1\\-2&3&-1\\1&-1&2\end{pmatrix}$, y las tres columnas $[T(b_j)]_B$ calculadas a mano coinciden: $(1,-2,1)$, $(0,3,-1)$, $(1,-1,2)$. ✓

**b) Descomposición $QR$ de $M_{BB}$ por Gram–Schmidt.**

Tomamos las columnas de $A = M_{BB}$ como vectores $a_1 = (1,-2,1)$, $a_2 = (0,3,-1)$, $a_3 = (1,-1,2)$ y ortonormalizamos (convención de la cátedra: $R_{ii} = \lVert u_i\rVert > 0$, $R_{ij} = \langle a_j, v_i\rangle$ para $i<j$).

**Paso 1.** $u_1 = a_1 = (1,-2,1)$, con $\lVert u_1\rVert = \sqrt{1+4+1} = \sqrt 6$. Entonces

$$r_{11} = \sqrt 6,\qquad v_1 = \frac{u_1}{\sqrt 6} = \frac{1}{\sqrt6}(1,-2,1).$$

**Paso 2.** Proyección de $a_2$ sobre $v_1$: $\langle a_2, u_1\rangle = (0)(1) + (3)(-2) + (-1)(1) = -7$, así que

$$r_{12} = \langle a_2, v_1\rangle = \frac{-7}{\sqrt6} = -\frac{7\sqrt6}{6}.$$

$$u_2 = a_2 - r_{12}\,v_1 = a_2 - \frac{\langle a_2,u_1\rangle}{\langle u_1,u_1\rangle}u_1 = (0,3,-1) - \frac{-7}{6}(1,-2,1) = \left(\tfrac76,\ \tfrac{4}{3},\ \tfrac16\right).$$

$$\lVert u_2\rVert = \sqrt{\tfrac{49}{36} + \tfrac{16}{9} + \tfrac{1}{36}} = \sqrt{\tfrac{49 + 64 + 1}{36}} = \sqrt{\tfrac{114}{36}}.$$

Aquí conviene una simplificación: $\langle u_2, u_2\rangle = \langle a_2,a_2\rangle - r_{12}^2 = 10 - \tfrac{49}{6} = \tfrac{11}{6}$, de donde

$$r_{22} = \lVert u_2\rVert = \sqrt{\tfrac{11}{6}} = \frac{\sqrt{66}}{6},\qquad v_2 = \frac{u_2}{r_{22}}.$$

**Paso 3.** $\langle a_3, u_1\rangle = (1)(1) + (-1)(-2) + (2)(1) = 5$, luego

$$r_{13} = \langle a_3, v_1\rangle = \frac{5}{\sqrt6} = \frac{5\sqrt6}{6}.$$

$\langle a_3, u_2\rangle = (1)(\tfrac76) + (-1)(\tfrac43) + (2)(\tfrac16) = \tfrac76 - \tfrac86 + \tfrac26 = \tfrac56$, y como $v_2 = u_2/r_{22}$:

$$r_{23} = \langle a_3, v_2\rangle = \frac{\langle a_3, u_2\rangle}{r_{22}} = \frac{5/6}{\sqrt{66}/6} = \frac{5}{\sqrt{66}} = \frac{5\sqrt{66}}{66}\quad(\approx 0.6155).$$

$$u_3 = a_3 - r_{13}v_1 - r_{23}v_2.$$

Para $r_{33}$ usamos de nuevo el atajo de Pitágoras (las restas de Gram–Schmidt son ortogonales): con $r_{23}^2 = \big(\tfrac{5}{\sqrt{66}}\big)^2 = \tfrac{25}{66}$,

$$\langle u_3,u_3\rangle = \langle a_3,a_3\rangle - r_{13}^2 - r_{23}^2 = 6 - \tfrac{25}{6} - \tfrac{25}{66} = \tfrac{396 - 275 - 25}{66} = \tfrac{96}{66} = \tfrac{16}{11}.$$

Entonces

$$r_{33} = \lVert u_3\rVert = \sqrt{\tfrac{16}{11}} = \frac{4}{\sqrt{11}} = \frac{4\sqrt{11}}{11}\quad(\approx 1.2060).$$

Reuniendo, con $v_3 = u_3/r_{33}$, las matrices son (en forma exacta):

$$\boxed{Q = \begin{pmatrix}
\dfrac{\sqrt6}{6} & \dfrac{7\sqrt{66}}{66} & -\dfrac{\sqrt{11}}{11} \\[2mm]
-\dfrac{\sqrt6}{3} & \dfrac{2\sqrt{66}}{33} & \dfrac{\sqrt{11}}{11} \\[2mm]
\dfrac{\sqrt6}{6} & \dfrac{\sqrt{66}}{66} & \dfrac{3\sqrt{11}}{11}
\end{pmatrix},\qquad
R = \begin{pmatrix}
\sqrt6 & -\dfrac{7\sqrt6}{6} & \dfrac{5\sqrt6}{6} \\[2mm]
0 & \dfrac{\sqrt{66}}{6} & \dfrac{5\sqrt{66}}{66} \\[2mm]
0 & 0 & \dfrac{4\sqrt{11}}{11}
\end{pmatrix}.}$$

En **decimales** (4 cifras):

$$Q \approx \begin{pmatrix}
0.4082 & 0.8616 & -0.3015 \\
-0.8165 & 0.4924 & 0.3015 \\
0.4082 & 0.1231 & 0.9045
\end{pmatrix},\qquad
R \approx \begin{pmatrix}
2.4495 & -2.8577 & 2.0412 \\
0 & 1.3540 & 0.6155 \\
0 & 0 & 1.2060
\end{pmatrix}.$$

> **Punto sutil (signos y atajos).** (1) La columna $a_1$ tiene una entrada $-2$, así que $v_1$ lleva $-\sqrt6/3$ en la segunda fila — cuidar el signo. (2) `numpy.linalg.qr` devuelve los signos de las dos primeras columnas invertidos (su convención no fuerza $R_{ii}>0$); la **convención de Gram–Schmidt de la cátedra** sí pide $R_{ii} = \lVert u_i\rVert > 0$, que es lo que da el cuadro de arriba. Ambas son QR válidas, difieren solo en signos de columnas de $Q$ / filas de $R$. (3) El truco $\lVert u_j\rVert^2 = \lVert a_j\rVert^2 - \sum_{i<j} r_{ij}^2$ evita simplificar fracciones feas.

**Verificación numérica** (sympy, exacto). $Q R - M_{BB} = 0$ (matriz nula exacta) y $Q^T Q = I_3$ exacto. Radicales reportados: $r_{11} = \sqrt6$, $r_{22} = \sqrt{66}/6$, $r_{33} = 4\sqrt{11}/11$; decimales chequeados con numpy. $\det M_{BB} = 4$ y $\prod R_{ii} = \sqrt6\cdot\tfrac{\sqrt{66}}{6}\cdot\tfrac{4\sqrt{11}}{11} = 4$ ✓ (en módulo, ya que $\det A = \pm\prod R_{ii}$).

## Ejercicio 2

Considere el problema de contorno

$$\frac{\partial u}{\partial t} = \frac{\partial^2 u}{\partial x^2},\qquad u_x(0,t) = 0\ (\text{Neumann}),\qquad u(1,t) = 0\ (\text{Dirichlet}),\qquad u(x,0) = e^{-x^2}.$$

a) Plantear un esquema de diferencias finitas implícito de 4 nodos internos.
b) Indicar cómo quedan las matrices.

### Resolución

**Malla.** Dominio $x \in [0,1]$ con 4 nodos internos $\Rightarrow h = \tfrac{1}{5} = 0.2$, nodos

$$x_0 = 0,\quad x_1 = 0.2,\quad x_2 = 0.4,\quad x_3 = 0.6,\quad x_4 = 0.8,\quad x_5 = 1.$$

Notación $u_i^k \approx u(x_i, t_k)$, paso temporal $\Delta t$, $r = \dfrac{\Delta t}{h^2}$.

**Discretización (Euler implícito / hacia atrás en tiempo).** Evaluando $u_{xx}$ en el nivel $k+1$:

$$\frac{u_i^{k+1} - u_i^k}{\Delta t} = \frac{u_{i-1}^{k+1} - 2u_i^{k+1} + u_{i+1}^{k+1}}{h^2}\ \Longrightarrow\ -r\,u_{i-1}^{k+1} + (1+2r)\,u_i^{k+1} - r\,u_{i+1}^{k+1} = u_i^k.$$

**Tratamiento de los bordes (el corazón del ejercicio: bordes mixtos).**

- **Dirichlet en $x_5 = 1$:** $u_5^{k+1} = 0$ es un **dato conocido**. En la ecuación del nodo $x_4$ aparece $-r\,u_5^{k+1}$, que al ser nulo desaparece del lado derecho. El nodo $x_5$ **no es incógnita** (sale del sistema).
- **Neumann en $x_0 = 0$:** no hay valor prescrito de $u$, así que el nodo de borde $x_0$ **pasa a ser incógnita**. Para cerrar la ecuación en $x_0$ (que necesita el vecino inexistente $x_{-1}$) usamos un **nodo fantasma** con diferencia centrada:
$$u_x(0,t) \approx \frac{u_1^{k+1} - u_{-1}^{k+1}}{2h} = 0 \ \Longrightarrow\ u_{-1}^{k+1} = u_1^{k+1}.$$
Sustituyendo el fantasma en la ecuación general en $i=0$:
$$-r\,u_{-1}^{k+1} + (1+2r)u_0^{k+1} - r\,u_1^{k+1} = u_0^k \ \Longrightarrow\ (1+2r)u_0^{k+1} - 2r\,u_1^{k+1} = u_0^k.$$
Notar el coeficiente $-2r$ (no $-r$): es la huella del nodo fantasma de Neumann.

**Resultado: las incógnitas son los 5 nodos $u_0, u_1, u_2, u_3, u_4$** (el $x_0$ de Neumann más los 4 internos; $x_5$ Dirichlet queda afuera). El sistema es $5\times5$.

**b) Las matrices.** Escribiendo las ecuaciones para $i = 0,1,2,3,4$:

$$M\,\mathbf{u}^{k+1} = \mathbf{b}^k,\qquad
M = \begin{pmatrix}
1+2r & -2r & 0 & 0 & 0 \\
-r & 1+2r & -r & 0 & 0 \\
0 & -r & 1+2r & -r & 0 \\
0 & 0 & -r & 1+2r & -r \\
0 & 0 & 0 & -r & 1+2r
\end{pmatrix},\qquad
\mathbf{u}^{k+1} = \begin{pmatrix} u_0^{k+1} \\ u_1^{k+1} \\ u_2^{k+1} \\ u_3^{k+1} \\ u_4^{k+1} \end{pmatrix}.$$

El lado derecho es $\mathbf{b}^k = (u_0^k, u_1^k, u_2^k, u_3^k, u_4^k)^T$ (la solución del paso anterior); el término Dirichlet del nodo $x_4$ es $-r\,u_5^{k+1} = -r\cdot 0 = 0$, así que **no aparece** en $\mathbf b^k$.

El **vector de condición inicial** sale de $u(x,0) = e^{-x^2}$ evaluado en los nodos incógnita $x_0,\dots,x_4$:

$$\mathbf{u}^0 = \begin{pmatrix} e^{-x_0^2} \\ e^{-x_1^2} \\ e^{-x_2^2} \\ e^{-x_3^2} \\ e^{-x_4^2} \end{pmatrix} = \begin{pmatrix} e^{0} \\ e^{-0.04} \\ e^{-0.16} \\ e^{-0.36} \\ e^{-0.64} \end{pmatrix} \approx \begin{pmatrix} 1 \\ 0.9608 \\ 0.8521 \\ 0.6977 \\ 0.5273 \end{pmatrix}.$$

(En $x_5 = 1$ sería $e^{-1} \approx 0.3679$, pero la condición Dirichlet $u(1,t)=0$ tiene prioridad para $t>0$: se toma $u_5^k = 0$.)

> **Puntos sutiles de este ejercicio.** (1) **Bordes mixtos:** Neumann en un extremo *agrega* una incógnita y Dirichlet en el otro la *quita*, así que el sistema es $5\times5$ (no $4\times4$ como en Dirichlet–Dirichlet, ni $6\times6$ como en Neumann–Neumann). (2) La **primera fila** lleva $-2r$ (fantasma), la **última fila** es tridiagonal normal (su $-r\,u_5$ va al RHS y se anula). (3) $M$ deja de ser simétrica por el $-2r$ aislado en la fila 0; es diagonalmente dominante, así que el sistema siempre tiene solución única.

**Verificación numérica** (numpy). CI evaluada $= (1, 0.9608, 0.8521, 0.6977, 0.5273)$ ✓ (coincide con el cuadro). Con $r = 1$, $M = \begin{pmatrix}3&-2&0&0&0\\-1&3&-1&0&0\\0&-1&3&-1&0\\0&0&-1&3&-1\\0&0&0&-1&3\end{pmatrix}$, $\det M = 123 \ne 0$ (bien planteado), y un paso implícito da $\mathbf u^1 \approx (0.9287, 0.8930, 0.7896, 0.6236, 0.3836)$ — el perfil decae y se aplana cerca de $x_0$ (flujo nulo) y cae hacia $0$ en $x_5$ (Dirichlet), como debe ser. ✓

## Ejercicio 3

Hallar la Transformada de Fourier de $f(t) = 1 - |t|$ si $-1 \le t \le 1$, y $f(t) = 0$ en otro caso (pulso triangular).

### Resolución

**Definición (convención de la cátedra)** $\displaystyle \hat f(\omega) = \int_{-\infty}^{\infty} f(t)\,e^{-i\omega t}\,dt$. Como $f$ tiene soporte compacto $[-1,1]$, integramos solo ahí:

$$\hat f(\omega) = \int_{-1}^{1} (1 - |t|)\,e^{-i\omega t}\,dt.$$

**Simetría: la transformada es real.** $f$ es **par** ($f(-t) = f(t)$, pues $1-|{-t}| = 1-|t|$). Para una función par, la parte impar $e^{-i\omega t} = \cos(\omega t) - i\sin(\omega t)$ integra a cero la componente del seno (integrando impar sobre intervalo simétrico). Entonces

$$\hat f(\omega) = \int_{-1}^{1}(1-|t|)\cos(\omega t)\,dt = 2\int_{0}^{1}(1-t)\cos(\omega t)\,dt,$$

donde en el último paso usamos que $(1-|t|)\cos(\omega t)$ es par y que en $[0,1]$ es $|t| = t$.

**Cálculo de la integral** (por partes, $u = 1-t$, $dv = \cos(\omega t)\,dt$, $\omega \ne 0$):

$$\int_0^1 (1-t)\cos(\omega t)\,dt = \left[(1-t)\frac{\sin(\omega t)}{\omega}\right]_0^1 + \frac{1}{\omega}\int_0^1 \sin(\omega t)\,dt.$$

El término de borde se anula en ambos extremos: en $t=1$ porque $(1-t)=0$, en $t=0$ porque $\sin 0 = 0$. Queda

$$\frac{1}{\omega}\int_0^1 \sin(\omega t)\,dt = \frac{1}{\omega}\left[-\frac{\cos(\omega t)}{\omega}\right]_0^1 = \frac{1}{\omega^2}\big(1 - \cos\omega\big).$$

Multiplicando por $2$:

$$\boxed{\hat f(\omega) = \frac{2\,(1 - \cos\omega)}{\omega^2}.}$$

**Forma equivalente con sinc.** Usando la identidad del ángulo mitad $1 - \cos\omega = 2\sin^2(\omega/2)$:

$$\hat f(\omega) = \frac{2\cdot 2\sin^2(\omega/2)}{\omega^2} = \frac{4\sin^2(\omega/2)}{\omega^2} = \left(\frac{\sin(\omega/2)}{\omega/2}\right)^2 = \operatorname{sinc}^2\!\left(\frac{\omega}{2}\right).$$

$$\boxed{\hat f(\omega) = \frac{2(1-\cos\omega)}{\omega^2} = \frac{4\sin^2(\omega/2)}{\omega^2} = \operatorname{sinc}^2\!\left(\frac{\omega}{2}\right).}$$

(Esto refleja un hecho conocido: el pulso triangular es la **autoconvolución** de un pulso rectangular de ancho $1$, cuya TF es $\operatorname{sinc}(\omega/2)$; por el teorema de convolución, la TF del triángulo es su cuadrado.)

**Caso $\omega = 0$.** La fórmula es $\tfrac00$ en apariencia, pero el valor sale directo de la integral (o por el desarrollo $1-\cos\omega \approx \omega^2/2$):

$$\hat f(0) = \int_{-1}^{1}(1 - |t|)\,dt = 2\int_0^1 (1-t)\,dt = 2\left[t - \tfrac{t^2}{2}\right]_0^1 = 2\cdot\tfrac12 = 1.$$

$$\boxed{\hat f(0) = 1.}$$

(Consistente: $\lim_{\omega\to0}\operatorname{sinc}^2(\omega/2) = 1$, y $\hat f(0) = \int f = $ área del triángulo, que es $1$.)

> **Puntos sutiles.** (1) **La TF es real** porque $f$ es par; conviene argumentarlo para colapsar $e^{-i\omega t}$ a $\cos$ y ahorrar trabajo (no hay parte imaginaria que calcular). (2) El truco $2\int_0^1$ usa $|t| = t$ en $[0,1]$. (3) Reportar la forma sinc deja explícito que $\hat f(\omega) \ge 0$ para todo $\omega$ (cuadrado de algo real) — el espectro del triángulo no cambia de signo, a diferencia del rectángulo.

**Verificación numérica** (sympy + scipy). `sympy.integrate` da $2\int_0^1(1-t)\cos(\omega t)\,dt = \tfrac{2(1-\cos\omega)}{\omega^2}$ (con valor $1$ en $\omega=0$), y `simplify` confirma que coincide exactamente con $(\sin(\omega/2)/(\omega/2))^2$. La parte imaginaria de la integral de definición es $0$ a precisión de máquina para todo $\omega$ probado (función par ✓). Tabla de chequeo (fórmula vs. `scipy.quad` sobre la definición): $\hat f(0.5) = 0.97934$, $\hat f(1) = 0.91939$, $\hat f(2) = 0.70807$, $\hat f(3) = 0.44222$, $\hat f(\pi) = 0.40528$, $\hat f(5) = 0.05731$, $\hat f(-2) = 0.70807$ (par ✓); todos coinciden a $\sim 10^{-8}$. ✓
