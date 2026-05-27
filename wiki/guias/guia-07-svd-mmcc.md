---
tags: [guia, svd, pseudoinversa, mmcc]
fuente: raw/Practicas/Guias_TP2026/Guia_TP_VII_MNA_ITBA_2025.pdf
unidad: VII
---

# Guía de Trabajos Prácticos VII — Descomposición SVD y mínimos cuadrados

## Descomposición SVD

### Ejercicio 1

Sea la matriz $A$:

$$A = \begin{pmatrix} 0 & 3 & 3 \\ 4 & 1 & -1 \\ 4 & 1 & -1 \\ 0 & 3 & 3 \end{pmatrix}$$

Verifique que puede descomponerse en valores singulares como:

$$\begin{pmatrix} 0 & 3 & 3 \\ 4 & 1 & -1 \\ 4 & 1 & -1 \\ 0 & 3 & 3 \end{pmatrix} = \frac{1}{2}\begin{pmatrix} 1 & -1 & -1 & 1 \\ 1 & 1 & 1 & 1 \\ 1 & 1 & -1 & -1 \\ 1 & -1 & 1 & 1 \end{pmatrix} \begin{pmatrix} 6 & 0 & 0 \\ 0 & 6 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} \frac{1}{3}\begin{pmatrix} 0 & 2 & 2 & 1 \\ 1 & 2 & -1 & -2 \\ 1 & -2 & 2 & a \end{pmatrix}$$

O como

$$\begin{pmatrix} 0 & 3 & 3 \\ 4 & 1 & -1 \\ 4 & 1 & -1 \\ 0 & 3 & 3 \end{pmatrix} = \frac{1}{2}\begin{pmatrix} 1 & -1 \\ 1 & 1 \\ 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} 6 & 0 \\ 0 & 6 \end{pmatrix} \frac{1}{3}\begin{pmatrix} 0 & 1 & 2 & 2 & 1 \\ 1 & 2 & 3 & -1 & -2 \end{pmatrix}$$

Ver resolución detallada en [[../resueltos/resueltos-svd]].

### Ejercicio 2

Encuentre la descomposición en valores singulares y la pseudo-inversa de las siguientes matrices:

$$A = \begin{pmatrix} 1 \\ 3 \end{pmatrix},\quad B = \begin{pmatrix} 1 & 1 \\ 1 & 0 \\ 0 & 1 \end{pmatrix},\quad C = \begin{pmatrix} 3 & 2 & 2 \\ 2 & 3 & -2 \end{pmatrix},\quad D = \begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}$$

### Ejercicio 3

Considera las matrices:

$$A = \begin{pmatrix} -2 & 11 \\ -10 & 5 \end{pmatrix},\quad B = \begin{pmatrix} -1 & 2 & 1 \\ 3 & 4 & 7 \\ 5 & 6 & 11 \\ 8 & 9 & 17 \end{pmatrix}$$

Halla, mediante la descomposición SVD:

- a) Su rango
- b) Su matriz inversa/pseudoinversa
- c) Su determinante
- d) Su norma 1, 2 y de Frobenius

## Mínimos cuadrados

### Ejercicio 4

Considera el conjunto de datos que se presentan en la tabla 1. Se desean ajustar estos puntos, usando el método de cuadrados mínimos, a una línea recta:

$$y = a_1 x + a_0$$

Encuentra el valor de $a_0$ y $a_1$.

| $x$ | $y$ | $x$ | $y$ | $x$ | $y$ |
|---|---|---|---|---|---|
| 1 | 1.2 | 1 | 1.1 | 0 | 6.2 |
| 2 | 3.9 | 2 | 3.9 | $\pi/4$ | 2.3 |
| 3 | 4.2 | 3 | 8.8 | $\pi/2$ | -1.95 |
| 4 | 5.5 | 4 | 15.5 | $3\pi/4$ | 0.4 |
| 5 | 6.9 | 5 | 23.0 | $\pi$ | 2.01 |

### Ejercicio 5

Considere el conjunto de datos del inciso anterior. Se los desea ajustar, usando el método de cuadrados mínimos, a la siguiente función:

$$y = a_2 x^2 + a_1 x + a_0$$

### Ejercicio 6

Los datos se quieren ajustar por la función:

$$y = a_0 + a_1 \cos(x) + a_2 \cos(2x)$$

Hallar los valores de los $a_j$.

### Ejercicio 7

En el fichero `pressure.dat` se encuentran los datos de: presión máxima $p_s$, edad $e$ y masa corporal $m$ de 11 pacientes estadounidenses. Se quiere encontrar una correlación del tipo:

$$p = p_0 + p_1 e + p_2 m$$

¿Cuáles son los valores de $p_0$, $p_1$ y $p_2$? Los datos son una modificación del dataset que se aloja en `https://college.cengage.com/mathematics/brase/understandable_statistics/7e/students/datasets/mlr/frames/`.

### Ejercicio 8

Es importante conocer el volumen de madera aprovechable de un árbol, a partir de su diámetro en el fichero se encuentran datos de diámetro (en pulgadas) y volumen aprovechable (en pies cúbicos) se establece una relación funcional del tipo:

$$V = p_1 x^{p_2}$$

Determina el valor de $p_1$ y $p_2$. Problema tomado de la página `https://online.stat.psu.edu/stat501/lesson/9/9`.

### Ejercicio 9

La descomposición SVD puede ser empleada para eliminar ruido de datos medidos. Considere el dataset que se encuentra en el fichero `denoise.dat`. Calcule el error cuadrático medio de las mediciones:

$$\text{MSE} = \frac{1}{N}\sum_{i=1}^{N} (y_i - \hat{y}_i)^2$$

donde $y_i$ es el valor medido y $\hat{y}_i$ el valor estimado por una regresión lineal. Construya la matriz de datos $D = [x;\, y]$ haga la composición SVD y construya la matriz de datos truncada con un sólo valor singular y ajústelos por una recta, calcule el MSE en este caso. ¿Qué puede comentar?

### Ejercicio 10

La fotografía que dio lugar a la "invención" del formato jpg es la de la suiza Lena. Has una versión comprimida de ella empleando la técnica de SVD truncado; decide "a ojo" cuántos valores singulares serían requeridos para no perder excesiva calidad y calcula la compresión que se logra. Si no se le ocurre a ojo considere que la matriz truncada contenga un 90% del contenido energético de los modos.

> [Figura: Imagen de Lena, original y reconstruida con $k$ valores singulares para distintos $k$.]
