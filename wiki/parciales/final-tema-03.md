---
tags: [final, transformaciones-lineales, cambio-base, diagonalizacion, fourier, edo, diferencias-finitas, transformada-fourier]
fuente: raw/Practicas/Modelos_Examenes/MNA_Final_Tema_III.pdf
tipo: final
tema: 3
tiene_resolucion: true
---

> ✅ **Resolución completa (verificada): [[final-tema-03-resolucion]]**

# Examen Final de Métodos Numéricos Avanzados — Tema III

## Ejercicio 1

Dada la TL $T : \mathbb{R}^3 \to \mathbb{R}^3 : T(x, y, z) = (x + 3y,\ x + y - z,\ z - x - y)$

a) Hallar la Matriz Asociada $M_{BB}$ con $B = \{(0, 0, 1),\ (1, 0, 0),\ (1, -1, 0)\}$.
b) Decidir si es o no diagonalizable en $\mathbb{R}$.

## Ejercicio 2

a) Hallar el desarrollo en serie de Fourier de la función $f(x) = x - x^2$ y $f(x) = f(x + 1)$.
b) Indique a qué converge la serie en $x = 0$ y $x = \dfrac{1}{2}$.

## Ejercicio 3

Considere la siguiente ecuación diferencial ordinaria:

$$\frac{d^2 x}{dt^2} + \frac{dx}{dt} + 3 x = \cos(t^2 + 1) \quad x(0) = x'(0) = 0$$

a) Escriba la ecuación como un sistema de orden 1.
b) Plantee un esquema implícito de diferencias finitas. Indique cómo implementa las condiciones iniciales.

## Ejercicio 4

Hallar la Transformada de Fourier de $f(t) = t - t^2$ si $0 \le t \le 1$, $f(t) = 0$ en otro punto.
