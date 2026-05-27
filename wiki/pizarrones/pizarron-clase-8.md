---
tags: [pizarron, factorizacion-plu, factorizacion-qr, gram-schmidt, sistema-triangular, descomposicion-matricial]
fuente: raw/Practicas/Pizarrones/Clase8.pdf
tipo: escaneo
---

# Pizarrón — Clase 8: Factorizaciones $PA = LU$ y $A = QR$ (Gram-Schmidt)

Dos descomposiciones matriciales fundamentales: $PA = LU$ (con permutaciones) y $QR$ vía Gram-Schmidt. Ambas con ejemplos completos y aplicación a resolver $Ax = b$.

## Página 1 — $PA = LU$: definición y ejemplo

**PLU.** Descomponer una matriz en dos donde una es triangular inferior y la otra triangular superior, con $P$ una matriz de permutaciones:
$$PA = LU.$$

- $P$: matriz de permutaciones.
- $U$: matriz triangular superior.
- $L$: matriz triangular inferior.

**Ejemplo.** $A = \begin{bmatrix} 0 & 0 & 2 \\ -1 & 5 & -2 \\ 3 & 6 & 7 \end{bmatrix}$. Buscar $PA = LU$.

Como el pivote $a_{11} = 0$, permutamos $F_3 \to F_1$:
$$U_0 = \begin{bmatrix} 0 & 0 & 2 \\ -1 & 5 & -2 \\ 3 & 6 & 7 \end{bmatrix} \xrightarrow{F_3 \to F_1} \begin{bmatrix} 3 & 6 & 7 \\ -1 & 5 & -2 \\ 0 & 0 & 2 \end{bmatrix} \xrightarrow{F_2 + \tfrac{1}{3}F_1} \underbrace{\begin{bmatrix} 3 & 6 & 7 \\ 0 & 7 & 1/3 \\ 0 & 0 & 2 \end{bmatrix}}_{U \text{ triangular superior}}$$

Construcción de $L$ con los multiplicadores cambiados de signo y la diagonal igual a 1:
$$L_0 = \begin{bmatrix} 0 & 0 & 0 \\ -1/3 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix} \;\rightarrow\; L = \begin{bmatrix} 1 & 0 & 0 \\ -1/3 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

Permutación $P$ correspondiente al intercambio $F_3 \to F_1$:
$$P_0 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \xrightarrow{F_3 \to F_1} P = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{pmatrix}$$

$$PA = LU \;\Rightarrow\; \begin{pmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{pmatrix}\begin{pmatrix} 0 & 0 & 2 \\ -1 & 5 & -2 \\ 3 & 6 & 7 \end{pmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ -1/3 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} 3 & 6 & 7 \\ 0 & 7 & 1/3 \\ 0 & 0 & 2 \end{bmatrix}$$

## Página 2 — Segundo ejemplo PLU y aplicación

**Ejemplo 2.** $A = \begin{pmatrix} 2 & -2 & 1 \\ -8 & 11 & 5 \\ 4 & -13 & 2 \end{pmatrix}$. Buscar $PLU$.

$$U_0 = \begin{pmatrix} 2 & -2 & 1 \\ -8 & 11 & 5 \\ 4 & -13 & 2 \end{pmatrix} \xrightarrow[F_3 - 2F_1]{F_2 + 4F_1} \begin{pmatrix} 2 & -2 & 1 \\ 0 & 3 & 9 \\ 0 & -9 & 0 \end{pmatrix} \xrightarrow{F_3 - (-3)F_2} \boxed{\begin{pmatrix} 2 & -2 & 1 \\ 0 & 3 & 9 \\ 0 & 0 & 9 \end{pmatrix}}$$

(El pizarrón anota la 3ª fila como $-2 \cdot 9 = -18 \;\to\; +27 = 9$ tras restar $-3F_2$.)

$$L_0 = \begin{bmatrix} 0 & 0 & 0 \\ -4 & 0 & 0 \\ 2 & 0 & 0 \end{bmatrix} \xrightarrow{F_3 + F_2} \begin{bmatrix} 0 & 0 & 0 \\ -4 & 0 & 0 \\ 2 & -3 & 0 \end{bmatrix} \;\Rightarrow\; L = \begin{bmatrix} 1 & 0 & 0 \\ -4 & 1 & 0 \\ 2 & -3 & 1 \end{bmatrix}$$

$$P_0 = I \;\Rightarrow\; P = I \quad \text{(no hubo permutaciones)}.$$

**Aplicación.** Resolver $A\vec x = \vec b$ usando $PLU$ (acceso inversa "implícito"):
$$\begin{cases} 2x_1 + 3x_2 + 4x_3 = 6 \\ 4x_1 + 5x_2 + 10x_3 = 16 \\ 4x_1 + 8x_2 + 2x_3 = 2 \end{cases}, \quad A = \begin{pmatrix} 2 & 3 & 4 \\ 4 & 5 & 10 \\ 4 & 8 & 2 \end{pmatrix}, \quad \vec b = \begin{pmatrix} 6 \\ 16 \\ 2 \end{pmatrix}.$$

$$\det(A) = (20 + 16\cdot 8 + 120) - (80 + 160 + 12) = 128 + 120 - 160 - 12 \neq 0.$$

$\therefore$ Compatible determinado.

## Página 3 — Esquema de resolución $PA = LU$ y eliminación

$$PA = LU \;\to\; A\vec x = \vec b \;\Rightarrow\; PA\vec x = P\vec b \;\Rightarrow\; LU\vec x = P\vec b.$$

Definir $\vec z = U\vec x$ (nuevo vector de incógnitas) y $\tilde{\vec b} = P\vec b$. Entonces
$$L \vec z = \tilde{\vec b} \quad \text{(triangular inferior, fácil de resolver).}$$

Después: $U\vec x = \vec z$ (triangular superior).

Calcular $U$ para $A = \begin{pmatrix} 2 & 3 & 4 \\ 4 & 5 & 10 \\ 4 & 8 & 2 \end{pmatrix}$:
$$U_0 = \begin{pmatrix} 2 & 3 & 4 \\ 4 & 5 & 10 \\ 4 & 8 & 2 \end{pmatrix} \xrightarrow[F_3 - 2F_1]{F_2 - 2F_1} \begin{pmatrix} 2 & 3 & 4 \\ 0 & -1 & 2 \\ 0 & 2 & -6 \end{pmatrix} \xrightarrow{F_3 - (-2)F_2} \begin{pmatrix} 2 & 3 & 4 \\ 0 & -1 & 2 \\ 0 & 0 & -2 \end{pmatrix}$$

$$L_0 = \begin{pmatrix} 0 & 0 & 0 \\ 2 & 0 & 0 \\ 2 & -2 & 0 \end{pmatrix} \;\Rightarrow\; L = \begin{pmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 2 & -2 & 1 \end{pmatrix}, \quad P = I \;\Rightarrow\; A = LU.$$

$L\vec z = \vec b$:
$$\begin{pmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 2 & -2 & 1 \end{pmatrix}\begin{pmatrix} z_1 \\ z_2 \\ z_3 \end{pmatrix} = \begin{pmatrix} 6 \\ 16 \\ 2 \end{pmatrix} \;\Rightarrow\; \begin{cases} z_1 = 6 \\ 2z_1 + z_2 = 16 \;\Rightarrow\; z_2 = 4 \\ 2z_1 - 2z_2 + z_3 = 2 \;\Rightarrow\; z_3 = 2 - 12 + 8 = -2 \end{cases}$$

## Página 4 — Backward sustitución $U\vec x = \vec z$ y arranque QR

$$U\vec x = \vec z \;\Rightarrow\; \begin{pmatrix} 2 & 3 & 4 \\ 0 & -1 & 2 \\ 0 & 0 & -2 \end{pmatrix}\begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} 6 \\ 4 \\ -2 \end{pmatrix}$$

$$\begin{cases} 2x_1 + 3x_2 + 4x_3 = 6 \\ -x_2 + 2x_3 = 4 \\ -2x_3 = -2 \end{cases}$$

$x_3 = 1$; $x_2 = 2x_3 - 4 = 2 - 4 = -2$; $x_1 = (6 - 3(-2) - 4(1))/2 = (6 + 6 - 4)/2 = 4$.

$$\boxed{\;x_1 = 4,\; x_2 = -2,\; x_3 = 1.\;}$$

**Verificación del determinante vía $LU$:**
$$\det(A) = \det(L)\det(U) = 1 \cdot (2)(-1)(-2) = 4.$$

### Factorización $QR$

$$A = QR$$

- $Q$: matriz unitaria (ortogonal), columnas ortonormales: $QQ^T = I$.
- $R$: matriz triangular superior.

Con $Q = (\vec f_1, \vec f_2, \dots)$ donde $\vec f_i$ es la columna $i$-ésima:
$$\langle \vec f_i, \vec f_j\rangle = 0 \;(i \neq j), \quad \langle \vec f_i, \vec f_i\rangle = 1.$$

**Ejemplo (2×2).** $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$, $\vec a_1 = \binom{1}{3}$, $\vec a_2 = \binom{2}{4}$.

$\det(A) = 4 - 6 \neq 0 \;\therefore$ las columnas son LI, $\{\vec a_1, \vec a_2\}$ forma base.

## Página 5 — Gram-Schmidt y QR del ejemplo 2×2

**Algoritmo (Gram-Schmidt).** Para una base $\{\vec a_1, \vec a_2, \dots\}$:
$$\vec u_1 = \vec a_1$$
$$\vec u_2 = \vec a_2 - \operatorname{Proy}_{\vec u_1}(\vec a_2)$$
$$\vec u_3 = \vec a_3 - \operatorname{Proy}_{\vec u_1}(\vec a_3) - \operatorname{Proy}_{\vec u_2}(\vec a_3)$$

Recordatorio:
$$\operatorname{Proy}_{\vec B}(\vec A) = \frac{\langle \vec A, \vec B\rangle}{\langle \vec B, \vec B\rangle}\,\vec B$$

Por construcción, $\langle \vec u_i, \vec u_j\rangle = 0$ para $i \neq j$.

Caso general:
$$\boxed{\;\vec u_K = \vec a_K - \sum_{j=1}^{K-1} \operatorname{Proy}_{\vec u_j}(\vec a_K)\;}$$

Normalizando: $\vec e_i = \dfrac{\vec u_i}{\|\vec u_i\|}$, $\vec e_2 = \dfrac{\vec u_2}{\|\vec u_2\|}$.

**Cálculo para el ejemplo.**
$$\vec u_1 = \vec a_1 = \binom{1}{3}$$
$$\vec u_2 = \vec a_2 - \operatorname{Proy}_{\vec u_1}(\vec a_2) = \binom{2}{4} - \frac{\langle (2,4),(1,3)\rangle}{\langle (1,3),(1,3)\rangle}\binom{1}{3} = \binom{2}{4} - \tfrac{14}{10}\binom{1}{3} = \binom{2}{4} - \tfrac{7}{5}\binom{1}{3} = \binom{3/5}{-1/5}$$

**Verificación:** $\langle \vec u_1, \vec u_2\rangle = \langle (1,3),(3/5,-1/5)\rangle = 3/5 - 3/5 = 0.\;\checkmark$ $\vec u_1 \perp \vec u_2$.

$$\vec e_1 = \frac{\vec u_1}{\sqrt{\langle \vec u_1, \vec u_1\rangle}} = \binom{1}{3}\cdot\tfrac{1}{\sqrt{10}}$$

## Página 6 — Construcción de Q, R y aplicación

$$\vec e_2 = \frac{\vec u_2}{\sqrt{\langle \vec u_2, \vec u_2\rangle}} = \tfrac{1}{5}\binom{3}{-1}\cdot\tfrac{1}{\sqrt{9/25 + 1/25}} = \tfrac{1}{5}\binom{3}{-1}\cdot\tfrac{1}{\sqrt{10/25}} = \tfrac{1}{5}\binom{3}{-1}\cdot\tfrac{5}{\sqrt{10}} = \tfrac{1}{\sqrt{10}}\binom{3}{-1}.$$

$$Q = (\vec e_1, \vec e_2) = \tfrac{1}{\sqrt{10}}\begin{pmatrix} 1 & 3 \\ 3 & -1 \end{pmatrix}.$$

$$A = QR \;\Rightarrow\; Q^T A = \underbrace{Q^T Q}_I R \;\Rightarrow\; R = Q^T A.$$

$$R = \tfrac{1}{\sqrt{10}}\begin{pmatrix} 1 & 3 \\ 3 & -1 \end{pmatrix}\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = \tfrac{1}{\sqrt{10}}\begin{pmatrix} 10 & 14 \\ 0 & 2 \end{pmatrix}.$$

$$\boxed{\;A = \underbrace{\tfrac{1}{\sqrt{10}}\begin{pmatrix} 1 & 3 \\ 3 & -1 \end{pmatrix}}_{Q}\,\underbrace{\tfrac{1}{\sqrt{10}}\begin{pmatrix} 10 & 14 \\ 0 & 2 \end{pmatrix}}_{R}\;}$$

Verificar $Q^T Q = I$ y $Q Q^T = I$.

**Aplicación a $A\vec x = \vec b$:**
$$Q\,R\,\vec x = \vec b \;\Rightarrow\; Q\,\vec z = \vec b \;\Rightarrow\; \vec z = Q^T \vec b = \tilde{\vec b} \;\Rightarrow\; R\,\vec x = \tilde{\vec b}.$$

Sistema escalonado (triangular superior), fácil de resolver hacia atrás.

## Página 7 — Ejemplo QR con $A \in \mathbb{R}^{3\times 2}$

$$A = \begin{pmatrix} 1 & 2 \\ 2 & 3 \\ 2 & 1 \end{pmatrix}, \quad \vec a_1 = \binom{1}{2}{2}, \quad \vec a_2 = \binom{2}{3}{1}.$$

$A \in \mathbb{R}^{3\times 2}, Q \in \mathbb{R}^{3\times 2}, R \in \mathbb{R}^{2\times 2}$.

$\vec u_1 = \vec a_1 = (1, 2, 2)^\top$.

$$\vec u_2 = \vec a_2 - \operatorname{Proy}_{\vec u_1}(\vec a_2) = \binom{2}{3}{1} - \frac{\langle (2,3,1),(1,2,2)\rangle}{\langle (1,2,2),(1,2,2)\rangle}\binom{1}{2}{2} = \binom{2}{3}{1} - \frac{2 + 6 + 2}{1 + 4 + 4}\binom{1}{2}{2} = \binom{2}{3}{1} - \tfrac{10}{9}\binom{1}{2}{2}$$

(El pizarrón anota $- (1 + 6 + 2)/(1 + 4 + 4) = -9/9 = -1$ — revisar; el resultado mostrado es $\vec u_2 = (8/9, 7/9, -8/9)$ aprox. Se reporta $\vec u_2 = (0, -1, 1)/\cdots$ — versión final $\vec u_2 \propto (0, -1, 1)$ tras simplificar.)

$$\boxed{\;\vec u_1 = (1, 2, 2),\;\; \vec u_2 = (0, -1, 1)\;\text{(tras simplificar)}\;}$$

Verificar ortogonalidad: $\langle \vec u_1, \vec u_2\rangle = 0 - 2 + 2 = 0. \;\checkmark$

$\vec e_1 = \vec u_1 / \|\vec u_1\| = (1, 2, 2)/3$; $\vec e_2 = \vec u_2 / \|\vec u_2\| = (0, -1, 1)/\sqrt{2}$.

$$Q = \begin{bmatrix} 1/3 & 0 \\ 2/3 & -1/\sqrt{2} \\ 2/3 & 1/\sqrt{2} \end{bmatrix}$$

$$R = Q^T A = \begin{bmatrix} 1/3 & 2/3 & 2/3 \\ 0 & -1/\sqrt{2} & 1/\sqrt{2} \end{bmatrix}\begin{bmatrix} 1 & 2 \\ 2 & 3 \\ 2 & 1 \end{bmatrix} = \begin{bmatrix} 3 & 3 \\ 0 & \sqrt{2} \end{bmatrix} \quad \text{(redondeado en pizarrón)}.$$

$$Q^T Q = \begin{bmatrix} \cdots \end{bmatrix} = I_{2\times 2}.$$

## Página 8 — Tercer ejemplo (3×3): GS y QR

$$A = \begin{bmatrix} 1 & -2 & 1 \\ -1 & 3 & 2 \\ 1 & 1 & -4 \end{bmatrix}, \quad \vec a_1 = (1, -1, 1),\; \vec a_2 = (-2, 3, 1),\; \vec a_3 = (1, 2, -4).$$

$$\vec u_1 = \vec a_1 = (1, -1, 1).$$

$$\vec u_2 = \vec a_2 - \frac{\langle \vec a_2, \vec u_1\rangle}{\langle \vec u_1, \vec u_1\rangle}\vec u_1 = (-2, 3, 1) - \frac{-2 - 3 + 1}{1 + 1 + 1}(1, -1, 1) = (-2, 3, 1) - \tfrac{-4}{3}(1, -1, 1) = (-2, 3, 1) + \tfrac{4}{3}(1, -1, 1)$$
$$= (-2 + 4/3,\; 3 - 4/3,\; 1 + 4/3) = (-2/3,\; 5/3,\; 7/3) \quad (\text{en el pizarrón se trunca distinto: } (0, 1, 1)).$$

> ⚠️ El pizarrón consigna el resultado simplificado $\vec u_2 = (0, 1, 1)$ tras ajustar el factor; cuenta intermedia: $\vec u_2 = (-2, 3, 1) - 6/3 (1, -1, 1) = (-2 - 2, 3 + 2, 1 - 2) \neq$ — la transcripción literal del pizarrón da $\vec u_2 = (0, 1, 1)$.

$$\vec u_3 = \vec a_3 - \operatorname{Proy}_{\vec u_1}(\vec a_3) - \operatorname{Proy}_{\vec u_2}(\vec a_3) = (1, 2, -4) - \tfrac{-5}{3}(1, -1, 1) - \tfrac{-2}{2}(0, 1, 1) = (1, 2, -4) + \tfrac{5}{3}(1, -1, 1) + (0, 1, 1)$$
$$= \tfrac{4}{3}(2, -1, -1) \quad \text{(según pizarrón)}.$$

> ⚠️ Tarea (anotada por el profe): verificar $\langle \vec u_1, \vec u_2\rangle, \langle \vec u_1, \vec u_3\rangle, \langle \vec u_2, \vec u_3\rangle = 0$.

Normalización:
$$\vec e_1 = \tfrac{1}{\sqrt{3}}\binom{1}{-1}{1}, \quad \vec e_2 = \tfrac{1}{\sqrt{2}}\binom{0}{1}{1}, \quad \vec e_3 = \tfrac{1}{\sqrt{6}}\binom{2}{-1}{-1} \text{ (con signo según pizarrón } \binom{\sqrt{4/6}}{1/\sqrt{6}}{-1/\sqrt{6}}\text{).}$$

## Página 9 — Cierre QR (3×3): $Q$, $R$, verificaciones

$$Q = \begin{bmatrix} 1/\sqrt{3} & 0 & \sqrt{2}/\sqrt{3} \\ -1/\sqrt{3} & 1/\sqrt{2} & 1/\sqrt{6} \\ 1/\sqrt{3} & 1/\sqrt{2} & -1/\sqrt{6} \end{bmatrix}$$

$$R = Q^T A = \dots \quad \text{(no calculado en el pizarrón, sólo planteado).}$$

**Verificar:** $Q^T Q = I$ y $Q Q^T = I$.
