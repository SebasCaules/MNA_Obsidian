---
tags: [parcial, ip, resolucion, transformaciones-lineales, nucleo-imagen, antiimagen, diagonalizacion, autovalores, plu, qr]
fuente: raw/Practicas/Modelos_Examenes/MNA_IP_Tema_IV.pdf
tipo: ip
tema: 4
tiene_resolucion: true
---

# Primer Parcial de Métodos Numéricos Avanzados — Tema IV (Resolución)

> Recetas relacionadas: [[ip-tema-01-resolucion]], [[ip-tema-05-resolucion]]. Convenciones: $p_A(\lambda)=\det(\lambda I-A)$, $S_\lambda=N(\lambda I-A)$, diagonalizable $\iff m_g=m_a$ para todo autovalor.

## Ejercicio 1

Sea $T:\mathbb{R}^3\to\mathbb{R}^3$ tal que

$$M_{EB}(T)=\begin{pmatrix}2&0&2\\0&3&3\\1&-1&0\end{pmatrix},\qquad B=\{(0,1,-1),\,(0,0,1),\,(1,1,0)\}.$$

Aquí $B$ es base del **dominio** y el **codominio** está en la base canónica $E$. Es decir, $M_{EB}(T)$ recibe las coordenadas de un vector en la base $B$ y devuelve el resultado en coordenadas canónicas.

a) Hallar $v\in\mathbb{R}^3$, si existe, tal que $T(v)=(0,2,1)$.

b) Hallar $\dim N(T)$.

### Resolución

**Punto de partida — la convención de la matriz.** Como $M_{EB}(T)$ actúa sobre coordenadas en $B$, para un vector $v$ con coordenadas $[v]_B=(x_1,x_2,x_3)$ se tiene

$$T(v)=M_{EB}(T)\,[v]_B\quad(\text{resultado en canónica}).$$

Por lo tanto, en **a)** hay que resolver $M_{EB}(T)\,[v]_B=(0,2,1)$ para obtener $[v]_B$, y luego reconstruir $v=\sum_j [v]_{B,j}\,b_j$ en canónica. En **b)**, el núcleo se obtiene de $M_{EB}(T)\,[v]_B=0$ y $\dim N(T)=\dim$ del núcleo de la matriz (ambas bases son isomorfismos, así que la dimensión no cambia).

**a) Antiimagen de $(0,2,1)$.** Planteamos el sistema $M_{EB}(T)\,[v]_B=(0,2,1)$:

$$\left(\begin{array}{ccc|c}2&0&2&0\\0&3&3&2\\1&-1&0&1\end{array}\right).$$

Notar de entrada que la matriz es **singular**: desarrollando por la primera columna,

$$\det M_{EB}(T)=2\,(3\cdot 0-3\cdot(-1))-0+1\,(0\cdot 3-2\cdot 3)=2\cdot 3+(-6)=0.$$

Como $\det=0$, el sistema puede no tener solución. Triangulamos. Intercambiamos para tener pivote cómodo y reducimos; la forma escalonada reducida de la matriz **ampliada** resulta

$$\left(\begin{array}{ccc|c}1&0&1&0\\0&1&1&0\\0&0&0&1\end{array}\right).$$

La última fila dice $0=1$, **absurdo**. Entonces

$$\operatorname{rg}\big(M_{EB}(T)\big)=2\quad\text{pero}\quad \operatorname{rg}\big(M_{EB}(T)\mid (0,2,1)\big)=3.$$

Por el teorema de Rouché–Frobenius el sistema es **incompatible**: **no existe** $v\in\mathbb{R}^3$ tal que $T(v)=(0,2,1)$.

> **Lectura geométrica (por qué falla).** La imagen de $T$ es el espacio columna de $M_{EB}(T)$, generado por $c_1=(2,0,1)$ y $c_2=(0,3,-1)$ (la tercera columna $(2,3,0)=c_1+c_2$ es combinación de las otras dos). Es el plano de $\mathbb{R}^3$ con vector normal
> $$n=c_1\times c_2=(2,0,1)\times(0,3,-1)=(-3,\,2,\,6).$$
> Como $n\cdot(0,2,1)=0\cdot(-3)+2\cdot 2+1\cdot 6=10\neq 0$, el vector $(0,2,1)$ **no pertenece al plano imagen**. De ahí la incompatibilidad.

$$\boxed{\text{No existe } v\in\mathbb{R}^3 \text{ con } T(v)=(0,2,1):\ (0,2,1)\notin \operatorname{Im}(T).}$$

**b) $\dim N(T)$.** El núcleo está formado por los $[v]_B$ con $M_{EB}(T)\,[v]_B=0$. Como $\operatorname{rg}\big(M_{EB}(T)\big)=2$, por el teorema de la dimensión aplicado a la matriz ($3\times 3$):

$$\dim N(T)=3-\operatorname{rg}\big(M_{EB}(T)\big)=3-2=1.$$

Resolviendo $M_{EB}(T)\,[v]_B=0$ con la forma escalonada $\begin{psmallmatrix}1&0&1\\0&1&1\\0&0&0\end{psmallmatrix}$ se obtiene $x_1=-x_3,\ x_2=-x_3$, de donde una base del núcleo en coordenadas $B$ es

$$[v]_B=(-1,-1,1).$$

Reconstruyendo en canónica, $v=-1\cdot(0,1,-1)-1\cdot(0,0,1)+1\cdot(1,1,0)=(1,0,0)$. Es decir,

$$\boxed{\dim N(T)=1,\qquad N(T)=\langle (1,0,0)\rangle.}$$

> **Verificación numérica.** $\det M_{EB}=0$, $\operatorname{rg}(M_{EB})=2$ y $\operatorname{rg}(\text{ampliada})=3$ (sistema incompatible, confirma a). El núcleo de $M_{EB}$ tiene dimensión $1$ generado por $(-1,-1,1)$, y $M_{EB}\,(-1,-1,1)^T=(0,0,0)$; reconstruido en canónica da $v_{\ker}=(1,0,0)$. Construyendo $M_{EE}=M_{EB}\,B^{-1}=\begin{psmallmatrix}0&2&0\\0&3&3\\0&0&-1\end{psmallmatrix}$ (con $B$ la matriz cuyas columnas son los vectores de la base), se comprueba $M_{EE}\,(1,0,0)^T=0$ y que $(0,2,1)\notin$ espacio columna de $M_{EE}$.

## Ejercicio 2

Sea

$$A=\begin{pmatrix}2&-2&0\\0&2&k\\0&0&3\end{pmatrix}.$$

a) Hallar $k\in\mathbb{R}$ para que $A$ sea diagonalizable en $\mathbb{R}$.

b) Para $k=0$, hallar, si existe, una base de autovectores de $\mathbb{R}^3$.

### Resolución

**Polinomio característico.** $A$ es triangular superior, así que sus autovalores están en la diagonal: $2$ (doble) y $3$ (simple). En efecto,

$$p_A(\lambda)=\det(\lambda I-A)=\begin{vmatrix}\lambda-2&2&0\\0&\lambda-2&-k\\0&0&\lambda-3\end{vmatrix}=(\lambda-2)^2(\lambda-3).$$

Multiplicidades algebraicas: $m_a(2)=2$, $m_a(3)=1$. El autovalor $\lambda=3$ es simple, así que siempre $m_g(3)=m_a(3)=1$ (no da problemas). Todo depende del autovalor doble $\lambda=2$.

**a) Análisis de $m_g(2)$ según $k$.** Calculamos $S_2=N(A-2I)$:

$$A-2I=\begin{pmatrix}0&-2&0\\0&0&k\\0&0&1\end{pmatrix}.$$

La clave está acá: **independientemente del valor de $k$**, esta matriz contiene siempre las dos filas $(0,-2,0)$ y $(0,0,1)$, que son linealmente independientes. Por lo tanto

$$\operatorname{rg}(A-2I)=2\quad\text{para todo }k\in\mathbb{R}\ \Longrightarrow\ m_g(2)=\dim S_2=3-2=1.$$

(La fila $(0,0,k)$ es, para cualquier $k$, múltiplo de $(0,0,1)$, por lo que nunca aporta rango; el rango queda fijo en $2$.)

Como $m_g(2)=1<2=m_a(2)$ **para todo $k$**, falla siempre la condición de diagonalización. Conclusión:

$$\boxed{\text{No existe }k\in\mathbb{R}\text{ que haga a }A\text{ diagonalizable: }A\text{ nunca es diagonalizable en }\mathbb{R}.}$$

> **Trampa del enunciado.** Es tentador pensar que con algún $k$ "especial" (por ejemplo $k=0$) el bloque se rompe y aparece un segundo autovector para $\lambda=2$. Pero el responsable de bloquear $m_g(2)$ no es la entrada $k$, sino la entrada $-2$ en la posición $(1,2)$, que es constante. Aun con $k=0$ el rango de $A-2I$ sigue siendo $2$.

**b) Base de autovectores para $k=0$.** Con $k=0$,

$$A=\begin{pmatrix}2&-2&0\\0&2&0\\0&0&3\end{pmatrix}.$$

Autovalores: $2$ (doble), $3$ (simple). Buscamos autovectores.

*Para $\lambda=2$:* $\,(A-2I)v=0$ con $A-2I=\begin{psmallmatrix}0&-2&0\\0&0&0\\0&0&1\end{psmallmatrix}$. Las ecuaciones son $-2y=0$ y $z=0$, o sea $y=0,\ z=0$, $x$ libre:

$$S_2=\langle (1,0,0)\rangle,\qquad m_g(2)=1.$$

*Para $\lambda=3$:* $\,(A-3I)v=0$ con $A-3I=\begin{psmallmatrix}-1&-2&0\\0&-1&0\\0&0&0\end{psmallmatrix}$. De $-y=0$ y $-x-2y=0$ sale $x=0,\ y=0$, $z$ libre:

$$S_3=\langle (0,0,1)\rangle,\qquad m_g(3)=1.$$

En total disponemos de **solo 2 autovectores linealmente independientes** ($1+1=2<3$), por lo que **no se puede formar una base de autovectores de $\mathbb{R}^3$**:

$$\boxed{\text{Para }k=0\text{ no existe base de autovectores de }\mathbb{R}^3\ (A\text{ no es diagonalizable}).}$$

> **Verificación numérica.** $p_A(\lambda)=(\lambda-2)^2(\lambda-3)$ confirmado simbólicamente. Para todo $k$ probado ($k=-2,-1,0,1,2,5$) se obtuvo $\operatorname{rg}(A-2I)=2$, luego $m_g(2)=1$. Para $k=0$ los autoespacios son $S_2=\langle(1,0,0)\rangle$ y $S_3=\langle(0,0,1)\rangle$; la suma de multiplicidades geométricas es $2<3$, y el algoritmo de diagonalización falla con error "Matrix is not diagonalizable", consistente con la cuenta a mano.

## Ejercicio 3

Sea

$$A=\begin{pmatrix}3&1\\2&6\\7&-3\end{pmatrix}\quad(3\times 2).$$

a) Hallar la factorización $PLU$.

b) Hallar la factorización $QR$.

### Resolución

**a) Factorización $PLU$.** Aplicamos eliminación de Doolittle. El pivote $a_{11}=3\neq 0$, así que **no hace falta permutar**: tendremos $P=I$ y $A=LU$ directamente. Para una matriz $3\times 2$, $U$ resulta $3\times 2$ triangular superior y $L$ es $3\times 3$ con unos en la diagonal.

*Columna 1 — anular debajo del $3$.* Multiplicadores
$$m_{21}=\frac{2}{3},\qquad m_{31}=\frac{7}{3}.$$
$$F_2\leftarrow F_2-\tfrac23 F_1:\ (2,6)-\tfrac23(3,1)=\Big(0,\ 6-\tfrac23\Big)=\Big(0,\ \tfrac{16}{3}\Big),$$
$$F_3\leftarrow F_3-\tfrac73 F_1:\ (7,-3)-\tfrac73(3,1)=\Big(0,\ -3-\tfrac73\Big)=\Big(0,\ -\tfrac{16}{3}\Big).$$

Estado intermedio: $\begin{psmallmatrix}3&1\\[2pt]0&\tfrac{16}{3}\\[2pt]0&-\tfrac{16}{3}\end{psmallmatrix}$.

*Columna 2 — anular el $-\tfrac{16}{3}$ de la fila 3.* Pivote $a_{22}=\tfrac{16}{3}$, multiplicador
$$m_{32}=\frac{-16/3}{16/3}=-1.$$
$$F_3\leftarrow F_3-(-1)F_2=F_3+F_2:\ \Big(0,-\tfrac{16}{3}\Big)+\Big(0,\tfrac{16}{3}\Big)=(0,0).$$

Obtenemos así

$$U=\begin{pmatrix}3&1\\[2pt]0&\tfrac{16}{3}\\[2pt]0&0\end{pmatrix},\qquad
L=\begin{pmatrix}1&0&0\\[2pt]\tfrac23&1&0\\[2pt]\tfrac73&-1&1\end{pmatrix},\qquad
P=I_3.$$

(El signo de cada entrada de $L$ es el **opuesto** al del coeficiente usado en $F_i\leftarrow F_i - m_{ij}F_j$; como hicimos resta, $L_{ij}=+m_{ij}$. En particular $L_{32}=m_{32}=-1$.)

*Verificación $PA=LU$ (aquí $P=I$, o sea $A=LU$):*
$$LU=\begin{pmatrix}1&0&0\\ \tfrac23&1&0\\ \tfrac73&-1&1\end{pmatrix}\begin{pmatrix}3&1\\0&\tfrac{16}{3}\\0&0\end{pmatrix}=\begin{pmatrix}3&1\\ 2&\tfrac23+\tfrac{16}{3}\\ 7&\tfrac73-\tfrac{16}{3}\end{pmatrix}=\begin{pmatrix}3&1\\2&6\\7&-3\end{pmatrix}=A.\ \checkmark$$

$$\boxed{P=I_3,\quad L=\begin{pmatrix}1&0&0\\ \tfrac23&1&0\\ \tfrac73&-1&1\end{pmatrix},\quad U=\begin{pmatrix}3&1\\0&\tfrac{16}{3}\\0&0\end{pmatrix}.}$$

**b) Factorización $QR$ (Gram–Schmidt).** Columnas de $A$: $a_1=(3,2,7)$, $a_2=(1,6,-3)$. $Q$ será $3\times 2$ y $R$ será $2\times 2$ triangular superior.

*Columna 1.* $u_1=a_1=(3,2,7)$,
$$\lVert u_1\rVert=\sqrt{3^2+2^2+7^2}=\sqrt{9+4+49}=\sqrt{62},\qquad v_1=\frac{1}{\sqrt{62}}(3,2,7).$$

*Columna 2 — proyección sobre $v_1$.*
$$\langle a_2,v_1\rangle=\frac{1}{\sqrt{62}}\big(3\cdot 1+2\cdot 6+7\cdot(-3)\big)=\frac{3+12-21}{\sqrt{62}}=\frac{-6}{\sqrt{62}}=-\frac{3\sqrt{62}}{31}.$$

*Restar la proyección.*
$$u_2=a_2-\langle a_2,v_1\rangle v_1=(1,6,-3)-\frac{-6}{\sqrt{62}}\cdot\frac{1}{\sqrt{62}}(3,2,7)=(1,6,-3)+\frac{6}{62}(3,2,7).$$
$$u_2=(1,6,-3)+\frac{3}{31}(3,2,7)=\Big(1+\tfrac{9}{31},\ 6+\tfrac{6}{31},\ -3+\tfrac{21}{31}\Big)=\Big(\tfrac{40}{31},\ \tfrac{192}{31},\ -\tfrac{72}{31}\Big)=\frac{8}{31}(5,24,-9).$$

*Normalizar $u_2$.* Conviene usar el vector "limpio" $(5,24,-9)$ (proporcional a $u_2$):
$$\lVert (5,24,-9)\rVert=\sqrt{25+576+81}=\sqrt{682}\ \Longrightarrow\ v_2=\frac{1}{\sqrt{682}}(5,24,-9).$$
La norma de $u_2$ (que va en $R_{22}$) es
$$\lVert u_2\rVert=\frac{8}{31}\sqrt{682}=\frac{8\sqrt{682}}{31}\quad\Big(\lVert u_2\rVert^2=\tfrac{1408}{31}\approx 45.42,\ \lVert u_2\rVert\approx 6.7394\Big).$$

*Armar $Q$ y $R$.*
$$Q=(v_1\mid v_2)=\begin{pmatrix}\tfrac{3}{\sqrt{62}}&\tfrac{5}{\sqrt{682}}\\[4pt]\tfrac{2}{\sqrt{62}}&\tfrac{24}{\sqrt{682}}\\[4pt]\tfrac{7}{\sqrt{62}}&-\tfrac{9}{\sqrt{682}}\end{pmatrix},
\qquad
R=\begin{pmatrix}\lVert u_1\rVert&\langle a_2,v_1\rangle\\[2pt]0&\lVert u_2\rVert\end{pmatrix}=\begin{pmatrix}\sqrt{62}&-\tfrac{3\sqrt{62}}{31}\\[4pt]0&\tfrac{8\sqrt{682}}{31}\end{pmatrix}.$$

Numéricamente $\sqrt{62}\approx 7.8740$, $R_{12}\approx -0.7620$, $R_{22}\approx 6.7394$.

*Verificación $QR=A$ y $Q^TQ=I$:* entrada $(1,1)$ de $QR$:
$$\frac{3}{\sqrt{62}}\cdot\sqrt{62}+\frac{5}{\sqrt{682}}\cdot 0=3\ \checkmark.$$
Entrada $(2,2)$:
$$\frac{2}{\sqrt{62}}\Big(-\tfrac{3\sqrt{62}}{31}\Big)+\frac{24}{\sqrt{682}}\cdot\frac{8\sqrt{682}}{31}=-\frac{6}{31}+\frac{192}{31}=\frac{186}{31}=6\ \checkmark.$$
Las demás entradas se comprueban igual; además $\langle v_1,v_1\rangle=\langle v_2,v_2\rangle=1$ y $\langle v_1,v_2\rangle=0$, de modo que $Q^TQ=I_2$.

$$\boxed{Q=\begin{pmatrix}\tfrac{3}{\sqrt{62}}&\tfrac{5}{\sqrt{682}}\\[4pt]\tfrac{2}{\sqrt{62}}&\tfrac{24}{\sqrt{682}}\\[4pt]\tfrac{7}{\sqrt{62}}&-\tfrac{9}{\sqrt{682}}\end{pmatrix},\qquad R=\begin{pmatrix}\sqrt{62}&-\tfrac{3\sqrt{62}}{31}\\[4pt]0&\tfrac{8\sqrt{682}}{31}\end{pmatrix}.}$$

> **Verificación numérica.** $LU=A$ exacto (sin permutaciones, $P=I$). Para QR: $QR=A$ y $Q^TQ=I_2$ exactos en aritmética simbólica; $\lVert u_1\rVert=\sqrt{62}$, $\lVert u_2\rVert=\tfrac{8\sqrt{682}}{31}$ ($\lVert u_2\rVert^2=\tfrac{1408}{31}$) y $\langle a_2,v_1\rangle=-\tfrac{6}{\sqrt{62}}=-\tfrac{3\sqrt{62}}{31}$ confirmados.
