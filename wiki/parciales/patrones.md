---
tags: [parciales, analisis-transversal, patrones, meta]
fuente: raw/Practicas/Modelos_Examenes/
tipo: analisis
---

# Patrones transversales — Modelos de exámenes MNA

Análisis transversal sobre los 30 PDFs procesados:

- **Primer Parcial (IP)**: 9 temas (I–IX). 3 con resolución oficial (I, V, IX).
- **Segundo Parcial (IIP)**: 5 temas (I, III, IV, V, VI). 0 resoluciones.
- **Parcial recuperatorio**: 1 (Tema XIII).
- **Finales**: 13 archivos cubriendo temas I–XI, XIV (XI tiene dos variantes). 0 resoluciones.

## 1. Frecuencia por tipo de ejercicio

### En IPs (9 temas)

| Tipo de ejercicio | Apariciones en IPs | Notas |
|---|---|---|
| Transformación lineal con matriz/regla → núcleo, imagen, dim | 9/9 | Aparece en TODOS los IP, casi siempre como Ej. 1 |
| Análisis de diagonalización con parámetro $k$ | 7/9 | Polinomio característico + casos |
| Factorización QR | 6/9 | Casi siempre como Ej. 2 o Ej. 3 |
| Factorización PLU | 4/9 | Suele ir junto a QR |
| Descomposición SVD | 3/9 | Más típico de finales que de IPs |
| Cuadrados mínimos vía QR | 2/9 | Solo I y II |
| Subespacios de matrices/polinomios + base + coordenadas | 3/9 | I (P2), V (R2×2), V (subespacio) |
| Independencia lineal con parámetros | 1/9 | Tema VI |
| Cambio de base ($M_{EB}$, $M_{BB}$) | 2/9 | IV y VII |
| Series de Fourier (de funciones absolutas) | 2/9 | VII (\|cos\|), VIII (\|sen\|) |

### En IIPs (5 temas)

| Tipo de ejercicio | Apariciones |
|---|---|
| Serie trigonométrica de Fourier de función periódica | 5/5 |
| Transformada de Fourier de pulso/decaimiento | 5/5 |
| Esquema de diferencias finitas implícito (4 nodos) — calor / onda / convección | 4/5 (todos salvo I/III donde se reemplaza por exponencial/laboratorio) |
| Serie exponencial de Fourier + forma de laboratorio | 2/5 (Temas I, III) |
| Uso del desarrollo de Fourier para probar identidades | 3/5 |

### En Finales (13 archivos)

| Tipo de ejercicio | Apariciones |
|---|---|
| TL $T : \mathbb{R}^3 \to \mathbb{R}^3$ → núcleo, imagen, diagonalizable | 9/13 |
| Serie de Fourier de función lineal/cuadrática + convergencia puntual | 9/13 |
| Factorización (QR, SVD o PLU) de matriz pequeña | 9/13 |
| Transformada de Fourier de pulso o función con soporte compacto | 7/13 |
| Esquema implícito de diferencias finitas (4 nodos) | 6/13 |
| EDO 2do orden → sistema de orden 1 + diferencias finitas | 3/13 (Temas I, II, III) |
| Cambio de base $M_{BB}$ con base no canónica | 3/13 (III, IX, X) |
| TL no estándar (polinomios, matrices) | 2/13 (XI: $T(A) = A - A^T$; XIV: $P_2 \to \mathbb{R}^3$) |

## 2. Estructura típica de un IP

**Cantidad de ejercicios**: entre 3 y 5 (la mayoría tiene 3 o 5).

**Orden canónico**:

1. **Ejercicio 1 — Transformación Lineal**: dada por regla $T(x,y,z) = (\ldots)$ o por matriz con parámetro $k$. Pide núcleo, imagen, antiimagen de un vector o condiciones sobre rango/dim del núcleo.
2. **Ejercicio 2 — Diagonalización con parámetro**: matriz $3 \times 3$ con un $k$. Pide hallar los $k$ que la hacen diagonalizable y luego diagonalizar para un valor concreto.
3. **Ejercicio 3 — Factorización matricial**: QR + PLU (o QR + SVD). Matriz $2 \times 2$ o $3 \times 3$ con entradas decimales o enteras.
4. *(Si el IP tiene 5 ejercicios)* **Ejercicio 4 — Cuadrados mínimos**: ajuste a $y = a\,f(x) + b\,g(x)$ resuelto vía QR. 3 puntos típicos.
5. *(Si el IP tiene 5 ejercicios)* **Ejercicio 5 — Subespacio con parámetro**: $H \subset P_2$ o $H \subset \mathbb{R}^{2\times 2}$ con ecuaciones lineales. Pide base, dimensión, coordenadas, o valores del parámetro para que un vector pertenezca.

**Peso aproximado**: como todos los ejercicios suman la calificación con casillas de igual ancho (`1 | 2 | 3 | 4 | 5`), se asume peso uniforme ≈ 20% c/u (en parciales de 5) o ≈ 33% c/u (en parciales de 3).

## 3. Estructura típica de un IIP

**Cantidad de ejercicios**: siempre 3.

**Orden canónico**:

1. **Ejercicio 1 — Serie trigonométrica de Fourier** de una función periódica concreta (exponencial, polinómica o sinusoidal), con un inciso b) que pide:
   - O bien usar el desarrollo para probar una identidad numérica (Temas I, III).
   - O bien derivar la serie para obtener el desarrollo de $x'(t)$ (Temas IV, V, VI).
2. **Ejercicio 2 — Transformada de Fourier** de una función con soporte compacto o exponencial decaída (Temas I y III combinan también serie exponencial + forma de laboratorio).
3. **Ejercicio 3 — Diferencias finitas implícitas** sobre una EDP (calor, onda o convección-difusión) con 4 nodos internos y dos pares de condiciones de borde distintas.

**Peso aproximado**: ≈ 33% c/u.

## 4. Top 10 tipos de ejercicio más comunes (todo el dataset)

| # | Tipo | Apariciones | Ejemplo concreto |
|---|---|---|---|
| 1 | TL $\mathbb{R}^3 \to \mathbb{R}^3$ → núcleo + imagen / decidir si diagonaliza | 18+ | Final Tema I, Ej. 1: $T(x,y,z) = (2x-y, x+y-z, z)$ |
| 2 | Serie trigonométrica de Fourier de función periódica de período 1 | 11 | Final Tema II, Ej. 2: $f(x) = 1-x$, $f(x) = f(x+1)$ |
| 3 | Diagonalización con parámetro $k$ y análisis por casos | 10 | IP Tema I, Ej. 2: matriz $3 \times 3$ con $k$, casos $k = -2, 4$ |
| 4 | Factorización QR de matriz $2 \times 2$ o $3 \times 3$ | 9 | IP Tema VIII, Ej. 2 |
| 5 | Transformada de Fourier de pulso ($f$ no nula en $[0,1]$) | 8 | Final Tema III, Ej. 4: $f(t) = t - t^2$ en $[0,1]$ |
| 6 | Diferencias finitas implícitas para EDP del calor con 4 nodos internos | 7 | Final Tema V, Ej. 3: $u_t = u_{xx}$, dos juegos de condiciones |
| 7 | Factorización SVD | 6 | Final Tema XI, Ej. 3: $A_{3 \times 2}$ |
| 8 | Factorización PLU | 5 | Parcial Tema XIII, Ej. 3 |
| 9 | Cuadrados mínimos resueltos por QR | 2 | IP Tema I, Ej. 4: $y = a\cos x + b\sen x$, 3 puntos |
| 10 | EDO 2do orden → sistema de orden 1 + diferencias finitas implícitas | 3 | Final Tema I, Ej. 3: Duffing $\ddot x + \delta \dot x + \beta x + \alpha x^3 = \gamma \cos(\omega t + \phi)$ |

## 5. Ejercicios "tipo" que se repiten con variaciones

### 5.1. La matriz $\begin{pmatrix} 2 & 8 & k \\ -1 & -4 & 0 \\ k+3 & 12 & 2k \end{pmatrix}$

Aparece **idéntica** en:
- IP Tema III, Ej. 1
- IP Tema VI, Ej. 1
- Final Tema VIII, Ej. 1 (escrito como regla en lugar de matriz)

Pide siempre: $k$ tal que $\dim R(T) = 1$ o base de $N(T)$ con $k = 0$.

### 5.2. La matriz $A = \begin{pmatrix} 1 & 0 & 0 \\ 2 & -1 & 0 \\ -4 & 0 & -1 \end{pmatrix}$

Aparece en:
- IP Tema VI, Ej. 2 (diagonalizar, hallar base $B$ para $M(T)_{BB} = \diag(1, -1, -1)$)
- Final Tema IV (titulado "Tema VII" internamente), Ej. 3 (QR + SVD + PLU)
- Final Tema VII tiene una TL equivalente $T(x,y,z) = (kx, 2x-2y-z, -2x+5y+4z)$

### 5.3. La matriz $A = \begin{pmatrix} 0.92 & 1.44 \\ 1.44 & 0.08 \end{pmatrix}$

Aparece en:
- IP Tema I, Ej. 3 (SVD + QR)
- Final Tema I, Ej. 4 (SVD + diagonalización)

### 5.4. La matriz $A = \begin{pmatrix} 2 & k-2 & 0 \\ 0 & 3 & k-1 \\ 0 & 0 & 3 \end{pmatrix}$

Aparece en:
- IP Tema III, Ej. 2 (diagonalización + base de autovectores con $k = 0$)
- Final Tema XIV, Ej. 2 (diagonalización + resolver $A^T A X = 0$ con $k = 2$)

### 5.5. Base $B = \{(0, 0, 1), (1, 0, 0), (1, -1, 0)\}$

Repite en:
- Final Tema III, Ej. 1 — para hallar $M_{BB}$ y diagonalizar.
- Final Tema IX, Ej. 1 — para hallar $M_{BB}$ y SVD.
- Final Tema X, Ej. 1 — para hallar $M_{BB}$ y QR.

### 5.6. Base $B = \{(0, 1, -1), (0, 0, 1), (1, 1, 0)\}$

Repite en:
- IP Tema IV, Ej. 1 — antiimagen $(0, 2, 1)$.
- IP Tema VII, Ej. 2 — exactamente la misma matriz y antiimagen.

### 5.7. Función $f(x) = 1 - x$ con $f(x) = f(x+1)$

Aparece en al menos 5 finales (II, IV/VII, VI, VII y como variante en V con $1-x^2$ y XI(1)). El inciso b) siempre pide convergencia en $x = 0$ y $x = 1/2$.

### 5.8. Ecuación del calor $u_t = u_{xx}$ con esquema implícito de 4 nodos

Repite en IIP IV, IIP VI, Final V, Final VI, Final IX, Final X, Final XI(1). Las variantes son:
- Las condiciones de borde: Dirichlet en ambos lados ($u = 0$), mixto ($u_x = 0$ + $u = 0$), Neumann puro ($u_x = 0$ en ambos lados).
- La condición inicial: $\sen(x)$, $\cos(x)$, $e^{-x}\sen x$, $x^2$, $xe^{-x}$, $|x|$, $e^{-x^2}$.

### 5.9. EDO 2do orden → sistema de orden 1

Repite en Final I (Duffing forzado), Final II (oscilador amortiguado con forzante $e^{-t^2}$), Final III ($\ddot x + \dot x + 3x = \cos(t^2+1)$). Siempre piden:
1. Reescribirla como sistema de primer orden.
2. Esquema implícito + cómo se cargan las condiciones iniciales.

### 5.10. Transformada de Fourier de pulso polinómico

Repite con variantes: $(t-1)^2$ (Final II), $t - t^2$ (Final III), $t^2 - t$ (Final IX), $1 - |t|$ (Final X), $e^{-a|t|}$ con soporte truncado (Final XI(1)), $e^{-2|t|+1}$ (Final VI), $e^{-|t-1|}$ (Final V).

## 6. Observaciones operativas

- **Temas IIP I y III son casi idénticos**: cambia solo la función del Ej. 1 ($e^t$ vs $t + 1$); Ej. 2 y 3 son exactamente iguales.
- **Temas IIP V y VI**: misma estructura, cambian la función ($\cos$ vs $\sen$), la transformada del Ej. 2 y la EDP del Ej. 3 (onda vs convección-difusión).
- **Hay una errata en el filename oficial**: `MNA_IP_Tema_V_Resoloucion.pdf` (sic).
- **Conflicto de numeración**: `MNA_Final_Tema_IV.pdf` está internamente rotulado como "Tema VII" — preservé el nombre de archivo pero anoté el conflicto.
- **Dos archivos rotulados como "Final Tema XI"** (`MNA_Final_Tema_XI.pdf` y `MNA_Final_Tema_XI(1).pdf`) con contenidos diferentes. Se guardaron como `final-tema-11.md` y `final-tema-11-alt.md`.
- **Resoluciones disponibles**: sólo 3 (IP I completa, IP V completa, IP IX truncada al primer renglón del Ej. 3).

## 7. Recomendación de prioridades para el "parcial central"

Si el "parcial central" cubre IP + IIP, los ejercicios más probables son:

1. TL en $\mathbb{R}^3$ con matriz parametrizada → núcleo/imagen/diagonalización (probabilidad muy alta).
2. Factorización matricial (QR casi seguro; SVD/PLU como alternativas).
3. Serie trigonométrica de Fourier con un inciso b) (convergencia puntual o derivación).
4. Esquema implícito de diferencias finitas para EDP del calor con 4 nodos internos.
5. Subespacio con parámetro (típico Ej. 5 de IP de 5 ejercicios).

Las matrices que más se repiten (ver §5) son candidatas de alta probabilidad.
