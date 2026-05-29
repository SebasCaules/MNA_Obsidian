---
tags: [final, resolucion, transformaciones-lineales, cambio-base, matriz-asociada, svd, diferencias-finitas, ecuacion-calor, dirichlet, transformada-fourier]
fuente: raw/Practicas/Modelos_Examenes/MNA_Final_Tema_IX.pdf
tipo: final
tema: 9
tiene_resolucion: true
---

# Examen Final de Métodos Numéricos Avanzados — Tema IX (Resolución)

Enunciado original sin resolver en [[final-tema-09]]. Referencias de método: [[../resueltos/resueltos-svd]], [[../guias/guia-08-fourier-series]], [[../resueltos/resueltos-fourier]].

## Ejercicio 1

Dada la TL $T : \mathbb{R}^3 \to \mathbb{R}^3 : T(x, y, z) = (2x + y,\ y - z,\ z + x)$.

a) Hallar la matriz asociada $M_{BB}$ con $B = \{(0, 0, 1),\ (1, 0, 0),\ (1, -1, 0)\}$.
b) Hallar la descomposición SVD de $M_{BB}$.

### Resolución

**a) Matriz asociada $M_{BB}$.**

Primero la matriz en base canónica $M_{EE}(T)$, cuyas columnas son las imágenes de los versores:

$$T(e_1) = (2, 0, 1),\qquad T(e_2) = (1, 1, 0),\qquad T(e_3) = (0, -1, 1),$$

$$M_{EE}(T) = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 1 & -1 \\ 1 & 0 & 1 \end{pmatrix}.$$

Sea $P$ la matriz de cambio de base con las coordenadas de $B$ por columnas (de $B$ a la canónica):

$$P = \big(b_1 \mid b_2 \mid b_3\big) = \begin{pmatrix} 0 & 1 & 1 \\ 0 & 0 & -1 \\ 1 & 0 & 0 \end{pmatrix},\qquad \det P = -1 \ne 0\ (\text{base válida}).$$

La matriz asociada en base $B$ se obtiene por semejanza $M_{BB} = P^{-1} M_{EE}\, P$. Calculamos primero la inversa de $P$:

$$P^{-1} = \begin{pmatrix} 0 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & -1 & 0 \end{pmatrix}.$$

**Método directo (columna $j$ = $[T(b_j)]_B$).** Es la forma más segura de evitar errores: la columna $j$ de $M_{BB}$ son las coordenadas en $B$ de $T(b_j)$.

$$T(b_1) = T(0,0,1) = (0, -1, 1),\qquad [T(b_1)]_B = P^{-1}(0,-1,1)^T = (1, -1, 1)^T,$$
$$T(b_2) = T(1,0,0) = (2, 0, 1),\qquad [T(b_2)]_B = P^{-1}(2,0,1)^T = (1, 2, 0)^T,$$
$$T(b_3) = T(1,-1,0) = (1, -1, 1),\qquad [T(b_3)]_B = P^{-1}(1,-1,1)^T = (1, 0, 1)^T.$$

Apilando las tres columnas:

$$\boxed{M_{BB} = \begin{pmatrix} 1 & 1 & 1 \\ -1 & 2 & 0 \\ 1 & 0 & 1 \end{pmatrix}.}$$

(Coincide con $P^{-1} M_{EE}\, P$.)

> **Punto sutil.** $T(b_1) = (0,-1,1)$ "vive" en coordenadas canónicas; hay que **traducirlo a coordenadas en $B$** multiplicando por $P^{-1}$. Por ejemplo $[T(b_1)]_B = (1,-1,1)$ significa $T(b_1) = 1\cdot b_1 - 1\cdot b_2 + 1\cdot b_3 = (0,0,1)-(1,0,0)+(1,-1,0) = (0,-1,1)$ ✓. Olvidar este paso (y poner directamente las componentes canónicas) es el error típico.

**b) SVD de $M_{BB}$.** Escribimos $A := M_{BB}$ y buscamos $A = U\Sigma V^T$. Notar que $\det A = 1 \ne 0$, así que $A$ tiene **rango completo** (3) y todos los valores singulares serán positivos.

**Paso 1 — autovalores de $A^T A$.**

$$A^T A = \begin{pmatrix} 3 & -1 & 2 \\ -1 & 5 & 1 \\ 2 & 1 & 2 \end{pmatrix}.$$

Polinomio característico (convención de la cátedra $p(\lambda) = \det(\lambda I - A^TA)$):

$$p(\lambda) = \lambda^3 - 10\lambda^2 + 25\lambda - 1.$$

(El término independiente es $-\det(A^TA) = -(\det A)^2 = -1$, y la traza $10$ aparece como coeficiente de $\lambda^2$; buenos chequeos rápidos.) Este cúbico **no tiene raíces racionales** (no es "lindo"), así que resolvemos numéricamente y reportamos con 4 decimales:

$$\lambda_1 \approx 5.4292,\qquad \lambda_2 \approx 4.5302,\qquad \lambda_3 \approx 0.0407.$$

**Paso 2 — valores singulares** (raíces, en orden decreciente):

$$\boxed{\sigma_1 = \sqrt{\lambda_1} \approx 2.3301,\qquad \sigma_2 = \sqrt{\lambda_2} \approx 2.1284,\qquad \sigma_3 = \sqrt{\lambda_3} \approx 0.2016.}$$

Chequeo: $\sigma_1\sigma_2\sigma_3 \approx 1 = |\det A|$ (el producto de los valores singulares es $|\det A|$). ✓

**Paso 3 — matriz $V$** (autovectores ortonormales de $A^TA$, columnas en el mismo orden decreciente de $\lambda$). Para cada $\lambda_i$ se resuelve $(A^TA - \lambda_i I)v_i = 0$ y se normaliza; como los tres autovalores son distintos, los $v_i$ salen automáticamente ortogonales:

$$V \approx \begin{pmatrix} -0.3120 & \phantom{-}0.7364 & -0.6003 \\ \phantom{-}0.9454 & \phantom{-}0.1784 & -0.2726 \\ \phantom{-}0.0937 & \phantom{-}0.6526 & \phantom{-}0.7519 \end{pmatrix}.$$

**Paso 4 — matriz $U$.** Como todos los $\sigma_i > 0$, las columnas se obtienen con $u_i = \dfrac{A v_i}{\sigma_i}$ (no hace falta completar con $N(A^T)$ porque $A$ es de rango completo):

$$U \approx \begin{pmatrix} \phantom{-}0.3120 & \phantom{-}0.7364 & -0.6003 \\ \phantom{-}0.9454 & -0.1784 & \phantom{-}0.2726 \\ -0.0937 & \phantom{-}0.6526 & \phantom{-}0.7519 \end{pmatrix}.$$

**Resultado (SVD completa):**

$$\boxed{A = U\,\Sigma\,V^T,\qquad \Sigma = \begin{pmatrix} 2.3301 & 0 & 0 \\ 0 & 2.1284 & 0 \\ 0 & 0 & 0.2016 \end{pmatrix}.}$$

> **Puntos sutiles.** (1) Los signos de cada columna $v_i$ (y por ende $u_i$) **no son únicos**: si se cambia el signo de $v_i$ hay que cambiar el de $u_i$ para que $u_i = Av_i/\sigma_i$ siga valiendo. Cualquier elección consistente es una SVD válida. (2) $\Sigma$ es $3\times3$ y $A$ es cuadrada inversible, así que esta SVD también da directamente $A^{-1} = V\Sigma^{-1}U^T$ y la pseudoinversa coincide con la inversa.

**Verificación numérica** (numpy/sympy). $\det A = 1$. `sympy` confirma $M_{BB} = P^{-1}M_{EE}P = \begin{pmatrix}1&1&1\\-1&2&0\\1&0&1\end{pmatrix}$ y que el cálculo columna a columna $[T(b_j)]_B$ da lo mismo. El polinomio característico de $A^TA$ es $\lambda^3 - 10\lambda^2 + 25\lambda - 1$, con autovalores $\{5.4292, 4.5302, 0.0407\}$. Se chequeó $V^TV = I$, $U^TU = I$ y la reconstrucción $U\Sigma V^T = A$ (error $\sim 10^{-15}$). Además $\prod \sigma_i = 1.000000 = |\det A|$. ✓

## Ejercicio 2

Considere el problema de contorno

$$\frac{\partial u}{\partial t} = \frac{\partial^2 u}{\partial x^2},\qquad u(0, t) = u(1, t) = 0,\qquad u(x, 0) = x^2.$$

a) Plantear un esquema de diferencias finitas implícito de 4 nodos internos.
b) Indicar cómo quedan las matrices.

> **Errata del enunciado.** El PDF escribe la condición de borde como "$u(1,t) = u(1,t) = 0$", repitiendo $x=1$. Se interpreta como **Dirichlet homogéneo en ambos bordes**, $u(0,t) = u(1,t) = 0$ (es lo único que da un problema bien planteado y es la lectura estándar).

### Resolución

**Malla.** Dominio $x \in [0,1]$ con 4 nodos internos $\Rightarrow$ $h = \tfrac{1}{5} = 0.2$, nodos $x_0 = 0,\ x_1 = 0.2,\ x_2 = 0.4,\ x_3 = 0.6,\ x_4 = 0.8,\ x_5 = 1$. Notación $u_i^k \approx u(x_i, t_k)$, paso temporal $\Delta t$.

**Discretización (Euler implícito / hacia atrás en tiempo).** Derivada temporal hacia atrás y segunda derivada espacial evaluada en el nivel nuevo $k+1$:

$$\frac{u_i^{k+1} - u_i^k}{\Delta t} = \frac{u_{i-1}^{k+1} - 2u_i^{k+1} + u_{i+1}^{k+1}}{h^2}.$$

Con $r = \dfrac{\Delta t}{h^2}$, reordenando para dejar las incógnitas (nivel $k+1$) a la izquierda:

$$\boxed{-r\,u_{i-1}^{k+1} + (1 + 2r)\,u_i^{k+1} - r\,u_{i+1}^{k+1} = u_i^k,\qquad i = 1,2,3,4.}$$

**Borde (Dirichlet homogéneo).** Los bordes son **datos conocidos**: $u_0^{k+1} = u_5^{k+1} = 0$. Como son nulos, los términos $-r\,u_0^{k+1}$ (en la ecuación de $i=1$) y $-r\,u_5^{k+1}$ (en la de $i=4$) **desaparecen** del lado derecho. Las incógnitas son únicamente los 4 nodos internos $u_1, u_2, u_3, u_4$.

**b) Matrices.** El sistema queda tridiagonal $4\times 4$:

$$M\,\mathbf{u}^{k+1} = \mathbf{b}^k,\qquad
M = \begin{pmatrix}
1+2r & -r & 0 & 0 \\
-r & 1+2r & -r & 0 \\
0 & -r & 1+2r & -r \\
0 & 0 & -r & 1+2r
\end{pmatrix},\qquad
\mathbf{u}^{k+1} = \begin{pmatrix} u_1^{k+1} \\ u_2^{k+1} \\ u_3^{k+1} \\ u_4^{k+1} \end{pmatrix}.$$

El lado derecho es simplemente el vector del paso anterior (no hay aporte de borde porque Dirichlet es homogéneo):

$$\mathbf{b}^k = \mathbf{u}^k = \big(u_1^k,\ u_2^k,\ u_3^k,\ u_4^k\big)^T.$$

**Vector de condición inicial** $u_i^0 = (x_i)^2$ con $x_i = 0.2, 0.4, 0.6, 0.8$:

$$\boxed{\mathbf{u}^0 = \begin{pmatrix} 0.2^2 \\ 0.4^2 \\ 0.6^2 \\ 0.8^2 \end{pmatrix} = \begin{pmatrix} 0.04 \\ 0.16 \\ 0.36 \\ 0.64 \end{pmatrix}.}$$

Cada paso temporal se resuelve invirtiendo el mismo $M$ (constante en el tiempo): $\mathbf{u}^{k+1} = M^{-1}\mathbf{u}^k$.

> **Puntos sutiles.** (1) $M$ es **constante** y no depende de $k$: se factoriza (LU) una sola vez. (2) Es simétrica, tridiagonal y **diagonalmente dominante** ($1+2r > 2r$), así que es inversible para todo $r > 0$ — el esquema implícito es incondicionalmente estable. (3) Hay una **incompatibilidad de esquina** en $t=0$, $x=1$: la condición inicial da $u(1,0) = 1^2 = 1$ mientras que el borde pide $u(1,t) = 0$ para $t>0$. Para $t>0$ manda el borde (se toma $u_5^k = 0$); el dato $u_5^0$ no entra en el sistema $4\times4$ de los nodos internos.

**Verificación numérica.** Para $r = 1$ se obtiene $M = \begin{pmatrix}3&-1&0&0\\-1&3&-1&0\\0&-1&3&-1\\0&0&-1&3\end{pmatrix}$ con $\det M = 55 \ne 0$ (sistema bien planteado). El vector inicial computado es $\mathbf{u}^0 = (0.04, 0.16, 0.36, 0.64)$, exactamente $x_i^2$. ✓

## Ejercicio 3

Hallar la Transformada de Fourier de $f(t) = t^2 - t$ si $0 \le t \le 1$, y $f(t) = 0$ en otro caso.

### Resolución

**Definición (convención de la cátedra)** $\hat f(\omega) = \displaystyle\int_{-\infty}^{\infty} f(t)\,e^{-i\omega t}\,dt$. Como $f$ tiene soporte compacto en $[0,1]$, integramos solo ahí:

$$\hat f(\omega) = \int_0^1 (t^2 - t)\,e^{-i\omega t}\,dt.$$

**Caso $\omega = 0$** (espectro en el origen = área bajo $f$):

$$\hat f(0) = \int_0^1 (t^2 - t)\,dt = \Big[\tfrac{t^3}{3} - \tfrac{t^2}{2}\Big]_0^1 = \tfrac13 - \tfrac12 = \boxed{-\tfrac16}.$$

**Caso $\omega \ne 0$.** Separamos $\hat f(\omega) = \displaystyle\int_0^1 t^2 e^{-i\omega t}dt - \int_0^1 t\, e^{-i\omega t}dt$ e integramos por partes. Con $a := -i\omega$ las primitivas son

$$\int t^2 e^{at}\,dt = e^{at}\Big(\tfrac{t^2}{a} - \tfrac{2t}{a^2} + \tfrac{2}{a^3}\Big),\qquad \int t\, e^{at}\,dt = e^{at}\Big(\tfrac{t}{a} - \tfrac{1}{a^2}\Big).$$

Evaluando entre $0$ y $1$ (con $a = -i\omega$, de modo que $e^{a\cdot 1} = e^{-i\omega}$) y agrupando, se obtiene la forma cerrada

$$\boxed{\hat f(\omega) = \frac{(\omega + 2i) + (\omega - 2i)\,e^{-i\omega}}{\omega^3}.}$$

**Parte real e imaginaria.** Usando $e^{-i\omega} = \cos\omega - i\sin\omega$ y separando:

$$\operatorname{Re}\hat f(\omega) = \frac{\omega + \omega\cos\omega - 2\sin\omega}{\omega^3},\qquad
\operatorname{Im}\hat f(\omega) = \frac{2 - \omega\sin\omega - 2\cos\omega}{\omega^3}.$$

> **Punto sutil (límite en $\omega\to 0$).** La forma cerrada parece $\tfrac{0}{0}$ en $\omega = 0$, pero por Taylor ($\cos\omega \approx 1 - \tfrac{\omega^2}{2}$, $\sin\omega \approx \omega - \tfrac{\omega^3}{6}$) se cancela el numerador a orden $\omega^2$ y queda $\operatorname{Re}\hat f \to -\tfrac16$, $\operatorname{Im}\hat f \to 0$, en concordancia con el cálculo directo $\hat f(0) = -\tfrac16$. La transformada es continua en $\omega = 0$.

> **Por qué $\operatorname{Im}\hat f \ne 0$.** El soporte $[0,1]$ no es simétrico respecto del origen, así que $f$ no es par ni impar: el espectro es genuinamente complejo (tiene parte imaginaria), no puramente real ni puramente imaginario.

**Verificación numérica.** Integración numérica (`scipy.quad`) de parte real $\int_0^1(t^2-t)\cos\omega t\,dt$ e imaginaria $-\int_0^1(t^2-t)\sin\omega t\,dt$ coincide con la forma cerrada y con las expresiones de $\operatorname{Re}/\operatorname{Im}$ a $\sim 10^{-8}$ para $\omega \in \{0.5, 1, 2, 3, -1.5, 5\}$; p.ej. $\hat f(1) = -0.142640 + 0.077924\,i$, $\hat f(2) = -0.081361 + 0.126712\,i$. En $\omega = 0$ todas dan $-\tfrac16 = -0.16667$. También se verificaron simbólicamente (`sympy`) las primitivas por partes y la igualdad con $\int_0^1(t^2-t)e^{-i\omega t}dt$. ✓
