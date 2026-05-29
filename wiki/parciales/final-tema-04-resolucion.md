---
tags: [final, transformaciones-lineales, diagonalizacion, nucleo-imagen, fourier-series, qr, svd, plu]
fuente: raw/Practicas/Modelos_Examenes/MNA_Final_Tema_IV.pdf
tipo: final
tema: 4
tiene_resolucion: true
---

# Examen Final de Métodos Numéricos Avanzados — Tema 4 (Resolución)

> **Nota sobre el rótulo.** El archivo de origen es `MNA_Final_Tema_IV.pdf`, pero el encabezado interno del PDF dice **"Tema VII"**. Se conserva el número de archivo (Tema 4 / IV) para la nomenclatura de la wiki; el contenido es el del enunciado reproducido abajo.

Ver páginas teóricas relacionadas: [[../guias/guia-08-fourier-series]], [[../resueltos/resueltos-svd]], [[ip-tema-01-resolucion]] (TL / diagonalización), [[ip-tema-06-resolucion]] (la misma matriz del Ej. 3 aparece allí).

## Ejercicio 1

Dada la TL $T:\mathbb{R}^3\to\mathbb{R}^3:\;T(x,y,z)=(x+y,\;y-z,\;x+z)$

a) Hallar el Núcleo y la Imagen.
b) Decidir si es o no diagonalizable en $\mathbb{R}$.

### Resolución

**Matriz en base canónica.** Las columnas de $M_{EE}(T)$ son $T(e_1),T(e_2),T(e_3)$:

$$T(1,0,0)=(1,0,1),\quad T(0,1,0)=(1,1,0),\quad T(0,0,1)=(0,-1,1),$$

$$A=M_{EE}(T)=\begin{pmatrix}1&1&0\\0&1&-1\\1&0&1\end{pmatrix}.$$

**a) Núcleo e Imagen.** Primero el determinante (expansión por la primera fila):

$$\det A = 1\cdot\big(1\cdot1-(-1)\cdot0\big)-1\cdot\big(0\cdot1-(-1)\cdot1\big)+0 = 1-1 = 0.$$

> **Cuidado.** $\det A = 0$ (no $2$): $T$ **no** es isomorfismo, el núcleo **no** es trivial. Esto se verificó numéricamente; conviene no confiarse del "parece inversible".

Como $\det A=0$, hay núcleo no nulo. Resolvemos $T(x,y,z)=(0,0,0)$:

$$x+y=0,\qquad y-z=0,\qquad x+z=0.$$

De la primera $y=-x$; de la segunda $z=y=-x$; la tercera $x+z=x-x=0$ se cumple automáticamente. Luego todo el núcleo es

$$N(T)=\{\,(x,-x,-x):x\in\mathbb{R}\,\}=\big\langle (1,-1,-1)\big\rangle,\qquad \dim N(T)=1.$$

(Comprobación: $T(1,-1,-1)=(1-1,\,-1+1,\,1-1)=(0,0,0)$ ✓.)

Por el **Teorema de la dimensión**, $\dim N(T)+\dim \operatorname{Im}(T)=3$, de modo que $\dim\operatorname{Im}(T)=2$ y $\operatorname{Im}(T)\ne\mathbb{R}^3$. La imagen está generada por las columnas pivote de $A$ (escalonando, los pivotes quedan en las columnas 1 y 2):

$$\boxed{N(T)=\big\langle(1,-1,-1)\big\rangle,\qquad \operatorname{Im}(T)=\big\langle(1,0,1),\,(1,1,0)\big\rangle.}$$

(La tercera columna es combinación de las otras dos: $(0,-1,1)=(1,0,1)-(1,1,0)$, coherente con $\operatorname{rg}A=2$.)

**b) ¿Diagonalizable en $\mathbb{R}$?** Polinomio característico con la convención de la cátedra $p_A(\lambda)=\det(\lambda I-A)$:

$$\lambda I-A=\begin{pmatrix}\lambda-1&-1&0\\0&\lambda-1&1\\-1&0&\lambda-1\end{pmatrix},$$

$$p_A(\lambda)=\lambda^3-3\lambda^2+3\lambda=\lambda\,(\lambda^2-3\lambda+3).$$

Las raíces del factor cuadrático son

$$\lambda=\frac{3\pm\sqrt{9-12}}{2}=\frac{3}{2}\pm\frac{\sqrt{3}}{2}\,i,$$

(discriminante $9-12=-3<0$). Entonces los autovalores son

$$\lambda_1=0\ (\text{real}),\qquad \lambda_{2,3}=\tfrac{3}{2}\pm\tfrac{\sqrt3}{2}\,i\ (\text{complejos conjugados}).$$

Como **dos de los tres autovalores no son reales**, $A$ no tiene una base de autovectores en $\mathbb{R}^3$.

$$\boxed{T\ \textbf{no es diagonalizable en }\mathbb{R}\ \text{(solo un autovalor real, }\lambda=0\text{; los otros dos son complejos).}}$$

(Sobre $\mathbb{C}$ sí diagonalizaría, pues los tres autovalores son simples.)

## Ejercicio 2

a) Hallar el desarrollo en serie de Fourier de la función $f:[0,1]\to\mathbb{R}:\;f(x)=1-x$, con $f(x)=f(x+1)$ (período $T=1$).
b) Indique a qué converge la serie en $x=0$ y $x=\tfrac12$.

### Resolución

Usamos la convención de la cátedra con período $T=1$ (frecuencia base $\tfrac{2\pi}{T}=2\pi$):

$$f(x)=a_0+\sum_{n\ge1}a_n\cos(2\pi n x)+\sum_{n\ge1}b_n\sin(2\pi n x),$$

con $a_0=\dfrac1T\displaystyle\int_0^1 f$ (valor medio), $a_n=\dfrac2T\displaystyle\int_0^1 f\cos(2\pi n x)\,dx$, $b_n=\dfrac2T\displaystyle\int_0^1 f\sin(2\pi n x)\,dx$.

**a) Coeficientes.**

**Término constante (valor medio):**

$$a_0=\int_0^1 (1-x)\,dx=\Big[x-\tfrac{x^2}{2}\Big]_0^1=1-\tfrac12=\boxed{\tfrac12}.$$

**Cosenos:** con $\omega_n=2\pi n$,

$$a_n=2\int_0^1 (1-x)\cos(2\pi n x)\,dx.$$

Separando, $\displaystyle\int_0^1\cos(2\pi n x)\,dx=0$. Para la parte con $x$, por partes ($\int x\cos(\omega x)dx=\tfrac{x\sin\omega x}{\omega}+\tfrac{\cos\omega x}{\omega^2}$):

$$\int_0^1 x\cos(2\pi n x)\,dx=\Big[\tfrac{x\sin(2\pi n x)}{2\pi n}+\tfrac{\cos(2\pi n x)}{(2\pi n)^2}\Big]_0^1=0+\tfrac{1-1}{(2\pi n)^2}=0.$$

(En $x=1$, $\sin(2\pi n)=0$ y $\cos(2\pi n)=1=\cos 0$.) Por lo tanto

$$\boxed{a_n=0\quad\text{para todo }n\ge1.}$$

**Senos:**

$$b_n=2\int_0^1 (1-x)\sin(2\pi n x)\,dx.$$

De nuevo $\displaystyle\int_0^1\sin(2\pi n x)\,dx=0$, y por partes ($\int x\sin(\omega x)dx=-\tfrac{x\cos\omega x}{\omega}+\tfrac{\sin\omega x}{\omega^2}$):

$$\int_0^1 x\sin(2\pi n x)\,dx=\Big[-\tfrac{x\cos(2\pi n x)}{2\pi n}+\tfrac{\sin(2\pi n x)}{(2\pi n)^2}\Big]_0^1=-\tfrac{1\cdot1}{2\pi n}+0=-\tfrac{1}{2\pi n}.$$

Entonces

$$b_n=2\Big(\underbrace{0}_{\int\sin}-\big(-\tfrac{1}{2\pi n}\big)\Big)=\frac{2}{2\pi n}=\boxed{\frac{1}{\pi n}.}$$

**Serie de Fourier:**

$$\boxed{f(x)=\frac12+\sum_{n=1}^{\infty}\frac{1}{\pi n}\,\sin(2\pi n x).}$$

> Esto es coherente con la simetría: respecto del valor medio $\tfrac12$, la función $g(x)=f(x)-\tfrac12=\tfrac12-x$ es **impar** en $(0,1)$ recentrada, por eso sobreviven solo senos ($a_n=0$). Es la clásica "diente de sierra".

**b) Convergencia (Dirichlet).**

- **En $x=\tfrac12$:** es un punto de **continuidad** de la extensión periódica (dentro de $(0,1)$), así que la serie converge a $f(\tfrac12)=1-\tfrac12=\tfrac12$. (Además, todos los senos valen $\sin(\pi n)=0$, de modo que la suma es exactamente $a_0=\tfrac12$.)

$$\boxed{\text{en }x=\tfrac12:\ \text{converge a }f(\tfrac12)=\tfrac12.}$$

- **En $x=0$ (y en todo entero):** hay un **salto** de la extensión periódica. Por la izquierda $f(0^-)=\lim_{x\to1^-}(1-x)=0$; por la derecha $f(0^+)=1$. Dirichlet da el **promedio**:

$$\tfrac12\big(f(0^+)+f(0^-)\big)=\tfrac12(1+0)=\tfrac12.$$

(También se ve directamente: en $x=0$ todos los senos se anulan, así que la suma vale $a_0=\tfrac12$.)

$$\boxed{\text{en }x=0:\ \text{converge a }\tfrac12\ \text{(promedio del salto }1\leftrightarrow0\text{).}}$$

> Curiosamente la serie vale $\tfrac12$ en **ambos** puntos, pero por razones distintas: en $x=\tfrac12$ es el valor de la función; en $x=0$ es el promedio del salto.

## Ejercicio 3

Dada la matriz

$$A=\begin{pmatrix}1&0&0\\2&-1&0\\-4&0&-1\end{pmatrix}$$

a) Hallar una descomposición $QR$.
b) Hallar una descomposición en valores singulares (SVD).
c) Hallar una descomposición $PLU$.

> Es la **misma matriz** del IP Tema VI, Ej. 2; allí se calculan sus autovalores: $1,-1,-1$ (con $\det A=1\cdot(-1)\cdot(-1)\cdot\ldots=1$; nótese que $A$ es triangular inferior, así que sus autovalores son la diagonal $1,-1,-1$). Ver [[ip-tema-06-resolucion]].

### Resolución

#### a) Factorización $QR$ (Gram–Schmidt por columnas)

Columnas de $A$: $a_1=(1,2,-4)^T$, $a_2=(0,-1,0)^T$, $a_3=(0,0,-1)^T$.

**Columna 1.** $u_1=a_1$,

$$r_{11}=\lVert u_1\rVert=\sqrt{1+4+16}=\sqrt{21}\approx 4.5826,\qquad v_1=\frac{u_1}{\sqrt{21}}=\frac{1}{\sqrt{21}}(1,2,-4)^T.$$

**Columna 2.** Coeficientes de proyección sobre $v_1$:

$$r_{12}=\langle a_2,v_1\rangle=\frac{(0)(1)+(-1)(2)+(0)(-4)}{\sqrt{21}}=-\frac{2}{\sqrt{21}}\approx -0.4364,$$

$$u_2=a_2-r_{12}v_1=(0,-1,0)^T+\frac{2}{21}(1,2,-4)^T=\Big(\tfrac{2}{21},-\tfrac{17}{21},-\tfrac{8}{21}\Big)^T,$$

$$r_{22}=\lVert u_2\rVert=\frac{\sqrt{2^2+17^2+8^2}}{21}=\frac{\sqrt{357}}{21}\approx 0.8997,\qquad v_2=\frac{u_2}{r_{22}}=\frac{1}{\sqrt{357}}(2,-17,-8)^T.$$

**Columna 3.**

$$r_{13}=\langle a_3,v_1\rangle=\frac{(0)(1)+(0)(2)+(-1)(-4)}{\sqrt{21}}=\frac{4}{\sqrt{21}}\approx 0.8729,$$

$$r_{23}=\langle a_3,v_2\rangle=\frac{(0)(2)+(0)(-17)+(-1)(-8)}{\sqrt{357}}=\frac{8}{\sqrt{357}}\approx 0.4234,$$

$$u_3=a_3-r_{13}v_1-r_{23}v_2=\Big(-\tfrac{4}{17},0,-\tfrac{1}{17}\Big)^T,$$

$$r_{33}=\lVert u_3\rVert=\frac{\sqrt{16+1}}{17}=\frac{\sqrt{17}}{17}=\frac{1}{\sqrt{17}}\approx 0.2425,\qquad v_3=\frac{u_3}{r_{33}}=\frac{1}{\sqrt{17}}(-4,0,-1)^T.$$

**Resultado** ($Q$ con columnas $v_i$, $R$ triangular superior con $R_{ii}=\lVert u_i\rVert$, $R_{ij}=\langle a_j,v_i\rangle$):

$$\boxed{Q=\begin{pmatrix}\tfrac{1}{\sqrt{21}}&\tfrac{2}{\sqrt{357}}&-\tfrac{4}{\sqrt{17}}\\[4pt]\tfrac{2}{\sqrt{21}}&-\tfrac{17}{\sqrt{357}}&0\\[4pt]-\tfrac{4}{\sqrt{21}}&-\tfrac{8}{\sqrt{357}}&-\tfrac{1}{\sqrt{17}}\end{pmatrix}\approx\begin{pmatrix}0.2182&0.1058&-0.9701\\0.4364&-0.8997&0\\-0.8729&-0.4234&-0.2425\end{pmatrix},}$$

$$\boxed{R=\begin{pmatrix}\sqrt{21}&-\tfrac{2}{\sqrt{21}}&\tfrac{4}{\sqrt{21}}\\[4pt]0&\tfrac{\sqrt{357}}{21}&\tfrac{8}{\sqrt{357}}\\[4pt]0&0&\tfrac{1}{\sqrt{17}}\end{pmatrix}\approx\begin{pmatrix}4.5826&-0.4364&0.8729\\0&0.8997&0.4234\\0&0&0.2425\end{pmatrix}.}$$

**Verificación.** $Q^TQ=I$ (columnas ortonormales) y $QR=A$ — comprobado en forma exacta con `sympy` ✓.

#### b) Descomposición en valores singulares $A=U\Sigma V^T$

**Paso 1 — autovalores de $A^TA$.**

$$A^TA=\begin{pmatrix}1&2&-4\\0&-1&0\\0&0&-1\end{pmatrix}\begin{pmatrix}1&0&0\\2&-1&0\\-4&0&-1\end{pmatrix}=\begin{pmatrix}21&-2&4\\-2&1&0\\4&0&1\end{pmatrix}.$$

Polinomio característico:

$$p_{A^TA}(\lambda)=\lambda^3-23\lambda^2+23\lambda-1=(\lambda-1)\big(\lambda^2-22\lambda+1\big).$$

Las raíces son $\lambda=1$ y $\lambda=\dfrac{22\pm\sqrt{484-4}}{2}=11\pm 2\sqrt{30}$. Es decir

$$\lambda_1=11+2\sqrt{30}\approx 21.9545,\quad \lambda_2=1,\quad \lambda_3=11-2\sqrt{30}\approx 0.04555.$$

**Valores singulares** $\sigma_i=\sqrt{\lambda_i}$ en orden decreciente. Conviene notar que $11\pm 2\sqrt{30}=(\sqrt6\pm\sqrt5)^2$ (porque $6+5=11$ y $2\sqrt{6\cdot5}=2\sqrt{30}$), así que las raíces salen "lindas":

$$\boxed{\sigma_1=\sqrt6+\sqrt5\approx 4.6856,\qquad \sigma_2=1,\qquad \sigma_3=\sqrt6-\sqrt5\approx 0.2134.}$$

(Chequeo: $\sigma_1\sigma_2\sigma_3=(\sqrt6+\sqrt5)(1)(\sqrt6-\sqrt5)=6-5=1=|\det A|$ ✓.)

**Paso 2 — autovectores de $A^TA$ → columnas de $V$.**

- $\lambda_2=1$: $(A^TA-I)X=0$ con $A^TA-I=\begin{pmatrix}20&-2&4\\-2&0&0\\4&0&0\end{pmatrix}$ da $x=0$ y $-2y+4z=0\Rightarrow y=2z$. Autovector $\tilde v_2=(0,2,1)^T$, $\lVert\tilde v_2\rVert=\sqrt5$:
$$v_2=\frac{1}{\sqrt5}(0,2,1)^T\approx(0,\,0.8944,\,0.4472)^T.$$

- $\lambda_{1,3}=11\pm2\sqrt{30}$: resolviendo $(A^TA-\lambda I)X=0$ se obtienen (despejando) los autovectores sin normalizar
$$\tilde v_1=(5+\sqrt{30},\,-1,\,2)^T,\qquad \tilde v_3=(5-\sqrt{30},\,-1,\,2)^T,$$
con $\lVert\tilde v_1\rVert=\sqrt{60+10\sqrt{30}}\approx 10.7132$ y $\lVert\tilde v_3\rVert=\sqrt{60-10\sqrt{30}}\approx 2.2864$. Normalizando (los números quedan irracionales, se dan en decimales):
$$v_1\approx(0.9780,\,-0.0933,\,0.1867)^T,\qquad v_3\approx(-0.2087,\,-0.4374,\,0.8747)^T.$$

$$V=\begin{pmatrix}0.9780&0&-0.2087\\-0.0933&0.8944&-0.4374\\0.1867&0.4472&0.8747\end{pmatrix}.$$

**Paso 3 — columnas de $U$** mediante $u_i=\dfrac{Av_i}{\sigma_i}$ (todos los $\sigma_i>0$, así que $U$ queda completa):

$$u_1\approx(0.2087,\,0.4374,\,-0.8747)^T,\quad u_2\approx(0,\,-0.8944,\,-0.4472)^T,\quad u_3\approx(-0.9780,\,0.0933,\,-0.1867)^T.$$

$$U\approx\begin{pmatrix}0.2087&0&-0.9780\\0.4374&-0.8944&0.0933\\-0.8747&-0.4472&-0.1867\end{pmatrix},\qquad \Sigma=\begin{pmatrix}\sqrt6+\sqrt5&0&0\\0&1&0\\0&0&\sqrt6-\sqrt5\end{pmatrix}.$$

**Verificación.** $U^TU=V^TV=I$ y $U\Sigma V^T=A$ — comprobado en forma **exacta** con `sympy` (usando los autovectores con radicales), reconstruyendo $A$ sin error ✓.

$$\boxed{A=U\Sigma V^T\ \text{con}\ \sigma=\{\sqrt6+\sqrt5,\,1,\,\sqrt6-\sqrt5\},\ U,V\ \text{ortogonales }3\times3.}$$

#### c) Factorización $PLU$ (Doolittle)

$A$ es **triangular inferior** con diagonal $(1,-1,-1)$, todos no nulos, así que **no hace falta permutar** ($P=I$). Igual aplicamos Doolittle para exhibir $L$ y $U$.

**Pivote $a_{11}=1$.** Multiplicadores $m_{21}=\tfrac{a_{21}}{a_{11}}=\tfrac{2}{1}=2$ y $m_{31}=\tfrac{a_{31}}{a_{11}}=\tfrac{-4}{1}=-4$. Operaciones $F_2\leftarrow F_2-2F_1$, $F_3\leftarrow F_3-(-4)F_1$:

$$\begin{pmatrix}1&0&0\\2&-1&0\\-4&0&-1\end{pmatrix}\longrightarrow\begin{pmatrix}1&0&0\\0&-1&0\\0&0&-1\end{pmatrix}.$$

**Pivote $a_{22}=-1$.** El elemento debajo, $a_{32}$, ya es $0$, así que $m_{32}=0$ y la matriz ya está en forma triangular superior. Por lo tanto

$$\boxed{P=I=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix},\quad L=\begin{pmatrix}1&0&0\\2&1&0\\-4&0&1\end{pmatrix},\quad U=\begin{pmatrix}1&0&0\\0&-1&0\\0&0&-1\end{pmatrix}.}$$

**Verificación.** $LU=A$ y $PA=LU$ — comprobado en forma exacta ✓. (Resulta $U=$ la propia diagonal de $A$ y $L$ recoge $-A$ fuera de la diagonal en la primera columna: como $A$ ya era triangular inferior, $LU$ no hace más que "separarla" en su diagonal y su parte estrictamente inferior.)

> **Sobre el pivoteo.** Numéricamente, `scipy.linalg.lu` aplica pivoteo parcial (busca el mayor pivote $|{-4}|$ y permuta), devolviendo un $P\ne I$ y otros $L,U$; esa factorización también es válida. La de la cátedra (Doolittle sin pivoteo, posible porque ningún pivote se anula) es la que se pide y da $P=I$ con resultados enteros.

---

## Resumen de verificaciones (numpy / sympy)

| Resultado | Chequeo | Estado |
|---|---|---|
| Ej. 1 | $\det A=0$, $N(T)=\langle(1,-1,-1)\rangle$, autovalores $0,\;\tfrac32\pm\tfrac{\sqrt3}{2}i$ | ✓ |
| Ej. 2 | $a_0=\tfrac12$, $a_n=0$, $b_n=\tfrac1{\pi n}$ (cuadratura), sumas parciales $\to\tfrac12$ en $x=0,\tfrac12$ | ✓ |
| Ej. 3a | $Q^TQ=I$, $QR=A$ (exacto) | ✓ |
| Ej. 3b | $\sigma=\{\sqrt6+\sqrt5,1,\sqrt6-\sqrt5\}$, $U^TU=V^TV=I$, $U\Sigma V^T=A$ (exacto) | ✓ |
| Ej. 3c | $P=I$, $LU=A$ (exacto) | ✓ |
