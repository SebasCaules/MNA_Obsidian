---
tags: [parcial, recuperatorio, transformaciones-lineales, diagonalizacion, fourier, plu, qr]
fuente: raw/Practicas/Modelos_Examenes/MNA_Parcial_Tema_XIII.pdf
tipo: parcial
tema: 13
tiene_resolucion: true
---

> ✅ **Resolución completa (verificada): [[parcial-tema-13-resolucion]]**

# Recuperatorio de Métodos Numéricos Avanzados — Tema XIII

## Ejercicio 1

Sea $T : \mathbb{R}^3 \to \mathbb{R}^3$ una transformación lineal tal que

$$M_{EE}(T) = \begin{pmatrix} 2 & 0 & 0 \\ 0 & h & 0 \\ -1 & 1 & 1 \end{pmatrix}$$

a) Hallar todos los valores de $a, b \in \mathbb{R}$ tal que $\dim(R(T)) < 3$.

*(Nota: el enunciado original menciona variables $a, b$ pero la matriz contiene $h$ — interpretarlo como buscar valores de los parámetros que reducen el rango.)*

b) Hallar $h \in \mathbb{R}$, si existe, para que $T$ no sea diagonalizable.

## Ejercicio 2

Dada la función $f : [0, 1] \to \mathbb{R} : f(t) = t$ y $f(t) = f(t + 1)$.

a) Hallar el desarrollo en serie de Fourier.
b) Indicar a qué converge la serie en $t = 1$ y $t = \dfrac{1}{4}$.

## Ejercicio 3

Dada la Matriz $A = \begin{pmatrix} 0 & -1 \\ 1 & -1 \\ -1 & 0 \end{pmatrix}$

a) Hallar su factorización $PLU$.
b) Hallar su factorización $QR$.
