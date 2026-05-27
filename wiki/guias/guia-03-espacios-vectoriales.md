---
tags: [guia, espacios-vectoriales, producto-interno, normas]
fuente: raw/Practicas/Guias_TP2026/Guia_TP_III_MNA_ITBA_2025.pdf
unidad: III
---

# Guía de Trabajos Prácticos III — Espacios vectoriales, producto interno y normas

## Definiciones preliminares

Diremos que $(V; +; \mathbb{K}; \cdot)$ es un espacio vectorial sobre un cuerpo de escalares $\mathbb{K}$ si:

- $v_1, v_3 \in V \Rightarrow (v_1 + v_3) \in V$
- $\lambda \in \mathbb{K}, v \in V \Rightarrow \lambda \cdot v \in V$

Diremos que $(S \subseteq V; +; \mathbb{K}; \cdot)$ es un subespacio vectorial sobre $\mathbb{K}$ si:

- $S \ne \emptyset$
- $v_1, v_3 \in S \Rightarrow (v_1 + v_3) \in S$
- $\lambda \in \mathbb{K}, v \in S \Rightarrow \lambda \cdot v \in S$

Está claro que si $S$ es un subespacio de $V$, $0 \in S$.

## Espacios Vectoriales

### Ejercicio 1

Probar que el conjunto $V$ con la suma y el producto por escalares definidos a continuación, es un espacio vectorial sobre $\mathbb{R}$:

$$V \equiv \mathbb{R}^{\mathbb{R}} = \{f : \mathbb{R} \to \mathbb{R} \mid f \text{ es función}\}$$

$$+ : (f + g)(x) = f(x) + g(x)\;\forall x \in \mathbb{R}$$
$$\cdot : (k \cdot f)(x) = k \cdot f(x)\;\forall x \in \mathbb{R}$$

### Ejercicio 2

Prueba que el conjunto $C^k$, el conjunto de las funciones $k$ veces derivables, con $f^{(k)}$ continua, es un espacio vectorial con la suma y el producto por escalar definidos en el ítem anterior.

### Ejercicio 3

Caracteriza geométricamente todos los subespacios de $\mathbb{R}^2$ y de $\mathbb{R}^3$.

### Ejercicio 4

Indica cuáles de los siguientes subconjuntos de $\mathbb{R}^2$ son un subespacio con la suma y el producto por escalar ordinario.

- a) $A = \{(x_1, x_2) \in \mathbb{R}^2 \mid x_1 = 0\}$
- b) $B = \{(x_1, x_2) \in \mathbb{R}^2 \mid 2x_1 - 2x_2 - 2 = 0\}$
- c) $C = \{(x_1, x_2) \in \mathbb{R}^2 \mid 3x_1 - 2x_2 - 3 = 0\}$
- d) $D = \{(x_1, x_2) \in \mathbb{R}^2 \mid x_1 \le 0\}$

### Ejercicio 5

Analiza en cada caso si $S$ es un subespacio de $V$.

- a) $V = \mathbb{R}^4$, $\mathbb{K} = \mathbb{R}$; $S = \{(x_1, x_2, x_3, x_4) \in \mathbb{R}^4 \mid x_1 + x_2 - x_4 = 0\}$.
- b) $V = \mathbb{R}^4$, $\mathbb{K} = \mathbb{R}$; $S = \{(x_1, x_2, x_3, x_4) \in \mathbb{R}^4 \mid x_1 - x_4 = 0\}$.
- c) $V = \mathbb{R}^{2\times 2}$, $\mathbb{K} = \mathbb{R}$; $S = \{A \in \mathbb{R}^{2\times 2} \mid A \text{ es singular}\}$.
- d) $V = \mathbb{C}$, $\mathbb{K} = \mathbb{R}$; $S = \{a\,i \mid a \in \mathbb{R}\}$.
- e) $V = \mathbb{C}$, $\mathbb{K} = \mathbb{C}$; $S = \{a\,i \mid a \in \mathbb{R}\}$.

### Ejercicio 6

Analiza para cada caso si $S$ es un subespacio de $V$.

- a) $V = P_n$, $S = \{p \in P_n \mid p = 0 \text{ o } \operatorname{gr}(p) \le n\}$.
- b) $V = P_2$, $S = \{p \in P_2 \mid a_0 - a_1 + a_2 = 0 \text{ y } 2a_2 - a_0 = 0\}$.

### Ejercicio 7

- a) Determina si $a = (1, -1, 3)$ es combinación lineal de $b = (0, 2, 2)$; $c = (1, -1, 1)$.
- b) Expresa el polinomio $p(t) = t^2 + 4t - 3$ como combinación lineal de $(t^2 - 2t + 5)$, $(2t^2 - 3t)$, $(t + 3)$.
- c) Halla $k \in \mathbb{R}$ tal que $(1, 2, 0)$ sea combinación lineal de $\{(1, 2, -1), (2, 2, 1), (2, 1 + k, k)\}$.

### Ejercicio 8

Hallar todos los $k \in \mathbb{R}$ para los cuales cada uno de los siguientes subconjuntos de $\mathbb{R}^3$ es un conjunto de vectores linealmente independiente.

- a) $\{(1, 2, k), (1, 1, 1), (0, 1, 1 - k)\}$.
- b) $\{(k, 1, 0), (3, -1, 2), (k, 2, -2)\}$.
- c) $\left\{\begin{pmatrix}1 & 0 \\ 0 & 1\end{pmatrix},\, \begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix},\, \begin{pmatrix}0 & k \\ 1 & -1\end{pmatrix},\, \begin{pmatrix}0 & 3 \\ -k & 1\end{pmatrix}\right\}$

### Ejercicio 9

Demuestra que $B = \{(1, 1, 0), (0, 1, 1), (1, 0, 1)\}$ es una base de $\mathbb{R}^3$.

### Ejercicio 10

Prueba que el conjunto $\{(1, 0, 0), (0, i, 0), (1, 1, i)\}$ es base de $\mathbb{C}^3$ como espacio vectorial sobre $\mathbb{C}$, pero no como espacio vectorial sobre $\mathbb{R}$. Calcula la dimensión de $\mathbb{C}^3$ como espacio vectorial sobre $\mathbb{R}$.

### Ejercicio 11

¿Qué dimensión tienen el conjunto de vectores generado por los siguientes conjuntos? Completa los siguientes conjuntos L.I. a una base del $\mathbb{K}$-espacio vectorial.

- a) $\{(1, 1, 1, 1), (0, 2, 1, 1)\}$, $V = \mathbb{R}^4$, $\mathbb{K} = \mathbb{R}$.
- b) $\{x^3 - 2x + 1,\, x^3 + 3x\}$, $V = \mathbb{R}_3[x]$, $\mathbb{K} = \mathbb{R}$.
- c) $\left\{\begin{pmatrix}1 & 0 \\ i & 1\end{pmatrix},\, \begin{pmatrix}0 & i \\ 1 & 1\end{pmatrix},\, \begin{pmatrix}0 & 2 \\ 1 & 1\end{pmatrix}\right\}$

### Ejercicio 12

Probar que $\mathbb{R}^{n\times m}$, con la suma y producto por escalar estándar, es un espacio vectorial de dimensión $n \times m$.

### Ejercicio 13

Sea $A \in \mathbb{K}^{n\times m}$ y sea $S = \{x \in \mathbb{K}^m \mid A \cdot x = 0\}$ el conjunto de soluciones del sistema lineal homogéneo cuya matriz asociada es $A$. Probar que $S$ es un subespacio de $\mathbb{K}^m$.

### Ejercicio 14

Probar que $u = (2, 1)$ es combinación lineal de $w_1 = (1, 0)$, $w_2 = (0, 1)$.

### Ejercicio 15

Sea $S = \operatorname{gen}\{(1, -1, 2, 1), (3, 1, 0, -1), (1, 1, -1, -1)\} \subseteq \mathbb{R}^4$:

- a) Determina si $u = (2, 1, 3, 5) \in S$.

## Producto interno y norma

### Ejercicio 1

Considera los siguientes pares de vectores:

$$x_1 = \begin{pmatrix}1 \\ -1\end{pmatrix},\; y_1 = \begin{pmatrix}-1 \\ 1\end{pmatrix};\quad x_2 = \begin{pmatrix}e^{i\pi/4} \\ -1\end{pmatrix},\; y_2 = \begin{pmatrix}1 - i \\ e^{i\pi/3}\end{pmatrix};$$

$$x_3 = \begin{pmatrix}1 \\ -1 \\ 2\end{pmatrix},\; y_3 = \begin{pmatrix}10 \\ 5 \\ -2\end{pmatrix};\quad x_4 = \begin{pmatrix}1 + 2i \\ -1 \\ 2 - i\end{pmatrix},\; y_4 = \begin{pmatrix}i \\ 4 + 4i \\ -1\end{pmatrix}.$$

- a) Verifica la desigualdad de Cauchy-Schwarz para cada par.
- b) Encuentra el ángulo formado por cada par de vectores en $\mathbb{R}^2$ o $\mathbb{R}^3$.
- c) Encuentra la proyección de $x_k$ sobre $y_k$ para $k = 1, 2, 3, 4$.

### Ejercicio 2

Interpretación geométrica de algunas normas.

- a) Dibujar el espacio geométrico correspondiente al conjunto de vectores $x \in \mathbb{R}^2$ tal que $\|x\|_p = 1$ con $p = 1, 2, \infty$.
- b) ¿Por qué a la norma 1 se la suele asociar con los nombres "distancia de Manhattan", base de la "geometría del taxista"?

### Ejercicio 3

Sean $a$ y $b$ dos vectores en $\mathbb{R}^2$.

- a) Encuentra el valor de $\alpha$ que minimiza la función $f(\alpha) = \|b - \alpha a\|^2$. Nota: $\alpha a$ es la proyección de $b$ en la dirección de $a$.
- b) Demuestra que el vector "error" $e = b - \alpha a$ es perpendicular a $a$.

### Ejercicio 4

Determina cuáles de las siguientes funciones pertenecen a $L^1(\mathbb{R})$ y cuáles a $L^2(\mathbb{R})$:

$$f_1(x) = \begin{cases} 0 & x < 0 \\ e^{-x} & x \ge 0 \end{cases},\quad f_2(x) = e^{-|x|},$$

$$f_3(x) = \begin{cases} 0 & x \le 0 \\ \tfrac{1}{x} & x > 0 \end{cases},\quad f_4(x) = \begin{cases} 0 & x \le 0 \\ \tfrac{1}{x^2} & x > 0 \end{cases},$$

$$f_5(x) = \begin{cases} 0 & x \le 0 \\ e^{(-1+i)x} & x > 0 \end{cases},\quad f_6(x) = \cos(x).$$

### Ejercicio 5

Determina el producto interno entre cada par de funciones en $L^2([0, 2\pi])$:

$$f_k(x) = \cos(kx),\quad g_k(x) = \sin(kx),$$

con $k \in \mathbb{N}_0$. Es decir, encuentra $\langle f_k, g_n\rangle$, $\langle f_k, f_n\rangle$, $\langle g_k, g_n\rangle$ para todo $k, n = 0, 1, 2, \dots$.

### Ejercicio 6

Determina el producto interno entre cada par de funciones en $L^2([0, 2\pi])$:

$$f_k(x) = e^{ikx},$$

con $k \in \mathbb{N}_0$. Es decir, encuentra $\langle f_k, f_n\rangle$ para todo $k, n \in \mathbb{Z}$.
