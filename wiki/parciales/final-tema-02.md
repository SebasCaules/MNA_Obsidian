---
tags: [final, transformaciones-lineales, nucleo-imagen, diagonalizacion, fourier, edo, diferencias-finitas, transformada-fourier]
fuente: raw/Practicas/Modelos_Examenes/MNA_Final_Tema_II.pdf
tipo: final
tema: 2
tiene_resolucion: true
---

> ✅ **Resolución completa (verificada): [[final-tema-02-resolucion]]**

# Examen Final de Métodos Numéricos Avanzados — Tema II

## Ejercicio 1

Dada la TL $T : \mathbb{R}^3 \to \mathbb{R}^3 : T(x, y, z) = (2x - y,\ x + y - z,\ z - x - y)$

a) Hallar el Núcleo y la Imagen.
b) Decidir si es o no diagonalizable en $\mathbb{R}$.

## Ejercicio 2

a) Hallar el desarrollo en serie de Fourier de la función $f(x) = 1 - x$ y $f(x) = f(x + 1)$.
b) Indique a qué converge la serie en $x = 0$ y $x = \dfrac{1}{2}$.

## Ejercicio 3

Considere la siguiente ecuación diferencial ordinaria:

$$\frac{d^2 x}{dt^2} + 2 \frac{dx}{dt} + x = e^{-t^2} \quad x(0) = x'(0)$$

a) Escriba la ecuación como un sistema de orden 1.
b) Plantee un esquema implícito de diferencias finitas. Indique cómo implementa las condiciones iniciales.

## Ejercicio 4

Hallar la Transformada de Fourier de $f(t) = (t - 1)^2$ si $0 \le t \le 1$, $f(t) = 0$ en otro punto.
