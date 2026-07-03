---
tags: [parcial, iip, fourier, serie-trigonometrica, transformada-fourier, diferencias-finitas, ecuacion-onda]
fuente: raw/Practicas/Modelos_Examenes/MNA_IIP_Tema_V.pdf
tipo: iip
tema: 5
tiene_resolucion: true
---

> ✅ **Resolución completa (verificada): [[iip-tema-05-resolucion]]**

# Segundo Parcial de Métodos Numéricos Avanzados — Tema V

## Ejercicio 1

Sea la función $x(t) = \cos(t)$ en el intervalo $\left(-\dfrac{\pi}{4}, \dfrac{\pi}{4}\right)$, $x(t) = x(t + \pi/2)$.

a) Hallar la Serie Trigonométrica de Fourier de $x(t)$.
b) Usando el desarrollo hallado en a) hallar el desarrollo de $y(t) = x'(t)$.

## Ejercicio 2

Dada la función $x(t) = e^{-2|t|}$. Hallar su Transformada de Fourier.

## Ejercicio 3

Dada la ecuación diferencial

$$\frac{\partial^2 u(x, t)}{\partial t^2} = \frac{\partial^2 u(x, t)}{\partial x^2}$$

a) Desarrollar un esquema de diferencias finitas implícito con 4 nodos internos si

$$u(0, t) = u(1, t) = 0 \quad \text{y} \quad u(x, 0) = \sen(x),\quad u_t(x, 0) = 0$$

b) Desarrollar un esquema de diferencias finitas implícito con 4 nodos internos si

$$u_x(0, t) = u(1, t) = 0 \quad \text{y} \quad u(x, 0) = \cos(x),\quad u_t(x, 0) = x$$
