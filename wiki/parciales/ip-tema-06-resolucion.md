---
tags: [parcial, ip, resolucion, transformaciones-lineales, nucleo-imagen, diagonalizacion, autovectores, independencia-lineal]
fuente: raw/Practicas/Modelos_Examenes/MNA_IP_Tema_VI.pdf
tipo: ip
tema: 6
tiene_resolucion: true
---

# Primer Parcial de Métodos Numéricos Avanzados — Tema VI (Resolución)

## Ejercicio 1

Sea $T : \mathbb{R}^3 \to \mathbb{R}^3 : M_{EE}(T) = \begin{pmatrix} 2 & 8 & k \\ -1 & -4 & 0 \\ k+3 & 12 & 2k \end{pmatrix}$

a) Hallar $k \in \mathbb{R}$, si existe, tal que $\dim(R(T)) = 1$.
b) Para $k = 0$ hallar una base de $N(T)$.

### Resolución

Se llama $A = M_{EE}(T)$. Recordar que $\dim(R(T)) = \operatorname{rg}(A)$, es decir, la cantidad de columnas linealmente independientes de $A$. Pedir $\dim(R(T)) = 1$ equivale a pedir que **todas las columnas sean proporcionales entre sí** (y que $A \ne 0$, para que el rango no sea $0$).

**a)** Las columnas de $A$ son
$$c_1 = \begin{pmatrix} 2 \\ -1 \\ k+3 \end{pmatrix},\qquad c_2 = \begin{pmatrix} 8 \\ -4 \\ 12 \end{pmatrix},\qquad c_3 = \begin{pmatrix} k \\ 0 \\ 2k \end{pmatrix}.$$

Conviene primero descartar el caso de rango máximo mirando el determinante. Desarrollando por la segunda fila (o por cofactores),
$$\det(A) = \begin{vmatrix} 2 & 8 & k \\ -1 & -4 & 0 \\ k+3 & 12 & 2k \end{vmatrix} = 4k^2.$$

Si $k \ne 0$ entonces $\det(A) = 4k^2 \ne 0$, con lo cual $\operatorname{rg}(A) = 3$ y $\dim(R(T)) = 3$. Por lo tanto **el único candidato posible es $k = 0$.**

Verifiquemos que para $k = 0$ el rango es efectivamente $1$ (y no $2$). Con $k = 0$:
$$A = \begin{pmatrix} 2 & 8 & 0 \\ -1 & -4 & 0 \\ 3 & 12 & 0 \end{pmatrix}.$$

Las columnas cumplen
$$c_2 = \begin{pmatrix} 8 \\ -4 \\ 12 \end{pmatrix} = 4\,c_1 = 4\begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix},\qquad c_3 = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}.$$

Las tres columnas son múltiplos de $c_1 = (2,-1,3)^T$ (y $c_1 \ne 0$), así que $R(T) = \langle (2,-1,3) \rangle$ tiene dimensión $1$.

$$\boxed{\;k = 0\;}$$

> **Punto sutil.** El razonamiento por $\det = 0$ solo descarta el rango $3$; podría haber dado rango $2$. Por eso hay que confirmar explícitamente la proporcionalidad de las columnas con $k=0$ para garantizar $\dim(R(T)) = 1$ y no $2$. Aquí la columna $c_3$ se anula y $c_2 = 4c_1$, lo que fija el rango en $1$.

**b)** Para $k = 0$ buscamos $N(T)$, es decir, las soluciones de $AX = 0$:
$$\begin{pmatrix} 2 & 8 & 0 \\ -1 & -4 & 0 \\ 3 & 12 & 0 \end{pmatrix}\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}.$$

Como $\operatorname{rg}(A) = 1$, todas las filas son proporcionales y el sistema se reduce a una sola ecuación independiente. Tomando la primera fila:
$$2x + 8y = 0 \implies x = -4y,$$
y la variable $z$ es **libre** (la tercera columna es nula, así que $z$ no aparece en ninguna ecuación).

Parametrizando con $y = s$, $z = t$:
$$(x, y, z) = (-4s,\ s,\ t) = s\,(-4, 1, 0) + t\,(0, 0, 1).$$

Por lo tanto una base del núcleo es
$$\boxed{\;B_{N(T)} = \{(-4, 1, 0),\ (0, 0, 1)\},\qquad \dim N(T) = 2.\;}$$

Esto es coherente con el **Teorema de la dimensión**: $\dim N(T) + \dim R(T) = 2 + 1 = 3 = \dim \mathbb{R}^3$. ✓

> *Verificación numérica (sympy):* $\operatorname{rg}(A) = 1$, $\operatorname{nullity} = 2$, y $A\,(-4,1,0)^T = A\,(0,0,1)^T = (0,0,0)^T$.

## Ejercicio 2

Sea la matriz $A = \begin{pmatrix} 1 & 0 & 0 \\ 2 & -1 & 0 \\ -4 & 0 & -1 \end{pmatrix}$

a) Analizar si $A$ es diagonalizable.
b) Si $A$ fuera la matriz asociada a una transformación lineal $T : \mathbb{R}^3 \to \mathbb{R}^3$ en las bases canónicas, hallar una base $B$ tal que
$$M(T)_{BB} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & -1 \end{pmatrix}.$$

### Resolución

**a)** Como $A$ es triangular inferior, sus autovalores son los elementos de la diagonal: $1, -1, -1$. Lo confirmamos con el polinomio característico $p_A(\lambda) = \det(\lambda I - A)$:
$$\lambda I - A = \begin{pmatrix} \lambda - 1 & 0 & 0 \\ -2 & \lambda + 1 & 0 \\ 4 & 0 & \lambda + 1 \end{pmatrix} \implies p_A(\lambda) = (\lambda - 1)(\lambda + 1)^2.$$

Entonces los autovalores son $\lambda_1 = 1$ con multiplicidad algebraica $m_a = 1$, y $\lambda_2 = -1$ con $m_a = 2$.

- Para $\lambda_1 = 1$: como $m_a = 1$, automáticamente $m_g = 1 = m_a$.
- Para $\lambda_2 = -1$ hay que calcular $m_g(-1) = \dim N(-I - A)$:
$$-I - A = \begin{pmatrix} -1 - 1 & 0 & 0 \\ -2 & -1 + 1 & 0 \\ 4 & 0 & -1 + 1 \end{pmatrix} = \begin{pmatrix} -2 & 0 & 0 \\ -2 & 0 & 0 \\ 4 & 0 & 0 \end{pmatrix}.$$

Esta matriz tiene rango $1$ (todas las filas son múltiplos de $(-2,0,0)$), así que
$$m_g(-1) = \dim N(-I - A) = 3 - 1 = 2 = m_a(-1).$$

Como para **todo** autovalor se cumple $m_g = m_a$, **$A$ es diagonalizable.** ✓

**b)** Para que $M(T)_{BB} = \operatorname{diag}(1, -1, -1)$, la base $B$ debe estar formada por autovectores ordenados de modo que el **primero** corresponda al autovalor $1$ y los **dos siguientes** al autovalor $-1$ (mismo orden que la diagonal pedida).

*Autovector de $\lambda_1 = 1$:* resolvemos $(A - I)v = 0$, es decir $(I - A)v = 0$:
$$\begin{pmatrix} 0 & 0 & 0 \\ -2 & 2 & 0 \\ 4 & 0 & 2 \end{pmatrix}\begin{pmatrix} x \\ y \\ z \end{pmatrix} = 0 \implies \begin{cases} -2x + 2y = 0 \\ 4x + 2z = 0 \end{cases} \implies y = x,\ z = -2x.$$
Tomando $x = 1$: $\;v_1 = (1, 1, -2)$.

*Autovectores de $\lambda_2 = -1$:* resolvemos $(A + I)v = 0$:
$$\begin{pmatrix} 2 & 0 & 0 \\ 2 & 0 & 0 \\ -4 & 0 & 0 \end{pmatrix}\begin{pmatrix} x \\ y \\ z \end{pmatrix} = 0 \implies x = 0,\quad y, z \text{ libres}.$$
Una base del autoespacio $S_{-1}$ es $\{(0, 1, 0),\ (0, 0, 1)\}$.

Por lo tanto
$$\boxed{\;B = \{\,(1, 1, -2),\ (0, 1, 0),\ (0, 0, 1)\,\}\;}$$
y con ese orden $M(T)_{BB} = \operatorname{diag}(1, -1, -1)$, como se pedía.

**Verificación ($AP = PD$).** Armando $P = (v_1 \mid v_2 \mid v_3)$ y $D = \operatorname{diag}(1,-1,-1)$:
$$P = \begin{pmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ -2 & 0 & 1 \end{pmatrix},\qquad \det(P) = 1 \ne 0\ (\text{base válida}).$$
$$AP = \begin{pmatrix} 1 & 0 & 0 \\ -1 & -1 & 0 \\ 2 & 0 & -1 \end{pmatrix} = PD. \quad\checkmark$$
Equivalentemente, $P^{-1}AP = \operatorname{diag}(1, -1, -1)$.

> **Punto sutil.** El orden importa: la base debe listar primero el autovector de $\lambda = 1$ y luego los de $\lambda = -1$ para que la diagonal salga $\operatorname{diag}(1,-1,-1)$ y no, por ejemplo, $\operatorname{diag}(-1,-1,1)$. Los dos autovectores de $\lambda=-1$ pueden ser cualquier base de $S_{-1}$; se eligieron $(0,1,0)$ y $(0,0,1)$ por simplicidad.

## Ejercicio 3

Sea $A = \{v, u, w\}$ un conjunto linealmente independiente de $\mathbb{R}^3$. Hallar todos los valores de $a, b \in \mathbb{R}$ para que el conjunto $B = \{\,u + a v,\ w,\ u + 2a v + b w\,\}$ sea linealmente independiente.

### Resolución

Planteamos una combinación lineal nula de los vectores de $B$:
$$\alpha\,(u + a v) + \beta\,w + \gamma\,(u + 2a v + b w) = 0.$$

Reagrupamos por los vectores $v, u, w$ del conjunto original:
$$(\alpha a + 2a\gamma)\,v + (\alpha + \gamma)\,u + (\beta + b\gamma)\,w = 0.$$

Como $\{v, u, w\}$ es **linealmente independiente**, los tres coeficientes deben anularse:
$$\begin{cases} a\,\alpha + 2a\,\gamma = 0 & (\text{coef. de } v) \\ \alpha + \gamma = 0 & (\text{coef. de } u) \\ \beta + b\,\gamma = 0 & (\text{coef. de } w) \end{cases}$$

El conjunto $B$ es linealmente independiente $\iff$ la **única** solución de este sistema homogéneo en $(\alpha, \beta, \gamma)$ es la trivial $\iff$ la matriz de coeficientes tiene determinante no nulo. Escribiendo el sistema en forma matricial (en el orden $\alpha, \beta, \gamma$):
$$\underbrace{\begin{pmatrix} a & 0 & 2a \\ 0 & 0 & 0 \\ 0 & 1 & b \end{pmatrix}}_{\text{¡cuidado, ojo al orden!}} \begin{pmatrix} \alpha \\ \beta \\ \gamma \end{pmatrix} = 0.$$

Esta forma tiene una fila nula y oscurece la cuenta. Es más limpio pensar en términos de las **coordenadas de los vectores de $B$ en la base $\{v, u, w\}$**, que son las columnas
$$[u + av]_{\{v,u,w\}} = \begin{pmatrix} a \\ 1 \\ 0 \end{pmatrix},\quad [w] = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix},\quad [u + 2av + bw] = \begin{pmatrix} 2a \\ 1 \\ b \end{pmatrix}.$$

$B$ es LI $\iff$ estas tres columnas son LI $\iff$ el determinante de la matriz $C$ que las tiene por columnas es no nulo:
$$\det(C) = \begin{vmatrix} a & 0 & 2a \\ 1 & 0 & 1 \\ 0 & 1 & b \end{vmatrix}.$$

Desarrollando por la **segunda columna** (que tiene un solo elemento no nulo, el $1$ en la posición $(3,2)$):
$$\det(C) = -1 \cdot \begin{vmatrix} a & 2a \\ 1 & 1 \end{vmatrix}\cdot(-1)^{3+2}\ \Big|_{\text{cofactor}} = (-1)\cdot(-1)\,(a\cdot 1 - 2a\cdot 1) = a - 2a = -a.$$

Es decir, $\det(C) = -a$ (salvo signo, $|\det| = |a|$). Lo importante:
$$\boxed{\;\det(C) = -a,\quad \text{independiente de } b.\;}$$

Entonces $B$ es linealmente independiente $\iff \det(C) \ne 0 \iff a \ne 0$, **para cualquier valor de $b$**:
$$\boxed{\;a \ne 0,\qquad b \in \mathbb{R}\ \text{(arbitrario)}.\;}$$

> **Punto sutil.** El parámetro $b$ **no influye**: el tercer vector $u + 2av + bw$ aporta una componente en $w$ que ya está cubierta de forma independiente por el segundo vector ($w$), de modo que cualquier $b$ deja la matriz con el mismo determinante $-a$. La dependencia lineal aparece solo cuando $a = 0$: en ese caso el primer vector es $u$, el tercero es $u + bw = (u) + b\,(w)$, combinación de los otros dos, y $B$ es LD. La verificación numérica confirmó que el determinante depende únicamente de $a$ (LI $\iff a \ne 0$ para todos los $b$ probados).

---

## Resumen de resultados

| Ej. | Resultado |
|-----|-----------|
| 1a | $k = 0$ (único; $\det A = 4k^2$, y columnas proporcionales con $k=0$) |
| 1b | $N(T) = \langle (-4,1,0),\ (0,0,1)\rangle$, $\dim N(T) = 2$ |
| 2a | Diagonalizable: $p_A(\lambda)=(\lambda-1)(\lambda+1)^2$, $m_g(-1)=m_a(-1)=2$ |
| 2b | $B = \{(1,1,-2),\ (0,1,0),\ (0,0,1)\}$, $\det P = 1$, $AP=PD$ ✓ |
| 3 | LI $\iff a \ne 0$, $\ b \in \mathbb{R}$ arbitrario ($\det C = -a$) |

Ver también: [[ip-tema-06]] (enunciado), [[ip-tema-01-resolucion]], [[ip-tema-05-resolucion]], [[patrones]].
