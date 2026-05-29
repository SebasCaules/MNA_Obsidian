---
tags: [parcial, recuperatorio, resolucion, transformaciones-lineales, diagonalizacion, fourier, plu, qr]
fuente: raw/Practicas/Modelos_Examenes/MNA_Parcial_Tema_XIII.pdf
tipo: parcial
tema: 13
tiene_resolucion: true
---

# Recuperatorio de Métodos Numéricos Avanzados — Tema XIII (Resolución)

Enunciado sin resolver en [[parcial-tema-13]].

## Ejercicio 1

Sea $T : \mathbb{R}^3 \to \mathbb{R}^3$ una transformación lineal tal que

$$M_{EE}(T) = \begin{pmatrix} 2 & 0 & 0 \\ 0 & h & 0 \\ -1 & 1 & 1 \end{pmatrix}$$

a) Hallar todos los valores del parámetro tal que $\dim(R(T)) < 3$.

*(Nota: el enunciado original menciona variables $a, b$, pero la matriz contiene un único parámetro $h$. Lo interpretamos como hallar los $h$ que reducen el rango.)*

b) Hallar $h \in \mathbb{R}$, si existe, para que $T$ no sea diagonalizable.

### Resolución

Rebautizamos $A = M_{EE}(T)$.

**a)** Como $T : \mathbb{R}^3 \to \mathbb{R}^3$, se tiene $\dim R(T) = \operatorname{rg}(A) < 3 \iff A$ no es inversible $\iff \det A = 0$. Calculamos el determinante desarrollando por la **primera columna** (que sólo tiene dos entradas no nulas), o más cómodo aún por la **primera fila**:

$$\det A = \begin{vmatrix} 2 & 0 & 0 \\ 0 & h & 0 \\ -1 & 1 & 1 \end{vmatrix} = 2\cdot\begin{vmatrix} h & 0 \\ 1 & 1 \end{vmatrix} = 2\,(h\cdot 1 - 0\cdot 1) = 2h.$$

Entonces

$$\det A = 0 \iff 2h = 0 \iff \boxed{h = 0.}$$

Para $h = 0$ es $\dim R(T) = \operatorname{rg}(A) = 2 < 3$ (y $\dim N(T) = 1$ por el teorema de la dimensión). Para todo $h \ne 0$, $A$ es inversible y $\dim R(T) = 3$.

**b)** Buscamos los autovalores mediante el polinomio característico $p_A(\lambda) = \det(\lambda I - A)$. La matriz $\lambda I - A$ es

$$\lambda I - A = \begin{pmatrix} \lambda - 2 & 0 & 0 \\ 0 & \lambda - h & 0 \\ 1 & -1 & \lambda - 1 \end{pmatrix}.$$

Desarrollando por la primera fila (sólo sobrevive el primer término):

$$p_A(\lambda) = (\lambda - 2)\begin{vmatrix} \lambda - h & 0 \\ -1 & \lambda - 1 \end{vmatrix} = (\lambda - 2)(\lambda - h)(\lambda - 1).$$

Los autovalores son entonces $\lambda = 2$, $\lambda = h$ y $\lambda = 1$.

Si $h \notin \{1, 2\}$, los tres autovalores son **distintos** $\Rightarrow$ $T$ es diagonalizable (tres autovalores simples siempre lo son). Quedan dos candidatos a no diagonalizable, donde un autovalor se repite: $h = 2$ y $h = 1$. En cada uno hay que comparar $m_a$ (multiplicidad algebraica) con $m_g = \dim S_\lambda = \dim N(\lambda I - A)$.

**Caso $h = 2$:** $\;p_A(\lambda) = (\lambda - 2)^2(\lambda - 1)$, de modo que $\lambda = 2$ tiene $m_a = 2$. Estudiamos $S_2 = N(2I - A)$:

$$2I - A = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 1 & -1 & 1 \end{pmatrix} \xrightarrow{\text{Gauss}} \begin{pmatrix} 1 & -1 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}.$$

La matriz tiene **rango 1**, así que $\dim S_2 = 3 - 1 = 2 = m_a$. El otro autovalor $\lambda = 1$ es simple ($m_g = m_a = 1$). Como todos los autovalores cumplen $m_g = m_a$, para $h = 2$ **$T$ SÍ es diagonalizable**.

(Una base de autovectores de $S_2$: de $x - y + z = 0$ salen $v = (1,1,0)$ y $v = (-1,0,1)$.)

**Caso $h = 1$:** $\;p_A(\lambda) = (\lambda - 2)(\lambda - 1)^2$, de modo que ahora $\lambda = 1$ tiene $m_a = 2$. Estudiamos $S_1 = N(1\cdot I - A)$:

$$I - A = \begin{pmatrix} -1 & 0 & 0 \\ 0 & 0 & 0 \\ 1 & -1 & 0 \end{pmatrix} \xrightarrow{\text{Gauss}} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix}.$$

Aquí $-x = 0$ y $x - y = 0$ obligan $x = y = 0$, con $z$ libre: la matriz tiene **rango 2**, así que $\dim S_1 = 3 - 2 = 1 < 2 = m_a$. El autovalor $\lambda = 1$ es **defectivo** $\Rightarrow$ para $h = 1$ **$T$ NO es diagonalizable**.

(El único autovector de $\lambda=1$ es $v = (0,0,1)$.)

$$\boxed{T \text{ no es diagonalizable únicamente para } h = 1.}$$

> **Punto sutil.** Aunque $h = 2$ y $h = 1$ son los dos casos con autovalor repetido, **sólo $h = 1$ falla**. La diferencia está en qué columna engendra la fila de eliminación $(-1, 1, \cdot)$: para $\lambda = 2$ esa fila colapsa con la diagonal nula (rango 1, $m_g = 2$), mientras que para $\lambda = 1$ aparecen dos pivotes (rango 2, $m_g = 1$). Conviene **siempre** reducir $\lambda I - A$ y contar pivotes, no asumir que todo autovalor repetido rompe la diagonalizabilidad.

*Verificación numérica (sympy).* Para $h = 2$: $\lambda = 2$ tiene $m_a = 2$, $m_g = 2$ y $\lambda = 1$ con $m_g = 1$ (diagonalizable). Para $h = 1$: $\lambda = 1$ tiene $m_a = 2$ pero $m_g = 1$ (no diagonalizable). Confirmado.

## Ejercicio 2

Dada la función $f : [0, 1] \to \mathbb{R} : f(t) = t$, extendida periódicamente con período $1$ ($f(t) = f(t + 1)$).

a) Hallar el desarrollo en serie trigonométrica de Fourier.
b) Indicar a qué converge la serie en $t = 1$ y en $t = \dfrac{1}{4}$.

### Resolución

Es la **onda diente de sierra**: en cada intervalo $[k, k+1)$ la función crece linealmente de $0$ a $1$ y vuelve a saltar a $0$. El período es $T = 1$, por lo que la frecuencia angular fundamental es $\tfrac{2\pi}{T} = 2\pi$. Usamos la convención de la cátedra (ver [[../guias/guia-08-fourier-series]]):

$$f(t) = a_0 + \sum_{n=1}^{\infty} a_n\cos(2\pi n\,t) + \sum_{n=1}^{\infty} b_n\sin(2\pi n\,t),$$

con $a_0 = \dfrac1T\displaystyle\int_0^1 f$ (valor medio), $a_n = \dfrac2T\displaystyle\int_0^1 f\cos(2\pi n t)\,dt$ y $b_n = \dfrac2T\displaystyle\int_0^1 f\sin(2\pi n t)\,dt$.

**a) Coeficientes.**

**Término constante** (valor medio):

$$a_0 = \int_0^1 t\,dt = \left.\frac{t^2}{2}\right|_0^1 = \frac12.$$

**Cosenos.** Por partes con $u = t$, $dv = \cos(2\pi n t)\,dt$:

$$a_n = 2\int_0^1 t\cos(2\pi n t)\,dt = 2\left[\frac{t\sin(2\pi n t)}{2\pi n} + \frac{\cos(2\pi n t)}{(2\pi n)^2}\right]_0^1.$$

Como $n$ es entero, $\sin(2\pi n) = 0$ y $\cos(2\pi n) = 1 = \cos 0$, los dos corchetes se cancelan:

$$a_n = 2\left[\frac{1\cdot 0}{2\pi n} + \frac{1 - 1}{(2\pi n)^2}\right] = 0.$$

(Es coherente: $f$ no es par, así que no hay razón de simetría para que se anulen, pero la integral da $0$ término a término.)

**Senos.** Por partes con $u = t$, $dv = \sin(2\pi n t)\,dt$:

$$b_n = 2\int_0^1 t\sin(2\pi n t)\,dt = 2\left[-\frac{t\cos(2\pi n t)}{2\pi n} + \frac{\sin(2\pi n t)}{(2\pi n)^2}\right]_0^1.$$

Evaluando ($\cos(2\pi n) = 1$, $\sin(2\pi n) = 0$):

$$b_n = 2\left[-\frac{1\cdot 1}{2\pi n} + 0 - (0 - 0)\right] = -\frac{2}{2\pi n} = -\frac{1}{\pi n}.$$

Resultado:

$$\boxed{a_0 = \frac12,\qquad a_n = 0,\qquad b_n = -\frac{1}{\pi n}\quad(n \ge 1),}$$

$$\boxed{f(t) = \frac12 - \frac{1}{\pi}\sum_{n=1}^{\infty}\frac{\sin(2\pi n\,t)}{n}.}$$

*Verificación numérica.* Integrando con `scipy.quad`: $a_0 = 0.5$; $a_n \approx 0$ para $n = 1,\dots,4$; $b_1 = -0.31831$, $b_2 = -0.15915$, $b_3 = -0.10610$, $b_4 = -0.07958$, que coinciden con $-\tfrac{1}{\pi n}$ ($-\tfrac1\pi = -0.31831$, etc.). ✓

**b) Convergencia (teorema de Dirichlet).**

- **En $t = 1$** (un punto entero, donde está el salto). Por izquierda $f(1^-) = 1$; por derecha, usando la periodicidad, $f(1^+) = f(0^+) = 0$. Hay una **discontinuidad de salto**, por lo que la serie converge al **promedio** de los límites laterales:

$$S(1) = \frac{f(1^-) + f(1^+)}{2} = \frac{1 + 0}{2} = \frac12.$$

(Se puede leer también directo de la fórmula: todos los $\sin(2\pi n\cdot 1) = 0$, así que la serie en $t = 1$ vale exactamente el término constante $a_0 = \tfrac12$.)

- **En $t = \tfrac14$** (punto **interior** de continuidad). Ahí la serie converge al valor de la función:

$$S\!\left(\tfrac14\right) = f\!\left(\tfrac14\right) = \frac14.$$

$$\boxed{S(1) = \frac12,\qquad S\!\left(\tfrac14\right) = \frac14.}$$

*Verificación numérica.* Sumas parciales $S_N(t) = \tfrac12 - \tfrac1\pi\sum_{n=1}^{N}\tfrac{\sin(2\pi n t)}{n}$: en $t = 1$ da exactamente $0.5$ para todo $N$; en $t = 1/4$ tiende a $0.25$ ($S_{50} = 0.2468$, $S_{500} = 0.25032$, $S_{5000} = 0.25003$). ✓

## Ejercicio 3

Dada la matriz $A = \begin{pmatrix} 0 & -1 \\ 1 & -1 \\ -1 & 0 \end{pmatrix}$ ($3\times 2$).

a) Hallar su factorización $PLU$.
b) Hallar su factorización $QR$.

### Resolución

#### a) Factorización $PLU$ ($PA = LU$, Doolittle)

El primer pivote candidato es $a_{11} = 0$. **No se puede usar como pivote**: hay que **permutar filas**. Intercambiamos la fila 1 con la fila 2 (que tiene $1$ en la columna 1). La matriz de permutación es

$$P = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix},\qquad PA = \begin{pmatrix} 1 & -1 \\ 0 & -1 \\ -1 & 0 \end{pmatrix}.$$

Ahora hacemos eliminación gaussiana sobre $PA$, registrando los multiplicadores en $L$ (con unos en la diagonal).

**Columna 1** (pivote $= 1$ en la fila 1):
- Fila 2: $a_{21} = 0 \Rightarrow m_{21} = 0$ (nada que hacer).
- Fila 3: $a_{31} = -1 \Rightarrow m_{31} = \dfrac{-1}{1} = -1$. Operación $F_3 \leftarrow F_3 - (-1)F_1 = F_3 + F_1$:

$$\begin{pmatrix} 1 & -1 \\ 0 & -1 \\ -1 & 0 \end{pmatrix} \to \begin{pmatrix} 1 & -1 \\ 0 & -1 \\ 0 & -1 \end{pmatrix}.$$

**Columna 2** (pivote $= -1$ en la fila 2):
- Fila 3: $a_{32} = -1 \Rightarrow m_{32} = \dfrac{-1}{-1} = 1$. Operación $F_3 \leftarrow F_3 - 1\cdot F_2$:

$$\begin{pmatrix} 1 & -1 \\ 0 & -1 \\ 0 & -1 \end{pmatrix} \to \begin{pmatrix} 1 & -1 \\ 0 & -1 \\ 0 & 0 \end{pmatrix} = U.$$

Los multiplicadores quedan en $L$ ($L_{ij} = m_{ij}$):

$$\boxed{P = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix},\quad L = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ -1 & 1 & 1 \end{pmatrix},\quad U = \begin{pmatrix} 1 & -1 \\ 0 & -1 \\ 0 & 0 \end{pmatrix}.}$$

($L$ es $3\times 3$ y $U$ es $3\times 2$, igual que $A$.)

**Verificación.**

$$LU = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ -1 & 1 & 1 \end{pmatrix}\begin{pmatrix} 1 & -1 \\ 0 & -1 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ 0 & -1 \\ -1 & 0 \end{pmatrix} = PA. \quad ✓$$

> **Punto sutil.** Por tener pivote inicial nulo, esta factorización **exige** la permutación: no existe $A = LU$ sin reordenar filas. La forma correcta de enunciar el resultado es $PA = LU$ (equivalentemente $A = P^{-1}LU = P^TLU$, ya que $P$ es ortogonal). También sería válido permutar la fila 1 con la fila 3; el $P$, $L$ resultantes serían distintos pero igualmente correctos.

#### b) Factorización $QR$ ($A = QR$ por Gram–Schmidt)

Tomamos las columnas $a_1 = (0, 1, -1)$ y $a_2 = (-1, -1, 0)$. Como $A$ es $3\times 2$ de rango columna completo, $Q$ será $3\times 2$ y $R$ será $2\times 2$ (QR reducida).

**Columna 1.** $u_1 = a_1$, con

$$r_{11} = \lVert u_1\rVert = \sqrt{0^2 + 1^2 + (-1)^2} = \sqrt{2},\qquad v_1 = \frac{u_1}{r_{11}} = \frac{1}{\sqrt2}(0, 1, -1) = \left(0,\ \tfrac{\sqrt2}{2},\ -\tfrac{\sqrt2}{2}\right).$$

**Columna 2.** Coeficiente de proyección sobre $v_1$:

$$r_{12} = \langle a_2, v_1\rangle = (-1)\cdot 0 + (-1)\cdot\tfrac{\sqrt2}{2} + 0\cdot\left(-\tfrac{\sqrt2}{2}\right) = -\frac{\sqrt2}{2}.$$

Restamos la proyección:

$$u_2 = a_2 - r_{12}\,v_1 = (-1, -1, 0) - \left(-\tfrac{\sqrt2}{2}\right)\left(0, \tfrac{\sqrt2}{2}, -\tfrac{\sqrt2}{2}\right) = (-1, -1, 0) + \left(0, \tfrac12, -\tfrac12\right) = \left(-1,\ -\tfrac12,\ -\tfrac12\right).$$

Su norma:

$$r_{22} = \lVert u_2\rVert = \sqrt{1 + \tfrac14 + \tfrac14} = \sqrt{\tfrac32} = \frac{\sqrt6}{2},\qquad v_2 = \frac{u_2}{r_{22}} = \frac{2}{\sqrt6}\left(-1, -\tfrac12, -\tfrac12\right) = \left(-\tfrac{\sqrt6}{3},\ -\tfrac{\sqrt6}{6},\ -\tfrac{\sqrt6}{6}\right).$$

Resultado:

$$\boxed{Q = \begin{pmatrix} 0 & -\tfrac{\sqrt6}{3} \\[2pt] \tfrac{\sqrt2}{2} & -\tfrac{\sqrt6}{6} \\[2pt] -\tfrac{\sqrt2}{2} & -\tfrac{\sqrt6}{6} \end{pmatrix} \approx \begin{pmatrix} 0 & -0.8165 \\ 0.7071 & -0.4082 \\ -0.7071 & -0.4082 \end{pmatrix},\quad R = \begin{pmatrix} \sqrt2 & -\tfrac{\sqrt2}{2} \\[2pt] 0 & \tfrac{\sqrt6}{2} \end{pmatrix} \approx \begin{pmatrix} 1.4142 & -0.7071 \\ 0 & 1.2247 \end{pmatrix}.}$$

**Verificación.** $Q^TQ = I_2$ (columnas ortonormales) ✓, y

$$QR = \begin{pmatrix} 0 & -\tfrac{\sqrt6}{3} \\ \tfrac{\sqrt2}{2} & -\tfrac{\sqrt6}{6} \\ -\tfrac{\sqrt2}{2} & -\tfrac{\sqrt6}{6} \end{pmatrix}\begin{pmatrix} \sqrt2 & -\tfrac{\sqrt2}{2} \\ 0 & \tfrac{\sqrt6}{2} \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 1 & -1 \\ -1 & 0 \end{pmatrix} = A. \quad ✓$$

(Comprobación de la primera columna: $\tfrac{\sqrt2}{2}\cdot\sqrt2 = 1$, $-\tfrac{\sqrt2}{2}\cdot\sqrt2 = -1$. Segunda columna fila 1: $-\tfrac{\sqrt6}{3}\cdot\tfrac{\sqrt6}{2} = -\tfrac{6}{6} = -1$. ✓)

---

### Páginas relacionadas
- [[parcial-tema-13]] — enunciado.
- [[../guias/guia-08-fourier-series]] — serie de Fourier (convención de la cátedra).
- [[ip-tema-01-resolucion]], [[ip-tema-05-resolucion]] — diagonalización y QR resueltos con el mismo formato.
