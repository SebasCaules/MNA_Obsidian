---
tags: [parcial, iip, resolucion, fourier, serie-trigonometrica, serie-exponencial, forma-laboratorio, transformada-fourier]
fuente: raw/Practicas/Modelos_Examenes/MNA_IIP_Tema_III.pdf
tipo: iip
tema: 3
tiene_resolucion: true
---

# Segundo Parcial de Métodos Numéricos Avanzados — Tema III (Resolución)

> Convención de la cátedra (período $T$):
> $$f(t) = a_0 + \sum_{n=1}^{\infty} a_n\cos\!\Big(\tfrac{2\pi n}{T}t\Big) + \sum_{n=1}^{\infty} b_n\sin\!\Big(\tfrac{2\pi n}{T}t\Big),$$
> con $a_0=\dfrac1T\displaystyle\int_T f$ (**valor medio**), $a_n=\dfrac2T\displaystyle\int_T f\cos(\tfrac{2\pi n}{T}t)\,dt$, $b_n=\dfrac2T\displaystyle\int_T f\sin(\tfrac{2\pi n}{T}t)\,dt$.
> Material relacionado: [[../guias/guia-08-fourier-series]], [[../resueltos/resueltos-fourier]], [[iip-tema-01]].

---

## Ejercicio 1

Sea la función $x(t) = t + 1$ en el intervalo $(0, 1)$, con $x(t) = x(t + 1)$ (período $T = 1$).

a) Hallar la Serie Trigonométrica de Fourier de $x(t)$.
b) Usando el desarrollo hallado en a) pruebe que
$$\sum_{n=1}^{\infty} \frac{(-1)^n}{n^2 + 1} = \frac{1 - \dfrac{\operatorname{sh}(\pi)}{\pi}}{\dfrac{2\operatorname{sh}(\pi)}{\pi}},\qquad \operatorname{sh}(\pi) = \frac{e^\pi - e^{-\pi}}{2}.$$

### Resolución

**a)** La función es una diente de sierra desplazada: en cada período de longitud $T=1$ vale $t+1$, subiendo linealmente de $1$ (en $t\to0^+$) a $2$ (en $t\to1^-$) y con un salto al volver a empezar. La frecuencia fundamental es $\omega_0 = \tfrac{2\pi}{T} = 2\pi$.

**Coeficiente $a_0$** (valor medio):
$$a_0 = \frac1T\int_0^1 (t+1)\,dt = \left.\frac{t^2}{2}+t\right|_0^1 = \frac12 + 1 = \boxed{\frac32}.$$

**Coeficientes $a_n$.** Integrando por partes $\int (t+1)\cos(2\pi n t)\,dt$ con $u=t+1$, $dv=\cos(2\pi n t)\,dt$:
$$a_n = 2\int_0^1 (t+1)\cos(2\pi n t)\,dt = 2\left[\frac{(t+1)\sin(2\pi n t)}{2\pi n} + \frac{\cos(2\pi n t)}{(2\pi n)^2}\right]_0^1.$$
En $t=0$ y $t=1$ es $\sin(2\pi n t)=0$ y $\cos(2\pi n t)=1$, de modo que el corchete vale lo mismo en ambos extremos y la resta se anula:
$$\boxed{a_n = 0\quad\text{para todo } n\ge1.}$$

**Coeficientes $b_n$.** Análogamente, $\int (t+1)\sin(2\pi n t)\,dt$ con $u=t+1$, $dv=\sin(2\pi n t)\,dt$:
$$b_n = 2\int_0^1 (t+1)\sin(2\pi n t)\,dt = 2\left[-\frac{(t+1)\cos(2\pi n t)}{2\pi n} + \frac{\sin(2\pi n t)}{(2\pi n)^2}\right]_0^1.$$
El término con $\sin$ se anula en ambos extremos. Para el primer término, con $\cos(2\pi n)=\cos 0=1$:
$$b_n = 2\left[-\frac{(1+1)\cdot 1}{2\pi n} + \frac{(0+1)\cdot 1}{2\pi n}\right] = 2\cdot\left(-\frac{2-1}{2\pi n}\right) = 2\cdot\left(-\frac{1}{2\pi n}\right) = \boxed{-\frac{1}{\pi n}.}$$

**Serie trigonométrica:**
$$\boxed{\,x(t) = \frac32 - \sum_{n=1}^{\infty}\frac{1}{\pi n}\,\sin(2\pi n t).\,}$$

*Verificación numérica.* Integrando $a_0$, $a_n$ y $b_n$ con cuadratura: $a_0=1.5$ exacto; $a_n\sim10^{-16}$ (cero numérico); $b_n=-0.318310,-0.159155,-0.106103,\dots$ que coincide con $-\tfrac{1}{\pi n}=-0.318310,-0.159155,\dots$. La suma parcial $S_{500}(t)$ da $S(0.25)=1.2503\approx1.25$, $S(0.5)=1.5000$, $S(0.75)=1.7497\approx1.75$, reproduciendo $x(t)=t+1$. En el salto $t=0$ la serie converge a $\tfrac12\big(x(0^-)+x(0^+)\big)=\tfrac12(2+1)=\tfrac32$, igual que $a_0$ (todos los senos se anulan), como predice Dirichlet.

---

**b)** **Aviso de inconsistencia del enunciado.** La identidad pedida **no se deduce** del desarrollo de $x(t)=t+1$ del inciso a). El motivo es estructural: el lado izquierdo $\sum_{n\ge1}\frac{(-1)^n}{n^2+1}$ tiene términos que decaen como $1/n^2$, mientras que **todos** los coeficientes de la serie de $t+1$ (período $1$) decaen como $1/n$ (los $a_n$ son nulos). No hay forma de generar un factor $\frac{1}{n^2+1}$ a partir de coeficientes $b_n=-\frac1{\pi n}$. Además aparece $\operatorname{sh}(\pi)$, que no surge de ninguna integral de $t+1$.

La identidad **sí** proviene de la serie de Fourier de $x(t)=e^{t}$ en $(-\pi,\pi)$ con período $T=2\pi$ — que es exactamente el Ejercicio 1 del [[iip-tema-01|IIP Tema I]], cuyo inciso b) es idéntico. Todo indica que el enunciado del Tema III **reutilizó por error de copiado** el inciso b) del Tema I, dejando un inciso a) (la función $t+1$) que no lo sustenta. Por honestidad lo resolvemos como corresponde, con la función que genera la identidad.

**Serie de $x(t)=e^t$ en $(-\pi,\pi)$, $T=2\pi$ (por lo tanto $\tfrac{2\pi}{T}=1$).** Usamos la primitiva estándar
$$\int e^{t}\cos(nt)\,dt = \frac{e^{t}\big(\cos(nt)+n\sin(nt)\big)}{1+n^2},\qquad \int e^{t}\sin(nt)\,dt = \frac{e^{t}\big(\sin(nt)-n\cos(nt)\big)}{1+n^2}.$$

Valor medio:
$$a_0 = \frac{1}{2\pi}\int_{-\pi}^{\pi} e^{t}\,dt = \frac{e^{\pi}-e^{-\pi}}{2\pi} = \frac{\operatorname{sh}(\pi)}{\pi}.$$

Coeficiente $a_n$ (con $\sin(\pm n\pi)=0$, $\cos(\pm n\pi)=(-1)^n$):
$$a_n = \frac{1}{\pi}\int_{-\pi}^{\pi} e^{t}\cos(nt)\,dt = \frac{1}{\pi}\cdot\frac{\big(e^{\pi}-e^{-\pi}\big)(-1)^n}{1+n^2} = \frac{2\operatorname{sh}(\pi)}{\pi}\,\frac{(-1)^n}{1+n^2}.$$

Coeficiente $b_n$ (mismo cálculo, ahora con $-n\cos(\pm n\pi)$):
$$b_n = \frac{1}{\pi}\int_{-\pi}^{\pi} e^{t}\sin(nt)\,dt = -\frac{2\operatorname{sh}(\pi)}{\pi}\,\frac{(-1)^n\,n}{1+n^2}.$$

Es decir
$$e^{t} = \frac{\operatorname{sh}(\pi)}{\pi} + \frac{2\operatorname{sh}(\pi)}{\pi}\sum_{n=1}^{\infty}\frac{(-1)^n}{1+n^2}\Big(\cos(nt) - n\sin(nt)\Big)\quad\text{en }(-\pi,\pi).$$

**Evaluamos en $t=0$.** Ahí la función es continua (en el interior del período), así que por Dirichlet la serie converge a $x(0)=e^0=1$. Con $\cos 0=1$ y $\sin 0=0$:
$$1 = \frac{\operatorname{sh}(\pi)}{\pi} + \frac{2\operatorname{sh}(\pi)}{\pi}\sum_{n=1}^{\infty}\frac{(-1)^n}{1+n^2}.$$

Despejando la suma:
$$\frac{2\operatorname{sh}(\pi)}{\pi}\sum_{n=1}^{\infty}\frac{(-1)^n}{n^2+1} = 1 - \frac{\operatorname{sh}(\pi)}{\pi}
\;\Longrightarrow\;
\boxed{\;\sum_{n=1}^{\infty}\frac{(-1)^n}{n^2+1} = \frac{1 - \dfrac{\operatorname{sh}(\pi)}{\pi}}{\dfrac{2\operatorname{sh}(\pi)}{\pi}}.\;}$$

que es exactamente lo pedido. (Forma cerrada equivalente: $\sum_{n\ge1}\frac{(-1)^n}{n^2+1}=\tfrac12\!\left(\frac{\pi}{\operatorname{sh}(\pi)}-1\right)$.)

*Verificación numérica.* Para $e^t$: $a_0=3.676078=\operatorname{sh}(\pi)/\pi$; los $a_n$ y $b_n$ integrados coinciden con las fórmulas (p. ej. $a_1=-3.676078$, $b_1=3.676078$, $a_2=1.470431$, $b_2=-2.940862$). La suma $\sum_{n=1}^{N}\frac{(-1)^n}{n^2+1}$ tiende a $-0.36398547$, idéntico a $\frac{1-\operatorname{sh}(\pi)/\pi}{2\operatorname{sh}(\pi)/\pi}=-0.36398547$ y a $\tfrac12\!\left(\frac{\pi}{\operatorname{sh}(\pi)}-1\right)$ (diferencia $\sim10^{-11}$).

---

## Ejercicio 2

Dada la función $x(t) = t - [t]$ (parte fraccionaria; período $T=1$):

a) Hallar la Serie Trigonométrica de Fourier de $x(t)$.
b) Hallar la Serie Exponencial de Fourier de $x(t)$.
c) Hallar la Forma de Laboratorio de la Serie Trigonométrica de Fourier de $x(t)$.

### Resolución

$x(t)=t-[t]$ es la **diente de sierra** clásica: en $[0,1)$ coincide con $t$ (de $0$ a $1$), y se repite con período $1$. Frecuencia fundamental $\omega_0=\tfrac{2\pi}{T}=2\pi$. En cada entero hay un salto de $1\to0$.

**a) Serie trigonométrica.** Sobre el período tomamos $x(t)=t$ en $(0,1)$.

Valor medio:
$$a_0 = \int_0^1 t\,dt = \boxed{\frac12.}$$

Coeficientes $a_n$ (por partes, $\int t\cos(2\pi n t)\,dt = \tfrac{t\sin(2\pi n t)}{2\pi n}+\tfrac{\cos(2\pi n t)}{(2\pi n)^2}$):
$$a_n = 2\int_0^1 t\cos(2\pi n t)\,dt = 2\left[\frac{t\sin(2\pi n t)}{2\pi n}+\frac{\cos(2\pi n t)}{(2\pi n)^2}\right]_0^1 = 0,$$
porque $\sin$ se anula en $0$ y $1$, y $\cos(2\pi n)=\cos 0=1$ (la resta se cancela). $\boxed{a_n=0}$.

Coeficientes $b_n$ (por partes, $\int t\sin(2\pi n t)\,dt = -\tfrac{t\cos(2\pi n t)}{2\pi n}+\tfrac{\sin(2\pi n t)}{(2\pi n)^2}$):
$$b_n = 2\int_0^1 t\sin(2\pi n t)\,dt = 2\left[-\frac{t\cos(2\pi n t)}{2\pi n}+\frac{\sin(2\pi n t)}{(2\pi n)^2}\right]_0^1 = 2\left(-\frac{1\cdot 1}{2\pi n}\right) = \boxed{-\frac{1}{\pi n}.}$$

$$\boxed{\,x(t) = \frac12 - \sum_{n=1}^{\infty}\frac{1}{\pi n}\,\sin(2\pi n t).\,}$$

(Coincide, salvo el término constante, con la serie del Ej. 1a: $t-[t]$ y $t+1$ difieren en la constante $1$, que solo cambia $a_0$ de $\tfrac32$ a $\tfrac12$; las partes oscilantes son idénticas.)

**b) Serie exponencial.** $x(t)=\sum_{n\in\mathbb Z}c_n e^{i2\pi n t}$, con $c_n=\int_0^1 t\,e^{-i2\pi n t}\,dt$.

Para $n=0$: $c_0=\int_0^1 t\,dt = \boxed{\tfrac12}$ (coincide con $a_0$).

Para $n\ne0$, por partes ($u=t$, $dv=e^{-i2\pi n t}dt$, $v=\tfrac{e^{-i2\pi n t}}{-i2\pi n}$):
$$c_n = \left[\frac{t\,e^{-i2\pi n t}}{-i2\pi n}\right]_0^1 - \int_0^1 \frac{e^{-i2\pi n t}}{-i2\pi n}\,dt = \frac{e^{-i2\pi n}}{-i2\pi n} + \frac{1}{i2\pi n}\underbrace{\int_0^1 e^{-i2\pi n t}\,dt}_{=0}.$$
Como $e^{-i2\pi n}=1$ y la última integral es nula ($n\ne0$):
$$c_n = \frac{1}{-i2\pi n} = \frac{i}{2\pi n}.$$
$$\boxed{\,c_0=\frac12,\qquad c_n=\frac{i}{2\pi n}\ (n\ne0),\qquad x(t)=\frac12+\sum_{n\ne0}\frac{i}{2\pi n}\,e^{i2\pi n t}.\,}$$

*Coherencia con la trigonométrica:* $a_n=c_n+c_{-n}=\tfrac{i}{2\pi n}+\tfrac{i}{-2\pi n}=0$ ✓; y $b_n=i(c_n-c_{-n})=i\big(\tfrac{i}{2\pi n}-\tfrac{i}{-2\pi n}\big)=i\cdot\tfrac{2i}{2\pi n}=-\tfrac{1}{\pi n}$ ✓. Además $x$ real $\Rightarrow c_{-n}=\overline{c_n}$ ✓ (es real e impar respecto del valor medio, por eso $c_n$ es imaginario puro).

**c) Forma de laboratorio.** $x(t)=a_0+\sum_{n\ge1}A_n\cos(2\pi n t-\varphi_n)$, con $A_n=\sqrt{a_n^2+b_n^2}$ y $\tan\varphi_n=b_n/a_n$.

Como $a_n=0$ y $b_n=-\tfrac1{\pi n}$:
$$A_n = \sqrt{0+\frac{1}{\pi^2 n^2}} = \frac{1}{\pi n}.$$
La fase: $\tan\varphi_n=b_n/a_n\to-\infty$ (denominador nulo, numerador negativo), o sea $\varphi_n=-\tfrac{\pi}{2}$. Verifiquémoslo: $A_n\cos(2\pi n t-\varphi_n)$ con $\varphi_n=-\tfrac\pi2$ da $\tfrac1{\pi n}\cos(2\pi n t+\tfrac\pi2)=-\tfrac1{\pi n}\sin(2\pi n t)$, que es justo el término $b_n\sin(2\pi n t)$. ✓
$$\boxed{\,x(t) = \frac12 + \sum_{n=1}^{\infty}\frac{1}{\pi n}\,\cos\!\Big(2\pi n t + \frac{\pi}{2}\Big),\qquad A_n=\frac{1}{\pi n},\quad \varphi_n=-\frac{\pi}{2}.\,}$$

*Verificación numérica.* Cuadratura: $a_0=c_0=0.5$; $a_n\sim10^{-16}$; $b_n=-0.318310,-0.159155,-0.106103,\dots=-\tfrac1{\pi n}$; $c_n=0.159155\,i,\ 0.079577\,i,\dots=\tfrac{i}{2\pi n}$; $A_n=0.318310,0.159155,\dots=\tfrac1{\pi n}$. Todo concuerda.

---

## Ejercicio 3

Dada la función $x(t) = t$ si $0 \le t \le 1$ y $x(t) = 0$ en caso contrario:

a) Hallar la Transformada de Fourier de $x(t)$.
b) Graficar en forma aproximada el espectro de frecuencias de $x(t)$.

### Resolución

**a)** Es una señal de **soporte compacto** $[0,1]$ (no periódica), así que usamos la transformada
$$\hat x(\omega) = \int_{-\infty}^{\infty} x(t)\,e^{-i\omega t}\,dt = \int_0^1 t\,e^{-i\omega t}\,dt.$$

Integramos por partes con $u=t$, $dv=e^{-i\omega t}\,dt$, $v=\dfrac{e^{-i\omega t}}{-i\omega}$:
$$\hat x(\omega) = \left[\frac{t\,e^{-i\omega t}}{-i\omega}\right]_0^1 - \int_0^1 \frac{e^{-i\omega t}}{-i\omega}\,dt = \frac{e^{-i\omega}}{-i\omega} + \frac{1}{i\omega}\left[\frac{e^{-i\omega t}}{-i\omega}\right]_0^1.$$
La última integral: $\dfrac{1}{i\omega}\cdot\dfrac{e^{-i\omega}-1}{-i\omega} = \dfrac{e^{-i\omega}-1}{\omega^2}$. Y $\dfrac{e^{-i\omega}}{-i\omega}=\dfrac{i\,e^{-i\omega}}{\omega}$. Por lo tanto
$$\boxed{\;\hat x(\omega) = \frac{i\,e^{-i\omega}}{\omega} + \frac{e^{-i\omega}-1}{\omega^2} = \frac{(1+i\omega)\,e^{-i\omega} - 1}{\omega^2}.\;}$$

Separando parte real e imaginaria con $e^{-i\omega}=\cos\omega - i\sin\omega$:
$$\boxed{\;\operatorname{Re}\hat x(\omega) = \frac{\omega\sin\omega + \cos\omega - 1}{\omega^2},\qquad \operatorname{Im}\hat x(\omega) = \frac{\omega\cos\omega - \sin\omega}{\omega^2}.\;}$$

**Módulo** (espectro de amplitud):
$$|\hat x(\omega)| = \frac{\sqrt{\,\omega^2 - 2\omega\sin\omega - 2\cos\omega + 2\,}}{\omega^2}.$$

En $\omega=0$ la expresión tiene una indeterminación removible; por continuidad (y porque $\hat x(0)=\int_0^1 t\,dt$):
$$\hat x(0) = \int_0^1 t\,dt = \frac12,$$
valor real (la parte imaginaria $\to0$). Es el "nivel de continua" o área de la señal.

*Verificación numérica.* Comparando la fórmula cerrada contra cuadratura de $\int_0^1 t\,e^{-i\omega t}dt$ en varios $\omega$: $\omega=0.5\to0.469181-0.162537i$; $\omega=1\to0.381773-0.301169i$; $\omega=2\to0.100612-0.435398i$; $\omega=3\to-0.174070-0.345677i$ — coincidencia exacta. Las partes Re/Im con las fórmulas anteriores también coinciden. $|\hat x(\omega)|^2=\tfrac{\omega^2-2\omega\sin\omega-2\cos\omega+2}{\omega^4}\to0.25$ cuando $\omega\to0$ (es decir $|\hat x(0)|=\tfrac12$ ✓), y $|\hat x(1)|=0.4863$, $|\hat x(2)|=0.4469$, $|\hat x(3)|=0.3870$.

**b) Espectro de frecuencias.** El espectro de amplitud $|\hat x(\omega)|$ es una función **par** (porque $x$ es real, $|\hat x(-\omega)|=|\hat x(\omega)|$), con las siguientes características:

- **Máximo en $\omega=0$:** $|\hat x(0)|=\tfrac12$ (componente de continua = área bajo la rampa). Es el pico global.
- **Decaimiento como $1/\omega$** para $|\omega|$ grande: $\hat x(\omega)\sim \dfrac{i\,e^{-i\omega}}{\omega}$, dominado por el término $\tfrac{i e^{-i\omega}}{\omega}$; la discontinuidad de salto de la rampa en $t=1$ (de $1$ a $0$) hace que el espectro decaiga lentamente, sólo como $1/|\omega|$.
- **Lóbulos / oscilaciones amortiguadas:** por el soporte finito $[0,1]$ aparecen ondulaciones tipo $\sin\omega,\cos\omega$ moduladas por $1/\omega$ y $1/\omega^2$; el espectro no se anula exactamente en ceros regulares (a diferencia de un pulso rectangular puro), sino que tiene mínimos locales decrecientes.

Cualitativamente:

```
|x̂(ω)|
 0.5 ┤ ●                       (pico en ω=0)
     │  \
     │   \___                  decaimiento ~ 1/|ω|
     │       \___              con ondulaciones (lóbulos)
     │           \__/‾\__/‾\__ 
   0 ┼────────────────────────────► ω
     0    π    2π   3π   4π
        (simétrico en ω<0: espectro par)
```

La **fase** $\arg\hat x(\omega)$ es impar y varía con $\omega$ (no es lineal pura por la asimetría de la rampa respecto del origen del soporte).

---

## Resumen de resultados

| Item | Resultado |
|------|-----------|
| Ej 1a — serie de $t+1$, $T=1$ | $x(t)=\tfrac32-\sum_{n\ge1}\tfrac{1}{\pi n}\sin(2\pi n t)$ |
| Ej 1b — identidad | $\sum_{n\ge1}\tfrac{(-1)^n}{n^2+1}=\tfrac{1-\operatorname{sh}(\pi)/\pi}{2\operatorname{sh}(\pi)/\pi}=\tfrac12\!\big(\tfrac{\pi}{\operatorname{sh}(\pi)}-1\big)$; surge de la serie de $e^t$ en $(-\pi,\pi)$ evaluada en $t=0$ (enunciado con inciso b) copiado del Tema I) |
| Ej 2a — trigonométrica | $\tfrac12-\sum_{n\ge1}\tfrac{1}{\pi n}\sin(2\pi n t)$ |
| Ej 2b — exponencial | $c_0=\tfrac12,\ c_n=\tfrac{i}{2\pi n}\ (n\ne0)$ |
| Ej 2c — laboratorio | $\tfrac12+\sum_{n\ge1}\tfrac{1}{\pi n}\cos(2\pi n t+\tfrac\pi2)$, $A_n=\tfrac1{\pi n}$, $\varphi_n=-\tfrac\pi2$ |
| Ej 3a — TF | $\hat x(\omega)=\dfrac{(1+i\omega)e^{-i\omega}-1}{\omega^2}$, $\hat x(0)=\tfrac12$ |
| Ej 3b — espectro | par, pico $\tfrac12$ en $\omega=0$, decaimiento $\sim1/|\omega|$ con lóbulos |
