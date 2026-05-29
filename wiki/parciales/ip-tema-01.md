---
tags: [parcial, ip, transformaciones-lineales, diagonalizacion, svd, qr, cuadrados-minimos, subespacios]
fuente: raw/Practicas/Modelos_Examenes/MNA_IP_Tema_I.pdf
tipo: ip
tema: 1
tiene_resolucion: true
---

> ✅ **Resolución completa (verificada): [[ip-tema-01-resolucion]]**

# Primer Parcial de Métodos Numéricos Avanzados — Tema I

## Ejercicio 1

Dada la Transformación Lineal $T : \mathbb{R}^3 \to \mathbb{R}^3 : T(x, y, z) = (2x - y + z,\ x + y - z,\ z + y - x)$

a) Hallar el Núcleo y la Imagen
b) Hallar $(x, y, z)$, si existe, de modo que $T(x, y, z) = (1, 1, -2)$

## Ejercicio 2

Sea $F : \mathbb{R}^3 \to \mathbb{R}^3$ una transformación lineal tal que

$$M(F)_{EE} = \begin{pmatrix} 1 & 0 & 1 \\ 0 & k & 1 \\ 0 & 9 & k \end{pmatrix}$$

a) Hallar todos los valores de $k$ para los cuales $F$ es diagonalizable.
b) Para $k = 3$ hallar una base $B$ de $\mathbb{R}^3$ tal que $M(F)_{BB}$ sea diagonal y dar la expresión de $M(F)_{BB}$.

## Ejercicio 3

Considere la matriz

$$A = \begin{pmatrix} 0.92 & 1.44 \\ 1.44 & 0.08 \end{pmatrix}$$

a) Realizar la descomposición en valores singulares.
b) Realizar la factorización QR.

## Ejercicio 4

Dado el siguiente conjunto de datos

| x | y |
|---|---|
| $0$ | $+0.97$ |
| $\pi/4$ | $+1.42$ |
| $\pi$ | $-1.04$ |

Usando cuadrados mínimos, realice el ajuste de los datos experimentales a la ecuación

$$y(x) = a \cos(x) + b \sin(x)$$

Utilice descomposición QR para resolver el problema de cuadrados mínimos.

## Ejercicio 5

Sea $H = \langle x^2 + 2x - 1,\ x^2 + x + a^2 - 4,\ x^2 - 2x + 3 \rangle \subset P_2$. Determinar todos los valores de $a$ si existen para que $\dim(H) = 2$ y $x^2 + a - 1 \in H$.
