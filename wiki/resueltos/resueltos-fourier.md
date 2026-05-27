---
tags: [resueltos, fourier, transformada-continua]
fuente: raw/Practicas/Ejercicios_Resueltos/Ejercicios_Transformadas_Fourier_Resueltos.pdf
unidad: IX
---

# Ejercicios Resueltos — Transformadas de Fourier

Ver enunciados relacionados en [[../guias/guia-09-tf]].

## Ejercicio 1

Hallar la Transformada de Fourier de las siguientes funciones.

**a)** $x(t) = e^{-at}$ con $t \ge 0 \wedge a > 0$

**b)** $f(t) = u\!\left(t + \tfrac{a}{2}\right) - u\!\left(t - \tfrac{a}{2}\right)$ (pulso rectangular)

**c)** $\Lambda_n : [-n, n] \to \mathbb{R} : \Lambda_n(t) = \dfrac{n - |t|}{n^2}$

**d)** $f(t) = e^{\beta t}\, e^{i\alpha t}$, $t \ge 0$

**e)** $f(t) = e^{-t^2}$ (gaussiana)

### Resolución

**a)** Por definición:

$$\mathcal{F}\{x(t)\} = \int_0^\infty e^{-at}\, e^{-i\omega t}\, dt \Rightarrow \mathcal{F}\{x(t)\} = \int_0^\infty e^{-(a + i\omega) t}\, dt$$

Calculando la integral impropia:

$$\lim_{\lambda \to \infty} \int_0^\lambda e^{-(a + i\omega) t}\, dt = \lim_{\lambda \to \infty} \left.\frac{e^{-(a + i\omega) t}}{-(a + i\omega)}\right|_0^\lambda = \lim_{\lambda \to \infty} \frac{e^{-(a + i\omega)\lambda} - 1}{-(a + i\omega)} = \frac{1}{a + i\omega}$$

$$\boxed{F(\omega) = \frac{1}{a + i\omega}}$$

**b)** El pulso rectangular de ancho $a$ centrado en el origen.

$$\mathcal{F}\{f(t)\} = \int_{-a/2}^{a/2} e^{-i\omega t}\, dt = \left.\frac{e^{-i\omega t}}{-i\omega}\right|_{-a/2}^{a/2} = \frac{e^{i\omega\frac{a}{2}} - e^{-i\omega\frac{a}{2}}}{i\omega}$$

$$= \frac{2\sin\!\left(\omega\,\tfrac{a}{2}\right)}{\omega}$$

$$\boxed{F(\omega) = a\,\frac{\sin\!\left(\omega\,\tfrac{a}{2}\right)}{\omega\,\tfrac{a}{2}} = a\,\operatorname{sinc}\!\left(\tfrac{\omega a}{2}\right)}$$

**c)** Para el triángulo $\Lambda_n$:

$$\mathcal{F}\{\Lambda_n(t)\} = \int_{-n}^{n} \frac{n - |t|}{n^2}\, e^{-i\omega t}\, dt$$

Separando:

$$= \frac{1}{n}\int_{-n}^{n} e^{-i\omega t}\, dt - \frac{1}{n^2}\int_{-n}^{n} |t|\, e^{-i\omega t}\, dt$$

$$= \left.\frac{e^{-i\omega t}}{-i\omega\, n}\right|_{-n}^{n} - \frac{1}{n^2}\left[\int_{-n}^{0} -t\, e^{-i\omega t}\, dt + \int_{0}^{n} t\, e^{-i\omega t}\, dt\right]$$

Si en la primera integral se hace $t \to -t$, se tiene $\int_{0}^{n} t\, e^{i\omega t}\, dt$. Reemplazando:

$$\mathcal{F}\{\Lambda_n(t)\} = \frac{e^{i\omega n} - e^{-i\omega n}}{i\omega n} - \frac{1}{n^2} \int_{0}^{n} t(e^{i\omega t} + e^{-i\omega t})\, dt$$

$$= 2\frac{\sin(\omega n)}{\omega n} - \frac{2}{n^2}\int_{0}^{n} t\cos(\omega t)\, dt$$

Calculando la integral por partes ($\int t\cos(\omega t)\,dt = \tfrac{t\sin(\omega t)}{\omega} + \tfrac{\cos(\omega t)}{\omega^2}$):

$$\mathcal{F}\{\Lambda_n(t)\} = 2\frac{\sin(\omega n)}{\omega n} - \frac{2}{n^2}\left[\frac{t\sin(\omega t)}{\omega} + \frac{\cos(\omega t)}{\omega^2}\right]_0^n$$

$$= 2\frac{\sin(\omega n)}{\omega n} - \frac{2}{n^2}\left[\frac{n\sin(\omega n)}{\omega} + \frac{\cos(\omega n)}{\omega^2} - \frac{1}{\omega^2}\right]$$

$$= -2\frac{\cos(\omega n)}{(\omega n)^2} + \frac{2}{(\omega n)^2} = 2\,\frac{1 - \cos(\omega n)}{(\omega n)^2} = \frac{\sin^2\!\left(\tfrac{\omega n}{2}\right)}{\left(\tfrac{\omega n}{2}\right)^2}$$

$$\boxed{F(\omega) = \operatorname{sinc}^2\!\left(\tfrac{\omega n}{2}\right)}$$

**d)** $f(t) = e^{(\beta + i\alpha) t}$ para $t \ge 0$:

$$\mathcal{F}\{f(t)\} = \int_0^\infty e^{(\beta + i\alpha) t}\, e^{-i\omega t}\, dt = \int_0^\infty e^{(\beta + i(\alpha - \omega)) t}\, dt$$

Análogo a (a), para que la integral converja debe ser $\beta < 0$ (en cuyo caso):

$$F(\omega) = \frac{1}{-\beta - i(\alpha - \omega)} = \frac{1}{-\beta + i(\omega - \alpha)}$$

**e)** Gaussiana $f(t) = e^{-t^2}$:

$$\mathcal{F}\{e^{-t^2}\} = \int_{-\infty}^{\infty} e^{-t^2}\, e^{-i\omega t}\, dt$$

Completando cuadrados $-t^2 - i\omega t = -(t + i\omega/2)^2 - \omega^2/4$:

$$= e^{-\omega^2/4}\int_{-\infty}^{\infty} e^{-(t + i\omega/2)^2}\, dt = \sqrt{\pi}\, e^{-\omega^2/4}$$

$$\boxed{F(\omega) = \sqrt{\pi}\, e^{-\omega^2/4}}$$

(La gaussiana es eigenfunción de la TF: su transformada es otra gaussiana.)
