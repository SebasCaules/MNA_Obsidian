---
tags: [guia, fourier, series]
fuente: raw/Practicas/Guias_TP2026/Guia_TP_VIII_MNA_ITBA_2025.pdf
unidad: VIII
---

# Guía de Trabajos Prácticos VIII — Serie de Fourier

## Ejercicio 1

De ser posible, encuentre el período y la frecuencia fundamental de las siguientes funciones:

- a) $\cos\left(10\pi t + \tfrac{\pi}{6}\right)$
- b) $\sin\left(17\pi t + \tfrac{\pi}{4}\right)$
- c) $2\cos\left(10\pi t + \tfrac{\pi}{6}\right) + 5\sin\left(17\pi t + \tfrac{\pi}{4}\right)$
- d) $\cos\left(\sqrt{2\pi}\, t\right)$
- e) $\cos\left(\sqrt{2}\, t\right)$
- f) $24\cos\left(\sqrt{2\pi}\, t\right) + 32\cos\left(\sqrt{2}\, t\right)$

Grafica las funciones del ejercicio anterior para comprobar tu resultado.

## Ejercicio 2

Demuestre que, si una función $f(t)$ es periódica con período $T$, entonces para todo $a, b \in \mathbb{R}$:

$$\int_{-T/2}^{T/2} f(t)\, dt = \int_{a}^{a+T} f(t)\, dt;\quad \int_{a}^{b} f(t)\, dt = \int_{a+T}^{b+T} f(t)\, dt$$

## Ejercicio 3

Sea $f(t)$ periódica con período $T$. Encuentra un ejemplo en el cual la "primitiva"

$$y(t) = \int_{0}^{t} f(u)\, du$$

no sea periódica.

## Ejercicio 4

Encuentre la serie trigonométrica de las siguientes funciones:

**a)** $x_1(t) = \cos^2(t)$

**b)** Onda cuadrada:

$$x_2(t) = \begin{cases} A & \text{si } t \in \left[0, \tfrac{T}{2}\right) \\ -A & \text{si } t \in \left[\tfrac{T}{2}, T\right) \end{cases}$$

con $A \in \mathbb{R}$, $T > 0$ y $x_2(t + T) = x_2(t)$ para todo $t$.

**c)** Onda triangular:

$$x_3(t) = \begin{cases} -\tfrac{A}{2} + \tfrac{2A}{T} t & \text{si } t \in \left[0, \tfrac{T}{2}\right) \\ \tfrac{3A}{2} - \tfrac{2A}{T} t & \text{si } t \in \left[\tfrac{T}{2}, T\right) \end{cases}$$

con $A \in \mathbb{R}$, $T > 0$ y $x_3(t + T) = x_3(t)$ para todo $t$.

**d)** Seno "ventanado":

$$x_4(t) = \begin{cases} A \sin\left(2\pi \tfrac{t}{T}\right) & \text{si } t \in \left[0, \tfrac{T}{2}\right) \\ 0 & \text{si } t \in \left[\tfrac{T}{2}, T\right) \end{cases}$$

con $A \in \mathbb{R}$, $T > 0$ y $x_4(t + T) = x_4(t)$ para todo $t$.

## Ejercicio 5

Dibuja las funciones del ejercicio anterior junto a las sumas parciales de la serie para 1, 2, 3 y 4 armónicos (esto es, los cuatro primeros términos con senos y los cuatro primeros con cosenos). Usa $T = 1$ y $A = 1$ en todos los casos.

## Ejercicio 6

**Fenómeno de Gibbs.** Dibuja las sumas parciales con 5, 10, 50 y 100 armónicos para la onda triangular. ¿Qué sucede en las discontinuidades? Use $T = 1$ y $A = 1$.

> [Figura: Suma parcial de la serie de Fourier de la onda triangular con overshoot en las discontinuidades (fenómeno de Gibbs).]

## Ejercicio 7

Encuentra las series exponenciales las funciones en el Ejercicio 4.

## Ejercicio 8

**Identidad de Parseval.** Calcula la potencia de cada una de las funciones en el Ejercicio 4. Muestre la convergencia aparente de las sumas parciales $\sum_{n=-N}^{N} |c_n|^2$, donde $c_n$ son los coeficientes de la serie exponencial correspondiente y $N = 1, \dots, 100$. Use $T = 1$ y $A = 1$ en todos los casos.

## Ejercicio 9

**Linealidad.** Sean $f_1(t), f_2(t)$ dos funciones con desarrollos en serie de Fourier

$$f_k(t) \approx \sum_{n \in \mathbb{N}} c_n^{(k)}\, e^{i\frac{2\pi n t}{T}}\quad k = 1, 2$$

Demuestre que $w(t) = \alpha f_1(t) + \beta f_2(t)$ ($\alpha, \beta \in \mathbb{C}$) tiene desarrollo en serie de Fourier:

$$w(t) \approx \sum_{n \in \mathbb{N}} \left[\alpha c_n^{(1)} + \beta c_n^{(2)}\right]\, e^{i\frac{2\pi n t}{T}}$$

## Ejercicio 10

Supone que $f(t)$ es una función de período $T$ con desarrollos en series trigonométrica y exponencial de Fourier:

$$f(t) \approx a_0 + \sum_{n=1}^{+\infty} a_n \cos\left(\tfrac{2\pi n t}{T}\right) + \sum_{n=1}^{+\infty} b_n \sin\left(\tfrac{2\pi n t}{T}\right)$$

$$f(t) \approx \sum_{n \in \mathbb{N}} c_n\, e^{i\frac{2\pi n t}{T}}$$

Demuestra que:

- a) **Relación entre las series:**
  $$a_0 = c_0;\quad a_n = c_n + c_{-n};\quad b_n = i(c_n - c_{-n})\quad n = 1, 2, \dots$$
- b) **Funciones reales:** Si $x$ es real, entonces $c_{-n} = \overline{c_n}$ para todo $n \in \mathbb{N}$.
- c) **Simetría par:** Si $x$ es real y par, entonces $b_n = 0$ y $c_n \in \mathbb{R}$ para todo $n \in \mathbb{N}$. Más aún, $c_n = c_{-n}$.
- d) **Simetría impar:** Si $x$ es real e impar, entonces $a_n = 0$ y $c_n$ es imaginario puro para todo $n \in \mathbb{N}$. Más aún, $c_n = -c_{-n}$.

## Ejercicio 11

Supone que $f(t)$ es como en el ejercicio anterior.

- a) **Derivación:** Demuestra que si $f'(t)$ tiene desarrollo en serie de Fourier
  $$f'(t) \approx \sum_{n \in \mathbb{Z}} d_n\, e^{i\frac{2\pi n t}{T}}$$
  luego $d_n = i\,\tfrac{2\pi n}{T}\, c_n$ para todo $n \in \mathbb{N}$.
- b) **Integración:** Demuestra que si $y(t)$, la primitiva de $f(t)$, tiene desarrollo en serie de Fourier
  $$y(t) \approx \sum_{n \in \mathbb{Z}} g_n\, e^{i\frac{2\pi n t}{T}}$$
  luego $g_n = \left(i\,\tfrac{2\pi n}{T}\right)^{-1}\, c_n$ para todo $n \in \mathbb{N}$.

## Ejercicio 12

Considera la función periódica $x(t) = t^2$ en $[-\pi;\, \pi)$, con período $T = 2\pi$.

- a) Determina la serie exponencial de Fourier de $f(t)$.
- b) Determina la serie trigonométrica de Fourier de $f(t)$ a partir del resultado anterior.
- c) Usando el resultado del ejercicio 12a, determinar la serie exponencial de Fourier de la función periódica $y(t) = t$ en $[-\pi;\, \pi)$, con período $T = 2\pi$.
- d) Usando los resultados anteriores, determina la serie exponencial de Fourier de la función periódica $z(t) = t^3$ en $[-\pi;\, \pi)$, con período $T = 2\pi$.
- e) Demuestre las siguientes igualdades:
  $$\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6} \tag{1}$$
  $$\sum_{n=1}^{\infty} (-1)^n \frac{\sin(n t)}{n^3} = \frac{t}{12}\left(t^2 - \pi^2\right) \tag{2}$$
  $$\sum_{n=1}^{\infty} \frac{1}{n^6} = \frac{\pi^6}{945} \tag{3}$$

## Ejercicio 13

Considera la siguiente función periódica de período $T = 1$, cuyo modelo responde a:

$$x(t) = e^{-5t}\;\text{para } t \in [0, 1),\quad x(t + k) = x(t)\;\text{para todo } k \in \mathbb{Z}$$

- a) Determine la serie exponencial de Fourier correspondiente a la función $x(t)$.
- b) ¿A qué valor converge la serie exponencial de Fourier en $t = 1$?
- c) Determine la serie trigonométrica de Fourier correspondiente a la función $x(t)$.

## Ejercicio 14

Considere la siguiente función periódica:

$$x(t) = \begin{cases} 1 & \text{para } t \in \left[0, \tfrac{1}{2}\right) \\ 0 & \text{para } t \in \left[\tfrac{1}{2}, 1\right) \end{cases}$$

$$x(t + k) = x(t)\;\text{para todo } k \in \mathbb{N}$$

- a) Determine la serie exponencial de Fourier correspondiente a la función $x(t)$.
- b) ¿A qué valor converge la serie exponencial de Fourier en $t = 1$?
- c) Utilice el Teorema de Parseval para demostrar que
  $$\sum_{n=1}^{\infty} \frac{1}{(2k + 1)^2} = \frac{\pi^2}{8}$$

## Ejercicio 14 (extensión periódica impar)

Considere la función $x : [0, \pi] \to \mathbb{R}$ dada por

$$x(t) = \frac{t^2}{\pi}$$

- a) Extienda periódicamente la función $x(t)$ de manera que la correspondiente serie trigonométrica de Fourier tenga solo términos con senos. Use un período $T = 2\pi$.
- b) ¿A qué valor converge la serie trigonométrica en $t = \pi$? Justifique su respuesta.
- c) Encuentra la serie trigonométrica de Fourier mencionada.
