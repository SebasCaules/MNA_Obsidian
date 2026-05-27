---
tags: [teoria, unidad-I, numeros-complejos]
fuente: raw/Teoricas/Slides/MNA_Unidad_I_Numeros_Complejos_Clase_I_v4.pdf
unidad: I
---

# Números Complejos

## Introducción

### Motivación

Es frecuente en los modelos matemáticos la aparición de situaciones que involucran ecuaciones del tipo:

i) $x^2 + 1 = 0$
ii) $a x^2 + b x + c = 0$ con $b^2 - 4 a c < 0$
iii) $x^3 - 1 = 0 \iff (x - 1)(x^2 + x + 1) = 0$
iv) $e^x + 1 = 0$
v) $(-1)^x = e$

En todos los casos se observa que esos problemas no están totalmente resueltos en $\mathbb{R}$.

Se comenzará analizando los casos i), ii) y iii). En el caso i) se tiene $x^2 + 1 = 0 \iff x^2 = -1$. Se busca darle "algún sentido a $\sqrt{-1}$".

### La Unidad Imaginaria

Se define la unidad imaginaria $i$ a un número que cumple

$$i^2 = -1 \quad \wedge \quad (-i)^2 = -1$$

### Potencias de la Unidad Imaginaria

$$i^0 = 1, \quad i^1 = i, \quad i^2 = -1, \quad i^3 = i \cdot i^2 = -i$$
$$i^4 = i^2 \, i^2 = (-1)(-1) = 1$$

En general se tiene:

$$i^{2n} = (-1)^n \quad y \quad i^{2n+1} = (-1)^n \, i \qquad \forall \, n \in \mathbb{N}$$

### Número Complejo

> **Definición.** Un número complejo es un objeto matemático de la forma
> $$z = a_z + i \, b_z, \qquad a_z, b_z \in \mathbb{R}$$
> donde $a_z$ y $b_z$ se las denomina partes real e imaginaria de $z$ respectivamente y se las nota como
> $$a_z = \text{Re}(z) \quad y \quad b_z = \text{Im}(z)$$

### El conjunto de los números complejos

> **Definición.** Se define al conjunto de los números complejos como
> $$\mathbb{C} = \{ a + i b : a, b \in \mathbb{R} \}$$

Una notación común es escribir $\mathbb{C} = \mathbb{R} + i \, \mathbb{R}$ y de este modo se ve de una manera simple que $\mathbb{R} \subset \mathbb{C}$.

Para que tenga sentido el conjunto definido y se pueda trabajar con él, es necesario definir la igualdad y las operaciones que pueden hacerse en él.

Sean $z = a_z + i \, b_z$ y $w = a_w + i \, b_w$.

### Igualdad en $\mathbb{C}$

$$z = w \iff \text{Re}(z) = \text{Re}(w) \quad \wedge \quad \text{Im}(z) = \text{Im}(w)$$

En componentes:

$$z = w \iff a_z = a_w \quad \wedge \quad b_z = b_w$$

### Adición en $\mathbb{C}$

$$z + w = (\text{Re}(z) + \text{Re}(w)) + i \, (\text{Im}(z) + \text{Im}(w))$$

En componentes:

$$z + w = (a_z + a_w) + i \, (b_z + b_w)$$

### Multiplicación en $\mathbb{C}$

$$z \, w = (\text{Re}(z) \, \text{Re}(w) - \text{Im}(z) \, \text{Im}(w)) + i \, (\text{Re}(z) \, \text{Im}(w) + \text{Re}(w) \, \text{Im}(z))$$

En componentes:

$$z \, w = (a_z \, a_w - b_z \, b_w) + i \, (a_z \, b_w + a_w \, b_z)$$

**Observación informal:**

$$z \, w = (a_z + i \, b_z)(a_w + i \, b_w)$$

Aplicando propiedad distributiva y recordando que $i^2 = -1$ se llega a lo definido.

## Propiedades de $(\mathbb{C}, +, \cdot)$

### Propiedades de $(\mathbb{C}, +)$

i) **Ley de Composición Interna:** Si $z, w \in \mathbb{C}$ entonces $z + w \in \mathbb{C}$.
ii) **Asociatividad:** Si $z, w, u \in \mathbb{C}$ entonces $(z + w) + u = z + (w + u)$.
iii) **Existencia de elemento neutro:** $0_{\mathbb{C}} = 0_{\mathbb{R}} + i \, 0_{\mathbb{R}}$. Se escribirá simplemente $0$.
iv) **Existencia de elemento opuesto:** Si $z = a_z + i \, b_z$ el número $w = (-a_z) + i \, (-b_z)$ cumple que $z + w = w + z = 0$. Se escribirá $w = -z$.
v) **Conmutatividad:** Si $z, w \in \mathbb{C}$: $z + w = w + z$.

### Propiedades de $(\mathbb{C}, \cdot)$

i) **Ley de Composición Interna:** Si $z, w \in \mathbb{C}$ entonces $z \cdot w \in \mathbb{C}$.
ii) **Asociatividad:** Si $z, w, u \in \mathbb{C}$, $(z \cdot w) \cdot u = z \cdot (w \cdot u)$.
iii) **Existencia de elemento neutro:** $1_{\mathbb{C}} = 1_{\mathbb{R}} + i \, 0_{\mathbb{R}}$. Se escribirá simplemente $1$.
iv) **Existencia de elemento opuesto:** Si $z = a_z + i \, b_z$ el número
$$w = \frac{a_z}{a_z^2 + b_z^2} + i \, \frac{-b_z}{a_z^2 + b_z^2}$$
cumple que $z \cdot w = w \cdot z = 1$. Se suele escribir $w = z^{-1}$.
v) **Conmutatividad:** Si $z, w \in \mathbb{C}$: $z \cdot w = w \cdot z$.

### Propiedad Distributiva

Si $z, w, u \in \mathbb{C}$ entonces $z \cdot (w + u) = z \cdot w + z \cdot u$.

### División en $\mathbb{C}$

A partir del hecho de que todo número $w \neq 0$ tiene un inverso multiplicativo, es posible definir la división en $\mathbb{C}$ como

$$\frac{z}{w} = z \, w^{-1}$$

donde

$$z = a_z + i \, b_z, \qquad w = a_w + i \, b_w$$

y

$$w^{-1} = \frac{a_w}{a_w^2 + b_w^2} + i \, \frac{-b_w}{a_w^2 + b_w^2}$$

Luego:

$$\frac{z}{w} = \left( \frac{a_z \, a_w}{a_w^2 + b_w^2} + \frac{b_z \, b_w}{a_w^2 + b_w^2} \right) + i \, \left( \frac{b_z \, a_w}{a_w^2 + b_w^2} - \frac{a_z \, b_w}{a_w^2 + b_w^2} \right)$$

**Ejemplo:** Dados $z = 4 + i \, 2$ y $w = 3 + i \, 7$ se desea calcular $\dfrac{z}{w}$.

$$z = 4 + i \, 2, \quad w^{-1} = \frac{3}{58} - i \, \frac{7}{58} \implies z \, w^{-1} = \frac{26}{58} - i \, \frac{22}{58}$$

## Axiomas de orden en $\mathbb{R}$

En esta sección recordamos los axiomas de orden en $\mathbb{R}$ para luego ver qué ocurre en $\mathbb{C}$. Sean $a, b, c \in \mathbb{R}$ entonces:

- **A.1 Tricotomía:** $a > b \;\veebar\; a = b \;\veebar\; a < b$.
- **A.2 Transitividad:** Si $a < b \wedge b < c \implies a < c$.
- **A.3 Monotonía I:** Si $a < b \implies a + c < b + c$.
- **A.4 Monotonía II:** Si $a < b \wedge c > 0 \implies a \, c < b \, c$.

### Consecuencias

i) Sean $a, b, c \in \mathbb{R}$. Si $a < b \wedge c < 0 \implies a \, c > b \, c$.
ii) Sean $a, b, c \in \mathbb{R}$. Si $a + c < b + c \implies a < b$.
iii) Sean $a, b, c \in \mathbb{R}$. Si $a \, c < b \, c$ y $c > 0 \implies a < b$.

> **Proposición.** No existe un orden en $\mathbb{C}$ que cumpla con los axiomas A.1 a A.4 y sus consecuencias por lo que suele decirse que $\mathbb{C}$ es un cuerpo no ordenado.

## Representación Gráfica y Forma Polar

Si se considera la transformación:

$$T : \mathbb{R}^2 \to \mathbb{C} : T(x, y) = x + i \, y$$

Es fácil ver que $T$ es un isomorfismo entre espacios vectoriales por lo tanto se puede decir que $\mathbb{C}$ es isomorfo a $\mathbb{R}^2$ como espacio vectorial. De este modo es posible pensar a un número complejo como un vector en el plano $\mathbb{R}^2$.

### Valor Absoluto o Módulo de un Número Complejo

> **Definición.** Sea $z = a_z + i \, b_z$:
> $$|z| = \sqrt{a_z^2 + b_z^2}$$

Es frecuente usar la notación $\rho = |z|$.

#### Propiedades

i) $|z| \geq 0$ y $|z| = 0 \iff z = 0$
ii) $|z \, w| = |z| \, |w| \quad \forall \, z, w \in \mathbb{C}$
iii) $\left| \dfrac{z}{w} \right| = \dfrac{|z|}{|w|} \quad \forall \, z, w \in \mathbb{C}, \, w \neq 0$
iv) $|z + w| \leq |z| + |w| \quad \forall \, z, w \in \mathbb{C}$
v) $|z - w| \geq |z| - |w| \quad \forall \, z, w \in \mathbb{C}$
vi) $|\text{Re}(z)| \leq |z|$ y $|\text{Im}(z)| \leq |z| \quad \forall \, z \in \mathbb{C}$

### Argumento de un Número Complejo

$$
\arg(z) = \begin{cases}
0 & \text{si } b_z = 0 \text{ y } a_z > 0 \\
\arctan\left( \dfrac{b_z}{a_z} \right) & \text{si } b_z > 0 \text{ y } a_z > 0 \\
\dfrac{\pi}{2} & \text{si } b_z > 0 \text{ y } a_z = 0 \\
\pi - \arctan\left( \dfrac{|b_z|}{|a_z|} \right) & \text{si } b_z > 0 \text{ y } a_z < 0 \\
\pi & \text{si } b_z = 0 \text{ y } a_z < 0 \\
\pi + \arctan\left( \dfrac{|b_z|}{|a_z|} \right) & \text{si } b_z < 0 \text{ y } a_z < 0 \\
\dfrac{3 \pi}{2} & \text{si } b_z < 0 \text{ y } a_z = 0 \\
2 \pi - \arctan\left( \dfrac{|b_z|}{|a_z|} \right) & \text{si } b_z < 0 \text{ y } a_z > 0
\end{cases}
$$

> **Nota.** En el slide aparece el último renglón etiquetado como "si $b_z > 0$ y $a_z > 0$"; por contexto (ya cubierto en el segundo caso) y por la inclusión del término $2\pi - \arctan(\cdot)$, corresponde al cuarto cuadrante: $b_z < 0$ y $a_z > 0$.

#### Propiedades del argumento

i) $\arg(z \, w) = \arg(z) + \arg(w) \quad \forall \, z, w \in \mathbb{C}$
ii) $\arg\left( \dfrac{z}{w} \right) = \arg(z) - \arg(w) \quad \forall \, z, w \in \mathbb{C}, \, w \neq 0$
iii) $\arg(z^n) = n \, \arg(z) \quad \forall \, z \in \mathbb{C}, \, n \in \mathbb{N}$
iv) $\arg(z^{-1}) = -\arg(z) \quad \forall \, z \in \mathbb{C} - \{0\}$

**Notación:** $\theta = \arg(z)$.

### Fórmula de Euler

$$e^{i \theta} = \cos \theta + i \, \sen \theta \qquad \forall \, \theta \in \mathbb{R}$$

## Forma Polar

- **Forma Polar Elemental:** $z = (\rho, \theta)$
- **Forma Polar Trigonométrica:** $z = \rho \cos \theta + i \, \rho \sen \theta$
- **Forma Polar Exponencial:** $z = \rho \, e^{i \theta}$

### Igualdad en forma polar exponencial

Sean $z = \rho_z \, e^{i \theta_z}$ y $w = \rho_w \, e^{i \theta_w}$:

$$z = w \iff |z| = |w| \quad y \quad \arg(z) = \arg(w) + 2 k \pi, \quad k \in \mathbb{Z}$$

En componentes:

$$z = w \iff \rho_z = \rho_w \quad y \quad \theta_z = \theta_w + 2 k \pi, \quad k \in \mathbb{Z}$$

### Multiplicación y división en forma polar exponencial

$$z \, w = |z| \, |w| \, e^{i \, (\arg(z) + \arg(w))} \qquad \frac{z}{w} = \frac{|z|}{|w|} \, e^{i \, (\arg(z) - \arg(w))}$$

En componentes:

$$z \, w = \rho_z \, \rho_w \, e^{i (\theta_z + \theta_w)} \qquad \frac{z}{w} = \frac{\rho_z}{\rho_w} \, e^{i (\theta_z - \theta_w)}$$

> **Nota.** El slide tiene una errata: escribe $\dfrac{z}{w} = \dfrac{\rho_z}{\rho_z} \, e^{i(\theta_z - \theta_w)}$. La forma correcta es la usada arriba: $\dfrac{\rho_z}{\rho_w}$.

## Potenciación y Fórmula de De Moivre

### Potenciación

$$z^n = |z|^n \, e^{i \, n \, \arg(z)} \quad \text{con } n \in \mathbb{N}$$

$$z^n = |z|^n \cos(n \, \arg(z)) + i \, |z|^n \sen(n \, \arg(z))$$

Si la escribimos en componentes queda, con $z = \rho_z \, e^{i \theta_z}$ y $n \in \mathbb{N}$:

$$z^n = \rho_z^n \, e^{i \, n \, \theta_z}$$

$$z^n = \rho_z^n \cos(n \, \theta_z) + i \, \rho_z^n \sen(n \, \theta_z)$$

## Radicación

Dada la ecuación

$$w^n = z, \qquad n \in \mathbb{N}$$

Se deduce que:

$$w_k = \sqrt[n]{\rho_z} \, e^{i \left( \frac{\theta_z + 2 k \pi}{n} \right)}$$

con $k = 0, \dots, n - 1$.

**Observación:** En el caso particular de raíces cuadradas $n = 2$, la ecuación $w^2 = z$ tiene por soluciones

$$\text{Re}(w) = \pm \sqrt{\frac{|z| + \text{Re}(z)}{2}}, \qquad \text{Im}(w) = \pm \sqrt{\frac{|z| - \text{Re}(z)}{2}}$$

Se cumple que $2 \, \text{Re}(w) \, \text{Im}(w) = \text{Im}(z)$. De ahí se eligen los signos.

## Logaritmación y Potencia

### Logaritmación

Dada la ecuación

$$e^w = z$$

Se demuestra que las soluciones son

$$w_k = \ln|z| + i \, (\arg(z) + 2 k \pi), \quad k \in \mathbb{Z}$$

A veces se trabaja en el valor principal del logaritmo dado por

$$w_0 = \ln|z| + i \, \arg(z)$$

### Potencia Compleja

$$z^w = e^{w \, \ln z}$$

## Conjugación

> **Definición.** Sea $z \in \mathbb{C}$, se define el conjugado de $z$ al único número $w \in \mathbb{C}$ que cumple
> $$\text{Re}(w) = \text{Re}(z) \quad y \quad \text{Im}(w) = -\text{Im}(z)$$
> **Notación:** $w = \bar{z}$.

### Propiedades

i) $\bar{z} = z \iff \text{Im}(z) = 0$
ii) $\overline{z + w} = \bar{z} + \bar{w}$
iii) $\overline{z \, w} = \bar{z} \, \bar{w}$
iv) $\overline{\left( \dfrac{z}{w} \right)} = \dfrac{\bar{z}}{\bar{w}}$
v) $z \, \bar{z} = |z|^2$
vi) $z + \bar{z} = 2 \, \text{Re}(z)$
vii) $z - \bar{z} = 2 \, i \, \text{Im}(z)$
viii) $|\bar{z}| = |z|$

---

## Ver también

- [[02-vectores-cn-rn]] — vectores en $\mathbb{C}^n$ y $\mathbb{R}^n$
- [[03-matrices]] — matrices sobre $\mathbb{R}$ y $\mathbb{C}$
- [[04-determinantes]] — determinantes
