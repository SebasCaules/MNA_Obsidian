---
tags: [final, transformaciones-lineales, diagonalizacion, fourier, qr]
fuente: raw/Practicas/Modelos_Examenes/MNA_Final_Tema_VII.pdf
tipo: final
tema: 7
tiene_resolucion: true
---

# Examen Final de Métodos Numéricos Avanzados — Tema VII (Resolución)

Enunciado base en [[final-tema-07]]. Referencias de método: [[../resueltos/resueltos-diagonalizacion]], [[../resueltos/resueltos-fourier]], [[../guias/guia-08-fourier-series]].

## Ejercicio 1

Dada la TL $T : \mathbb{R}^3 \to \mathbb{R}^3 : T(x, y, z) = (k x,\ 2x - 2y - z,\ -2x + 5y + 4z)$

a) Hallar todos los valores de $k \in \mathbb{R}$ tales que $\dim(R(T)) < 3$.
b) Hallar todos los valores de $k \in \mathbb{R}$ para que $T$ sea diagonalizable en $\mathbb{R}$.

### Resolución

La matriz en base canónica (columnas $= T(e_j)$) es

$$M_{EE}(T) = A = \begin{pmatrix} k & 0 & 0 \\ 2 & -2 & -1 \\ -2 & 5 & 4 \end{pmatrix}.$$

**a) ¿Cuándo $\dim R(T) < 3$?** La imagen es el espacio columna, y $\dim R(T) = \operatorname{rg}(A)$. Para una matriz $3\times3$,

$$\dim R(T) < 3 \iff \operatorname{rg}(A) < 3 \iff \det A = 0.$$

Como la primera fila es $(k,0,0)$, desarrollamos el determinante por esa fila:

$$\det A = k\cdot\det\begin{pmatrix} -2 & -1 \\ 5 & 4 \end{pmatrix} = k\,\big((-2)(4) - (-1)(5)\big) = k\,(-8 + 5) = -3k.$$

$$\boxed{\det A = -3k = 0 \iff k = 0.}$$

Para todo $k \ne 0$ se tiene $\det A \ne 0$, $T$ es isomorfismo y $\dim R(T) = 3$. **Sólo $k=0$** hace $\dim R(T) < 3$ (de hecho $\operatorname{rg}(A)=2$, así que $\dim R(T)=2$).

**b) ¿Cuándo $T$ es diagonalizable en $\mathbb{R}$?** Buscamos los autovalores. El polinomio característico es muy cómodo por la estructura **bloque-triangular** de $A$: la primera columna es $(k,2,-2)^T$ pero la primera **fila** es $(k,0,0)$, lo que al armar $\lambda I - A$ deja la primera fila $(\lambda-k,\,0,\,0)$. Desarrollando $p_A(\lambda)=\det(\lambda I - A)$ por esa fila:

$$p_A(\lambda) = (\lambda - k)\,\det\begin{pmatrix} \lambda+2 & 1 \\ -5 & \lambda-4 \end{pmatrix} = (\lambda - k)\big[(\lambda+2)(\lambda-4) + 5\big] = (\lambda-k)(\lambda^2 - 2\lambda - 3).$$

$$\boxed{p_A(\lambda) = (\lambda - k)(\lambda - 3)(\lambda + 1).}$$

Es decir, el **bloque inferior** $\begin{pmatrix}-2&-1\\5&4\end{pmatrix}$ aporta los autovalores fijos $3$ y $-1$, y el lugar $(1,1)$ aporta $\lambda = k$. Los autovalores son entonces $\{k,\ 3,\ -1\}$, y hay que estudiar las repeticiones.

**Caso genérico $k \notin \{3, -1\}$.** Los tres autovalores $k, 3, -1$ son **distintos** $\Rightarrow$ tres autovalores reales simples $\Rightarrow$ $T$ es diagonalizable. ✓

Antes de los casos repetidos conviene tener los autovectores "estructurales". El autovalor $\lambda=k$ siempre tiene como autovector

$$v_k = (k+1,\ 2,\ -2)^T \qquad \big((A-kI)v_k = 0\big),$$

mientras que los autovectores que vienen del bloque inferior viven en el plano $x=0$:

$$\lambda = -1:\quad v_{-1} = (0,\ 1,\ -1)^T, \qquad \lambda = 3:\quad v_{3} = (0,\ -1,\ 5)^T.$$

(Para el bloque, $\lambda=3$ da autovector $(-1,5)$ en $(y,z)$ y $\lambda=-1$ da $(1,-1)$; ambos con primera componente nula porque la primera ecuación $k x = \lambda x$ con $\lambda\ne k$ obliga $x=0$.)

**Caso $k = 3$ (autovalor $\lambda=3$ doble).** Multiplicidad algebraica $m_a(3)=2$, $m_a(-1)=1$. Estudiamos $m_g(3)=\dim N(A-3I)$:

$$A - 3I = \begin{pmatrix} 0 & 0 & 0 \\ 2 & -5 & -1 \\ -2 & 5 & 1 \end{pmatrix} \xrightarrow{\text{Gauss}} \begin{pmatrix} 1 & -\tfrac52 & -\tfrac12 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}.$$

La primera fila se anula (porque $\lambda=k=3$ hace $\lambda - k = 0$) y la tercera es $-1$ veces la segunda, así que **queda una sola ecuación** $x = \tfrac52 y + \tfrac12 z$, con $y,z$ libres:

$$\boxed{m_g(3) = 2 = m_a(3)} \implies S_3 = \big\langle (5,\,2,\,0),\ (1,\,0,\,2)\big\rangle.$$

Como además $m_g(-1)=m_a(-1)=1$, **$T$ es diagonalizable** para $k=3$. Una base de autovectores y la matriz diagonal:

$$P = \begin{pmatrix} 5 & 1 & 0 \\ 2 & 0 & 1 \\ 0 & 2 & -1 \end{pmatrix},\qquad D = \begin{pmatrix} 3 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & -1 \end{pmatrix},\qquad \det P = -8 \ne 0.$$

(Verificación: $AP = PD$ ✓.)

**Caso $k = -1$ (autovalor $\lambda=-1$ doble).** Ahora $m_a(-1)=2$, $m_a(3)=1$. Estudiamos $m_g(-1)=\dim N(A+I)$:

$$A + I = \begin{pmatrix} 0 & 0 & 0 \\ 2 & -1 & -1 \\ -2 & 5 & 5 \end{pmatrix} \xrightarrow{\text{Gauss}} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{pmatrix}.$$

Aquí la primera fila también se anula (por $\lambda - k = 0$), pero las filas 2 y 3 **no** son proporcionales (al reducir quedan $x=0$ y $y+z=0$), de modo que el rango de $A+I$ es $2$ y el núcleo tiene dimensión $1$:

$$\boxed{m_g(-1) = 1 < 2 = m_a(-1)} \implies S_{-1} = \big\langle (0,\,1,\,-1)\big\rangle.$$

Falta un autovector $\Rightarrow$ **$T$ NO es diagonalizable** para $k=-1$.

> **Sutileza (por qué $k=3$ sí y $k=-1$ no).** En ambos casos un autovalor del bloque colisiona con $\lambda=k$, pero el desenlace es opuesto. La clave es el autovector "móvil" $v_k=(k+1,2,-2)$:
> - En $k=3$, $v_k=(4,2,-2)\parallel(2,1,-1)$ **no** está en el plano $x=0$ donde vive el autovector del bloque $v_3=(0,-1,5)$. Son linealmente independientes, así que $S_3$ es genuinamente 2-dimensional.
> - En $k=-1$, $v_k=(0,2,-2)\parallel(0,1,-1)$ es **exactamente** el autovector del bloque $v_{-1}$. Los dos candidatos colapsan en la misma dirección y el autoespacio queda de dimensión 1.

**Conclusión.**

$$\boxed{T \text{ es diagonalizable en }\mathbb{R} \iff k \ne -1.}$$

(Esto incluye $k=0$ —pese a que allí $T$ no es inyectiva, los autovalores $0,3,-1$ son distintos— y el caso especial $k=3$.)

**Verificación numérica.** `sympy`: $\det A = -3k$ (raíz $k=0$); $p_A(\lambda)=(\lambda-k)(\lambda-3)(\lambda+1)$. Para $k=3$, `is_diagonalizable()` $=$ True con $m_g(3)=2$; para $k=-1$, $=$ False con $m_g(-1)=1$. Barriendo con `numpy.linalg.eig` y midiendo $\operatorname{rg}$ de la matriz de autovectores: $k\in\{-2,0,3,5\}\to$ rango 3 (diagonalizable), $k=-1\to$ rango 2 (no diagonalizable). Para $k=3$, $AP-PD=0$ con $P,D$ de arriba ✓.

## Ejercicio 2

a) Hallar el desarrollo en serie de Fourier de $f : [0, 1] \to \mathbb{R} : f(x) = 1 - x$, extendiéndola con $f(x) = f(x + 1)$ para todo $x\in\mathbb{R}$.
b) Indique a qué converge la serie en $x = 0$ y $x = \dfrac{1}{2}$.

### Resolución

Es la onda **diente de sierra** de período $T=1$: en cada celda $[0,1)$ vale $1-x$, que decrece de $f(0^+)=1$ a $f(1^-)=0$ y luego salta de vuelta a $1$. La frecuencia fundamental es $\omega_0=\tfrac{2\pi}{T}=2\pi$. Usamos la convención de la cátedra:

$$f(x) = a_0 + \sum_{n=1}^{\infty} a_n\cos(2\pi n x) + \sum_{n=1}^{\infty} b_n\sin(2\pi n x),$$

con $a_0=\tfrac1T\int_T f$ (**valor medio**), $a_n=\tfrac2T\int_T f\cos(2\pi n x)\,dx$, $b_n=\tfrac2T\int_T f\sin(2\pi n x)\,dx$. Aquí $T=1$.

**Término constante (valor medio).**

$$a_0 = \int_0^1 (1-x)\,dx = \left[x - \tfrac{x^2}{2}\right]_0^1 = 1 - \tfrac12 = \frac12.$$

**Coeficientes coseno.** Separamos $\int_0^1(1-x)\cos(2\pi n x)dx = \int_0^1\cos(2\pi n x)dx - \int_0^1 x\cos(2\pi n x)dx$. El primero es $0$. El segundo, por partes, vale $\dfrac{\cos(2\pi n)-1}{(2\pi n)^2}=0$ (pues $\cos(2\pi n)=1$). Por lo tanto

$$a_n = 2\int_0^1 (1-x)\cos(2\pi n x)\,dx = 0\qquad (n\ge 1).$$

**Coeficientes seno.** Con $\int_0^1\sin(2\pi n x)dx = 0$ y, por partes, $\displaystyle\int_0^1 x\sin(2\pi n x)\,dx = -\frac{\cos(2\pi n)}{2\pi n} = -\frac{1}{2\pi n}$ (usa $\cos(2\pi n)=1$, $\sin(2\pi n)=0$):

$$b_n = 2\int_0^1 (1-x)\sin(2\pi n x)\,dx = 2\Big(\underbrace{\textstyle\int_0^1\sin(2\pi n x)dx}_{0} - \underbrace{\textstyle\int_0^1 x\sin(2\pi n x)dx}_{-1/(2\pi n)}\Big) = 2\cdot\frac{1}{2\pi n} = \frac{1}{\pi n}.$$

(El signo importa: el aporte de $-x$ resulta positivo, dando $b_n>0$.)

$$\boxed{f(x) = \frac12 + \sum_{n=1}^{\infty} \frac{1}{\pi n}\,\sin(2\pi n x).}$$

**Verificación numérica.** Integrando con `scipy.quad`: $a_0=0.5$, $a_n\approx 0$ y $b_n=\{0.31831,\,0.15915,\,0.10610,\,0.07958,\dots\}$, que coincide con $\tfrac{1}{\pi n}=\{1/\pi,\,1/2\pi,\,1/3\pi,\,1/4\pi,\dots\}$. Simbólicamente (`sympy`, $n$ entero) $a_n=\tfrac{\sin^2(\pi n)}{\pi^2 n^2}=0$ y $b_n=\tfrac{1}{\pi n}$ exacto ✓.

**b) Convergencia puntual (Dirichlet).**

- En $x=\tfrac12$ la función es **continua** (interior de la celda, $f$ lineal allí), así que la serie converge al valor de la función:
  $$\boxed{S\!\left(\tfrac12\right) = f\!\left(\tfrac12\right) = 1 - \tfrac12 = \frac12.}$$
  Además, en $x=\tfrac12$ todos los senos valen $\sin(\pi n)=0$, de modo que la serie da directamente $a_0=\tfrac12$, consistente.

- En $x=0$ hay un **salto** (extremo de la celda): por la derecha $f(0^+)=1$ y por la izquierda $f(0^-)=f(1^-)=0$. La serie converge al **promedio** del salto:
  $$\boxed{S(0) = \tfrac12\big(f(0^+) + f(0^-)\big) = \tfrac12(1 + 0) = \frac12.}$$
  (También coincide con $a_0=\tfrac12$, ya que $\sin(0)=0$ anula toda la suma de senos.)

> Curiosidad: en este diente de sierra particular **ambos** puntos dan $\tfrac12$, pero por razones distintas (continuidad en $x=\tfrac12$, promedio del salto en $x=0$).

**Verificación numérica.** Sumas parciales $S_N$ con $N=10,100,1000,5000$: $S(0)\to 0.500000$ y $S(\tfrac12)\to 0.500000$ ✓ (cerca de $x=0$ persiste el *overshoot* de Gibbs, pero el valor exacto en el punto es $\tfrac12$).

## Ejercicio 3

Hallar una factorización $QR$ para $A = \begin{pmatrix} 1 & -3 & 2 \\ 5 & 2 & 0 \end{pmatrix}$.

### Resolución

$A$ es $2\times3$: tiene **3 columnas en $\mathbb{R}^2$**. Hacemos Gram–Schmidt sobre las columnas

$$a_1 = \begin{pmatrix}1\\5\end{pmatrix},\qquad a_2 = \begin{pmatrix}-3\\2\end{pmatrix},\qquad a_3 = \begin{pmatrix}2\\0\end{pmatrix}.$$

Como $\mathbb{R}^2$ tiene dimensión 2, las tres columnas **no pueden ser linealmente independientes**: la tercera será combinación de las dos primeras, lo que hará $u_3 = 0$. El resultado es un $Q$ ortogonal $2\times2$ y un $R$ rectangular $2\times3$ triangular superior (rango deficiente por columnas).

**Columna 1.** $u_1 = a_1$, con

$$r_{11} = \lVert u_1\rVert = \sqrt{1^2 + 5^2} = \sqrt{26} \approx 5.0990,\qquad v_1 = \frac{u_1}{r_{11}} = \frac{1}{\sqrt{26}}\begin{pmatrix}1\\5\end{pmatrix} \approx \begin{pmatrix}0.1961\\0.9806\end{pmatrix}.$$

**Columna 2.** Coeficiente de proyección y ortogonalización:

$$r_{12} = \langle a_2, v_1\rangle = \frac{1}{\sqrt{26}}\big((-3)(1) + (2)(5)\big) = \frac{7}{\sqrt{26}} \approx 1.3728,$$

$$u_2 = a_2 - r_{12}\,v_1 = \begin{pmatrix}-3\\2\end{pmatrix} - \frac{7}{26}\begin{pmatrix}1\\5\end{pmatrix} = \begin{pmatrix}-\tfrac{85}{26}\\[2pt] \tfrac{17}{26}\end{pmatrix} \approx \begin{pmatrix}-3.2692\\0.6538\end{pmatrix},$$

$$r_{22} = \lVert u_2\rVert = \frac{17}{\sqrt{26}} \approx 3.3340,\qquad v_2 = \frac{u_2}{r_{22}} = \frac{1}{\sqrt{26}}\begin{pmatrix}-5\\1\end{pmatrix} \approx \begin{pmatrix}-0.9806\\0.1961\end{pmatrix}.$$

(Como estamos en $\mathbb{R}^2$, $v_2$ es la única dirección unitaria $\perp v_1$, salvo signo: en efecto $v_2\propto(-5,1)\perp(1,5)$.) Con $\{v_1,v_2\}$ ya tenemos una base ortonormal de $\mathbb{R}^2$.

**Columna 3.** Sus coeficientes contra la base ya construida:

$$r_{13} = \langle a_3, v_1\rangle = \frac{1}{\sqrt{26}}(2\cdot1 + 0\cdot5) = \frac{2}{\sqrt{26}} \approx 0.3922,$$
$$r_{23} = \langle a_3, v_2\rangle = \frac{1}{\sqrt{26}}(2\cdot(-5) + 0\cdot1) = -\frac{10}{\sqrt{26}} \approx -1.9612,$$

$$u_3 = a_3 - r_{13}\,v_1 - r_{23}\,v_2 = \begin{pmatrix}2\\0\end{pmatrix} - \frac{2}{26}\begin{pmatrix}1\\5\end{pmatrix} - \frac{-10}{26}\begin{pmatrix}-5\\1\end{pmatrix} = \begin{pmatrix}0\\0\end{pmatrix}.$$

Como anticipamos, $u_3 = 0$: $a_3$ ya es combinación lineal de $v_1, v_2$ (de hecho de cualquier base de $\mathbb{R}^2$). No genera nueva columna de $Q$; sus coeficientes $r_{13}, r_{23}$ ocupan la tercera columna de $R$.

**Resultado.** $Q = (v_1\mid v_2)$ es $2\times2$ y $R = Q^TA$ es $2\times3$:

$$\boxed{Q = \frac{1}{\sqrt{26}}\begin{pmatrix} 1 & -5 \\ 5 & 1 \end{pmatrix} \approx \begin{pmatrix} 0.1961 & -0.9806 \\ 0.9806 & 0.1961 \end{pmatrix},\qquad R = \frac{1}{\sqrt{26}}\begin{pmatrix} 26 & 7 & 2 \\ 0 & 17 & -10 \end{pmatrix} \approx \begin{pmatrix} 5.0990 & 1.3728 & 0.3922 \\ 0 & 3.3340 & -1.9612 \end{pmatrix}.}$$

(Equivalente: $r_{11}=\sqrt{26}$, $r_{12}=\tfrac{7}{\sqrt{26}}$, $r_{13}=\tfrac{2}{\sqrt{26}}$, $r_{22}=\tfrac{17}{\sqrt{26}}$, $r_{23}=-\tfrac{10}{\sqrt{26}}$.)

**Observación sobre el rango.** $\operatorname{rg}(A)=2$ (las dos primeras columnas son LI). Aunque haya 3 columnas, sólo 2 son independientes; por eso $Q$ tiene **2 columnas** y la tercera columna de $R$ no tiene pivote propio ($R$ es "ancha"). Esta es la forma reducida $A = Q\,R$ con $Q$ de columnas ortonormales ($Q^TQ = I_2$) y $R$ triangular superior $2\times3$.

**Verificación.** $Q^TQ = I_2$ ✓ y

$$QR = \frac{1}{26}\begin{pmatrix} 1 & -5 \\ 5 & 1 \end{pmatrix}\begin{pmatrix} 26 & 7 & 2 \\ 0 & 17 & -10 \end{pmatrix} = \begin{pmatrix} 1 & -3 & 2 \\ 5 & 2 & 0 \end{pmatrix} = A. \quad ✓$$

(`sympy` confirma $QR - A = 0$ y $Q^TQ = I$ exactamente; `numpy.linalg.qr` da el mismo $Q,R$ salvo el signo global de la primera columna —convención de signo de LAPACK—, y $\operatorname{rg}(A)=2$.)

---

## Resumen de resultados

| Ej. | Resultado |
|---|---|
| 1a | $\det A = -3k$ → $\dim R(T) < 3 \iff k = 0$ (allí $\dim R(T)=2$) |
| 1b | Autovalores $\{k, 3, -1\}$; diagonalizable $\iff k \ne -1$ (en $k=3$ sí: $m_g=2$; en $k=-1$ no: $m_g=1$) |
| 2a | $f(x) = \tfrac12 + \sum_{n\ge1}\tfrac{1}{\pi n}\sin(2\pi n x)$ |
| 2b | $S(0) = \tfrac12$ (promedio del salto); $S(\tfrac12) = \tfrac12$ (continuidad) |
| 3 | $Q = \tfrac{1}{\sqrt{26}}\begin{pmatrix}1&-5\\5&1\end{pmatrix}$, $R = \tfrac{1}{\sqrt{26}}\begin{pmatrix}26&7&2\\0&17&-10\end{pmatrix}$; $u_3=0$ por rango deficiente de columnas |
