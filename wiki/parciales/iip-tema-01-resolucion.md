---
tags: [parcial, iip, resolucion, fourier, serie-trigonometrica, serie-exponencial, forma-laboratorio, transformada-fourier]
fuente: raw/Practicas/Modelos_Examenes/MNA_IIP_Tema_I.pdf
tipo: iip
tema: 1
tiene_resolucion: true
---

# Segundo Parcial de Métodos Numéricos Avanzados — Tema I (Resolución)

Convenciones de la cátedra (ver [[../guias/guia-08-fourier-series]] y [[../resueltos/resueltos-fourier]]). Para una función de período $T$,
$$f(t) = a_0 + \sum_{n=1}^{\infty} a_n\cos\!\Big(\tfrac{2\pi n}{T}t\Big) + \sum_{n=1}^{\infty} b_n\sin\!\Big(\tfrac{2\pi n}{T}t\Big),$$
con el **valor medio** $a_0=\tfrac1T\int_T f$, y $a_n=\tfrac2T\int_T f\cos(\tfrac{2\pi n}{T}t)\,dt$, $b_n=\tfrac2T\int_T f\sin(\tfrac{2\pi n}{T}t)\,dt$. La serie exponencial es $f(t)=\sum_{n\in\mathbb Z}c_n e^{i2\pi n t/T}$ con $c_n=\tfrac1T\int_T f\,e^{-i2\pi n t/T}dt$, y vale $a_0=c_0$, $a_n=c_n+c_{-n}$, $b_n=i(c_n-c_{-n})$. La transformada de Fourier es $\hat x(\omega)=\int_{-\infty}^\infty x(t)e^{-i\omega t}dt$.

---

## Ejercicio 1

Sea la función $x(t) = e^t$ en el intervalo $(-\pi, \pi)$, con $x(t) = x(t + 2\pi)$ (período $T = 2\pi$).

a) Hallar la Serie Trigonométrica de Fourier de $x(t)$.
b) Usando el desarrollo hallado en a), probar que
$$\sum_{n=1}^{\infty} \frac{(-1)^n}{n^2 + 1} = \frac{1 - \dfrac{\sh(\pi)}{\pi}}{\dfrac{2\sh(\pi)}{\pi}}, \qquad \text{donde } \sh(\pi) = \frac{e^\pi - e^{-\pi}}{2}.$$

### Resolución

Como $T = 2\pi$, la frecuencia fundamental es $\tfrac{2\pi}{T} = 1$, de modo que los armónicos son $\cos(nt)$ y $\sin(nt)$. Usaremos repetidamente que $\sh(\pi)=\sinh(\pi)=\tfrac{e^\pi-e^{-\pi}}{2}$ y que la primitiva $\int e^t\cos(nt)\,dt = \dfrac{e^t(\cos nt + n\sin nt)}{1+n^2}$, $\int e^t\sin(nt)\,dt = \dfrac{e^t(\sin nt - n\cos nt)}{1+n^2}$.

#### a) Coeficientes

**Término medio $a_0$.**
$$a_0 = \frac{1}{2\pi}\int_{-\pi}^{\pi} e^t\,dt = \frac{1}{2\pi}\Big[e^t\Big]_{-\pi}^{\pi} = \frac{e^\pi - e^{-\pi}}{2\pi} = \frac{\sh(\pi)}{\pi}.$$

**Coeficientes coseno $a_n$** (con $\tfrac{2\pi}{T}=1$):
$$a_n = \frac{1}{\pi}\int_{-\pi}^{\pi} e^t\cos(nt)\,dt = \frac{1}{\pi}\left[\frac{e^t(\cos nt + n\sin nt)}{1+n^2}\right]_{-\pi}^{\pi}.$$
En los extremos $t=\pm\pi$ es $\sin(n\pi)=0$ y $\cos(n\pi)=(-1)^n$, así que
$$a_n = \frac{1}{\pi}\cdot\frac{(-1)^n\big(e^\pi - e^{-\pi}\big)}{1+n^2} = \frac{1}{\pi}\cdot\frac{2(-1)^n\,\sh(\pi)}{1+n^2} = \frac{\sh(\pi)}{\pi}\cdot\frac{2(-1)^n}{1+n^2}.$$

**Coeficientes seno $b_n$:**
$$b_n = \frac{1}{\pi}\int_{-\pi}^{\pi} e^t\sin(nt)\,dt = \frac{1}{\pi}\left[\frac{e^t(\sin nt - n\cos nt)}{1+n^2}\right]_{-\pi}^{\pi} = \frac{1}{\pi}\cdot\frac{-n(-1)^n\big(e^\pi - e^{-\pi}\big)}{1+n^2},$$
$$b_n = \frac{\sh(\pi)}{\pi}\cdot\frac{-2n(-1)^n}{1+n^2}.$$

$$\boxed{\;x(t) = \frac{\sh(\pi)}{\pi}\left[1 + \sum_{n=1}^{\infty}\frac{2(-1)^n}{1+n^2}\cos(nt) - \sum_{n=1}^{\infty}\frac{2n(-1)^n}{1+n^2}\sin(nt)\right].\;}$$

> **Verificación numérica.** Integrando $a_0,a_n,b_n$ con cuadratura (`scipy.integrate.quad`) para $n=1,\dots,5$ se obtiene exactamente las fórmulas anteriores (diferencias $<10^{-15}$). Reconstruyendo la serie con $2000$ armónicos en $t=1$ (punto de continuidad) da $2.7169 \approx e^1 = 2.7183$, y en el salto $t=\pi$ converge a $\cosh(\pi)=11.592$ (promedio $\tfrac12(e^\pi+e^{-\pi})$), como predice Dirichlet.

#### b) La identidad

La función $x(t)=e^t$ es continua en $t=0$ (no hay salto allí: el único salto del período está en $t=\pm\pi$). Por el **teorema de convergencia puntual de Dirichlet**, en un punto de continuidad la serie converge al valor de la función:
$$\text{serie}(0) = x(0) = e^0 = 1.$$

Evaluamos la serie en $t=0$. Como $\cos(0)=1$ y $\sin(0)=0$, los términos en seno se anulan:
$$1 = \frac{\sh(\pi)}{\pi}\left[1 + \sum_{n=1}^{\infty}\frac{2(-1)^n}{1+n^2}\right] = \frac{\sh(\pi)}{\pi}\left[1 + 2\sum_{n=1}^{\infty}\frac{(-1)^n}{1+n^2}\right].$$

Despejamos la suma. Dividiendo por $\tfrac{\sh(\pi)}{\pi}$:
$$\frac{\pi}{\sh(\pi)} = 1 + 2\sum_{n=1}^{\infty}\frac{(-1)^n}{1+n^2} \;\Longrightarrow\; 2\sum_{n=1}^{\infty}\frac{(-1)^n}{1+n^2} = \frac{\pi}{\sh(\pi)} - 1.$$

Para llevarlo a la forma del enunciado, partimos de $1 = \tfrac{\sh(\pi)}{\pi}\big(1 + 2S\big)$ con $S=\sum\tfrac{(-1)^n}{1+n^2}$ y despejamos $S$ directamente:
$$1 + 2S = \frac{\pi}{\sh(\pi)} = \frac{1}{\sh(\pi)/\pi} \;\Longrightarrow\; 2S = \frac{1}{\sh(\pi)/\pi} - 1 = \frac{1 - \sh(\pi)/\pi}{\sh(\pi)/\pi},$$
$$\boxed{\;\sum_{n=1}^{\infty}\frac{(-1)^n}{n^2+1} = \frac{1 - \dfrac{\sh(\pi)}{\pi}}{\dfrac{2\,\sh(\pi)}{\pi}}.\;}$$
que es exactamente la igualdad pedida.

> **Verificación numérica.** Sumando $\sum_{n=1}^{2\cdot10^5}\tfrac{(-1)^n}{n^2+1} = -0.363985\ldots$, mientras que el miembro derecho $\dfrac{1-\sh(\pi)/\pi}{2\sh(\pi)/\pi} = -0.363985\ldots$ (coinciden hasta $10^{-11}$; la serie alternada converge lento). El valor cerrado equivalente es $\tfrac12\big(\tfrac{\pi}{\sinh\pi}-1\big)$.

---

## Ejercicio 2

Dada la función $x(t) = t - [t]$ (parte fraccionaria, período $T = 1$):

a) Hallar la Serie Trigonométrica de Fourier de $x(t)$.
b) Hallar la Serie Exponencial de Fourier de $x(t)$.
c) Hallar la Forma de Laboratorio de la Serie Trigonométrica de Fourier de $x(t)$.

### Resolución

$x(t)=t-[t]$ es la **parte fraccionaria**: un diente de sierra que en cada período $[0,1)$ vale $x(t)=t$ y salta de $1^-$ a $0$ en los enteros. Tiene período $T=1$, así que la frecuencia fundamental es $\tfrac{2\pi}{T}=2\pi$ y los armónicos son $\cos(2\pi n t)$, $\sin(2\pi n t)$. Integramos sobre un período, $[0,1)$, donde $x(t)=t$.

#### a) Serie trigonométrica

**Valor medio:**
$$a_0 = \frac{1}{1}\int_0^1 t\,dt = \left[\frac{t^2}{2}\right]_0^1 = \frac{1}{2}.$$

**Coeficientes coseno.** Por partes, $\int t\cos(2\pi n t)\,dt = \dfrac{t\sin(2\pi n t)}{2\pi n} + \dfrac{\cos(2\pi n t)}{(2\pi n)^2}$:
$$a_n = \frac{2}{1}\int_0^1 t\cos(2\pi n t)\,dt = 2\left[\frac{t\sin(2\pi n t)}{2\pi n} + \frac{\cos(2\pi n t)}{(2\pi n)^2}\right]_0^1.$$
En $t=1$ y $t=0$ es $\sin(2\pi n)=0$ y $\cos(2\pi n)=\cos 0 = 1$, así que ambos corchetes coinciden y la diferencia se anula:
$$a_n = 0 \qquad (n\ge 1).$$
(Era esperable que no se anulara por simetría — el diente de sierra no es par ni impar respecto del origen del período —, pero al integrar sobre $[0,1)$ con $x(t)=t$ el término coseno se cancela exactamente.)

**Coeficientes seno.** Por partes, $\int t\sin(2\pi n t)\,dt = -\dfrac{t\cos(2\pi n t)}{2\pi n} + \dfrac{\sin(2\pi n t)}{(2\pi n)^2}$:
$$b_n = 2\int_0^1 t\sin(2\pi n t)\,dt = 2\left[-\frac{t\cos(2\pi n t)}{2\pi n} + \frac{\sin(2\pi n t)}{(2\pi n)^2}\right]_0^1 = 2\left(-\frac{1\cdot 1}{2\pi n} + 0\right) = -\frac{1}{\pi n}.$$

$$\boxed{\;x(t) = \frac{1}{2} - \sum_{n=1}^{\infty}\frac{1}{\pi n}\sin(2\pi n t).\;}$$

> **Verificación numérica.** Cuadratura de $a_0,a_n,b_n$ para $n=1,\dots,5$: $a_0=0.5$, $a_n\approx 0$, $b_n=-\tfrac1{\pi n}$ ($b_1=-0.31831$, $b_2=-0.15915$, …), todo coincidente. La serie con $5000$ armónicos en $t=0.3$ da $0.30002\approx 0.3$ (continuidad) y en el salto $t=0$ da $0.5$ = promedio $\tfrac12(0+1)$ (Dirichlet). ✓

#### b) Serie exponencial

$$c_0 = \int_0^1 t\,dt = \frac{1}{2}.$$
Para $n\ne 0$, por partes con $u=t$, $dv=e^{-i2\pi n t}dt$, $v=\dfrac{e^{-i2\pi n t}}{-i2\pi n}$:
$$c_n = \int_0^1 t\,e^{-i2\pi n t}\,dt = \left[\frac{t\,e^{-i2\pi n t}}{-i2\pi n}\right]_0^1 - \int_0^1 \frac{e^{-i2\pi n t}}{-i2\pi n}\,dt.$$
El primer término en $t=1$ usa $e^{-i2\pi n}=1$, y en $t=0$ se anula: vale $\dfrac{1}{-i2\pi n}$. La integral restante es
$$-\frac{1}{-i2\pi n}\int_0^1 e^{-i2\pi n t}\,dt = -\frac{1}{-i2\pi n}\cdot\underbrace{\left[\frac{e^{-i2\pi n t}}{-i2\pi n}\right]_0^1}_{=\,0\ (\text{pues } e^{-i2\pi n}=1)} = 0.$$
Por lo tanto
$$c_n = \frac{1}{-i2\pi n} = \frac{i}{2\pi n} \qquad (n\ne 0),$$
usando $\tfrac{1}{-i}=i$.

$$\boxed{\;c_0 = \frac{1}{2}, \qquad c_n = \frac{i}{2\pi n}\ \ (n\ne 0), \qquad x(t) = \frac{1}{2} + \sum_{\substack{n\in\mathbb Z\\ n\ne 0}}\frac{i}{2\pi n}\,e^{i2\pi n t}.\;}$$

**Coherencia con a).** Como $x$ es real, debe valer $c_{-n}=\overline{c_n}$: en efecto $c_{-n}=\tfrac{i}{2\pi(-n)}=-\tfrac{i}{2\pi n}=\overline{c_n}$. ✓ Y se recupera la serie trigonométrica:
$$a_n = c_n + c_{-n} = \frac{i}{2\pi n} - \frac{i}{2\pi n} = 0, \qquad b_n = i(c_n - c_{-n}) = i\left(\frac{i}{2\pi n} + \frac{i}{2\pi n}\right) = i\cdot\frac{2i}{2\pi n} = -\frac{1}{\pi n}. \checkmark$$

> **Verificación numérica.** Cuadratura compleja de $c_n$ para $n=-3,\dots,3$: $c_0=0.5$, $c_1=0+0.15915i=\tfrac{i}{2\pi}$, $c_{-1}=-0.15915i$, etc., exactos. Las relaciones $a_n=c_n+c_{-n}=0$ y $b_n=i(c_n-c_{-n})=-\tfrac1{\pi n}$ se reproducen numéricamente. ✓

#### c) Forma de laboratorio

La forma de laboratorio reescribe $x(t)=a_0 + \sum_{n\ge1}A_n\cos\big(2\pi n t - \varphi_n\big)$ con amplitud $A_n=\sqrt{a_n^2+b_n^2}$ y fase dada por $\tan\varphi_n = b_n/a_n$ (interpretando $a_n=A_n\cos\varphi_n$, $b_n=A_n\sin\varphi_n$).

Con $a_n=0$ y $b_n=-\tfrac{1}{\pi n}$:
$$A_n = \sqrt{0^2 + \left(\frac{1}{\pi n}\right)^2} = \frac{1}{\pi n}.$$
Para la fase: $a_n = A_n\cos\varphi_n = 0 \Rightarrow \cos\varphi_n = 0 \Rightarrow \varphi_n = \pm\tfrac{\pi}{2}$; y $b_n = A_n\sin\varphi_n < 0$ con $A_n>0 \Rightarrow \sin\varphi_n<0 \Rightarrow$
$$\varphi_n = -\frac{\pi}{2}.$$

$$\boxed{\;x(t) = \frac{1}{2} + \sum_{n=1}^{\infty}\frac{1}{\pi n}\cos\!\left(2\pi n t + \frac{\pi}{2}\right) = \frac{1}{2} + \sum_{n=1}^{\infty}\frac{1}{\pi n}\cos\!\left(2\pi n t - \varphi_n\right),\quad \varphi_n = -\frac{\pi}{2}.\;}$$

(Consistente con $\cos(\theta+\tfrac{\pi}{2})=-\sin\theta$, que devuelve exactamente $-\tfrac{1}{\pi n}\sin(2\pi n t)$.)

> **Verificación numérica.** $A_n=\tfrac1{\pi n}$ coincide con $|b_n|$, y graficando $A_n\cos(2\pi n t - \varphi_n)$ con $\varphi_n=-\tfrac\pi2$ contra $a_n\cos(\cdot)+b_n\sin(\cdot)$ la diferencia máxima es $<10^{-16}$. ✓

---

## Ejercicio 3

Dada la función $x(t) = t$ si $0 \le t \le 1$ y $x(t) = 0$ si $t < 0$ o $t > 1$:

a) Hallar la Transformada de Fourier de $x(t)$.
b) Graficar en forma aproximada el espectro de frecuencias de $x(t)$.

### Resolución

A diferencia de los anteriores, esta función **no es periódica**: es una rampa de soporte compacto en $[0,1]$. Le corresponde la **transformada de Fourier** (espectro continuo), no una serie.

#### a) Transformada de Fourier

Por definición, integrando sólo sobre el soporte $[0,1]$:
$$\hat x(\omega) = \int_{-\infty}^{\infty} x(t)\,e^{-i\omega t}\,dt = \int_0^1 t\,e^{-i\omega t}\,dt.$$

**Integración por partes** con $u=t$, $dv=e^{-i\omega t}\,dt$, de donde $du=dt$, $v=\dfrac{e^{-i\omega t}}{-i\omega}$:
$$\hat x(\omega) = \left[\frac{t\,e^{-i\omega t}}{-i\omega}\right]_0^1 - \int_0^1 \frac{e^{-i\omega t}}{-i\omega}\,dt = \frac{e^{-i\omega}}{-i\omega} - \frac{1}{-i\omega}\left[\frac{e^{-i\omega t}}{-i\omega}\right]_0^1.$$
La integral restante es $\dfrac{1}{-i\omega}\cdot\dfrac{e^{-i\omega}-1}{-i\omega} = \dfrac{e^{-i\omega}-1}{(-i\omega)^2} = \dfrac{e^{-i\omega}-1}{-\omega^2}$ (pues $(-i\omega)^2=-\omega^2$). Entonces
$$\hat x(\omega) = \frac{e^{-i\omega}}{-i\omega} - \frac{e^{-i\omega}-1}{-\omega^2}.$$

Llevando todo a denominador común $-\omega^2$ (multiplicamos el primer término por $\tfrac{-i\omega}{-i\omega}$, usando $\tfrac{1}{-i\omega}=\tfrac{-i\omega}{-\omega^2}$):
$$\hat x(\omega) = \frac{-i\omega\,e^{-i\omega}}{-\omega^2} - \frac{e^{-i\omega}-1}{-\omega^2} = \frac{-i\omega\,e^{-i\omega} - e^{-i\omega} + 1}{-\omega^2},$$
$$\boxed{\;\hat x(\omega) = \frac{e^{-i\omega}\big(-i\omega - 1\big) + 1}{-\,\omega^2}.\;}$$

Separando en partes real e imaginaria (con $e^{-i\omega}=\cos\omega - i\sin\omega$):
$$\operatorname{Re}\hat x(\omega) = \frac{\omega\sin\omega + \cos\omega - 1}{\omega^2}, \qquad \operatorname{Im}\hat x(\omega) = \frac{\omega\cos\omega - \sin\omega}{\omega^2}.$$

**Valor en $\omega=0$.** Por L'Hôpital (o directamente $\hat x(0)=\int_0^1 t\,dt$):
$$\hat x(0) = \int_0^1 t\,dt = \frac{1}{2}.$$
Es el área bajo la rampa; la expresión cerrada tiende a $\tfrac12$ cuando $\omega\to0$ (no es una singularidad real).

> **Verificación numérica.** Integrando $\int_0^1 t\,e^{-i\omega t}dt$ con cuadratura para $\omega\in\{0.5,1,2,3,\pi,5,-2\}$ se obtiene exactamente la fórmula encajonada (p.ej. $\hat x(1)=0.38177-0.30117i$, $\hat x(2)=0.10061-0.43540i$), con diferencias $<10^{-15}$. El límite $\omega\to0$ confirmado analíticamente con `sympy` es $\tfrac12$. ✓

#### b) Espectro de frecuencias

El **espectro de amplitud** es el módulo $|\hat x(\omega)|$. A partir de Re e Im:
$$|\hat x(\omega)|^2 = \frac{(\omega\sin\omega + \cos\omega - 1)^2 + (\omega\cos\omega - \sin\omega)^2}{\omega^4} = \frac{\omega^2 + 2 - 2\cos\omega - 2\omega\sin\omega}{\omega^4},$$
$$\boxed{\;|\hat x(\omega)| = \frac{\sqrt{\,\omega^2 + 2 - 2\cos\omega - 2\omega\sin\omega\,}}{\omega^2}.\;}$$

Características del gráfico de $|\hat x(\omega)|$ (función **par** en $\omega$, pues $x$ es real):

- **Máximo en el origen:** $|\hat x(0)| = \tfrac12$. Es el pico del espectro (componente de baja frecuencia / valor medio del pulso).
- **Decaimiento global $\sim 1/\omega$:** el numerador crece como $|\omega|$ (domina el término $\omega^2$ bajo la raíz), de modo que $|\hat x(\omega)|\sim \dfrac{|\omega|}{\omega^2}=\dfrac{1}{|\omega|}$ para $|\omega|$ grande. El decaimiento lento ($1/\omega$) es típico de una señal con **discontinuidad de salto** (aquí el salto está en el borde $t=1$, donde $x$ pasa de $1$ a $0$).
- **Oscilaciones / lóbulos:** los términos $\cos\omega$ y $\omega\sin\omega$ producen una envolvente con lóbulos sucesivos (similar a un $\operatorname{sinc}$), decrecientes en altura, montados sobre la caída $1/|\omega|$. No hay ceros exactos del módulo en general (a diferencia del pulso rectangular puro), porque la parte real y la imaginaria no se anulan simultáneamente.

```
|x̂(ω)|
0.5 ┤●                          (pico en ω=0)
    │ ╲
    │  ╲___        lóbulos decrecientes
    │      ╲__  __        envolvente ~ 1/|ω|
    │         ╲╱  ╲_  _
    │              ╲╱ ╲__ _
  0 └──────────────────────────► ω
    0    π   2π   3π   4π
```

> **Verificación numérica.** $|\hat x(\omega)|$ evaluado en $\omega=0.5,1,2,3,5$ da $0.49654, 0.48627, 0.44687, 0.38703, 0.24007$ — decreciente y bien ajustado a $\tfrac{\sqrt{\omega^2+2-2\cos\omega-2\omega\sin\omega}}{\omega^2}$. Límite $\omega\to0$: $\tfrac12$. ✓

---

## Resumen de resultados

| Ej. | Resultado |
|-----|-----------|
| 1a | $x(t) = \tfrac{\sh\pi}{\pi}\big[1 + \sum_{n\ge1}\tfrac{2(-1)^n}{1+n^2}\cos nt - \sum_{n\ge1}\tfrac{2n(-1)^n}{1+n^2}\sin nt\big]$ |
| 1b | $\sum_{n\ge1}\tfrac{(-1)^n}{n^2+1} = \dfrac{1-\sh\pi/\pi}{2\sh\pi/\pi} = \tfrac12\big(\tfrac{\pi}{\sinh\pi}-1\big)$ (evaluar en $t=0$) |
| 2a | $a_0=\tfrac12,\ a_n=0,\ b_n=-\tfrac1{\pi n}$ |
| 2b | $c_0=\tfrac12,\ c_n=\tfrac{i}{2\pi n}\ (n\ne0)$ |
| 2c | $A_n=\tfrac1{\pi n},\ \varphi_n=-\tfrac\pi2$: $\ x(t)=\tfrac12+\sum_{n\ge1}\tfrac1{\pi n}\cos(2\pi n t+\tfrac\pi2)$ |
| 3a | $\hat x(\omega) = \dfrac{e^{-i\omega}(-i\omega-1)+1}{-\omega^2}$, $\ \hat x(0)=\tfrac12$ |
| 3b | $\lvert\hat x(\omega)\rvert = \dfrac{\sqrt{\omega^2+2-2\cos\omega-2\omega\sin\omega}}{\omega^2}$, par, pico $\tfrac12$ en $0$, decae $\sim1/\lvert\omega\rvert$ |

Enunciado sin resolver: [[iip-tema-01]]. Material relacionado: [[../guias/guia-08-fourier-series]], [[../guias/guia-09-tf]], [[../resueltos/resueltos-fourier]].
