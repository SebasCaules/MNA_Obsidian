---
tags: [pizarron, transformaciones-lineales, matriz-asociada, nucleo, imagen, cambio-de-base, derivada-polinomios]
fuente: raw/Practicas/Pizarrones/Clase6.pdf
tipo: escaneo
---

# Pizarrón — Clase 6: Transformaciones lineales, matriz asociada, núcleo e imagen, cambio de base

Contenido: verificación de la linealidad de $f(x) = Ax$ y de $D : \mathbb{P}_2 \to \mathbb{P}_2$ (derivada); cálculo de la **matriz asociada** a una TL en bases canónicas; núcleo e imagen; existencia y unicidad de TL a partir de su acción sobre una base; **matriz de cambio de base**.

## Página 1 — TL definidas por matriz y por derivada

**Sea** $f : \mathbb{R}^n \to \mathbb{R}^n$ tal que $\boxed{f(x) = A\,x}$ donde $A \in \mathbb{R}^{n \times n}$.

Sean $\vec x_1, \vec x_2 \in \mathbb{R}^n$ y $\alpha, \beta \in \mathbb{R}$. Sea $\vec x = \alpha \vec x_1 + \beta \vec x_2$.

$$f(\vec x) = A\vec x = A(\alpha \vec x_1 + \beta \vec x_2) = \alpha A \vec x_1 + \beta A \vec x_2 = \alpha\,f(\vec x_1) + \beta\,f(\vec x_2)$$
$$= \alpha\,T\{\vec x_1\} + \beta\,T\{\vec x_2\}. \;\checkmark \;\; f\text{ es TL.}$$

**3)** Sea la TL $\;T : \mathbb{P}_2 \to \mathbb{P}_2,\; T(p) = p'(x)$ — equivalentemente $D : \mathbb{P}_2 \to \mathbb{P}_2,\; D(p) = p'(x)$.

Si $p(x) = ax^2 + bx + c$, entonces $D(p) = 2ax + b$.

$$D(\alpha p_1 + \beta p_2) = \alpha D(p_1) + \beta D(p_2)$$

**Verificar que $D$ es una TL.** $p(x) = \alpha p_1(x) + \beta p_2(x)$ con $p_1, p_2 \in \mathbb{P}_2$:
$$p_1(x) = a_1 x^2 + b_1 x + c_1, \quad p_2(x) = a_2 x^2 + b_2 x + c_2$$

$$D(p(x)) = p'(x) = (\alpha p_1(x) + \beta p_2(x))' = \alpha p_1'(x) + \beta p_2'(x) = \alpha D(p_1(x)) + \beta D(p_2(x)). \;\checkmark$$

## Página 2 — Coordenadas en una base y matriz asociada

Si $T : V \to I$ es una TL entre espacios vectoriales ($V$ dominio, $I$ imagen),
$$\vec v_i \xrightarrow{TL\{\vec v_i\}} \vec u_i = TL(\vec v_i).$$

Ejemplo: $\vec v_i = ax^2 + bx + c$, $TL\{\vec v_i\} = \vec u_i = 2ax + b$.

**Coordenadas en una base.** Sea $\{b_1, \dots, b_n\}$ base de $V$ y $\{c_1, \dots, c_m\}$ base de $I$:
$$\vec v_i = \sum_{i=1}^n \alpha_i\,b_i \;\rightarrow\; \text{coordenadas de }\vec v_i\text{ en base }\{b_i\}.$$
$$\vec u_i = \sum_{j=1}^m \beta_j\,c_j \;\rightarrow\; \text{coordenadas de }\vec u_i\text{ en base }\{c_j\}.$$

**Base de $\mathbb{P}_2$:** $\{x^2, x, 1\}$ (base canónica).

**Ejemplo.** $\vec v_i = 2x^2 - x + 3 = 2 x^2 + (-1) x + 3\cdot 1$.

$$[\vec v_i]_E = \begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix} \quad \text{(coordenadas en base canónica)}$$

(Análogamente para $\vec u_i$: $[\vec u_i]_C$.)

Lo que se busca es algo que vincule los coeficientes $\alpha_i$ con los $\beta_j$ — la **matriz asociada a la TL**. Trabajamos con la base canónica para ambos espacios.

$D : \mathbb{P}_2 \to \mathbb{P}_2$ (dominio = imagen aquí, ambos $\mathbb{P}_2$).

## Página 3 — Construcción de la matriz $[D]_{EE}$ y aplicación

Acción de $D$ sobre la base canónica:
$$D(x^2) = 2x, \quad D(x) = 1, \quad D(1) = 0$$
$$(\vec v_1 = x^2 \;\rightarrow\; \vec u_1 = 2x), \quad (\vec v_2 = x \;\rightarrow\; \vec u_2 = 1), \quad (\vec v_3 = 1 \;\rightarrow\; \vec u_3 = 0).$$

Coordenadas de los vectores base en base canónica:
$$[x^2]_E = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix},\; [x]_E = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix},\; [1]_E = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}.$$

Coordenadas de los transformados:
$$[2x]_E = \begin{pmatrix} 0 \\ 2 \\ 0 \end{pmatrix},\; [1]_E = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix},\; [0]_E = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}.$$

Matriz asociada a la TL (columnas = coordenadas de las imágenes):
$$[D]_{EE} = \begin{pmatrix} 0 & 0 & 0 \\ 2 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}.$$

**A nivel transformación:** $p(x) = 2x^2 - x + 3 \;\Rightarrow\; D(p) = 4x - 1$.

**A nivel coordenadas:** $[p]_E = \begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix}$.

$$[D(p)]_E = [D]_{EE}\,[p]_E = \begin{pmatrix} 0 & 0 & 0 \\ 2 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}\begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix} = \begin{pmatrix} 0 \\ 4 \\ -1 \end{pmatrix}$$

$$D(p) = 0\cdot x^2 + 4 x - 1\cdot 1 = 4x - 1.\;\checkmark$$

**Núcleo.** $\operatorname{Nu}(T) = \{\vec v \in V \mid T(\vec v) = \vec 0\}$.

## Página 4 — Núcleo e imagen de $D$, teorema de la dimensión

**Buscar el núcleo de $D$:** buscar los polinomios de grado dos tales que $D(p) = \vec 0 = 0 x^2 + 0 x + 0$.

Sea $p = ax^2 + bx + c$. $D(p) = 2ax + b = 0 x^2 + 0x + 0 \;\Rightarrow\; \begin{cases} 2a = 0 \;\Rightarrow\; a = 0 \\ b = 0 \end{cases}$.

El núcleo de $D$ está formado por los polinomios de la forma $p(x) = \alpha$ con $\alpha \in \mathbb{R}$ (constantes).

**A través de la imagen de $D$**, y $[\vec 0]_E = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$:
$$[D]_{EE}\,[p]_E = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} \;\Rightarrow\; \begin{pmatrix} 0 & 0 & 0 \\ 2 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}\begin{pmatrix} \alpha \\ \beta \\ \gamma \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$$
$$\Rightarrow \begin{cases} 2\alpha = 0 \\ \beta = 0 \end{cases} \;\Rightarrow\; [p]_E = \begin{pmatrix} 0 \\ 0 \\ \gamma \end{pmatrix}.$$

$$\boxed{\;B_{\text{Nu}(D)} = \left\{\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}\right\}\;}$$

**Imagen de $D$.** $D(p) = 2ax + b = 0 x^2 + 2ax + b\cdot 1$.

$$\text{Base } \operatorname{Im}(D) = \left\{\begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix},\; \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}\right\}$$

**Teorema de la dimensión.**
$$\dim(\mathbb{P}_2) = 3, \quad \dim(\operatorname{Nu}(D)) = 1, \quad \dim(\operatorname{Im}(D)) = 2.$$

$3 = 1 + 2.\;\checkmark$

## Página 5 — Ejercicio 5: existencia y unicidad de TL desde acción sobre base

**5)** Probar que existe una única transformación lineal $f : \mathbb{R}^2 \to \mathbb{R}^2$ tal que $f\binom{1}{1} = \binom{-5}{3}$ y $f\binom{-1}{1} = \binom{1}{2}$.

> Esquema: $\mathbb{R}^2 \xrightarrow{f} \mathbb{R}^2$, ambos con la base canónica $\{(1,0)^\top, (0,1)^\top\}$.

Coordenadas en base canónica $E$:
$$[(1, 1)]_E = \binom{1}{1}, \quad [(-1, 1)]_E = \binom{-1}{1}.$$

A nivel coordenadas, con $f$ representada por matriz $A = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}$:
$$\binom{-5}{3} = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}\binom{1}{1} \;\Rightarrow\; \begin{cases} -5 = a_{11} + a_{12} \\ 3 = a_{21} + a_{22} \end{cases}$$
$$\binom{1}{2} = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}\binom{-1}{1} \;\Rightarrow\; \begin{cases} 1 = -a_{11} + a_{12} \\ 2 = -a_{21} + a_{22} \end{cases}$$

Sumando primer par:
$$\begin{cases} 0 = a_{11} - a_{11} + 2a_{12} \;\Rightarrow\; 2a_{12} = -5 + 1 = -4 \;\Rightarrow\; a_{12} = -2 \\ -5 = a_{11} + (-2) \;\Rightarrow\; a_{11} = -3 \end{cases}$$

Análogamente:
$$\begin{cases} 5 = 2a_{22} \;\Rightarrow\; a_{22} = \tfrac{5}{2} \\ 3 = a_{21} + \tfrac{5}{2} \;\Rightarrow\; a_{21} = \tfrac{1}{2} \end{cases}$$

$$A = \begin{pmatrix} -3 & -2 \\ \tfrac{1}{2} & \tfrac{5}{2} \end{pmatrix}$$

> ⚠️ El pizarrón muestra $A = \begin{pmatrix} -5 & 0 \\ \tfrac{1}{2} & \tfrac{5}{2} \end{pmatrix}$ con un descarte tachado; la cuenta numérica fiel a las condiciones es la mostrada arriba (revisar).

Buscar el núcleo de $f$ es equivalente a buscar el espacio nulo de la matriz de coordenadas $A$:
$$A\binom{x}{y} = \binom{0}{0}.$$

Como la matriz es inversible (si $\det A \neq 0$):

## Página 6 — Conclusión 5 y matriz de cambio de base

$\det A \neq 0 \;\Rightarrow\;$ la solución es $\binom{x}{y} = \binom{0}{0}$. Es decir $\operatorname{Nu}(f) = \{\vec 0\}$, lo que confirma que la TL existe y es única.

**Matriz de cambio de base.** Sean $B_1$ y $B_2$ bases de $\mathbb{R}^2$ y $P = \begin{pmatrix} 0 & 1 \\ 0 & -3 \end{pmatrix}$ la matriz de cambio de base de $B_1$ a $B_2$.

> ⚠️ La $P$ del pizarrón aparece como $\begin{pmatrix} 0 & 1 \\ 0 & -3 \end{pmatrix}$, pero el cálculo posterior usa $\begin{pmatrix} 1 & 1 \\ 0 & -3 \end{pmatrix}$; la primera columna real debería ser no nula. Se interpreta $P = \begin{pmatrix} 1 & 1 \\ 0 & -3 \end{pmatrix}$.

Sea $\vec s$ un vector de $\mathbb{R}^2$: en $B_1$ tiene coordenadas $[\vec s]_{B_1} = \binom{p}{q}$ y en $B_2$ tiene coordenadas $[\vec s]_{B_2} = \binom{a}{b}$.

Entonces: $P\,[\vec s]_{B_1} = [\vec s]_{B_2}$, es decir $P\binom{p}{q} = \binom{a}{b}$.

**a)** Si $[\vec u]_{B_1} = \binom{1}{4}$, calcular $[\vec u]_{B_2}$:
$$P[\vec u]_{B_1} = [\vec u]_{B_2} \;\Rightarrow\; \begin{pmatrix} 1 & 1 \\ 0 & -3 \end{pmatrix}\binom{1}{4} = \binom{5}{-12}.$$

**b)** $[\vec s]_{B_2} = \binom{3}{5}$, calcular $[\vec s]_{B_1}$:
$$P[\vec s]_{B_1} = [\vec s]_{B_2} \;\Rightarrow\; \begin{pmatrix} 1 & 1 \\ 0 & -3 \end{pmatrix}\binom{x}{y} = \binom{3}{5}$$
$$\Rightarrow \begin{cases} x + y = 3 \\ -3y = 5 \;\Rightarrow\; y = -\tfrac{5}{3} \end{cases} \;\Rightarrow\; x = 3 + \tfrac{5}{3} = \tfrac{14}{3}.$$

$$[\vec s]_{B_1} = \binom{14/3}{-5/3}.$$

> Nota del pizarrón: $x = 3 + 5/3$ y $y = -5/3$.
