---
tags: [parcial, iip, fourier, serie-trigonometrica, transformada-fourier, diferencias-finitas, ecuacion-calor]
fuente: raw/Practicas/Modelos_Examenes/MNA_IIP_Tema_IV.pdf
tipo: iip
tema: 4
tiene_resolucion: true
---

> ✅ **Resolución completa (verificada): [[iip-tema-04-resolucion]]**

# Segundo Parcial de Métodos Numéricos Avanzados — Tema IV

## Ejercicio 1

Sea la función $x(t) = t^2$ en el intervalo $(0, 2\pi)$, $x(t) = x(t + 2\pi)$.

a) Hallar la Serie Trigonométrica de Fourier de $x(t)$.
b) Usando el desarrollo hallado en a) hallar el desarrollo de $y(t) = x'(t)$.

## Ejercicio 2

Dada la función $x(t) = t^2$ si $0 \le t \le 2\pi$ y $x(t) = 0$ si $t < 0$ y $t > 2\pi$. Hallar su Transformada de Fourier.

## Ejercicio 3

Dada la ecuación diferencial

$$\frac{\partial u(x, t)}{\partial t} = \frac{\partial^2 u(x, t)}{\partial x^2}$$

a) Desarrollar un esquema de diferencias finitas implícito con 4 nodos internos si

$$u(0, t) = u(1, t) = 0 \quad \text{y} \quad u(x, 0) = \sen(x)$$

b) Desarrollar un esquema de diferencias finitas implícito con 4 nodos internos si

$$u_x(0, t) = u(1, t) = 0 \quad \text{y} \quad u(x, 0) = \cos(x)$$
