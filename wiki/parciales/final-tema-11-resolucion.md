---
tags: [final, transformaciones-lineales, diagonalizacion, sobreyectividad, nucleo-imagen, sistemas-lineales, svd, qr]
fuente: raw/Practicas/Modelos_Examenes/MNA_Final_Tema_XI.pdf
tipo: final
tema: 11
tiene_resolucion: true
---

# Examen Final de Métodos Numéricos Avanzados — Tema XI (Resolución)

Enunciado base en [[final-tema-11]]. Referencias de método: [[../resueltos/resueltos-diagonalizacion]], [[../resueltos/resueltos-svd]].

## Ejercicio 1

Sea $T : \mathbb{R}^3 \to \mathbb{R}^3$ una transformación lineal tal que

$$M_{EE}(T) = \begin{pmatrix} 4 & -1 & a \\ 0 & -2a + 1 & 0 \\ 0 & 0 & 4a \end{pmatrix}.$$

a) Hallar todos los valores de $a \in \mathbb{R}$ para que $T$ sea sobreyectiva.
b) Para $a = 1$, analizar si $T$ es diagonalizable. En caso de que lo sea, hallar $D$ y $P$.

### Resolución

Llamamos $A = M_{EE}(T)$.

**a) Sobreyectividad.** Como $T : \mathbb{R}^3 \to \mathbb{R}^3$ va de un espacio en otro de **igual dimensión**, $T$ es sobreyectiva $\iff$ $\operatorname{rg}(A) = 3$ $\iff$ $\det A \ne 0$ (es decir, $T$ sobreyectiva $\iff$ $T$ inyectiva $\iff$ $T$ isomorfismo).

La matriz es **triangular superior**, así que su determinante es el producto de la diagonal:

$$\det A = 4\cdot(-2a+1)\cdot 4a = 16a\,(1 - 2a) = -32a^2 + 16a.$$

$$\det A = 0 \iff a = 0 \ \text{ ó } \ 1 - 2a = 0 \iff a = 0 \ \text{ ó } \ a = \tfrac12.$$

Por lo tanto

$$\boxed{T \text{ es sobreyectiva} \iff a \in \mathbb{R} \setminus \left\{0,\ \tfrac12\right\}.}$$

**b) Diagonalización para $a = 1$.** Sustituyendo $a=1$,

$$A = \begin{pmatrix} 4 & -1 & 1 \\ 0 & -1 & 0 \\ 0 & 0 & 4 \end{pmatrix}.$$

Sigue siendo **triangular superior**, así que los autovalores son los elementos de la diagonal. El polinomio característico (convención de la cátedra, $p_A(\lambda) = \det(\lambda I - A)$, coef. líder $+1$) es

$$p_A(\lambda) = (\lambda - 4)(\lambda + 1)(\lambda - 4) = (\lambda - 4)^2(\lambda + 1).$$

Autovalores: $\lambda = 4$ con **multiplicidad algebraica** $m_a(4) = 2$, y $\lambda = -1$ con $m_a(-1) = 1$.

El único candidato a romper la diagonalizabilidad es el autovalor repetido $\lambda = 4$: hay que ver si su **multiplicidad geométrica** $m_g(4) = \dim N(4I - A)$ alcanza el valor $2$.

$$4I - A = \begin{pmatrix} 0 & 1 & -1 \\ 0 & 5 & 0 \\ 0 & 0 & 0 \end{pmatrix}.$$

Resolvemos $(4I - A)X = 0$ con $X = (x,y,z)^T$:

$$\begin{cases} y - z = 0 \\ 5y = 0 \end{cases} \implies y = 0 \implies z = 0,\quad x \text{ libre}.$$

Luego $N(4I - A) = \langle (1,0,0)\rangle$ y

$$m_g(4) = \dim N(4I - A) = 1 < 2 = m_a(4).$$

Como la multiplicidad geométrica es **estrictamente menor** que la algebraica para $\lambda = 4$, no hay suficientes autovectores LI para formar una base de $\mathbb{R}^3$:

$$\boxed{T \text{ NO es diagonalizable (para } a = 1\text{).}}$$

(Solo se obtienen $m_g(4) + m_g(-1) = 1 + 1 = 2 < 3$ autovectores independientes. El autovalor defectuoso es el doble $\lambda = 4$, cuyo bloque $\begin{psmallmatrix}4&-1\\0&4\end{psmallmatrix}$ asociado a las direcciones $x,z$ es un bloque de Jordan no diagonal.)

> Sutileza: aunque $A$ es triangular y se leen los autovalores "de un vistazo", **tener un autovalor repetido no impide ni garantiza** la diagonalización: hay que calcular $m_g$. Aquí falla porque el acoplamiento $a=1$ en la posición $(1,3)$ deja a $\lambda=4$ con un solo autovector. Para referencia, el autovector de $\lambda=-1$ es $(1,5,0)$ (de $5y$ libre y $4x - y + z = -x \Rightarrow$ resolviendo $(-1)I - A$), pero no hace falta para concluir.

**Verificación numérica.** `sympy`: $\det A = -16a(2a-1)$, cuyas raíces son $a\in\{0,\tfrac12\}$ ✓. Para $a=1$, `eigenvals` devuelve $\{4:2,\ -1:1\}$ y $\operatorname{rg}(4I-A)=2$, de donde $m_g(4)=3-2=1$ ✓; el espacio propio de $\lambda=4$ es $\langle(1,0,0)\rangle$ y el de $\lambda=-1$ es $\langle(1,5,0)\rangle$ ✓.

## Ejercicio 2

Sea $T : \mathbb{R}^{n \times n} \to \mathbb{R}^{n \times n} : T(A) = A - A^T$.

a) Hallar $N(T)$ y $R(T)$.
b) Para $A = \begin{pmatrix} 1 & -1 \\ 2 & 0 \end{pmatrix}$, hallar las soluciones del sistema lineal $T(A)\,X = B$ con $B = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$.

### Resolución

**a) Núcleo e imagen.** $T$ es lineal (la transpuesta lo es). 

*Núcleo:* $A \in N(T) \iff T(A) = A - A^T = 0 \iff A = A^T$, es decir, $A$ es **simétrica**:

$$\boxed{N(T) = \{A \in \mathbb{R}^{n\times n} : A = A^T\} = \text{matrices simétricas},\qquad \dim N(T) = \frac{n(n+1)}{2}.}$$

(La dimensión cuenta las entradas de la diagonal y de un triángulo: $n + \binom{n}{2} = \tfrac{n(n+1)}{2}$.)

*Imagen:* para cualquier $A$, la salida $S = T(A) = A - A^T$ cumple $S^T = A^T - A = -S$, así que **toda imagen es antisimétrica**. Recíprocamente, toda matriz antisimétrica $S$ ($S^T=-S$) está en la imagen: tomando $A = \tfrac12 S$,

$$T\!\left(\tfrac12 S\right) = \tfrac12 S - \tfrac12 S^T = \tfrac12 S - \tfrac12(-S) = S.$$

Por lo tanto la imagen es exactamente el subespacio de las matrices antisimétricas:

$$\boxed{R(T) = \{S \in \mathbb{R}^{n\times n} : S^T = -S\} = \text{matrices antisimétricas},\qquad \dim R(T) = \frac{n(n-1)}{2}.}$$

(Consistencia con el teorema de la dimensión: $\dim N(T) + \dim R(T) = \tfrac{n(n+1)}{2} + \tfrac{n(n-1)}{2} = n^2 = \dim \mathbb{R}^{n\times n}$ ✓.)

**b) Sistema $T(A)\,X = B$.** Con la matriz concreta $A = \begin{pmatrix} 1 & -1 \\ 2 & 0 \end{pmatrix}$ (aquí $n=2$),

$$T(A) = A - A^T = \begin{pmatrix} 1 & -1 \\ 2 & 0 \end{pmatrix} - \begin{pmatrix} 1 & 2 \\ -1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & -3 \\ 3 & 0 \end{pmatrix}.$$

(Como debía ser, $T(A)$ es antisimétrica.) Hay que resolver el sistema lineal $T(A)\,X = B$ con $X = (x_1, x_2)^T$:

$$\begin{pmatrix} 0 & -3 \\ 3 & 0 \end{pmatrix}\begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \end{pmatrix} \implies \begin{cases} -3\,x_2 = 1 \\ 3\,x_1 = 1 \end{cases} \implies x_2 = -\tfrac13,\quad x_1 = \tfrac13.$$

El determinante de $T(A)$ es $\det\begin{psmallmatrix}0&-3\\3&0\end{psmallmatrix} = 0\cdot 0 - (-3)(3) = 9 \ne 0$, de modo que la solución es **única**:

$$\boxed{X = \begin{pmatrix} 1/3 \\ -1/3 \end{pmatrix}.}$$

**Verificación numérica.** `sympy`: $T(A) = \begin{psmallmatrix}0&-3\\3&0\end{psmallmatrix}$, y $T(A)\cdot(1/3,\,-1/3)^T = (1,1)^T = B$ ✓.

## Ejercicio 3

Dada la matriz $A = \begin{pmatrix} 1 & 1 \\ 0 & -3 \\ -3 & 5 \end{pmatrix}$ (de tamaño $3\times 2$).

a) Hallar su factorización $SVD$.
b) Hallar su factorización $QR$.

### Resolución

Como $A$ es $3\times 2$ de rango columna completo, $A^TA$ es $2\times2$ y tendrá dos autovalores positivos (dos valores singulares no nulos).

#### a) Descomposición en valores singulares $A = U\Sigma V^T$

**Paso 1 — autovalores de $A^TA$.**

$$A^TA = \begin{pmatrix} 1 & 0 & -3 \\ 1 & -3 & 5 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 0 & -3 \\ -3 & 5 \end{pmatrix} = \begin{pmatrix} 10 & -14 \\ -14 & 35 \end{pmatrix}.$$

Polinomio característico ($\operatorname{tr} = 45$, $\det = 10\cdot 35 - 14^2 = 350 - 196 = 154$):

$$p_{A^TA}(\lambda) = \lambda^2 - 45\lambda + 154 \implies \lambda = \frac{45 \pm \sqrt{45^2 - 4\cdot 154}}{2} = \frac{45 \pm \sqrt{1409}}{2}.$$

Los autovalores no son "lindos" (no salen cuadrados perfectos). Ordenados de mayor a menor:

$$\lambda_1 = \frac{45 + \sqrt{1409}}{2} \approx 41.2683,\qquad \lambda_2 = \frac{45 - \sqrt{1409}}{2} \approx 3.7317.$$

Los **valores singulares** son sus raíces, en orden decreciente:

$$\boxed{\sigma_1 = \sqrt{\lambda_1} \approx 6.4240,\qquad \sigma_2 = \sqrt{\lambda_2} \approx 1.9318.}$$

(Cross-check: $\sigma_1\sigma_2 = \sqrt{\lambda_1\lambda_2} = \sqrt{\det A^TA} = \sqrt{154} \approx 12.41$ ✓.)

**Paso 2 — autovectores de $A^TA$ → columnas de $V$.** Para cada $\lambda_i$ resolvemos $(A^TA - \lambda_i I)v = 0$. La primera fila $(10-\lambda)x - 14y = 0$ da la dirección $(14,\ 10-\lambda)$.

Para $\lambda_1$: $\tilde v_1 = (14,\ 10-\lambda_1) = \big(14,\ -\tfrac{25+\sqrt{1409}}{2}\big)$, que normalizado da

$$v_1 \approx (0.4086,\ -0.9127).$$

Para $\lambda_2$: $\tilde v_2 = (14,\ 10-\lambda_2) = \big(14,\ \tfrac{-25+\sqrt{1409}}{2}\big)$, normalizado

$$v_2 \approx (0.9127,\ 0.4086).$$

(Verificamos $v_1 \perp v_2$, como debe pasar por ser $A^TA$ simétrica.)

$$V = \big(v_1 \mid v_2\big) \approx \begin{pmatrix} 0.4086 & 0.9127 \\ -0.9127 & 0.4086 \end{pmatrix}.$$

**Paso 3 — columnas de $U$** mediante $u_i = \dfrac{A v_i}{\sigma_i}$ (para los $\sigma_i > 0$):

$$u_1 = \frac{A v_1}{\sigma_1} \approx \frac{1}{6.4240}\begin{pmatrix} -0.5040 \\ 2.7381 \\ -5.7898 \end{pmatrix} \approx \begin{pmatrix} -0.0785 \\ 0.4262 \\ -0.9012 \end{pmatrix},$$

$$u_2 = \frac{A v_2}{\sigma_2} \approx \frac{1}{1.9318}\begin{pmatrix} 1.3214 \\ -1.2259 \\ -0.6949 \end{pmatrix} \approx \begin{pmatrix} 0.6840 \\ -0.6346 \\ -0.3597 \end{pmatrix}.$$

**Paso 4 — completar $U$ (SVD completa).** Como $A$ es $3\times 2$, $U$ debe ser $3\times 3$; falta $u_3$, una base ortonormal de $N(A^T)$ (el complemento ortogonal de $\{u_1,u_2\}$ en $\mathbb{R}^3$). Resolviendo $A^T x = 0$:

$$\begin{cases} x_1 - 3x_3 = 0 \\ x_1 - 3x_2 + 5x_3 = 0 \end{cases} \implies x_1 = 3x_3,\ x_2 = \tfrac{8}{3}x_3 \implies \tilde u_3 = (9,\ 8,\ 3),$$

con $\lVert \tilde u_3\rVert = \sqrt{81+64+9} = \sqrt{154} \approx 12.41$, de donde

$$u_3 = \frac{1}{\sqrt{154}}(9,\ 8,\ 3) \approx (0.7252,\ 0.6447,\ 0.2417).$$

Resultado (SVD completa, $U$ es $3\times3$, $\Sigma$ es $3\times2$, $V$ es $2\times2$):

$$\boxed{U \approx \begin{pmatrix} -0.0785 & 0.6840 & 0.7252 \\ 0.4262 & -0.6346 & 0.6447 \\ -0.9012 & -0.3597 & 0.2417 \end{pmatrix},\ \ \Sigma = \begin{pmatrix} 6.4240 & 0 \\ 0 & 1.9318 \\ 0 & 0 \end{pmatrix},\ \ V \approx \begin{pmatrix} 0.4086 & 0.9127 \\ -0.9127 & 0.4086 \end{pmatrix}.}$$

**Verificación.** Columnas de $U$ y $V$ ortonormales ($U^TU = I_3$, $V^TV = I_2$) y

$$U\Sigma V^T \approx \begin{pmatrix} 1 & 1 \\ 0 & -3 \\ -3 & 5 \end{pmatrix} = A. \quad ✓$$

(`numpy`: error máximo $\sim 10^{-6}$ usando los valores redondeados a 4 cifras; exacto al usar los radicales.)

#### b) Factorización QR ($A = QR$ por Gram–Schmidt)

A diferencia de la SVD, aquí los números **sí** salen exactos. Tomamos las columnas $a_1 = (1,\ 0,\ -3)$, $a_2 = (1,\ -3,\ 5)$.

**Columna 1.** $u_1 = a_1$, con

$$r_{11} = \lVert u_1\rVert = \sqrt{1^2 + 0^2 + (-3)^2} = \sqrt{10} \approx 3.1623,$$

$$v_1 = \frac{u_1}{r_{11}} = \frac{1}{\sqrt{10}}(1,\ 0,\ -3) = \left(\tfrac{\sqrt{10}}{10},\ 0,\ -\tfrac{3\sqrt{10}}{10}\right) \approx (0.3162,\ 0,\ -0.9487).$$

**Columna 2.** Coeficiente de proyección:

$$r_{12} = \langle a_2, v_1\rangle = \frac{1\cdot 1 + (-3)\cdot 0 + 5\cdot(-3)}{\sqrt{10}} = \frac{1 - 15}{\sqrt{10}} = -\frac{14}{\sqrt{10}} = -\frac{7\sqrt{10}}{5} \approx -4.4272.$$

$$u_2 = a_2 - r_{12}\,v_1 = (1,-3,5) - \left(-\tfrac{14}{\sqrt{10}}\right)\frac{1}{\sqrt{10}}(1,0,-3) = (1,-3,5) + \tfrac{14}{10}(1,0,-3) = \left(\tfrac{12}{5},\ -3,\ \tfrac45\right).$$

$$r_{22} = \lVert u_2\rVert = \sqrt{\left(\tfrac{12}{5}\right)^2 + 9 + \left(\tfrac45\right)^2} = \sqrt{\tfrac{144 + 225 + 16}{25}} = \sqrt{\tfrac{385}{25}} = \frac{\sqrt{385}}{5} \approx 3.9243,$$

$$v_2 = \frac{u_2}{r_{22}} = \frac{5}{\sqrt{385}}\left(\tfrac{12}{5},\ -3,\ \tfrac45\right) = \frac{1}{\sqrt{385}}(12,\ -15,\ 4) \approx (0.6116,\ -0.7645,\ 0.2039).$$

Resultado ($Q$ es $3\times2$ con columnas ortonormales, $R$ es $2\times2$ triangular superior):

$$\boxed{Q = \big(v_1 \mid v_2\big) \approx \begin{pmatrix} 0.3162 & 0.6116 \\ 0 & -0.7645 \\ -0.9487 & 0.2039 \end{pmatrix},\qquad R = \begin{pmatrix} \sqrt{10} & -\tfrac{7\sqrt{10}}{5} \\[3pt] 0 & \tfrac{\sqrt{385}}{5} \end{pmatrix} \approx \begin{pmatrix} 3.1623 & -4.4272 \\ 0 & 3.9243 \end{pmatrix}.}$$

**Verificación.** $Q^TQ = I_2$ ✓ y

$$QR \approx \begin{pmatrix} 0.3162 & 0.6116 \\ 0 & -0.7645 \\ -0.9487 & 0.2039 \end{pmatrix}\begin{pmatrix} 3.1623 & -4.4272 \\ 0 & 3.9243 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 0 & -3 \\ -3 & 5 \end{pmatrix} = A. \quad ✓$$

---

## Resumen de resultados

| Ej. | Resultado |
|---|---|
| 1a | $T$ sobreyectiva $\iff \det A = 16a(1-2a)\ne 0 \iff a \notin\{0,\ \tfrac12\}$ |
| 1b | $a=1$: autovalores $4$ (doble), $-1$; $m_g(4)=1<2 \Rightarrow$ **no** diagonalizable |
| 2a | $N(T)=$ simétricas ($\dim\tfrac{n(n+1)}2$); $R(T)=$ antisimétricas ($\dim\tfrac{n(n-1)}2$) |
| 2b | $T(A)=\begin{psmallmatrix}0&-3\\3&0\end{psmallmatrix}$, solución única $X=(\tfrac13,\ -\tfrac13)^T$ |
| 3a | $\sigma_{1,2}=\sqrt{\tfrac{45\pm\sqrt{1409}}{2}}\approx 6.4240,\ 1.9318$; $u_3=\tfrac{1}{\sqrt{154}}(9,8,3)$; $U\Sigma V^T=A$ ✓ |
| 3b | $R=\begin{psmallmatrix}\sqrt{10}&-7\sqrt{10}/5\\0&\sqrt{385}/5\end{psmallmatrix}$, $Q^TQ=I$, $QR=A$ ✓ |
