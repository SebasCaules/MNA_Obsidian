---
tags: [final, transformaciones-lineales, nucleo-imagen, diagonalizacion, fourier, diferencias-finitas, ecuacion-calor, transformada-fourier]
fuente: raw/Practicas/Modelos_Examenes/MNA_Final_Tema_XI(1).pdf
tipo: final
tema: 11
tiene_resolucion: true
---

> ✅ **Resolución completa (verificada): [[final-tema-11-alt-resolucion]]**

# Examen Final de Métodos Numéricos Avanzados — Tema XI (variante)

> Nota: hay dos archivos rotulados "Tema XI". Este corresponde al segundo (`MNA_Final_Tema_XI(1).pdf`).

## Ejercicio 1

Dada la TL $T : \mathbb{R}^3 \to \mathbb{R}^3 : T(x, y, z) = (-y + z,\ x + y,\ x + z)$

a) Hallar el Núcleo y la Imagen.
b) Decidir si es o no diagonalizable en $\mathbb{R}$.

## Ejercicio 2

a) Hallar el desarrollo en serie de Fourier de la función

$$f : [0, 1] \to \mathbb{R} : f(x) = 1 - x^2,\quad f(x) = f(x + 1)$$

b) Indique a qué converge la serie en $x = 0$ y $x = \dfrac{1}{2}$.

## Ejercicio 3

Dada la ecuación diferencial

$$\frac{\partial u(x, t)}{\partial t} = \frac{\partial^2 u(x, t)}{\partial x^2}$$

a) Desarrollar un esquema de diferencias finitas implícito con 4 nodos internos si

$$u(0, t) = u(1, t) = 0 \quad \text{y} \quad u(x, 0) = x e^{-x}$$

b) Desarrollar un esquema de diferencias finitas implícito con 4 nodos internos si

$$u_x(0, t) = u_x(1, t) = 0 \quad \text{y} \quad u(x, 0) = x + 1$$

## Ejercicio 4

Hallar la Transformada de Fourier de $f(t) = e^{-a |t|}$ si $0 \le t \le 1$, $f(t) = 0$, $a > 0$ en otro punto.
