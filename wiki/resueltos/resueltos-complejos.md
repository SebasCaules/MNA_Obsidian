---
tags: [resueltos, complejos]
fuente: raw/Practicas/Ejercicios_Resueltos/MNA_Ejercicios_Numeros_Complejos.pdf
unidad: I
---

# Ejercicios Resueltos — Números Complejos

Ver enunciados en [[../guias/guia-01-complejos]].

## Ejercicio 1

Dados los siguientes números complejos:

$$z_1 = i,\quad z_2 = 1 + i,\quad z_3 = -1,\quad z_4 = 81,\quad z_5 = -21$$

**a)** Expresarlos en forma exponencial y trigonométrica.

**b)** Efectuar las siguientes operaciones:

- i) $|z_1|$
- ii) $|z_5|$
- iii) $\sqrt[4]{z_4}$
- iv) $\sqrt[6]{z_5}$
- v) $\operatorname{vp}:\ln z_1$
- vi) $\operatorname{vp}:\ln(z_2 z_5 z_1^{-1})$
- vii) $\operatorname{vp}:\ln\!\left(z_5 \sqrt[4]{z_4^{-1}}\right)$
- viii) $z_1^{245}$
- ix) $\operatorname{vp}:z_1^{z_2}$
- x) $\operatorname{vp}:z_4^{z_2}$
- xi) $\ln z_3$

### Resolución

**a)** Recuérdese que si $z = a + ib$ con $a, b \in \mathbb{R}$ se define:

$$\rho = |z|\quad \text{y}\quad \theta = \arg(z)$$

A partir de estas definiciones a un número complejo $z$ se lo puede escribir en forma exponencial y trigonométrica como:

$$z = \rho\, e^{i\theta}\quad \text{y}\quad z = \rho \cos\theta + i\,\rho \sin\theta$$

En la resolución del ejercicio solo se indicará el módulo y el argumento de cada número complejo dado.

- i) $z_1 = i \Rightarrow \rho_1 = 1,\quad \theta_1 = \tfrac{\pi}{2}$
- ii) $z_2 = 1 + i \Rightarrow \rho_2 = \sqrt{2},\quad \theta_2 = \tfrac{\pi}{4}$
- iii) $z_3 = -1 \Rightarrow \rho_3 = 1,\quad \theta_3 = \pi$
- iv) $z_4 = 81 \Rightarrow \rho_4 = 81,\quad \theta_4 = 0$
- v) $z_5 = -21 \Rightarrow \rho_5 = 21,\quad \theta_5 = \pi$

**b)** Los incisos i) y ii) fueron hechos en a). Empezaremos desde el iii).

**iii)** $\sqrt[4]{z_4} = \sqrt[4]{|z_4|}\, e^{i\,\frac{\theta_4 + 2k\pi}{4}}$, $k = 0, \dots, 3$

$$\Rightarrow \sqrt[4]{z_4} = \sqrt[4]{81}\, e^{i\,\frac{2k\pi}{4}} = 3\, e^{i\,\frac{k\pi}{2}},\quad k = 0, \dots, 3$$

Llamemos $w_k = 3\, e^{i\,\frac{k\pi}{2}}$ con $k = 0, \dots, 3$. Reemplazando se tiene:

$$w_0 = 3,\quad w_1 = 3\, e^{i\,\pi/2},\quad w_2 = 3\, e^{i\pi},\quad w_3 = 3\, e^{i\,\frac{3}{2}\pi}$$

En coordenadas cartesianas:

$$w_0 = 3,\quad w_1 = 3i,\quad w_2 = -3,\quad w_3 = -3i$$

**iv)** $\sqrt[6]{z_5} = \sqrt[6]{|z_5|}\, e^{i\,\frac{\theta_5 + 2k\pi}{6}}$, $k = 0, \dots, 5$

$$\Rightarrow \sqrt[6]{z_5} = \sqrt[6]{21}\, e^{i\,\frac{\pi + 2k\pi}{6}},\quad k = 0, \dots, 5$$

Reemplazando se tiene:

$$w_0 = \sqrt[6]{21}\, e^{i\,\pi/6},\quad w_1 = \sqrt[6]{21}\, e^{i\,\pi/2},\quad w_2 = \sqrt[6]{21}\, e^{i\,5\pi/6},$$
$$w_3 = \sqrt[6]{21}\, e^{i\,7\pi/6},\quad w_4 = \sqrt[6]{21}\, e^{i\,3\pi/2},\quad w_5 = \sqrt[6]{21}\, e^{i\,11\pi/6}$$

En coordenadas cartesianas:

$$w_0 = \sqrt[6]{21}\,\frac{\sqrt{3}}{2} + i\frac{\sqrt[6]{21}}{2},\quad w_1 = i\sqrt[6]{21},\quad w_2 = -\sqrt[6]{21}\,\frac{\sqrt{3}}{2} + i\frac{\sqrt[6]{21}}{2}$$

$$w_3 = -\sqrt[6]{21}\,\frac{\sqrt{3}}{2} - i\frac{\sqrt[6]{21}}{2},\quad w_4 = -i\sqrt[6]{21},\quad w_5 = \sqrt[6]{21}\,\frac{\sqrt{3}}{2} - i\frac{\sqrt[6]{21}}{2}$$

**v)** $\ln z_1 = \ln \rho_1 + i\theta_1 = \ln 1 + i\,\tfrac{\pi}{2} \Rightarrow \ln z_1 = i\,\tfrac{\pi}{2}$

**vi)** Llamamos $p = z_2 z_5 z_1^{-1}$. Luego $p = -21(1+i)(-i) = 21\,i\,(1+i) = -21 + 21i$. Entonces:

$$\ln(z_2 z_5 z_1^{-1}) = \ln p = \ln(-21 + 21i) = \ln(21\sqrt{2}) + i\,\tfrac{3}{4}\pi$$

**vii)** Llamamos $q = z_5 \sqrt[4]{z_4^{-1}}$, o sea $q = -21\sqrt[4]{\tfrac{1}{81}} = 21\, e^{i\pi}\, e^{i\,\tfrac{k\pi}{4}} = 7\, e^{i\,\left(\pi + \tfrac{k\pi}{2}\right)} = 7\, e^{i\,\tfrac{k+2}{2}\pi}$. Luego:

$$\ln q = \ln 7 + i\,\tfrac{(k+2)\pi}{2},\quad k = 0, \dots, 3$$

**viii)** $z_1^{245} = i^{245} = i^{244}\, i = (-1)^{122}\, i = i \Rightarrow z_1^{245} = i$

**ix)** $z_1^{z_2} = e^{z_2 \ln z_1} = e^{i(1+i)\tfrac{\pi}{2}} = e^{(-1+i)\tfrac{\pi}{2}} = e^{-\pi/2}\, e^{i\pi/2} = i\, e^{-\pi/2}$

$$\Rightarrow z_1^{z_2} = i\, e^{-\pi/2}$$

**x)** $z_4^{z_2} = e^{z_2 \ln z_4} = e^{(1+i)\ln 81} = e^{\ln 81}\, e^{i\ln 81} = 81\, e^{i\ln 81}$

$$\Rightarrow z_4^{z_2} = 81\, e^{i\ln 81}$$

**xi)** $\ln z_3 = \ln \rho_3 + i(\theta_3 + 2k\pi) = \ln 1 + i\,(2k+1)\pi$, $k \in \mathbb{Z}$

$$\Rightarrow \ln z_3 = i\,(2k+1)\pi,\quad k \in \mathbb{Z}$$

## Ejercicio 2

Resolver la siguiente ecuación en $\mathbb{C}$:

$$z^4 + 4iz^3 - 6z^2 - 4iz - 15 = 0$$

### Resolución

Recordemos el binomio de Newton: $(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k$.

En particular:

$$(a + b)^4 = \binom{4}{0}a^4 + \binom{4}{1}a^3 b + \binom{4}{2}a^2 b^2 + \binom{4}{3}a b^3 + \binom{4}{4}b^4 = a^4 + 4a^3 b + 6a^2 b^2 + 4ab^3 + b^4$$

En el caso de nuestra ecuación podemos escribir:

$$z^4 + 4iz^3 + 6i^2 z^2 + 4i^3 z + i^4 - 15 = 0$$

Si miramos la ecuación se tiene que es equivalente a:

$$(z + i)^4 - 16 = 0$$

Llamando $w = z + i$ se tiene la ecuación $w^4 = 16$. Aplicando la fórmula:

$$w_k = \sqrt[4]{16}\, e^{i\,\frac{2k\pi}{4}} \Rightarrow w_k = 2\, e^{i\,\frac{k\pi}{2}}$$

$$w_0 = 2,\quad w_1 = 2\, e^{i\pi/2},\quad w_2 = 2\, e^{i\pi},\quad w_3 = 2\, e^{i\,3\pi/2}$$

En forma binómica:

$$w_0 = 2,\quad w_1 = 2i,\quad w_2 = -2,\quad w_3 = -2i$$

Recordando que $w_k = z_k + i$:

$$z_0 = 2 - i,\quad z_1 = i,\quad z_2 = -2 - i,\quad z_3 = -3i$$

## Ejercicio 3

Sea $f : \mathbb{R} \to \mathbb{R} : f(x) = \sin^3 x$. Escribirla como un polinomio trigonométrico de grado 1.

### Resolución

Por otro lado se demostró que $\sin x = \dfrac{e^{ix} - e^{-ix}}{2i}$. Reemplazando:

$$\sin^3 x = \left(\frac{e^{ix} - e^{-ix}}{2i}\right)^3 = \frac{(e^{ix})^3 + 3(e^{ix})^2(-e^{-ix}) + 3 e^{ix}(-e^{-ix})^2 + (-e^{-ix})^3}{(2i)^3}$$

$$= \frac{e^{i3x} - 3e^{ix} + 3e^{-ix} - e^{-3ix}}{-8i} = -\frac{1}{4}\cdot\frac{e^{i3x} - e^{-3ix}}{2i} + \frac{3}{4}\cdot\frac{e^{ix} - e^{-ix}}{2i}$$

$$= -\frac{1}{4}\sin(3x) + \frac{3}{4}\sin x$$

Finalmente:

$$f(x) = -\frac{1}{4}\sin(3x) + \frac{3}{4}\sin x$$

## Ejercicio 4

Hallar todos los $z \in \mathbb{C} : (z - 1)^4 = (z + i)^4$.

### Resolución

Se hace diferencia de cuadrados:

$$(z - 1)^4 - (z + i)^4 = 0 \Rightarrow \left[(z - 1)^2 + (z + i)^2\right]\left[(z - 1)^2 - (z + i)^2\right] = 0$$

$$\Rightarrow \left[(z - 1)^2 + (z + i)^2\right]\left[(z - 1) + (z + i)\right]\left[(z - 1) - (z + i)\right] = 0$$

Analizando cada factor:

$$(z - 1)^2 + (z + i)^2 = 0\;\vee\; (z - 1) - (z + i) = 0\;\vee\; (z - 1) + (z + i) = 0$$

**Primera igualdad:**

$$z^2 - 2z + 1 + z^2 + 2iz - 1 = 0 \Rightarrow 2z^2 + 2iz - 2z = 0$$

Sea $z = x + iy$:

$$2(x^2 - y^2) + 2i(x - iy)(\cdots) + \cdots = 0$$

Desarrollando: $x^2 - y^2 + x + y = 0\;\wedge\; x + y = 0$.

$$(x - y)(x + y) + x + y = 0\;\wedge\; x + y = 0 \Rightarrow (x + y)(x - y + 1) = 0\;\wedge\; x + y = 0 \Rightarrow y = -x$$

Luego la primera solución son los $z \in \mathbb{C}$ de la forma $z = t - it$ con $t \in \mathbb{R}$.

**Segunda ecuación:**

$$z - 1 - z - i = 0 \Rightarrow \overline{z} - z = 1 + i \Rightarrow 2iy = 1 + i$$

Esto es absurdo pues un número imaginario puro no puede tener parte real.

**Tercera ecuación:**

$$z + \overline{z} = 1 - i \Rightarrow 2x = 1 - i$$

Por la misma razón, absurdo.

Luego la solución son los puntos de la forma $z = t - it$ con $t \in \mathbb{R}$.

## Ejercicio 5

Resolver las siguientes ecuaciones en $\mathbb{C}$ donde $z = x + iy$ con $x, y \in \mathbb{R}$:

- i) $2x + 3i = -5 + iy$
- ii) $-4 + 6yi = \tfrac{1}{2} x + \sqrt{3}\, y\, i$
- iii) $i(x - iy) = x + 5 + 2yi$
- iv) $(1 - 2i)x + (3 + 5i)y = 1 + 3i$
- v) $x + 2y + (4x - 3y)i = 2x - 1 + (y - 6)i$

### Resolución

**i)** $2x + 3i = -5 + iy \Rightarrow 2x = -5\;\wedge\; 3 = y \Rightarrow x = -\tfrac{5}{2}\;\wedge\; y = 3$

$$\Rightarrow z = -\tfrac{5}{2} + 3i$$

**ii)** $-4 + 6yi = \tfrac{1}{2}x + \sqrt{3}yi \Rightarrow \tfrac{1}{2}x = -4\;\wedge\; 6y = \sqrt{3}y \Rightarrow x = -8\;\wedge\; y = 0$

$$\Rightarrow z = -8$$

**iii)** $i(x - iy) = x + 5 + 2yi \Rightarrow ix + y = x + 5 + 2yi \Rightarrow x + 5 = y\;\wedge\; 2y = x$

$$\Rightarrow 2(x + 5) = x \Rightarrow 2x + 10 = x \Rightarrow x = -10 \Rightarrow y = -5 \Rightarrow z = -10 - 5i$$

**iv)** $(1 - 2i)x + (3 + 5i)y = 1 + 3i \Rightarrow x - 2xi + 3y + 5iy = 1 + 3i$

$$\Rightarrow x + 3y + i(5y - 2x) = 1 + 3i \Rightarrow x + 3y = 1\;\wedge\; 5y - 2x = 3$$

De la primera ecuación $x = 1 - 3y$. Reemplazando: $5y - 2(1 - 3y) = 3 \Rightarrow 11y = 6$.

$$\Rightarrow y = \tfrac{6}{11},\quad x = -\tfrac{7}{11},\quad z = -\tfrac{7}{11} + \tfrac{6}{11} i$$

**v)** $x + 2y + (4x - 3y)i = 2x - 1 + (y - 6)i$

$$\Rightarrow x + 2y = 2x - 1\;\wedge\; 4x - 3y = y - 6 \Rightarrow -x + 2y = -1\;\wedge\; 4x - 4y = -6$$

$$\Rightarrow -x + 2y = -1\;\wedge\; x - y = -\tfrac{3}{2} \Rightarrow y = -\tfrac{5}{2}\;\wedge\; x = -4$$

$$\Rightarrow z = -4 - \tfrac{5}{2} i$$

## Ejercicio 6

Dados los siguientes números complejos $z_1 = i$, $z_2 = 1 + i$, $z_3 = -1$, $z_4 = 81$, $z_5 = -21$, hallar:

- i) $z = z_2 z_5 z_1^{-1}$
- ii) $p = z_1^3 z_2^3$
- iii) $q = \dfrac{z_1 - z_3}{z_2^2}$
- iv) $r = z_1^{245}$
- v) $\operatorname{vp}: s = z_1^{z_2}$
- vi) $\operatorname{vp}: t = z_4^{z_2}$

### Resolución

**i)** $z = z_2 z_5 z_1^{-1} \Rightarrow z = (1 + i)(-21)\cdot\tfrac{1}{i} = (1+i)(-21)(-i) = 21\,i(1+i)$

$$\Rightarrow z = -21 + 21i$$

**ii)** $p = z_1^3 z_2^3 \Rightarrow p = i^3 (1+i)^3 = [i(1+i)]^3 = (i - 1)^3$.

En forma polar, $q = i - 1$ tiene $|q| = \sqrt{2}$ y $\arg(q) = \tfrac{3\pi}{4}$ (en el resuelto se usa $1 - i$ con arg $\tfrac{7}{4}\pi$ y exponente correspondiente). Luego:

$$p = (\sqrt{2})^3\, e^{i\,\tfrac{21}{4}\pi} = -2\sqrt{2}\left(\tfrac{\sqrt{2}}{2} + i\tfrac{\sqrt{2}}{2}\right) \Rightarrow p = -2 - 2i$$

**iii)** $q = \dfrac{z_1 - z_3}{z_2^2} = \dfrac{i + 1}{(1+i)^2} = \dfrac{1}{1+i} = \dfrac{1 - i}{(1+i)(1-i)} = \dfrac{1 - i}{2}$

$$\Rightarrow q = \tfrac{1}{2} - \tfrac{1}{2} i$$

**iv)** $r = z_1^{245} = i^{245} = i \cdot i^{244} = (-1)^{122}\, i = i \Rightarrow r = i$

**v)** $\operatorname{vp}: s = z_1^{z_2} = e^{z_2 \ln z_1} = e^{(1+i)\ln i}$. Ahora $\operatorname{vp}:\ln i = \ln|i| + i\,\tfrac{\pi}{2} = i\,\tfrac{\pi}{2}$.

$$\Rightarrow i\,\tfrac{\pi}{2}(1+i) = -\tfrac{\pi}{2} + i\,\tfrac{\pi}{2} \Rightarrow \operatorname{vp}: s = e^{-\pi/2 + i\pi/2} = e^{-\pi/2}\left(\cos\tfrac{\pi}{2} + i\sin\tfrac{\pi}{2}\right) = i\, e^{-\pi/2}$$

**vi)** $\operatorname{vp}: t = z_4^{z_2} = e^{z_2 \ln z_4} = e^{(1+i)\ln 81} = e^{\ln 81}\, e^{i\ln 81} = 81\, e^{i\ln 81}$

$$\Rightarrow \operatorname{vp}: t = 81\cos(\ln 81) + 81i\sin(\ln 81)$$
