---
tags: [pizarron, numeros-complejos, forma-polar, raices-complejas, formula-euler]
fuente: raw/Practicas/Pizarrones/Clase1 (1).pdf
tipo: escaneo
---

# Pizarrón — Clase 1: Números complejos

Transcripción del pizarrón. Tema central: introducción a $\mathbb{C}$, formas binómica / polar / exponencial, fórmula de Euler, raíces n-ésimas y ejercicios resueltos.

Cross-link: [[../teoria/01-numeros-complejos]] (cuando exista).

## Página 1 — Forma binómica, módulo y argumento

**Definición.** Sea $z \in \mathbb{C}$, $z = a + ib$ con $a, b \in \mathbb{R}$. Se llama **forma rectangular** (binómica) de un número complejo.

$$\operatorname{Re}(z) = a, \qquad \operatorname{Im}(z) = b$$

Representación en el plano complejo: el eje horizontal es $\operatorname{Re}$, el vertical $\operatorname{Im}$; $z = a + ib$ corresponde al punto $(a, b)$ con vector desde el origen de longitud $|z|$ y ángulo $\theta$ con el eje real.

**Forma polar.**
$$z = |z|\, e^{i\theta}$$
donde
$$|z| = \sqrt{a^2 + b^2} \quad \text{(módulo)}, \qquad \theta = \operatorname{Arg}(z) \quad \text{(argumento)}.$$

**Ejemplo.** $z = 1 + i$.

$$|z| = \sqrt{1^2 + 1^2} = \sqrt{2}$$
$$\operatorname{tg}(\theta) = \frac{b}{a} = 1 \;\Rightarrow\; \theta = \operatorname{Arctg}(1) = \tfrac{\pi}{4}$$
$$z = \sqrt{2}\, e^{i\pi/4}$$

> Recordar el dominio de $\operatorname{Arctg}$ — siempre devuelve un ángulo en $(-\tfrac{\pi}{2}, \tfrac{\pi}{2})$.

**Ejemplo** (cuadrante II). $z = -1 + 2i$.

$$|z| = \sqrt{(-1)^2 + 2^2} = \sqrt{5}$$
$$\theta = \pi - \alpha = \pi - \operatorname{Arctg}\!\big(\tfrac{2}{1}\big), \qquad \alpha = \operatorname{Arctg}\!\big(\tfrac{2}{1}\big) = -\operatorname{Arctg}(2)$$

> ⚠️ Pizarrón con un esbozo del gráfico de $\operatorname{Arctg}$ con sus asíntotas en $\pm \tfrac{\pi}{2}$ para recordar el cuidado del cuadrante.

## Página 2 — Fórmula de Euler y producto / potencias

**Fórmula de Euler.**
$$e^{i\theta} = \cos(\theta) + i\,\operatorname{sen}(\theta)$$

Aplicación a $z = \sqrt{2}\, e^{i\pi/4}$:
$$z = \sqrt{2}\big[\cos(\pi/4) + i\,\operatorname{sen}(\pi/4)\big] = \sqrt{2}\!\left[\tfrac{\sqrt{2}}{2} + i\,\tfrac{\sqrt{2}}{2}\right] = 1 + i.$$

(El paréntesis interno se etiqueta en el pizarrón como "fórmula trigonométrica" y la igualdad final como "forma rectangular".)

**Ejemplo (producto).** Sean $z_1 = i$ y $z_2 = 1 + i$. Calcular $P = z_1^3 \cdot z_2^3$.

$$z_1^3 = i \cdot i \cdot i = -i$$
$$z_2^3 = (1+i)^3 = (1+i)(1+i)(1+i) = (1 + 2i + i^2)(1+i) = (1 + 2i - 1)(1+i) = 2i(1+i) = 2i - 2$$

**Caso general.** Si $z = a + ib = |z|\, e^{i\theta}$, entonces
$$z^n = (|z|\, e^{i\theta})^n = |z|^n\, e^{in\theta}.$$

Verificación con $z = 1 + i = \sqrt{2}\, e^{i\pi/4}$:
$$z^3 = (\sqrt{2})^3 e^{i\,3\pi/4} = 2\sqrt{2}\big[\cos(3\pi/4) + i\,\operatorname{sen}(3\pi/4)\big] = 2\sqrt{2}\!\left[-\tfrac{\sqrt{2}}{2} + i\,\tfrac{\sqrt{2}}{2}\right] = -2 + 2i.$$

## Página 3 — Producto en forma polar y raíces n-ésimas

**Producto en forma polar.** Si $z_1 = a + ib = |z_1| e^{i\theta_1}$ y $z_2 = \alpha + i\beta = |z_2| e^{i\theta_2}$:
$$z_1 z_2 = |z_1|\, |z_2|\, e^{i(\theta_1 + \theta_2)}.$$

Aplicado al ejemplo anterior:
$$z_1^3 \cdot z_2^3 = (-i)(-2+2i) = 1 \cdot e^{-i\pi/2} \cdot 2\sqrt{2}\, e^{i\,3\pi/4} = 2\sqrt{2}\, e^{i\pi/4} = 2\sqrt{2}\!\left[\tfrac{\sqrt{2}}{2} + i\,\tfrac{\sqrt{2}}{2}\right] = 2 + 2i \;\checkmark$$

**Ejemplo (raíces).** Resolver $\omega^4 = i$, $\omega \in \mathbb{C}$ (también escrito $\sqrt[4]{i}$).

Si $\omega = a + ib$, $(a+ib)^4 = i$ — no es práctico desarrollar (marcado con $\times$).

Pasar a polar: $\omega = \rho\, e^{i\theta} \;\Rightarrow\; \omega^4 = \rho^4 e^{i\,4\theta} = i = 1 \cdot e^{i\pi/2}$.

Sistema:
$$\begin{cases} \rho^4 = 1 \\ 4\theta = \tfrac{\pi}{2} + 2k\pi, \quad k \in \mathbb{Z} \end{cases} \;\Rightarrow\; \begin{cases} \rho = 1 \\ \theta = \tfrac{\pi}{8} + \tfrac{k\pi}{2} \end{cases}$$

## Página 4 — Conjunto solución y raíz n-ésima general

Variando $k$:
$$\omega_0 = 1\cdot e^{i\pi/8}, \quad \omega_1 = 1\cdot e^{i\,5\pi/8}, \quad \omega_2 = 1\cdot e^{i\,9\pi/8}, \quad \omega_3 = 1\cdot e^{i\,13\pi/8}$$

Solución $\{\omega_0, \dots, \omega_3\}$ (4 raíces distintas para $\sqrt[4]{\cdot}$).

Para $k=4$: $\omega_4 = e^{i(\pi/8 + 2\pi)} = e^{i\pi/8}\cdot \underbrace{e^{i\,2\pi}}_{=1} = \omega_0$.

**Auxiliar.** $e^{i\,2\pi} = \cos(2\pi) + i\,\operatorname{sen}(2\pi) = 1$.

Por lo tanto $\omega_4 = \omega_0$, $\omega_5 = \omega_1$, $\omega_6 = \omega_2$, … (las raíces se repiten cíclicamente con período $n$). Además, $\omega^4 = i \;\Leftrightarrow\; \omega^4 - i = 0$.

**Raíz n-ésima de un $z \in \mathbb{C}$.** Sea $z = \rho\, e^{i\theta}$. Entonces
$$\boxed{\;\sqrt[n]{z} = \sqrt[n]{\rho}\; e^{i\left(\frac{\theta}{n} + \frac{2k\pi}{n}\right)}, \quad k \in \{0, 1, \dots, n-1\}\;}$$

**Ejercicio 2.d.** $\overline{x + 2y} + (4x - 3y)\,i = 2x - 1 + (y - 6)\,i$.

Igualando partes real e imaginaria:
$$\begin{cases} x + 2y = 2x - 1 \\ 4x - 3y = y - 6 \end{cases}$$

## Página 5 — Sistema lineal y ejercicio 4

$$\begin{cases} -x + 2y = -1 \\ 4x - 4y = -6 \end{cases} \;\Rightarrow\; \begin{cases} x = 1 + 2y \\ 4(1 + 2y) - 4y = -6 \end{cases} \;\Rightarrow\; 4 + 8y - 4y = -6 \;\Rightarrow\; 4y = -10 \;\Rightarrow\; y = -\tfrac{5}{2}$$

Forma matricial:
$$\begin{bmatrix} -1 & 2 \\ 4 & -4 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} -1 \\ -6 \end{bmatrix}$$

**Ejercicio 4.** Resolver $z^n = \bar z$ con $z = \rho\, e^{i\theta}$.

$z = a + ib \;\Rightarrow\; \bar z = a - ib = |z|\, e^{i(-\theta)}$, $|z| = |\bar z|$.

> Diagrama: $z$ y $\bar z$ son reflejos respecto del eje real; $\bar z$ tiene argumento $-\theta$.

$$z^n = \bar z \;\Rightarrow\; \rho^n\, e^{in\theta} = \rho\, e^{-i\theta}$$
$$\begin{cases} \rho^n = \rho \\ n\theta = -\theta + 2k\pi \end{cases} \;\Rightarrow\; \rho^n - \rho = 0 \;\Rightarrow\; \rho(\rho^{n-1} - 1) = 0 \;\Rightarrow\; \rho = 0 \;\lor\; \rho = 1$$

(El factor $\rho(\rho-1)\,p(\rho) = 0$ se anota como "polinomio de grado 2" en el caso particular; en general $\rho^{n-1} = 1 \Rightarrow \rho = 1$ en reales no negativos.)

Y del ángulo:
$$n\theta + \theta = 2k\pi \;\Rightarrow\; \theta(n+1) = 2k\pi \;\Rightarrow\; \theta = \tfrac{2k\pi}{n+1}.$$

## Página 6 — Parte real / imaginaria en función del conjugado. Ejercicio 8

$$z = 1\cdot e^{i\,\frac{2k\pi}{n+1}}, \qquad k \in \{0, \dots, n\}.$$

**Ejercicio 5.** Si $z = a + ib$:
$$z + \bar z = (a + ib) + (a - ib) = 2a = 2\,\operatorname{Re}\{z\}$$
$$\boxed{\;\operatorname{Re}\{z\} = \tfrac{z + \bar z}{2}\;}$$
$$z - \bar z = (a + ib) - (a - ib) = 2ib = 2i\,\operatorname{Im}(z)$$
$$\boxed{\;\operatorname{Im}(z) = \tfrac{z - \bar z}{2i}\;}$$

**Ejercicio 8.k.** $z^2 + |z|^2 = i\bar z$, con $z = a + ib = \rho\, e^{i\theta}$.

$$z^2 = (a + ib)^2 = a^2 - b^2 + 2iab$$
$$\operatorname{Re}\{z^2\} = a^2 - b^2, \qquad \operatorname{Im}\{z^2\} = 2ab$$
$$|z^2| = \sqrt{(a^2 - b^2)^2 + (2ab)^2} = \sqrt{a^4 - 2a^2 b^2 + b^4 + 4a^2 b^2} = \sqrt{a^4 + 2a^2 b^2 + b^4} = \sqrt{(a^2 + b^2)^2} = a^2 + b^2.$$

También: $z^2 = \rho^2\, e^{i\,2\theta} \Rightarrow |z^2| = \rho^2 = (\sqrt{a^2 + b^2})^2 = a^2 + b^2$.

## Página 7 — Continuación 8.k y ejercicio 10

$$z^2 + |z|^2 = i\bar z$$
$$(a^2 - b^2 + 2iab) + (a^2 + b^2) = i(a - ib) = b + ia$$
$$\begin{cases} 2a^2 = b \\ 2ab = a \end{cases} \;\Rightarrow\; 2a(2a^2) = a \;\Rightarrow\; 4a^3 - a = 0$$

(De $2ab = a$ con $a \neq 0$: $b = \tfrac{1}{2}$; combinado con $2a^2 = b$ da $a^2 = \tfrac{1}{4}$.)

**Ejercicio 10.** $\bar z = z^3 (z - i)^4$ con $|z| = 1$.

$$z\bar z = z^4 (z - i)^4 \;\Rightarrow\; 1 = z^4 (z - i)^4.$$

Auxiliar: con $z = x + iy$, $z\bar z = (x + iy)(x - iy) = x^2 + y^2 = |z|^2$.

$$1 = z^4 (z - i)^4 = [z(z - i)]^4 = \omega^4 \quad \text{con } \omega = z(z - i).$$

$$\omega^4 - 1 = 0 \;\Rightarrow\; (\omega^2 - 1)(\omega^2 + 1) = 0 \;\Rightarrow\; (\omega + 1)(\omega - 1)(\omega^2 + 1) = 0$$
$$\Rightarrow \omega \in \{1, -1, i, -i\}.$$

Caso $\omega = 1$: $z(z - i) = 1 \;\Rightarrow\; z^2 - iz - 1 = 0.$

## Página 8 — Ejercicio 11.a (logaritmo complejo)

**Ejercicio 11.a.** $e^\omega = z$ con $z = \sqrt{3} - i\sqrt{3}$.

Tomar $\omega \in \mathbb{C}$: $\omega = \alpha + i\beta = \rho\, e^{i\theta}$ (en el pizarrón se prefiere la forma $\alpha + i\beta$ y se anota $e^{i\theta}$ aparte).

$$e^{\alpha + i\beta} = \sqrt{3} - i\sqrt{3} \;\Rightarrow\; e^\alpha\, e^{i\beta} = \sqrt{3} - i\sqrt{3}$$

donde $e^\alpha$ es el módulo y $e^{i\beta}$ aporta el argumento. El segundo miembro debe expresarse como **número complejo en forma polar** de módulo $e^\alpha$ y argumento $\beta$:

$$|\sqrt{3} - i\sqrt{3}| = \sqrt{(\sqrt{3})^2 + (\sqrt{3})^2} = \sqrt{6}$$
$$\operatorname{Arg}(\sqrt{3} - i\sqrt{3}) \quad\text{(4° cuadrante)}\quad = \operatorname{Arctg}\!\big(\tfrac{-\sqrt{3}}{\sqrt{3}}\big) = \operatorname{Arctg}(-1) = -\tfrac{\pi}{4}$$

> Nota: en el pizarrón se escribe $\operatorname{Arctg}(\sqrt{3}/\sqrt{3}) = \pi/4$ omitiendo el signo y luego se incorpora la rama al sumar $2k\pi$.

$$e^\alpha\, e^{i\beta} = \sqrt{6}\, e^{i\,\pi/4} \;\Rightarrow\; \begin{cases} e^\alpha = \sqrt{6} \;\Rightarrow\; \alpha = \ln(\sqrt{6}) \\ \beta = \tfrac{\pi}{4} + 2k\pi, \quad k \in \mathbb{Z} \end{cases}$$

$$\boxed{\;\omega_k = \ln(\sqrt{6}) + i\!\left(\tfrac{\pi}{4} + 2k\pi\right), \quad k \in \mathbb{Z}\;}$$

> Esquema en el pizarrón: los $\omega_k$ se ubican en la recta vertical $\operatorname{Re}(\omega) = \ln(\sqrt{6})$, espaciados $2\pi$ a lo largo del eje imaginario.

## Página 9

> ⚠️ Página en blanco (sólo cuadrícula del pizarrón).
