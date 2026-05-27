---
tags: [pizarron, transformaciones-lineales, interpretacion-geometrica, cambio-de-base, matriz-asociada, autovalores, diagonalizacion]
fuente: raw/Practicas/Pizarrones/Clase_6_TL_Matriz_Asociada.pdf
tipo: escaneo
---

# Pizarrón — Clase 6 (TL y Matriz Asociada): interpretación geométrica, existencia/unicidad, núcleo/imagen y diagonalización

Conjunto de ejercicios enunciados explícitamente sobre interpretación geométrica de TLs en $\mathbb{R}^2$ (proyecciones / reflexiones / rotaciones), cambio de base, existencia y unicidad de TLs, coordenadas en $\mathbb{C}^2$, núcleo e imagen y diagonalización de una matriz $3\times 3$.

## Página 1 — Interpretación geométrica de TLs en $\mathbb{R}^2$

**Enunciado:** Interpretar geométricamente $f(x, y) = (x, 0)$. (Matriz canónica $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$.)

Esquema: $f(x, y) = (x, 0)$ — el núcleo es el eje $y$, la imagen es el eje $x$. $f$ es **proyección ortogonal sobre el eje $x$**.

**Enunciado:** Interpretar geométricamente $f(x, y) = (x, -y)$. (Matriz canónica $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$.)

Esquema: $f(x, y) = (x, -y)$ — el punto $(x, y)$ se refleja respecto del eje $x$. $f$ es **reflexión respecto del eje $x$**.

**Enunciado:** Interpretar geométricamente $f(x, y) = (x\cos\theta - y\sin\theta,\; x\sin\theta + y\cos\theta)$.

Matriz canónica $\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$.

Esquema: $f$ es una **rotación de ángulo $\theta$** (antihoraria) alrededor del origen.

**Enunciado:** Se tiene $P = \begin{pmatrix} 1 & 1 \\ 0 & -3 \end{pmatrix}$ la matriz de cambio de base de $B_1$ a $B_2$. Si $B_1 = \{\vec u_1, \vec u_2\} = \{(1, 0), (1, 1)\}$, obtener $B_2$. ¿Es única?

$$[\vec v]_{B_1} = P\,[\vec v]_{B_2}$$

con $B_2 = \{\vec v_1, \vec v_2\}$ a determinar.

## Página 2 — Resolución (cambio de base) y unicidad de TL

$[\vec u_1]_{B_2},\; [\vec u_2]_{B_2}$:
$$\vec u_1 = 1 \cdot \vec v_1 + 0\cdot \vec v_2 = \vec v_1, \qquad \vec u_2 = 1\cdot \vec v_1 - 3\cdot \vec v_2$$

$$\vec v_1 = \binom{1}{0} \;\Rightarrow\; \binom{1}{1} = 1\cdot\binom{1}{0} - 3\vec v_2$$
$$3\vec v_2 = \binom{1}{0} - \binom{1}{1} = \binom{0}{-1} \;\Rightarrow\; \vec v_2 = \binom{0}{-1/3}$$

> ⚠️ El pizarrón aparece con $\vec v_2 = \binom{1/3}{-1/3}$ (revisar): la cuenta correcta da $\vec v_2 = (0, -1/3)$. La transcripción reproduce ambos valores; queda anotado.

$$B_2 = \left\{\binom{1}{0},\; \binom{1/3}{-1/3}\right\}.$$

**Enunciado:** Determinar si existe una transformación lineal $f: \mathbb{R}^2 \to \mathbb{R}^2$ tal que
$$f(1, 1) = (2, 6), \quad f(-1, 1) = (2, 1), \quad f(2, 7) = (5, 3).$$

Como $(1, 1)$ y $(-1, 1)$ son LI, todo vector de $\mathbb{R}^2$ se escribe combinación lineal de ellos. En particular:
$$(2, 7) = \alpha(1, 1) + \beta(-1, 1)$$
$$\begin{cases} \alpha - \beta = 2 \\ \alpha + \beta = 7 \end{cases} \;\Rightarrow\; \alpha = 9/2 = 4{,}5, \quad \beta = 7 - 4{,}5 = 2{,}5$$

Si $f$ es TL:
$$f(2, 7) = \alpha\,f(1, 1) + \beta\,f(-1, 1) = 4{,}5\cdot(2, 6) + 2{,}5\cdot(2, 1) = (9, 27) + (5, 2{,}5) = (14,\; 29{,}5).$$

Como $(5, 3) \neq (14,\; 29{,}5)$: **no existe ninguna TL que cumpla las 3 condiciones**.

## Página 3 — Núcleo de TL con matriz dada en bases no canónicas

**Enunciado:** Sea $F: \mathbb{R}^3 \to \mathbb{P}_1$ con matriz asociada
$$M_{BE} = \begin{pmatrix} 1 & 0 & 1 \\ -1 & 0 & 0 \end{pmatrix}, \quad B = \{(1, 0, 0),\;(1, 1, 0),\;(1, 0, 1)\},\quad E = \{1, t\}.$$

**a) Hallar una base del núcleo de $F$.**

$$[F(\vec v)]_E = \vec 0; \quad [\vec v]_B = \begin{pmatrix} x_B \\ y_B \\ z_B \end{pmatrix}$$

$$\begin{pmatrix} 1 & 0 & 1 \\ -1 & 0 & 0 \end{pmatrix}\begin{pmatrix} x_B \\ y_B \\ z_B \end{pmatrix} = \binom{0}{0} \;\Rightarrow\; \begin{cases} x_B + z_B = 0 \\ -x_B = 0 \end{cases} \;\Rightarrow\; x_B = 0,\; z_B = 0,\; y_B\text{ libre.}$$

$$[\vec v]_B = \begin{pmatrix} 0 \\ t \\ 0 \end{pmatrix},\; t \neq 0 \;\Rightarrow\; \vec v = 0\cdot \vec b_1 + t\cdot \vec b_2 + 0\cdot \vec b_3 = t\cdot \vec b_2 = t\binom{1}{1}{0}.$$

$$\boxed{\;\text{Una base del núcleo es } \{(1, 1, 0)\}.\;}$$

**b) Encontrar $\vec v \in \mathbb{R}^3$ tal que $F(\vec v) = -1 + t$.**

$$M_{BE}\,[\vec v]_B = \binom{-1}{1} \;\Rightarrow\; \begin{cases} x_B + z_B = -1 \\ -x_B = 1 \end{cases} \;\Rightarrow\; x_B = -1,\; z_B = 0,\; y_B \text{ libre.}$$

Considerando $y_B = 0$: $[\vec v]_B = \binom{-1}{0}{0}$. En $\mathbb{R}^3$:
$$\vec v = -1\cdot \vec b_1 + 0\cdot \vec b_2 + 0\cdot \vec b_3 = (-1, 0, 0).$$

## Página 4 — Coordenadas de $\vec v \in \mathbb{C}^2$ en base compleja

**Enunciado.** Hallar las coordenadas de $\vec v = \binom{2 - i}{2 + 3i} \in \mathbb{C}^2$ respecto de la base $B = \left\{\binom{1 + i}{-i},\; \binom{i}{-i}\right\}$, con $\mathbb{K} = \mathbb{C}$.

$$c_1\binom{1 + i}{-i} + c_2\binom{i}{-i} = \binom{2 - i}{2 + 3i}$$

$$\begin{cases} (1 + i)c_1 + i c_2 = 2 - i \\ -i c_1 - i c_2 = 2 + 3i \quad (\star) \end{cases}$$

Sumando ambas (se cancela $i c_2$ y $-i c_2$ con el correcto cambio): se obtiene
$$(1 + i - i)\,c_1 = 4 + 2i \;\Rightarrow\; c_1 = 4 + 2i.$$

(El pizarrón cancela $+i$ y $-i$ y deja $1 \cdot c_1 = 4 + 2i$.)

Reemplazando en $(\star)$:
$$-i(4 + 2i) - i c_2 = 2 + 3i \;\Rightarrow\; -i c_2 = 2 + 3i + 4i - 2 = 7i \;\Rightarrow\; c_2 = -7.$$

$$\boxed{\;[\vec v]_B = \binom{4 + 2i}{-7}.\;}$$

## Página 5 — TL con matriz $2\times 2$, núcleo e imagen

**Enunciado.** Sea $F: \mathbb{R}^2 \to \mathbb{P}_1$ representada por
$$A = \begin{pmatrix} 1 & 2 \\ 2 & 2 \end{pmatrix}$$
en las bases $B_1 = \{(1, 0), (1, 1)\}$ de $\mathbb{R}^2$ y $B_2 = \{1,\; 1 - x\}$ de $\mathbb{P}_1$.

**a) Hallar $[F(\vec v)]_{B_2}$ si $\vec v = \binom{2}{1}$ (en base canónica).**

Convertir $\vec v$ a $B_1$: $\binom{2}{1} = a\binom{1}{0} + b\binom{1}{1} \;\Rightarrow\; a + b = 2,\; b = 1 \;\Rightarrow\; a = 1$.

$$[\vec v]_{B_1} = \binom{1}{1}$$

$$[F(\vec v)]_{B_2} = A \cdot [\vec v]_{B_1} = \begin{pmatrix} 1 & 2 \\ 2 & 2 \end{pmatrix}\binom{1}{1} = \binom{3}{4}.$$

**b) Hallar una base del núcleo de $F$.**

$$A\cdot[\vec v]_{B_1} = \vec 0 \;\Rightarrow\; \begin{pmatrix} 1 & 2 \\ 2 & 2 \end{pmatrix}\binom{x}{y} = \binom{0}{0} \;\Rightarrow\; \begin{cases} x + 2y = 0 \\ 2x + 2y = 0 \end{cases} \;\Rightarrow\; x = 0,\; y = 0.$$

Sólo solución trivial $\Rightarrow$ $\operatorname{Nu}(F) = \{\vec 0\}$, $\dim \operatorname{Nu} = 0$.

**c) Encontrar una base para la imagen de $F$.**

Las columnas de $A$ son las coordenadas de los transformados de la base $B_1$ en la base $B_2$:
- $C_1 = \binom{1}{2}_{B_2} \;\to\; p_1(t) = 1\cdot 1 + 2\cdot(1 - x) = 3 - 2x.$
- $C_2 = \binom{2}{2}_{B_2} \;\to\; p_2(t) = 2\cdot 1 + 2\cdot(1 - x) = 4 - 2x.$

$$\boxed{\;B_{\operatorname{Im}(F)} = \{p_1, p_2\} = \{3 - 2x,\; 4 - 2x\}.\;}$$

## Página 6 — Autovalores: polinomio característico

**Matriz dada:** $A = \begin{pmatrix} 3 & -1 & 1 \\ 0 & 2 & 0 \\ 1 & -1 & 3 \end{pmatrix}$.

**Polinomio característico:** $\det(A - \lambda I) = 0$.

$$\begin{vmatrix} 3 - \lambda & -1 & 1 \\ 0 & 2 - \lambda & 0 \\ 1 & -1 & 3 - \lambda \end{vmatrix} = 0$$

Desarrollando por la fila 2 (un único término no nulo $2 - \lambda$ en posición $(2, 2)$):
$$(-1)^{2+2}\cdot(2 - \lambda)\cdot\begin{vmatrix} 3 - \lambda & 1 \\ 1 & 3 - \lambda \end{vmatrix} = (2 - \lambda)\big[(3 - \lambda)^2 - 1\big] = 0$$
$$= (2 - \lambda)(9 - 6\lambda + \lambda^2 - 1) = (2 - \lambda)(\lambda^2 - 6\lambda + 8) = (2 - \lambda)(\lambda - 2)(\lambda - 4) = (\lambda - 2)^2(\lambda - 4) = 0$$

Resolviendo $\lambda^2 - 6\lambda + 8 = 0$: $\lambda = \tfrac{6 \pm \sqrt{36 - 32}}{2} = \tfrac{6 \pm 2}{2} \in \{4, 2\}$.

**Autovalores:** $\lambda_1 = 2$ (MA = 2), $\lambda_2 = 4$ (MA = 1).
**Espectro:** $\{2, 4\}$.
**Radio espectral:** $\rho(A) = \max\{|2|, |4|\} = 4$.

**Autoespacio $\lambda_1 = 2$:**
$$A - 2I = \begin{pmatrix} 1 & -1 & 1 \\ 0 & 0 & 0 \\ 1 & -1 & 1 \end{pmatrix} \;\Rightarrow\; \text{rango 1, ecuación } x - y + z = 0 \;\Rightarrow\; x = y - z.$$

$$(y - z,\; y,\; z) = y(1, 1, 0) + z(-1, 0, 1)$$

**Autovectores:** $(1, 1, 0)$ y $(-1, 0, 1)$. $MG(\lambda_1) = 2$.

**Autoespacio $\lambda_2 = 4$:**
$$A - 4I = \begin{pmatrix} -1 & -1 & 1 \\ 0 & -2 & 0 \\ 1 & -1 & -1 \end{pmatrix} \xrightarrow{F_3 + F_1} \begin{pmatrix} -1 & -1 & 1 \\ 0 & -2 & 0 \\ 0 & -2 & 0 \end{pmatrix}$$

## Página 7 — Cierre: autovector de $\lambda_2 = 4$ y diagonalización

$$\begin{cases} -x - y + z = 0 \\ -2y = 0 \;\Rightarrow\; y = 0 \end{cases} \;\Rightarrow\; x = z.$$

$$(z, 0, z) = z(1, 0, 1) \;\Rightarrow\; \text{autovector } (1, 0, 1),\; MG(\lambda_2) = 1.$$

**Diagonalización:**
- Para $\lambda = 2$: $MA = 2, MG = 2 \;\Rightarrow\; MA = MG$.
- Para $\lambda = 4$: $MA = 1, MG = 1 \;\Rightarrow\; MA = MG$.

$\Rightarrow$ **$A$ es diagonalizable.**

**Matriz de pasaje** (columnas = autovectores):
$$P = \begin{pmatrix} 1 & -1 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 1 \end{pmatrix}$$

**Matriz diagonal:**
$$D = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 4 \end{pmatrix}, \quad A = P\,D\,P^{-1}.$$
