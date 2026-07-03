---
tags: [finales, historico, banco, practica, svd, cuadrados-minimos, diagonalizacion]
fuente: raw/Practicas/Examenes_Historicos/ (finales reales 2009-2022)
---
# Banco de ejercicios de finales históricos — solo los que caen en tu programa 2026

De los [[catalogo-finales|40 finales históricos]] (programa viejo *Métodos Numéricos (K)*, dominado por métodos numéricos clásicos), estos son los **únicos ejercicios que corresponden a tu temario 2026** (álgebra lineal + Fourier). Todos verificados numéricamente. Sirven como **práctica real de examen** que complementa los [[../parciales/patrones|30 modelos oficiales]].

> El resto de esos finales (interpolación, Chebyshev, Newton-Raphson, Taylor, optimización por máximo descenso, EDOs por Taylor/Euler) **no entra en tu final** — quedan catalogados en [[catalogo-finales]] por si los necesitás.

---

## 1. Cuadrados mínimos (ajuste de curvas)

Método base: [[../guias/guia-07-svd-mmcc]] · [[../resueltos/resueltos-pseudoinversa]] · [[../clases/clase-2026-05-14]].
Se plantea $A\vec{x}\approx \vec{y}$ y se resuelve por **ecuaciones normales** $A^{T}A\,\vec{x}=A^{T}\vec{y}$ (vía Cholesky, porque $A^TA$ es simétrica definida positiva si $A$ tiene columnas LI), o por **SVD** ($\vec{x}=A^{+}\vec{y}$).

### 1.1 — Ajuste de temperatura (Final 2009, ej. 1)

> Se modela la temperatura como $T(t)=\alpha\,\sin\!\big(2\pi \tfrac{t}{24}\big)+\beta$. Con mediciones $(t_k,T_k)$, $k=1,\dots,100$ (errores de media 0), plantee el problema de cuadrados mínimos para estimar $\alpha,\beta$.

**Resolución.** El modelo es lineal en los parámetros $\alpha,\beta$. Con
$$
A=\begin{pmatrix}\sin(2\pi t_1/24) & 1\\ \vdots & \vdots\\ \sin(2\pi t_{100}/24) & 1\end{pmatrix}\in\mathbb{R}^{100\times2},\quad
\vec{x}=\begin{pmatrix}\alpha\\\beta\end{pmatrix},\quad
\vec{y}=\begin{pmatrix}T_1\\\vdots\\T_{100}\end{pmatrix},
$$
se busca $\min_{\vec x}\lVert A\vec x-\vec y\rVert_2$. Solución: ecuaciones normales $A^TA\,\vec x=A^T\vec y$ (sistema $2\times2$), o $\vec x=A^{+}\vec y$ con la pseudoinversa. La clave de examen: **reconocer que un modelo no lineal en $t$ pero lineal en los parámetros es un MMCC lineal**.

### 1.2 — Ajuste polinómico vía Cholesky (Final 2019, ej. 2) ✅ resuelto

> Ajuste $y=ax^3+bx+c$ a la tabla, por cuadrados mínimos usando descomposición **Cholesky**. Valores exactos.
>
> | $x_k$ | -2 | -1 | 0 | 1 | 2 |
> |---|---|---|---|---|---|
> | $y_k$ | -9 | 0 | 3 | 6 | 15 |

**Resolución.** Columnas $[\,x^3,\ x,\ 1\,]$:
$$
A=\begin{pmatrix}-8&-2&1\\-1&-1&1\\0&0&1\\1&1&1\\8&2&1\end{pmatrix},\quad \vec y=\begin{pmatrix}-9\\0\\3\\6\\15\end{pmatrix}.
$$
Ecuaciones normales $A^TA\,\vec v=A^T\vec y$ con $\vec v=(a,b,c)^T$:
$$
A^TA=\begin{pmatrix}130&34&0\\34&10&0\\0&0&5\end{pmatrix},\qquad A^T\vec y=\begin{pmatrix}198\\54\\15\end{pmatrix}.
$$
Cholesky de $A^TA=LL^T$ (bloque $2\times2$): $\ell_{11}=\sqrt{130}$, $\ell_{21}=34/\sqrt{130}$, $\ell_{22}=\sqrt{10-34^2/130}=\sqrt{10-8.8923}=\sqrt{1.1077}\approx1.0525$; el bloque $(3,3)$ da $\sqrt5$. Resolviendo $L\vec z=A^T\vec y$ y $L^T\vec v=\vec z$:
$$
\boxed{a=1,\quad b=2,\quad c=3}\qquad\Rightarrow\qquad y=x^3+2x+3.
$$
Los datos son **exactos** (el residuo es 0): $x{=}{-}2\!\to\!-9$, $x{=}0\!\to\!3$, $x{=}2\!\to\!15$. Verificado.

### 1.3 — MMCC vía Cholesky / SVD (compendio *Ejercicios para Final*)

El compendio [`Metodos Numéricos - Ejercicios para Final.pdf`](../../raw/Practicas/Examenes_Historicos/Finales/Metodos%20Nume%CC%81ricos%20-%20Ejercicios%20para%20Final.pdf) tiene varios ajustes por Cholesky y por SVD (buscar "cuadrados mínimos" / "descomposición en valores singulares"). Mismo procedimiento que 1.2.

---

## 2. Número de condición $\kappa_2(A)$ vía SVD / autovalores

Aplicación directa de SVD ([[../resueltos/resueltos-svd]]). Definición: $\kappa_2(A)=\dfrac{\sigma_{\max}(A)}{\sigma_{\min}(A)}$.

### 2.1 — κ₂ y matriz hermítica (Final 2010, ej. 1) ✅ resuelto

> (a) ¿Cómo se obtiene $\kappa_2(A)$ a partir de los valores singulares? (b) Si $A$ es hermítica, ¿cómo se obtiene de sus autovalores? (c) Calcule $\kappa_2$ de $A=\begin{pmatrix}-3&2\\2&4\end{pmatrix}$.

**Resolución.**
(a) $\kappa_2(A)=\sigma_{\max}/\sigma_{\min}$.
(b) Para $A$ hermítica, $\sigma_i=|\lambda_i|$ (los valores singulares son los módulos de los autovalores), luego $\kappa_2(A)=\dfrac{\max_i|\lambda_i|}{\min_i|\lambda_i|}$.
(c) $p_A(\lambda)=(-3-\lambda)(4-\lambda)-4=\lambda^2-\lambda-16$, de donde $\lambda=\tfrac{1\pm\sqrt{65}}{2}\Rightarrow \lambda_1\approx4.5311,\ \lambda_2\approx-3.5311$.
$$
\kappa_2(A)=\frac{|\lambda_1|}{|\lambda_2|}=\frac{4.5311}{3.5311}\approx \boxed{1.2832}.
$$

### 2.2 — κ₂ de matriz casi singular (compendio)

> Para cierta $A$ dependiente de $\varepsilon$ con $|\varepsilon|\ll1$, mostrar que $\kappa_2(A)\approx 4/|\varepsilon|$.

Idea: cuando $\sigma_{\min}\to0$ (matriz casi singular), $\kappa_2\to\infty$; el mal condicionamiento se lee en el **valor singular más chico**. Ver enunciado completo en el compendio (línea "número de condición $\kappa_2(A)\approx 4/|\varepsilon|$").

---

## 3. SVD (cálculo y uso)

Método paso a paso: [[../resueltos/resueltos-svd]] · [[../pizarrones/pizarron-svd]].

### 3.1 — SVD + valores singulares nulos por dependencia lineal (Final 2F 19-02-2021)

> Sin hacer cuentas, explique cuántos valores singulares nulos tiene $A$ (una fila/columna es combinación lineal de otras).

**Idea clave.** $\#\{\sigma_i=0\}=n-\operatorname{rango}(A)$. Si una columna es combinación lineal de las otras, $\operatorname{rango}<n$ y hay (al menos) **un valor singular nulo**. No hace falta calcular la SVD: se razona por el rango. (En el archivo lo verifican con `np.linalg.svd`.)

### 3.2 — SVD para resolver MMCC (Final 2016-07-07)

Calcula la SVD de una matriz y la usa para el problema de cuadrados mínimos ($\vec x=A^+\vec y=V\Sigma^{+}U^T\vec y$). Mismo esquema que [[../resueltos/resueltos-pseudoinversa]].

---

## 4. Diagonalización / definida positiva

Método: [[../resueltos/resueltos-diagonalizacion]] · [[../clases/clase-2026-04-30]].

### 4.1 — Definida positiva vía autovalores (Final 2022-07-15)

Para justificar que una matriz simétrica surgida de un esquema de diferencias finitas es **definida positiva**, se chequea que **todos sus autovalores sean $>0$** (criterio para simétricas). Conecta diagonalización con existencia de Cholesky (una matriz simétrica admite Cholesky $\iff$ es definida positiva).

---

## 5. Diferencias finitas (ecuación del calor / difusión / Poisson)

Esto **sí está en tus modelos oficiales** (esquema implícito de Euler hacia atrás, $h=1/5$). Ver los finales modelo con diferencias finitas en [[../parciales/patrones]].

- **Final 2016-07-07**: ecuación de difusión $\hat A_{k,l}$, condición inicial $t(1-t)$, contorno homogéneo — mismo esquema tridiagonal.
- **Final 2022-07-15**: esquema 2D tipo Poisson, matriz con **4s en la diagonal**, se resuelve el sistema por **LU** (con 1s en la diagonal de $L$) — practica el armado de la matriz del stencil 2D.
- **Final 2017-Julio**: otra difusión con diferencias finitas.

Estos ejercicios entrenan: armar la matriz del stencil, aplicar condiciones de borde (Dirichlet/Neumann con nodos fantasma) y resolver el sistema lineal (LU/PLU, [[../clases/clase-2026-05-07]]).

---

Ver también: [[catalogo-finales|catálogo completo de finales históricos]] · [[../index|índice de la wiki]] · [[../parciales/patrones|patrones de los 30 modelos]]
