---
tags: [parcial, ip, resolucion, transformaciones-lineales, nucleo-imagen, diagonalizacion, autovalores, lu, qr]
fuente: raw/Practicas/Modelos_Examenes/MNA_IP_Tema_III.pdf
tipo: ip
tema: 3
tiene_resolucion: true
---

# Primer Parcial de Métodos Numéricos Avanzados — Tema III (Resolución)

## Ejercicio 1

Sea $T : \mathbb{R}^3 \to \mathbb{R}^3$ tal que

$$M_E(T) = \begin{pmatrix} 2 & 8 & k \\ -1 & -4 & 0 \\ k+3 & 12 & 2k \end{pmatrix}$$

a) Hallar $k \in \mathbb{R}$, si existe, tal que $\dim(R(T)) = 1$.
b) Para $k = 0$, hallar una base y la dimensión del núcleo de $T$.

### Resolución

Llamamos $A = M_E(T)$ y notamos sus columnas

$$c_1 = \begin{pmatrix} 2 \\ -1 \\ k+3 \end{pmatrix},\qquad c_2 = \begin{pmatrix} 8 \\ -4 \\ 12 \end{pmatrix},\qquad c_3 = \begin{pmatrix} k \\ 0 \\ 2k \end{pmatrix}.$$

**a)** Como $\dim R(T) = \operatorname{rg}(A)$, pedir $\dim R(T) = 1$ equivale a $\operatorname{rg}(A) = 1$, es decir, que **todas las columnas no nulas sean proporcionales entre sí** (el espacio columna es una sola recta).

Observamos primero que $c_2 = (8, -4, 12)^T = 4\,(2, -1, 3)^T$. Para que $c_1$ sea proporcional a $c_2$ se necesita $c_1 = (2, -1, 3)^T$, lo que obliga a la tercera componente

$$k + 3 = 3 \implies k = 0.$$

Con $k = 0$ la tercera columna es $c_3 = (0,0,0)^T$, que no aporta dirección. Verifiquemos que con $k=0$ efectivamente $c_1 = c_2/4$:

$$c_1 = (2, -1, 3)^T = \tfrac14 (8, -4, 12)^T = \tfrac14 c_2.\ \checkmark$$

Por lo tanto, para $k = 0$ las dos columnas no nulas son proporcionales y $\operatorname{rg}(A) = 1$.

> **Comprobación numérica.** Para $k = 0$ la matriz tiene $\operatorname{rg}(A) = 1$ (un único valor singular no nulo, $\sigma_1 \approx 15.43$, los otros dos nulos). Para cualquier otro valor de prueba ($k = -3, -1, 1, 2$) se obtiene $\operatorname{rg}(A) = 3$ y $\det(A) \ne 0$. Es decir, $k = 0$ es el **único** valor que baja el rango, y lo lleva directamente a $1$.

$$\boxed{\,k = 0\,}$$

**b)** Con $k = 0$:

$$A = \begin{pmatrix} 2 & 8 & 0 \\ -1 & -4 & 0 \\ 3 & 12 & 0 \end{pmatrix}.$$

El núcleo se obtiene resolviendo $AX = 0$. Las tres filas son múltiplos de $(1, 4, 0)$ (de hecho $\operatorname{rg}(A) = 1$), así que el sistema se reduce a una sola ecuación independiente:

$$x + 4y = 0 \implies x = -4y,\qquad z \text{ libre}.$$

Un vector genérico del núcleo es

$$\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} -4y \\ y \\ z \end{pmatrix} = y\begin{pmatrix} -4 \\ 1 \\ 0 \end{pmatrix} + z\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}.$$

Por lo tanto

$$\boxed{\,B_{N(T)} = \left\{ (-4, 1, 0),\ (0, 0, 1) \right\},\qquad \dim N(T) = 2.\,}$$

Esto es consistente con el **teorema de la dimensión**: $\dim N(T) + \dim R(T) = 2 + 1 = 3 = \dim \mathbb{R}^3$. $\checkmark$

> **Comprobación numérica.** $A\,(-4, 1, 0)^T = (0,0,0)^T$ y $A\,(0,0,1)^T = (0,0,0)^T$; además $\operatorname{nul}(A) = 3 - \operatorname{rg}(A) = 2$.

---

## Ejercicio 2

Sea

$$A = \begin{pmatrix} 2 & k-2 & 0 \\ 0 & 3 & k-1 \\ 0 & 0 & 3 \end{pmatrix}.$$

a) Hallar $k \in \mathbb{R}$ para que $A$ sea diagonalizable en $\mathbb{R}$.
b) Para $k = 0$, hallar una base de autovectores de $A$.

### Resolución

**a)** $A$ es **triangular superior**, de modo que sus autovalores son los elementos de la diagonal:

$$\lambda = 2,\quad \lambda = 3,\quad \lambda = 3 \quad\Longrightarrow\quad p_A(\lambda) = (\lambda - 2)(\lambda - 3)^2.$$

Las multiplicidades algebraicas son $m_a(2) = 1$ y $m_a(3) = 2$. Para el autovalor simple $\lambda = 2$ siempre se cumple $m_g = m_a = 1$. El único riesgo de no diagonalizar está en $\lambda = 3$: se necesita $m_g(3) = m_a(3) = 2$, donde $m_g(3) = \dim S_3 = 3 - \operatorname{rg}(3I - A)$.

Calculamos (uso $A - 3I$, que tiene el mismo núcleo que $3I - A$):

$$A - 3I = \begin{pmatrix} -1 & k-2 & 0 \\ 0 & 0 & k-1 \\ 0 & 0 & 0 \end{pmatrix}.$$

La primera fila $(-1,\ k-2,\ 0)$ es siempre no nula. La segunda fila es $(0,\ 0,\ k-1)$:

- Si $k \ne 1$: la segunda fila es no nula y linealmente independiente de la primera, así que $\operatorname{rg}(A - 3I) = 2$, con lo cual $m_g(3) = 1 < 2$. **No diagonalizable.**
- Si $k = 1$: la segunda fila se anula y queda solo la primera, $\operatorname{rg}(A - 3I) = 1$, de modo que $m_g(3) = 3 - 1 = 2 = m_a(3)$. **Diagonalizable.**

$$\boxed{\,A \text{ es diagonalizable en } \mathbb{R} \iff k = 1.\,}$$

> **Comprobación numérica.** Recorriendo $k \in \{-1, 0, 1, 2, 3\}$, sólo $k = 1$ da $\operatorname{rg}(A - 3I) = 1$ (y por tanto $m_g(3) = 2$); el resto da rango $2$ y $m_g(3) = 1$. Para $k = 1$ se verifica $AP = PD$ con $P = \begin{pmatrix} 1 & -1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{pmatrix}$, $D = \operatorname{diag}(2,3,3)$ (residuo $\|AP - PD\| = 0$).

**b)** Para $k = 0$:

$$A = \begin{pmatrix} 2 & -2 & 0 \\ 0 & 3 & -1 \\ 0 & 0 & 3 \end{pmatrix}.$$

Por el inciso anterior, con $k = 0 \ (\ne 1)$ la matriz **no es diagonalizable**: el autoespacio $S_3$ tiene dimensión $1$ y no alcanzan los autovectores para formar una base de $\mathbb{R}^3$. Aun así, hallamos el conjunto máximo de autovectores linealmente independientes.

*Autovalor $\lambda = 2$* (resolvemos $(A - 2I)X = 0$):

$$A - 2I = \begin{pmatrix} 0 & -2 & 0 \\ 0 & 1 & -1 \\ 0 & 0 & 1 \end{pmatrix} \implies z = 0,\ y = 0,\ x \text{ libre} \implies v_2 = (1, 0, 0).$$

*Autovalor $\lambda = 3$* (resolvemos $(A - 3I)X = 0$):

$$A - 3I = \begin{pmatrix} -1 & -2 & 0 \\ 0 & 0 & -1 \\ 0 & 0 & 0 \end{pmatrix} \implies z = 0,\ -x - 2y = 0 \implies x = -2y \implies v_3 = (-2, 1, 0).$$

Por lo tanto, el conjunto de autovectores (linealmente independientes) es

$$\boxed{\,\{\,v_2 = (1,0,0),\ v_3 = (-2,1,0)\,\},\qquad \dim S_2 = 1,\ \dim S_3 = 1.\,}$$

Como sólo hay $2$ autovectores independientes para una matriz $3\times3$, **no constituyen una base de $\mathbb{R}^3$ y $A$ no es diagonalizable** para $k = 0$ (coherente con a).

> **Comprobación numérica.** $A\,v_2 = 2 v_2$ y $A\,v_3 = 3 v_3$ (residuos nulos). El cálculo numérico de autovalores devuelve $\{2, 3, 3\}$ y el autoespacio de $\lambda = 3$ tiene dimensión $1$ (la rutina entrega $\propto (-2, 1, 0)$), confirmando la deficiencia geométrica.

---

## Ejercicio 3

Sea

$$A = \begin{pmatrix} 1 & 3 & -1 \\ 2 & 8 & 4 \\ -1 & 3 & -4 \end{pmatrix}.$$

a) Hallar la factorización $PLU$.
b) Hallar la factorización $QR$.

### Resolución

**a) Factorización $PLU$ (Doolittle).**

Aplicamos eliminación gaussiana guardando los multiplicadores en $L$. El primer pivote es $a_{11} = 1 \ne 0$, así que no hace falta permutar.

*Paso 1 — eliminar la columna 1.* Multiplicadores $m_{21} = \dfrac{2}{1} = 2$ y $m_{31} = \dfrac{-1}{1} = -1$:

$$F_2 \leftarrow F_2 - 2 F_1,\qquad F_3 \leftarrow F_3 - (-1) F_1 = F_3 + F_1.$$

$$\begin{pmatrix} 1 & 3 & -1 \\ 2 & 8 & 4 \\ -1 & 3 & -4 \end{pmatrix} \longrightarrow \begin{pmatrix} 1 & 3 & -1 \\ 0 & 2 & 6 \\ 0 & 6 & -5 \end{pmatrix}.$$

*Paso 2 — eliminar la columna 2.* El segundo pivote es $2 \ne 0$ (no se permuta). Multiplicador $m_{32} = \dfrac{6}{2} = 3$:

$$F_3 \leftarrow F_3 - 3 F_2 \implies \begin{pmatrix} 1 & 3 & -1 \\ 0 & 2 & 6 \\ 0 & 0 & -23 \end{pmatrix}.$$

Como en ningún paso un pivote fue $0$, **no se requiere permutación**: $P = I$ y $A = LU$. Los multiplicadores arman $L$ (con unos en la diagonal):

$$\boxed{\,P = I,\quad L = \begin{pmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ -1 & 3 & 1 \end{pmatrix},\quad U = \begin{pmatrix} 1 & 3 & -1 \\ 0 & 2 & 6 \\ 0 & 0 & -23 \end{pmatrix}.\,}$$

**Verificación $LU = A$:**

$$LU = \begin{pmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ -1 & 3 & 1 \end{pmatrix}\begin{pmatrix} 1 & 3 & -1 \\ 0 & 2 & 6 \\ 0 & 0 & -23 \end{pmatrix} = \begin{pmatrix} 1 & 3 & -1 \\ 2 & 8 & 4 \\ -1 & 3 & -4 \end{pmatrix} = A.\ \checkmark$$

> **Comprobación numérica.** $\|LU - A\| = 0$. (Como control: $\det A = \det U = 1\cdot 2\cdot(-23) = -46$, no nulo, consistente con que $A$ es inversible.)

**b) Factorización $QR$ (Gram–Schmidt sobre las columnas).**

Columnas de $A$: $\;a_1 = (1, 2, -1)^T,\quad a_2 = (3, 8, 3)^T,\quad a_3 = (-1, 4, -4)^T.$

*Primer vector.* $u_1 = a_1 = (1, 2, -1)$, $\ \|u_1\| = \sqrt{1 + 4 + 1} = \sqrt{6}$.

$$v_1 = \frac{u_1}{\|u_1\|} = \frac{1}{\sqrt{6}}(1, 2, -1).$$

*Segundo vector.* $\langle a_2, a_1\rangle = 3 + 16 - 3 = 16$, así que la proyección sobre $u_1$ usa el coeficiente $\dfrac{\langle a_2, u_1\rangle}{\langle u_1, u_1\rangle} = \dfrac{16}{6} = \dfrac{8}{3}$:

$$u_2 = a_2 - \frac{8}{3}\,a_1 = (3, 8, 3) - \frac{8}{3}(1, 2, -1) = \frac{1}{3}(1, 8, 17).$$

$$\|u_2\|^2 = \frac{1}{9}(1 + 64 + 289) = \frac{354}{9} = \frac{118}{3} \implies \|u_2\| = \sqrt{\tfrac{118}{3}} = \frac{\sqrt{354}}{3}.$$

$$v_2 = \frac{u_2}{\|u_2\|} = \frac{1}{\sqrt{354}}(1, 8, 17).$$

*Tercer vector.* $\langle a_3, u_1\rangle = -1 + 8 + 4 = 11 \Rightarrow$ coef. $\dfrac{11}{6}$. Y $\langle a_3, u_2\rangle = \dfrac{1}{3}(-1 + 32 - 68) = -\dfrac{37}{3}$, con $\langle u_2, u_2\rangle = \dfrac{118}{3}$, así que coef. $\dfrac{-37/3}{118/3} = -\dfrac{37}{118}$:

$$u_3 = a_3 - \frac{11}{6}\,u_1 - \left(-\frac{37}{118}\right)u_2 = \frac{23}{59}(-7, 3, -1).$$

$$\|u_3\|^2 = \left(\frac{23}{59}\right)^2(49 + 9 + 1) = \frac{529}{3481}\cdot 59 = \frac{529}{59} \implies \|u_3\| = \frac{23}{\sqrt{59}}.$$

$$v_3 = \frac{u_3}{\|u_3\|} = \frac{1}{\sqrt{59}}(-7, 3, -1).$$

Entonces $Q = (v_1 \mid v_2 \mid v_3)$ y $R = Q^T A$ es triangular superior con $R_{ii} = \|u_i\|$ y $R_{ij} = \langle a_j, v_i\rangle$ para $i < j$:

$$\boxed{\,Q = \begin{pmatrix} \tfrac{1}{\sqrt{6}} & \tfrac{1}{\sqrt{354}} & \tfrac{-7}{\sqrt{59}} \\[4pt] \tfrac{2}{\sqrt{6}} & \tfrac{8}{\sqrt{354}} & \tfrac{3}{\sqrt{59}} \\[4pt] \tfrac{-1}{\sqrt{6}} & \tfrac{17}{\sqrt{354}} & \tfrac{-1}{\sqrt{59}} \end{pmatrix},\qquad R = \begin{pmatrix} \sqrt{6} & \tfrac{16}{\sqrt{6}} & \tfrac{11}{\sqrt{6}} \\[4pt] 0 & \tfrac{\sqrt{354}}{3} & \tfrac{-37}{\sqrt{354}} \\[4pt] 0 & 0 & \tfrac{23}{\sqrt{59}} \end{pmatrix}.\,}$$

Numéricamente,

$$Q \approx \begin{pmatrix} 0.4082 & 0.0531 & -0.9113 \\ 0.8165 & 0.4252 & 0.3906 \\ -0.4082 & 0.9035 & -0.1302 \end{pmatrix},\qquad R \approx \begin{pmatrix} 2.4495 & 6.5320 & 4.4907 \\ 0 & 6.2716 & -1.9665 \\ 0 & 0 & 2.9943 \end{pmatrix}.$$

> **Comprobación numérica.** $\|QR - A\| = 0$ y $\|Q^T Q - I\| \approx 2.2\times 10^{-16}$ (columnas ortonormales). Los valores exactos de la diagonal de $R$ son $R_{11} = \sqrt6$, $R_{22} = \tfrac{\sqrt{354}}{3}$, $R_{33} = \tfrac{23}{\sqrt{59}}$, que coinciden con $\|u_1\|, \|u_2\|, \|u_3\|$.

---

## Apéndice — código de verificación

```python
import numpy as np, scipy.linalg as sla
import math

# --- Ej 1 ---
def A1(k): return np.array([[2,8,k],[-1,-4,0],[k+3,12,2*k]], float)
assert np.linalg.matrix_rank(A1(0)) == 1
A = A1(0)
for v in ([-4,1,0],[0,0,1]):
    assert np.allclose(A @ v, 0)

# --- Ej 2 ---
def A2(k): return np.array([[2,k-2,0],[0,3,k-1],[0,0,3]], float)
assert np.linalg.matrix_rank(A2(1)-3*np.eye(3)) == 1          # k=1 diagonalizable
assert np.linalg.matrix_rank(A2(0)-3*np.eye(3)) == 2          # k=0 NO
A = A2(0)
assert np.allclose(A @ [1,0,0], 2*np.array([1,0,0]))
assert np.allclose(A @ [-2,1,0], 3*np.array([-2,1,0]))

# --- Ej 3 ---
A = np.array([[1,3,-1],[2,8,4],[-1,3,-4]], float)
L = np.array([[1,0,0],[2,1,0],[-1,3,1]], float)
U = np.array([[1,3,-1],[0,2,6],[0,0,-23]], float)
assert np.allclose(L @ U, A)                                  # PLU con P=I

v1 = np.array([1,2,-1.])/math.sqrt(6)
v2 = np.array([1,8,17.])/math.sqrt(354)
v3 = np.array([-7,3,-1.])/math.sqrt(59)
Q = np.column_stack([v1,v2,v3]); R = Q.T @ A
assert np.allclose(Q @ R, A) and np.allclose(Q.T @ Q, np.eye(3))
print("Todas las verificaciones OK")
```
