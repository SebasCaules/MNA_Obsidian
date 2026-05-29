---
tags: [final, transformaciones-lineales, cambio-base, qr, diferencias-finitas, ecuacion-calor, transformada-fourier]
fuente: raw/Practicas/Modelos_Examenes/MNA_Final_Tema_X.pdf
tipo: final
tema: 10
tiene_resolucion: true
---

> ✅ **Resolución completa (verificada): [[final-tema-10-resolucion]]**

# Examen Final de Métodos Numéricos Avanzados — Tema X

## Ejercicio 1

Dada la TL $T : \mathbb{R}^3 \to \mathbb{R}^3 : T(x, y, z) = (2x + y - z,\ x + 3y - z,\ z - y)$

a) Hallar la Matriz Asociada $M_{BB}$ con $B = \{(0, 0, 1),\ (1, 0, 0),\ (1, -1, 0)\}$.
b) Hallar la descomposición $QR$ de $M_{BB}$.

## Ejercicio 2

Considere el siguiente problema de contorno:

$$\frac{\partial u(x, t)}{\partial t} = \frac{\partial^2 u(x, t)}{\partial x^2} \quad u_x(0, t) = u(1, t) = 0 \quad u(x, 0) = e^{-x^2}$$

a) Plantear un esquema de diferencias finitas implícito de 4 nodos internos.
b) Indique cómo quedan las matrices.

## Ejercicio 3

Hallar la Transformada de Fourier de $f(t) = 1 - |t|$ si $-1 \le t \le 1$, $f(t) = 0$ en otro punto.
