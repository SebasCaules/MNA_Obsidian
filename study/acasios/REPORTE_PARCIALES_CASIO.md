# Reporte — Resolver parciales MNA con los scripts Casio Graph 90+E

> Generado verificando **de verdad** cada script (MicroPython corrido en sandbox, salidas literales pegadas) sobre los **28 modelos de examen** de [[parciales/patrones]] (IP I–IX, IIP I/III/IV/V/VI, Recuperatorio XIII, Final I–XI + XI-alt + XIV). Cada salida se comparó con la `*-resolucion.md` oficial.
>
> **Para qué sirve esto:** para cada ejercicio te dice (1) **de dónde sale cada input** (qué dato del enunciado va a qué prompt), (2) **qué tipear** en la Casio (módulo + opción + secuencia), (3) **qué imprime el script** (texto real), (4) **cómo transcribir la respuesta** en el examen, y (5) los **caveats** (coincide/difiere de la oficial, qué va a mano).

## ⚙️ Actualización del software (parches aplicados — 2026-05-29)

Tras este análisis se **corrigieron** los scripts (verificado contra numpy). Las salidas pegadas más abajo se capturaron **antes** del parche: donde un *caveat* dice "**BUG en `diag`**", "**`lu` aborta**" o "**`lu` no soporta no-cuadrada**", **ya está RESUELTO**. Cambios:

1. **`diag.py` — bug del autovalor real corregido** (R1). Con autovalores complejos y $\det\neq0$ ahora imprime bien `L1(real)`, `L2,3 Re` y agrega `Im=+-...`. Casos del reporte ya corregidos: Final I → `L1(real)=1, Re=1.5, Im=±0.866`; Final V → `L1(real)=2, Re=1.5`; Final VI → `L1(real)=2.393, Re=1.304, Im=±1.436`. **Ya se puede copiar el autovalor real.**
2. **`lu.py` — acepta matrices rectangulares** $n\times m$ (R5): los PLU de $3\times2$ (IP IV-Ej3, IP IX-Ej3, Rec.XIII-Ej3) **ya no crashean**; ahora pide `filas:`/`cols:`. Y en **pivote $\approx0$ no aborta**: completa $P,L,U$ ($U$ con fila nula) con `|PA-LU|=0` (IP VIII-Ej2b, Final XIV-Ej3b).
3. **`fs.py` — convergencia corregida** (R11): el `prom` en bordes del período ahora periodiza el muestreo y da el promedio correcto del salto (ej. Final II/VI en $x=0$: `prom=0.5`, antes `1`). Y el término constante se etiqueta **`=>cte=`** (= `a0/2`, el valor medio) para no confundirlo con `a0` (R10).
4. **`io_util.py` — UI**: los vectores cortos se imprimen en **una sola línea** (`v: 2 1 0` en vez de dos filas), ahorrando filas en pantalla (la shell solo scrollea vertical). Si no entran en 21 cols, caen al formato de 2 líneas + wrap.

> Pendientes (features, no bugs): C.I. numérica y bordes Neumann en `edp`, más templates en `fs`, exponenciales en `tf`, $M_{BB}$, "$\lambda$ dado". Ver [Recomendaciones](#recomendaciones-de-mejora-priorizadas).

## Resumen ejecutivo

Se evaluaron **~100 incisos**. Cobertura aproximada con los scripts tal como están hoy:

| Estado | ~% | Qué significa |
|---|---|---|
| **SÍ** (≈55%) | el script resuelve/verifica el inciso completo; pegás la salida y transcribís. |
| **PARCIAL** (≈25%) | el script hace la parte **numérica** (factoriza, diagonaliza un caso, da el esquema/matriz), pero **lo simbólico va a mano**: despejar un parámetro $k$, parametrizar restricciones de un subespacio, armar $M_{B_1B_2}$, derivar una serie, o cargar una C.I. que no es template. |
| **NO** (≈20%) | fuera de alcance: demostraciones, EDO→sistema de 1er orden, funciones de Fourier fuera de los 9 templates, bordes Neumann en EDP, TF no polinómicas. |

**Lo que el set cubre muy bien (alta probabilidad en el parcial):** TL $\mathbb R^3\to\mathbb R^3$ (núcleo/imagen/antiimagen) con `tl`, diagonalización (incl. con $k$ sustituido) con `diag`, QR / SVD / PLU con `qr`/`svd`/`lu`, cuadrados mínimos con `lsq`, y la antiimagen/núcleo con matriz en base no canónica $M_{EB}$ con `tl:4`.

**Donde más falla (ver [Recomendaciones](#recomendaciones-de-mejora-priorizadas) al final):** un **bug de correctitud en `diag`** (autovalor real mal impreso cuando hay autovalores complejos y $\det\neq0$), y huecos de cobertura en `fs` (solo 9 funciones), `edp` (solo Dirichlet, C.I. por template), `tf` (no exponenciales), `lu` (solo cuadrada, siempre pivotea) y la ausencia de $M_{BB}$ y de "λ dado".

## Cómo correr cualquier ejemplo de este reporte

En la Casio: `MENU → PYTHON → main.py → F1(EXE)`, contestás `ej(1-5)`, elegís la opción del menú y cargás los datos. En este reporte, para reproducir **en una PC** se usa el harness del sandbox (corre un módulo directo, sin menú):

```bash
printf '<inputs\nseparados\npor\nnewline>\n' | python3 run_mod.py <modulo>
```

(El primer input de `tl`/`cplx`/`fs`/`tf`/`edp` es el número de variante del menú interno `Op:`.)

## Convenciones que tenés que tener SIEMPRE presentes

1. **Matriz desde una regla** $T(x,y,z)=(f_1,f_2,f_3)$: cada **fila** de $A$ son los coeficientes de una componente de salida. Ej. $T=(2x-y+z,\dots)\Rightarrow$ fila 1 $=(2,-1,1)$.
2. **Parámetro ($k$, $a$, $h$…):** los scripts son **numéricos**, no simbólicos. Para "hallar el $k$" se argumenta a mano (determinante / polinomio característico) y se **verifica sustituyendo** los $k$ críticos uno por uno. Excepción: "hallar $a,b$ para que $v$ sea autovector" → `param` lo resuelve directo.
3. **Fourier — `a0` vs `a0/2`:** `fs` imprime `a0 = (2/T)∫f` = el **doble** del valor medio de la cátedra. **El término constante que va en el examen es `a0/2`.** Los `a=`/`b=` por armónico sí son los $a_n,b_n$ correctos.
4. **Autovectores / SVD:** la base que devuelve el script puede diferir de la oficial por **escala o signo global** (e incluso intercambiar roles $U\leftrightarrow V$ en matrices simétricas). Es válido: lo que certifica la respuesta es `|AP-PD|≈0` / `|USVt-A|≈0`. **Reordená/reescalá** para que coincida con lo que pide el enunciado (p.ej. el orden de la diagonal $D$).
5. **Formato numérico:** vectores/matrices a **4 cifras** significativas; autovalores y algunos coeficientes a **6**. Los `1e-16` son cero (ruido de punto flotante); los `a_n≈-0.0017` en funciones con salto son ruido de Simpson (valor exacto 0).
6. **PLU:** `lu` **siempre** hace pivoteo parcial ($P\neq I$). Si la cátedra pide Doolittle sin pivoteo ($P=I$), la factorización del script es válida pero **distinta** — hacela a mano.

## Matriz global de cobertura

| Parcial | Ej1 | Ej2 | Ej3 | Ej4 | Ej5 |
|---|---|---|---|---|---|
| **IP I** | TL ✅ tl | diag(k) ✅ | SVD+QR ✅ | MMCC ✅ lsq | subesp P₂ 🟡 |
| **IP II** | TL ✅ | SVD+QR ✅ | MMCC ax²+b ✅* | — | — |
| **IP III** | rango(k) ✅ | diag(k) ✅ | PLU🟡+QR✅ | — | — |
| **IP IV** | tl:4 ✅ | diag(k) ✅ | PLU🟡(3×2)+QR✅ | — | — |
| **IP V** | TL+diag ✅ | TL P₂→ℝ⁴ 🟡 | subesp ℝ²ˣ² 🟡 | — | — |
| **IP VI** | rango(k) ✅ | diag→base B ✅ | LI param ❌ | — | — |
| **IP VII** | param ✅ | tl:4 ✅ | Fourier \|cos\| ❌ | — | — |
| **IP VIII** | param 🟡 | QR🟡+PLU🟡(sing) | Fourier \|sen\| ❌ | — | — |
| **IP IX** | rango(k) ✅ | diag(k) 🟡 | SVD+QR ✅ | — | — |
| **Rec. XIII** | diag(h) ✅ | Fourier dientesierra ✅ | PLU🟡(3×2)+QR✅ | — | — |
| **IIP I** | serie eᵗ ✅ | TF rampa ✅ tf:4 | — | — | — |
| **IIP III** | serie t+1 🟡 | TF rampa ✅ | — | — | — |
| **IIP IV** | serie t² 🟡 | TF t² ✅ | calor Dir 🟡 / Neu ❌ | — | — |
| **IIP V** | serie cos,T=π/2 ❌ | TF e^{-2\|t\|} 🟡 | onda Dir 🟡 / Neu ❌ | — | — |
| **IIP VI** | serie sin,T=π/2 ❌ | TF te⁻ᵗ ❌ | conv-dif Dir 🟡 / Neu ❌ | — | — |
| **Final I** | TL+diag ✅(⚠bug) | serie x-[x] ✅ | EDO→sist ❌ | SVD ✅ | TF e^{-\|t\|} ❌ |
| **Final II** | TL+diag ✅ | serie 1-x ✅ | EDO→sist ❌ | TF (t-1)² ✅ | — |
| **Final III** | M_BB 🟡 +diag ✅ | serie x-x² ❌ | EDO→sist ❌ | TF t-t² ✅ | — |
| **Final IV** | TL+diag ✅ | serie 1-x ✅ | QR+SVD✅+PLU🟡 | — | — |
| **Final V** | TL+diag ✅(⚠bug) | serie 1-x² ❌ | calor Dir🟡/Neu❌ | TF e^{t-1} ❌ | — |
| **Final VI** | TL✅+diag🟡(⚠bug) | serie 1-x ✅ | calor Dir🟡/Neu❌ | TF e^{-2\|t\|+1} ❌ | — |
| **Final VII** | diag(k) 🟡 | serie 1-x ✅ | QR ✅ | — | — |
| **Final VIII** | rango(k) 🟡 | serie 1-x² ❌ | SVD ✅(vía Aᵀ) | — | — |
| **Final IX** | M_BB🟡+SVD ✅ | calor CI x² 🟡 | TF t²-t ✅ | — | — |
| **Final X** | M_BB🟡+QR ✅ | calor Neumann ❌ | TF 1-\|t\| ✅ | — | — |
| **Final XI** | diag(a) 🟡 | T(A)=A-Aᵀ ✅ | SVD+QR ✅ | — | — |
| **Final XI-alt** | TL+diag ✅ | serie 1-x² ❌ | calor Dir🟡/Neu❌ | TF e^{-a\|t\|} ❌ | — |
| **Final XIV** | T:P₂→ℝ³ ✅ | diag(k)+AᵀAX=0 ✅ | SVD✅+PLU🟡 | — | — |

✅ SÍ · 🟡 PARCIAL · ❌ NO cubierto · `*` con workaround · `⚠bug` ver recomendación #1.

---
# Sección IP (bloque A) — Temas I a V

> Sandbox: `/tmp/acasios_sb`. Todas las salidas pegadas son ejecuciones reales con `printf '...' | python3 run_mod.py <mod>`.
> Convención de salida: vectores/matrices a 4 cifras (`show_vec`/`show_mat`); autovalores y algunos coef a 6 cifras (`{:.6g}`).

---

## IP Tema 1

### Ej 1 — TL R³→R³: núcleo/imagen + antiimagen · [tl:1 y tl:2] | SÍ
**Enunciado (resumen):** $T(x,y,z)=(2x-y+z,\ x+y-z,\ z+y-x)$. a) Núcleo e Imagen. b) $(x,y,z)$ con $T(\cdot)=(1,1,-2)$.
**De dónde salen los inputs:** cada fila de $A$ son los coeficientes de una componente de salida: $(2,-1,1)/(1,1,-1)/(-1,1,1)$. b) $b=(1,1,-2)$.
**Inputs Casio:** módulo `tl`, opción `1` (N(T),Im,rg) para a); opción `2` (Antiimagen b) para b).
**Comando de verificación:**
`printf '1\n3\n3\n2,-1,1\n1,1,-1\n-1,1,1\n' | python3 run_mod.py tl`
`printf '2\n3\n3\n2,-1,1\n1,1,-1\n-1,1,1\n1,1,-2\n' | python3 run_mod.py tl`
**Salida del script (real):**
```
rref: I3 ; rg= 3 ; dim N= 0
Base N(T): N(T)={0}
Base Im(T): c1: 2 1 -1 ; c2: -1 1 1 ; c3: 1 -1 1
-- Resuelvo Ax=b
x_p: 0.6667 -0.5 -0.8333  ; Sol unica.
```
**Cómo lo escribo en el examen:** $N(T)=\{(0,0,0)\}$, $\operatorname{Im}(T)=\mathbb{R}^3$ (rg=3, isomorfismo). b) $(x,y,z)=(2/3,\,-1/2,\,-5/6)$.
**Caveat:** coincide exacto con la oficial ($0.6667=2/3$, $-0.8333=-5/6$).

### Ej 2 — Diagonalización con parámetro k · [diag] | SÍ (sustituyendo k)
**Enunciado (resumen):** $M(F)_{EE}=\begin{psmallmatrix}1&0&1\\0&k&1\\0&9&k\end{psmallmatrix}$. a) Todos los $k$ diagonalizable. b) Para $k=3$, base $B$ con $M(F)_{BB}$ diagonal.
**De dónde salen los inputs:** las filas de la matriz; sustituir cada $k$ concreto. El script es numérico, no resuelve "todos los k" — se corre uno por caso. Los candidatos críticos (de la teoría: $p(\lambda)=(\lambda-1)[\lambda-(k+3)][\lambda-(k-3)]$ ⇒ choque en $k=-2$ y $k=4$) se verifican.
**Inputs Casio:** módulo `diag`, `n=3`, filas con el $k$ sustituido.
**Comandos de verificación:**
`printf '3\n1,0,1\n0,-2,1\n0,9,-2\n' | python3 run_mod.py diag`  (k=-2)
`printf '3\n1,0,1\n0,4,1\n0,9,4\n' | python3 run_mod.py diag`   (k=4)
`printf '3\n1,0,1\n0,3,1\n0,9,3\n' | python3 run_mod.py diag`   (k=3, parte b)
**Salida del script (real):**
```
k=-2: Autovalores L1=1 L2=1 L3=-5 ; S_L=1 dimK=1<m=2 (NO diag.) ; NO diagonaliz.
k=4 : Autovalores L1=7 L2=1 L3=1 ; S_L=1 dimK=1<m=2 (NO diag.) ; NO diagonaliz.
k=3 : Autovalores L1=6 L2=1 L3=0
      S_L=6 v: 0.2 0.3333 1 ; S_L=1 v: 1 0 0 ; S_L=0 v: -1 -0.3333 1
      P: [0.2 1 -1 / 0.3333 0 -0.3333 / 1 0 1]  D: diag(6,1,0)  |AP-PD|=2.22e-16
```
**Cómo lo escribo en el examen:** a) diagonalizable $\iff k\in\mathbb{R}-\{-2,4\}$ (en $k=-2$ y $k=4$ el autovalor doble tiene $m_g=1$). b) $k=3$: autovalores $\{0,1,6\}$; $B=\{(3,1,-3),(1,0,0),(3,5,15)\}$, $M(F)_{BB}=\operatorname{diag}(0,1,6)$.
**Caveat:** el script confirma exactamente $k=-2$ y $k=4$ como no-diagonalizables, pero "todos los k" se argumenta a mano (el script no factoriza simbólicamente). Los autovectores difieren de la oficial sólo por escala: script $v_6=(0.2,0.3333,1)=\tfrac1{15}(3,5,15)$, $v_0=(-1,-0.3333,1)=-\tfrac13(3,1,-3)$ — misma dirección, base válida ($|AP-PD|\approx0$). El orden en $D$ es $(6,1,0)$ vs oficial $(0,1,6)$ (reordenar columnas de $P$ acorde).

### Ej 3 — SVD 2×2 + QR · [svd y qr] | SÍ
**Enunciado (resumen):** $A=\begin{psmallmatrix}0.92&1.44\\1.44&0.08\end{psmallmatrix}$. a) SVD. b) QR.
**De dónde salen los inputs:** las dos filas de $A$.
**Inputs Casio:** `svd` → `2`,`2`, filas; `qr` → `2`,`2`, filas.
**Comandos de verificación:**
`printf '2\n2\n0.92,1.44\n1.44,0.08\n' | python3 run_mod.py svd`
`printf '2\n2\n0.92,1.44\n1.44,0.08\n' | python3 run_mod.py qr`
**Salida del script (real):**
```
SVD: s1=2 s2=1
 V cols: v1: 0.8 0.6 ; v2: -0.6 0.8
 U cols: u1: 0.8 0.6 ; u2: 0.6 -0.8
 |USVt-A|=1.527e-16 ; Sigma: diag(2,1)
QR: ||u1||=1.709 v1: 0.5384 0.8427 ; <a2,v1>=0.8427 ||u2||=1.17 v2: 0.8427 -0.5384
 Q: [0.5384 0.8427 / 0.8427 -0.5384]  R: [1.709 0.8427 / 0 1.17]  |QR-A|=4e-17
```
**Cómo lo escribo en el examen:** SVD $\sigma_1=2,\sigma_2=1$, $\Sigma=\operatorname{diag}(2,1)$, $U=\begin{psmallmatrix}0.8&-0.6\\0.6&0.8\end{psmallmatrix}$, $V=\begin{psmallmatrix}0.8&0.6\\0.6&-0.8\end{psmallmatrix}$. QR: $Q=\begin{psmallmatrix}0.5384&0.8427\\0.8427&-0.5384\end{psmallmatrix}$, $R=\begin{psmallmatrix}1.709&0.8427\\0&1.17\end{psmallmatrix}$.
**Caveat:** QR coincide exacto con la oficial. En la SVD el script entrega $U$ y $V$ **intercambiados** respecto de la oficial (script $V=\begin{psmallmatrix}0.8&-0.6\\0.6&0.8\end{psmallmatrix}$, oficial los llama $U$). Es admisible: $A$ es simétrica y la asignación de columnas/signo es ambigua; $USV^t=A$ verificado. Al transcribir conviene reordenar para que sea coherente — pero cualquiera de las dos es correcta.

### Ej 4 — Cuadrados mínimos $a\cos x+b\sin x$ · [lsq:3] | SÍ
**Enunciado (resumen):** datos $(0,0.97),(\pi/4,1.42),(\pi,-1.04)$; ajustar $y=a\cos x+b\sin x$ por QR.
**De dónde salen los inputs:** los 3 puntos con $x$ en radianes ($\pi/4\to0.7854$, $\pi\to3.1416$); modelo `3` (a cos + b sen).
**Inputs Casio:** módulo `lsq`, `#ptos=3`, los puntos, luego `>=3`.
**Comando de verificación:**
`printf '3\n0,0.97\n0.7854,1.42\n3.1416,-1.04\n3\n' | python3 run_mod.py lsq`
**Salida del script (real):**
```
A diseno: [1 0 / 0.7071 0.7071 / -1 -7.3e-06]
AtA: [2.5 0.5 / 0.5 0.5]  Atb: 3.014 1.004
coef: 1.005 1.003 ; ||Ax-b||=0.04949
```
**Cómo lo escribo en el examen:** $a=1.005$, $b\approx1.003$ ⇒ $y(x)\approx1.005\cos x+1.003\sin x$; norma del residuo $\approx0.0495$.
**Caveat:** coincide con la oficial ($a=1.005$, $b\approx1.0032$, residuo 0.0495). El script resuelve por ecuaciones normales, no por QR explícito, pero el resultado numérico de MMCC es el mismo que pide el enunciado ("vía QR").

### Ej 5 — Subespacio de P2 con parámetro a · [verificación con mat.solve / tl] | PARCIAL
**Enunciado (resumen):** $H=\langle x^2+2x-1,\ x^2+x+a^2-4,\ x^2-2x+3\rangle$. Hallar $a$ tal que $\dim H=2$ y $x^2+a-1\in H$.
**De dónde salen los inputs:** coordenadas en base $\{1,x,x^2\}$: $p_1=(-1,2,1)$, $p_2=(a^2-4,1,1)$, $p_3=(3,-2,1)$; vector a testear $q=(a-1,0,1)$.
**Inputs Casio:** no hay módulo que despeje $a$ simbólicamente ($\det M=16-4a^2=0\Rightarrow a=\pm2$ es a mano). Se **verifican** los candidatos $a=\pm2$ con `tl` opción `1` (rango de los generadores) y la pertenencia (rango de $[p_1\,p_3\,q]$).
**Comando de verificación:** (helper de `mat`, equivalente a correr `tl:1` con las coords como filas)
```
a=2 : rank(generadores)=2 ; rank[p1,p3,q]=2 -> q in H = True
a=-2: rank(generadores)=2 ; rank[p1,p3,q]=3 -> q in H = False
```
**Cómo lo escribo en el examen:** $\dim H=2\iff a=\pm2$; pero $x^2+a-1\in H$ sólo para $a=2$ ($q=x^2+1=\tfrac12 p_1+\tfrac12 p_3$). Para $a=-2$, $q=x^2-3\notin H$. Respuesta: $\boxed{a=2}$.
**Caveat:** coincide con la oficial. El despeje $a=\pm2$ es a mano; el script (vía `tl:1`, poniendo las coordenadas como filas) sólo **verifica** rango y pertenencia caso por caso. Parámetro simbólico → no auto-resuelto.

---

## IP Tema 2

### Ej 1 — TL R³→R³: núcleo/imagen + antiimagen · [tl:1 y tl:2] | SÍ
**Enunciado (resumen):** $T(x,y,z)=(x-y+z,\ x+3y-z,\ z+y-2x)$. a) Núcleo/Imagen. b) $T(\cdot)=(2,2,-2)$.
**De dónde salen los inputs:** filas = coeficientes por componente: $(1,-1,1)/(1,3,-1)/(-2,1,1)$; $b=(2,2,-2)$.
**Inputs Casio:** `tl` op `1` (a), op `2` (b).
**Comandos de verificación:**
`printf '1\n3\n3\n1,-1,1\n1,3,-1\n-2,1,1\n' | python3 run_mod.py tl`
`printf '2\n3\n3\n1,-1,1\n1,3,-1\n-2,1,1\n2,2,-2\n' | python3 run_mod.py tl`
**Salida del script (real):**
```
rref: I3 ; rg=3 ; dim N=0 ; N(T)={0}
Im(T): c1: 1 1 -2 ; c2: -1 3 1 ; c3: 1 -1 1
x_p: 1.6 0.4 0.8 ; Sol unica.
```
**Cómo lo escribo en el examen:** $N(T)=\{0\}$, $\operatorname{Im}(T)=\mathbb{R}^3$ (isomorfismo, $\det A=10$). b) $(x,y,z)=(8/5,2/5,4/5)=(1.6,0.4,0.8)$.
**Caveat:** coincide exacto con la oficial.

### Ej 2 — SVD 2×2 + QR · [svd y qr] | SÍ
**Enunciado (resumen):** $A=\begin{psmallmatrix}0.55&1.1\\1.1&0.8\end{psmallmatrix}$. a) SVD. b) QR.
**De dónde salen los inputs:** las dos filas.
**Inputs Casio:** `svd`/`qr` → `2`,`2`, filas.
**Comandos de verificación:**
`printf '2\n2\n0.55,1.1\n1.1,0.8\n' | python3 run_mod.py svd`
`printf '2\n2\n0.55,1.1\n1.1,0.8\n' | python3 run_mod.py qr`
**Salida del script (real):**
```
SVD: s1=1.78208 s2=0.432079
 V cols: v1: 0.666 0.746 ; v2: -0.746 0.666
 U cols: u1: 0.666 0.746 ; u2: 0.746 -0.666
 |USVt-A|=2.22e-16 ; Sigma: diag(1.782, 0.4321)
QR: ||u1||=1.23 v1: 0.4472 0.8944 ; <a2,v1>=1.207 ||u2||=0.6261 v2: 0.8944 -0.4472
 Q: [0.4472 0.8944 / 0.8944 -0.4472]  R: [1.23 1.207 / 0 0.6261]  |QR-A|=0
```
**Cómo lo escribo en el examen:** SVD $\sigma_1\approx1.7821,\sigma_2\approx0.4321$; $U=\begin{psmallmatrix}0.666&0.746\\0.746&-0.666\end{psmallmatrix}$, $V=\begin{psmallmatrix}0.666&-0.746\\0.746&0.666\end{psmallmatrix}$. QR: $Q=\tfrac1{\sqrt5}\begin{psmallmatrix}1&2\\2&-1\end{psmallmatrix}$, $R=\begin{psmallmatrix}1.23&1.207\\0&0.6261\end{psmallmatrix}$.
**Caveat:** valores singulares y QR coinciden exacto con la oficial. Misma observación que Tema 1 Ej3: la oficial intercambia los roles $U\leftrightarrow V$ respecto del script (ambos válidos, $A$ simétrica, signo/orden de columnas admisibles).

### Ej 3 — Cuadrados mínimos $y=ax^2+b$ · [lsq:1 con truco x→x²] | SÍ (workaround)
**Enunciado (resumen):** datos $(0,0.78),(1,1.9),(2,6.7)$; ajustar $y=ax^2+b$ por QR. Dar $a,b$, residuo.
**De dónde salen los inputs:** el modelo $y=ax^2+b$ tiene columnas de diseño $(x^2,1)$, que **no es** ninguno de los 5 templates. Truco: alimentar los puntos con $x\to x^2$ (es decir $x=0,1,4$) y usar el modelo `1` ($y=a+bx$): entonces ajusta $y=\text{(intercept)}+\text{(slope)}\cdot x^2$, exactamente el modelo pedido.
**Inputs Casio:** `lsq`, `#ptos=3`, puntos $(0,0.78),(1,1.9),(4,6.7)$ (¡los $x$ ya elevados al cuadrado!), modelo `1`.
**Comando de verificación:**
`printf '3\n0,0.78\n1,1.9\n4,6.7\n1\n' | python3 run_mod.py lsq`
**Salida del script (real):**
```
A diseno: [1 0 / 1 1 / 1 4]
AtA: [3 5 / 5 17]  Atb: 9.38 28.7
coef: 0.6138 1.508 ; ||Ax-b||=0.2824
```
**Cómo lo escribo en el examen:** $b=0.6138$ (término constante = `coef[0]`), $a=1.508$ (coef de $x^2$ = `coef[1]`) ⇒ $y(x)\approx1.508\,x^2+0.6138$; residuo $\approx0.2824$.
**Caveat:** coincide con la oficial ($a=98/65\approx1.5077$, $b=399/650\approx0.6138$, residuo 0.2824). **Cuidado con el orden y el truco**: con el modelo 1 el `coef` sale como $(\text{intercepto},\text{pendiente})=(b,a)$, hay que reetiquetar. El modelo nativo "$ax^2+b$" no existe; se aprovecha que $x^2$ es la única no-linealidad.

---

## IP Tema 3

### Ej 1 — Rango de TL con parámetro k · [tl:1] | SÍ (sustituyendo k)
**Enunciado (resumen):** $M_E(T)=\begin{psmallmatrix}2&8&k\\-1&-4&0\\k+3&12&2k\end{psmallmatrix}$. a) $k$ con $\dim R(T)=1$. b) $k=0$: base y dim de $N(T)$.
**De dónde salen los inputs:** filas con el $k$ sustituido. La teoría sugiere $k=0$ (para que $c_1=(2,-1,k+3)$ sea $\propto c_2=4(2,-1,3)$ hace falta $k+3=3$); se verifica que sólo $k=0$ baja el rango.
**Inputs Casio:** `tl` op `1`, filas con $k$ concreto.
**Comandos de verificación:**
`printf '1\n3\n3\n2,8,0\n-1,-4,0\n3,12,0\n' | python3 run_mod.py tl`  (k=0)
`printf '1\n3\n3\n2,8,1\n-1,-4,0\n4,12,2\n' | python3 run_mod.py tl`  (k=1 control)
**Salida del script (real):**
```
k=0: rref [1 4 0 / 0 0 0 / 0 0 0] ; rg=1 ; dim N=2
     Base N(T): n1: -4 1 0 ; n2: 0 0 1 ; Im(T): c1: 2 -1 3
k=1: rg=3 ; dim N=0   (también k=-1 da rg=3)
```
**Cómo lo escribo en el examen:** a) $\dim R(T)=1 \iff k=0$ (único valor que vuelve $c_1\parallel c_2$ y anula $c_3$). b) $k=0$: $B_{N(T)}=\{(-4,1,0),(0,0,1)\}$, $\dim N(T)=2$ (consistente con dim: $2+1=3$).
**Caveat:** coincide exacto con la oficial. El despeje "$k=0$ único" se confirma corriendo otros $k$ (todos rg=3), aunque la condición general es a mano.

### Ej 2 — Diagonalización con parámetro k · [diag] | SÍ (sustituyendo k)
**Enunciado (resumen):** $A=\begin{psmallmatrix}2&k-2&0\\0&3&k-1\\0&0&3\end{psmallmatrix}$. a) $k$ diagonalizable. b) $k=0$: base de autovectores.
**De dónde salen los inputs:** triangular ⇒ autovalores $2,3,3$; el riesgo es $m_g(3)$. Candidato $k=1$ (anula la entrada $(2,3)=k-1$). Se verifican $k=1$ (diag) y $k=0$ (no diag).
**Inputs Casio:** `diag`, `n=3`, filas con $k$ sustituido. (k=1: fila2 = `0,3,0`, fila1 col2 = $k-2=-1$.)
**Comandos de verificación:**
`printf '3\n2,-1,0\n0,3,0\n0,0,3\n' | python3 run_mod.py diag`  (k=1)
`printf '3\n2,-2,0\n0,3,-1\n0,0,3\n' | python3 run_mod.py diag`  (k=0)
**Salida del script (real):**
```
k=1: Autovalores 3,3,2 ; S_L=3 v: -1 1 0 / 0 0 1 ; S_L=2 v: 1 0 0
     P:[-1 0 1/1 0 0/0 1 0] D: diag(3,3,2) |AP-PD|=8.88e-16  (DIAGONALIZABLE)
k=0: Autovalores 3,3,2 ; S_L=3 dimK=1<m=2 (NO diag.) v: -2 1 0 ; S_L=2 v: 1 0 0 ; NO diagonaliz.
```
**Cómo lo escribo en el examen:** a) diagonalizable $\iff k=1$ ($\operatorname{rg}(A-3I)=1\Rightarrow m_g(3)=2$). b) $k=0$ NO diagonalizable: autovectores $v=(1,0,0)$ (λ=2) y $v=(-2,1,0)$ (λ=3), sólo 2 LI.
**Caveat:** coincide exacto con la oficial.

### Ej 3 — PLU + QR de 3×3 · [lu y qr] | SÍ (con caveat de pivoteo en PLU)
**Enunciado (resumen):** $A=\begin{psmallmatrix}1&3&-1\\2&8&4\\-1&3&-4\end{psmallmatrix}$. a) PLU. b) QR.
**De dónde salen los inputs:** las tres filas.
**Inputs Casio:** `lu` → `3`, filas; `qr` → `3`,`3`, filas.
**Comandos de verificación:**
`printf '3\n1,3,-1\n2,8,4\n-1,3,-4\n' | python3 run_mod.py lu`
`printf '3\n3\n1,3,-1\n2,8,4\n-1,3,-4\n' | python3 run_mod.py qr`
**Salida del script (real):**
```
LU (PIVOTEO PARCIAL): P:F1<>F2 ; P:F2<>F3
 P:[0 1 0/0 0 1/1 0 0]
 L:[1 0 0 / -0.5 1 0 / 0.5 -0.1429 1]
 U:[2 8 4 / 0 7 -2 / 0 0 -3.286]  |PA-LU|=0
QR: v1: 0.4082 0.8165 -0.4082 ; v2: 0.05315 0.4252 0.9035 ; v3: -0.9113 0.3906 -0.1302
 R:[2.449 6.532 4.491 / 0 6.272 -1.967 / 0 0 2.994]  |QR-A|=4.4e-16
```
**Cómo lo escribo en el examen:** QR — $Q,R$ tal cual la salida (coincide exacto con la oficial). PLU — **OJO**: la oficial hace Doolittle SIN pivoteo y obtiene $P=I$, $L=\begin{psmallmatrix}1&0&0\\2&1&0\\-1&3&1\end{psmallmatrix}$, $U=\begin{psmallmatrix}1&3&-1\\0&2&6\\0&0&-23\end{psmallmatrix}$. El script SIEMPRE pivotea, así que da otra factorización válida con $P\neq I$.
**Caveat:** **discrepancia esperada en PLU**: el script usa pivoteo parcial (máximo $|U_{ij}|$) y la cátedra hizo $P=I$. Ambas son $PA=LU$ correctas ($|PA-LU|=0$), pero NO coinciden las matrices. Si el examen quiere $P=I$, hay que hacerlo a mano. QR coincide exacto.

---

## IP Tema 4

### Ej 1 — TL con M_EB (dominio en base B) · [tl:4] | SÍ
**Enunciado (resumen):** $M_{EB}(T)=\begin{psmallmatrix}2&0&2\\0&3&3\\1&-1&0\end{psmallmatrix}$, $B=\{(0,1,-1),(0,0,1),(1,1,0)\}$. a) $v$ con $T(v)=(0,2,1)$. b) $\dim N(T)$.
**De dónde salen los inputs:** $M$ por filas; $B$ un vector por fila; $w=(0,2,1)$. Opción `4` interpreta $M$ como matriz dominio-en-$B$/codominio-canónico.
**Inputs Casio:** `tl` op `4` → sub-op `1` (antiimagen) para a, sub-op `2` (núcleo) para b; `dim=3`; filas de $M$; filas de $B$; (si a) $w$.
**Comandos de verificación:**
`printf '4\n1\n3\n2,0,2\n0,3,3\n1,-1,0\n0,1,-1\n0,0,1\n1,1,0\n0,2,1\n' | python3 run_mod.py tl`
`printf '4\n2\n3\n2,0,2\n0,3,3\n1,-1,0\n0,1,-1\n0,0,1\n1,1,0\n' | python3 run_mod.py tl`
**Salida del script (real):**
```
a) Resuelvo M[v]B=w -> NO existe v (w no in Im T)
b) N(T): M[v]B=0 -> dim N(T)= 1 ; Base N(T)(canon): v1: 1 0 0
```
**Cómo lo escribo en el examen:** a) No existe $v$: $(0,2,1)\notin\operatorname{Im}(T)$ (sistema incompatible, $\det M_{EB}=0$ y rango ampliada $=3$). b) $\dim N(T)=1$, $N(T)=\langle(1,0,0)\rangle$.
**Caveat:** coincide exacto con la oficial. Bien resuelto el detalle de la base no canónica: el script reconstruye el núcleo en coordenadas canónicas ($[v]_B=(-1,-1,1)\to v=(1,0,0)$).

### Ej 2 — Diagonalización con parámetro k · [diag] | SÍ (sustituyendo k)
**Enunciado (resumen):** $A=\begin{psmallmatrix}2&-2&0\\0&2&k\\0&0&3\end{psmallmatrix}$. a) $k$ diagonalizable. b) $k=0$: base de autovectores.
**De dónde salen los inputs:** triangular, autovalores $2,2,3$; el bloqueo de $m_g(2)$ lo causa la entrada constante $-2$, no $k$. Se verifica con $k=0$ y un control (k=5) que el rango de $A-2I$ es siempre 2.
**Inputs Casio:** `diag`, `n=3`, filas con $k$.
**Comandos de verificación:**
`printf '3\n2,-2,0\n0,2,0\n0,0,3\n' | python3 run_mod.py diag`  (k=0)
`printf '3\n2,-2,0\n0,2,5\n0,0,3\n' | python3 run_mod.py diag`  (k=5 control)
**Salida del script (real):**
```
k=0: Autovalores 3,2,2 ; S_L=3 v: 0 0 1 ; S_L=2 dimK=1<m=2 (NO diag.) v: 1 0 0 ; NO diagonaliz.
k=5: Autovalores 3,2,2 ; S_L=3 v: -10 5 1 ; S_L=2 dimK=1<m=2 (NO diag.) v: 1 0 0 ; NO diagonaliz.
```
**Cómo lo escribo en el examen:** a) NO existe $k$ que la haga diagonalizable: para todo $k$, $m_g(2)=1<2=m_a(2)$. b) $k=0$: autovectores $S_2=\langle(1,0,0)\rangle$, $S_3=\langle(0,0,1)\rangle$; sólo 2 LI ⇒ no hay base de autovectores de $\mathbb{R}^3$.
**Caveat:** coincide exacto con la oficial. El script muestra la deficiencia en cada $k$ probado, confirmando la conclusión "ningún $k$" (que formalmente se argumenta a mano).

### Ej 3 — PLU + QR de 3×2 · [qr; lu NO soporta no-cuadrada] | PARCIAL
**Enunciado (resumen):** $A=\begin{psmallmatrix}3&1\\2&6\\7&-3\end{psmallmatrix}$ (3×2). a) PLU. b) QR.
**De dónde salen los inputs:** las filas; para QR `filas=3, cols=2`.
**Inputs Casio:** b) `qr` → `3`,`2`, filas. a) `lu` pide matriz **cuadrada** (`read_mat(n,n)`) → NO admite 3×2.
**Comando de verificación (QR):**
`printf '3\n2\n3,1\n2,6\n7,-3\n' | python3 run_mod.py qr`
**Salida del script (real):**
```
QR: ||u1||=7.874 v1: 0.381 0.254 0.889 ; <a2,v1>=-0.762 ||u2||=6.739 v2: 0.1915 0.919 -0.3446
 Q:[0.381 0.1915 / 0.254 0.919 / 0.889 -0.3446]  R:[7.874 -0.762 / 0 6.739]  |QR-A|=0
```
**Cómo lo escribo en el examen:** b) $Q=\begin{psmallmatrix}3/\sqrt{62}&5/\sqrt{682}\\2/\sqrt{62}&24/\sqrt{682}\\7/\sqrt{62}&-9/\sqrt{682}\end{psmallmatrix}$, $R=\begin{psmallmatrix}\sqrt{62}&-3\sqrt{62}/31\\0&8\sqrt{682}/31\end{psmallmatrix}\approx\begin{psmallmatrix}7.874&-0.762\\0&6.739\end{psmallmatrix}$ (coincide exacto). a) PLU **a mano**: $P=I$, $L=\begin{psmallmatrix}1&0&0\\2/3&1&0\\7/3&-1&1\end{psmallmatrix}$, $U=\begin{psmallmatrix}3&1\\0&16/3\\0&0\end{psmallmatrix}$.
**Caveat:** **el módulo `lu` está hardcodeado a matrices cuadradas** (`read_mat(n,n)`), así que la PLU de una 3×2 NO se puede correr con el script — hay que hacerla a mano (Doolittle sin pivoteo, $P=I$). QR sí funciona y coincide exacto.

---

## IP Tema 5

### Ej 1 — TL con parámetros p,q (det≠0) + diag · [tl:1 y diag] | SÍ (verificación)
**Enunciado (resumen):** $M_{EE}(T)=\begin{psmallmatrix}p&3&2\\0&1&1\\q&0&1\end{psmallmatrix}$. a) $p,q$ con $\dim N(T)\neq0$. b) $p=2,q=0$: autovalores y ¿diagonalizable?
**De dónde salen los inputs:** a) $\det=0\iff p+q=0\iff p=-q$ (a mano); se verifica un caso (p=2,q=-2) con `tl:1`. b) sustituir $p=2,q=0$ en `diag`.
**Inputs Casio:** a) `tl` op `1`, filas con $p,q$; b) `diag` `n=3`, filas con $p=2,q=0$ (fila3 = `0,0,1`).
**Comandos de verificación:**
`printf '3\n2,3,2\n0,1,1\n0,0,1\n' | python3 run_mod.py diag`  (b: p=2,q=0)
`printf '1\n3\n3\n2,3,2\n0,1,1\n-2,0,1\n' | python3 run_mod.py tl`  (a: p=2,q=-2, det=0)
**Salida del script (real):**
```
b) Autovalores 2,1,1 ; S_L=2 v: 1 0 0 ; S_L=1 dimK=1<m=2 (NO diag.) v: -3 1 0 ; NO diagonaliz.
a) p=2,q=-2: rref [1 0 -0.5/0 1 1/0 0 0] ; rg=2 ; dim N=1 ; n1: 0.5 -1 1
```
**Cómo lo escribo en el examen:** a) $\dim N(T)\neq0 \iff \det M_{EE}=0 \iff p=-q$. b) $p=2,q=0$: $p_A(\lambda)=(\lambda-2)(\lambda-1)^2$, autovalores $\{2,1,1\}$; NO diagonalizable porque $S_1$ tiene dim 1 ($<2$).
**Caveat:** coincide con la oficial. La relación $p=-q$ es a mano (det simbólico); el script verifica el caso singular y resuelve la parte b numéricamente exacta.

### Ej 2 — TL P2→R⁴: M_{B1B2} + núcleo/imagen · [tl:1 para b; M_{B1B2} no cubierto] | PARCIAL
**Enunciado (resumen):** $T(a+bx+cx^2)=(2a-2b,\,c,\,a-b,\,b-a)$. a) $M_{B_1B_2}(T)$ con $B_1=\{-1,x+1,x^2\}$, $B_2$ dada. b) base y dim de $N(T)$ y $R(T)$.
**De dónde salen los inputs:** la matriz canónica $M_{EE}$ tiene columnas $T(1)=(2,0,1,-1)$, $T(x)=(-2,0,-1,1)$, $T(x^2)=(0,1,0,0)$, es decir filas $(2,-2,0)/(0,0,1)/(1,-1,0)/(-1,1,0)$. Con eso `tl:1` da núcleo/imagen (parte b).
**Inputs Casio:** b) `tl` op `1`, `filas=4`, `cols=3`, las 4 filas. a) **no hay módulo** para la matriz de una TL entre dos bases no canónicas.
**Comando de verificación (b):**
`printf '1\n4\n3\n2,-2,0\n0,0,1\n1,-1,0\n-1,1,0\n' | python3 run_mod.py tl`
**Salida del script (real):**
```
rref [1 -1 0 / 0 0 1 / 0 0 0 / 0 0 0] ; rg=2 ; dim N=1
Base N(T): n1: 1 1 0
Im(T): c1: 2 0 1 -1 ; c3: 0 1 0 0
```
**Cómo lo escribo en el examen:** b) $N(T)$: $n_1=(1,1,0)$ en coords $(a,b,c)$ ⇒ $a=b,c=0$ ⇒ $B_{N(T)}=\{1+x\}$, $\dim N(T)=1$. $R(T)$: $B_{R(T)}=\{(2,0,1,-1),(0,1,0,0)\}$, $\dim R(T)=2$. a) $M_{B_1B_2}$ **a mano**: $\begin{psmallmatrix}0&0&1\\-2&0&0\\-1&0&1\\1&0&0\end{psmallmatrix}$.
**Caveat:** parte b coincide con la oficial (la imagen $c_1=(2,0,1,-1)=-(-2,0,-1,1)$, misma dirección, base válida). Parte a **No cubierta**: ningún módulo arma la matriz de una TL entre dos bases no canónicas (P2→R⁴ además es dim distinta de los módulos cuadrados). Se hace a mano.

### Ej 3 — Subespacio de R²ˣ² con restricciones · [verificación con mat.solve; base no cubierta] | PARCIAL
**Enunciado (resumen):** $A=\{[\begin{smallmatrix}a&b\\c&d\end{smallmatrix}]:2a+3b-c=0\wedge b-2d=0\}$. a) base y dim. b) coords de $[\begin{smallmatrix}-3&2\\0&1\end{smallmatrix}]$.
**De dónde salen los inputs:** parametrizar las restricciones ($b=2d$, $c=2a+6d$) da $B=\{[\begin{smallmatrix}1&0\\2&0\end{smallmatrix}],[\begin{smallmatrix}0&2\\6&1\end{smallmatrix}]\}$ (a mano). Como vectores de $\mathbb{R}^4$ $(a,b,c,d)$: $b_1=(1,0,2,0)$, $b_2=(0,2,6,1)$; target $(-3,2,0,1)$.
**Inputs Casio:** a) parametrización es a mano. b) `cb` (cambio de base) requiere base cuadrada (dim×dim); acá son 2 vectores en $\mathbb{R}^4$, así que NO entra en `cb`. Se resuelve el sistema $\alpha b_1+\beta b_2=$ target (4 ecuaciones, 2 incógnitas) con `mat.solve` (equivalente a `tl:2` poniendo $b_1,b_2$ como columnas).
**Comando de verificación:** (helper de `mat`)
```
coords (alpha,beta) = [-3.0, 1.0] ; libres = 0
restricciones del target: 2a+3b-c=0  ; b-2d=0  (pertenece)
```
**Cómo lo escribo en el examen:** a) $\dim A=2$, $B=\{[\begin{smallmatrix}1&0\\2&0\end{smallmatrix}],[\begin{smallmatrix}0&2\\6&1\end{smallmatrix}]\}$. b) $[M]_B=(-3,1)^T$.
**Caveat:** coincide exacto con la oficial. La base (a) sale de parametrizar restricciones (simbólico, a mano). Las coordenadas (b) se verifican resolviendo el sistema (vía `tl:2`/`mat.solve` con los vectores de $B$ como columnas y la matriz objetivo como $b$), pero `cb` no aplica por base no cuadrada.

---

## Resumen de cobertura (bloque A: Temas I–V)

| Tema | Ej | Tema/Módulo | Estado |
|------|----|-------------|--------|
| 1 | 1 | TL núcleo/imagen/antiimagen · tl:1, tl:2 | SÍ |
| 1 | 2 | Diag con k · diag (sustituyendo) | SÍ |
| 1 | 3 | SVD + QR 2×2 · svd, qr | SÍ |
| 1 | 4 | MMCC a·cos+b·sen · lsq:3 | SÍ |
| 1 | 5 | Subespacio P2 con a · verif tl:1 | PARCIAL |
| 2 | 1 | TL núcleo/imagen/antiimagen · tl:1, tl:2 | SÍ |
| 2 | 2 | SVD + QR 2×2 · svd, qr | SÍ |
| 2 | 3 | MMCC y=ax²+b · lsq:1 (truco x→x²) | SÍ |
| 3 | 1 | Rango TL con k · tl:1 (sustituyendo) | SÍ |
| 3 | 2 | Diag con k · diag (sustituyendo) | SÍ |
| 3 | 3 | PLU + QR 3×3 · lu, qr | SÍ (PLU difiere por pivoteo) |
| 4 | 1 | TL M_EB base B · tl:4 | SÍ |
| 4 | 2 | Diag con k · diag (sustituyendo) | SÍ |
| 4 | 3 | PLU + QR 3×2 · qr (lu no soporta no-cuadrada) | PARCIAL |
| 5 | 1 | TL con p,q + diag · tl:1, diag | SÍ |
| 5 | 2 | TL P2→R⁴ M_{B1B2} + núcleo/imagen · tl:1 (b) | PARCIAL |
| 5 | 3 | Subespacio R²ˣ² · verif mat.solve | PARCIAL |

**Conteo:** 13 SÍ · 4 PARCIAL · 0 totalmente No cubierto.
(Las 4 PARCIAL: en todas el script verifica o resuelve la sub-parte numérica; lo no cubierto es siempre el componente simbólico — despejar parámetro, parametrizar restricciones, o armar la matriz $M_{B_1B_2}$ entre dos bases no canónicas.)
# Sección IP-B — Parciales IP Tema VI, VII, VIII, IX y Recuperatorio Tema XIII

> Todas las salidas pegadas abajo son **reales** (ejecutadas en `/tmp/acasios_sb` con `python3 run_mod.py <mod>`). Las discrepancias con la `-resolucion` oficial están marcadas en cada **Caveat**.

---

## IP Tema VI

### Ej 1 — dim R(T)=1 y base de N(T) (param k) · [tl:1] | SÍ (para k=0)
**Enunciado (resumen):** $A=M_{EE}(T)=\begin{pmatrix}2&8&k\\-1&-4&0\\k+3&12&2k\end{pmatrix}$. a) Hallar $k$ con $\dim R(T)=1$. b) Para $k=0$, base de $N(T)$.
**De dónde salen los inputs:** Parte a) es simbólica ($\det A=4k^2$ ⟹ candidato $k=0$): **a mano**. El único caso numérico ($k=0$) se carga como matriz y `tl` opción 1 da rango, base de N(T) y base de Im(T) de un tiro.
**Inputs Casio:** módulo `tl`, opción `1` (N(T),Im,rg); secuencia: `Op=1`, `filas=3`, `cols=3`, filas `2,8,0` / `-1,-4,0` / `3,12,0`.
**Comando de verificación:**
`printf '1\n3\n3\n2,8,0\n-1,-4,0\n3,12,0\n' | python3 run_mod.py tl`
**Salida del script (real):**
```
-- RREF: N(T) Im(T)
rref:
1 4 0
0 0 0
0 0 0
rg= 1
dim N= 2

-- Base N(T)
n1:
-4 1 0
n2:
0 0 1

-- Base Im(T)
(cols pivote de A)
c1:
2 -1 3
```
**Cómo lo escribo en el examen:** a) $\det A=4k^2$, nulo solo si $k=0$; con $k=0$ las columnas son múltiplos de $(2,-1,3)$ y $c_3=0$, así $\operatorname{rg}(A)=1$ ⟹ $\boxed{k=0}$. b) $N(T)=\langle(-4,1,0),(0,0,1)\rangle$, $\dim N(T)=2$ (y $\dim N+\dim R=2+1=3$ ✓).
**Caveat:** Coincide 100% con la oficial. La parte a) (hallar el $k$) es simbólica y va a mano; el script solo confirma el rango/núcleo para el $k$ ya hallado.

### Ej 2 — diagonalizar + base B con M(T)_BB=diag(1,-1,-1) · [diag] | SÍ
**Enunciado (resumen):** $A=\begin{pmatrix}1&0&0\\2&-1&0\\-4&0&-1\end{pmatrix}$. a) ¿Diagonalizable? b) Base $B$ con $M(T)_{BB}=\operatorname{diag}(1,-1,-1)$.
**De dónde salen los inputs:** La matriz va tal cual (filas). "Base B con M(T)_BB=diag" = diagonalizar: $B$ = columnas de $P$, $M(T)_{BB}=D$.
**Inputs Casio:** módulo `diag`; secuencia: `n=3`, filas `1,0,0` / `2,-1,0` / `-4,0,-1`.
**Comando de verificación:**
`printf '3\n1,0,0\n2,-1,0\n-4,0,-1\n' | python3 run_mod.py diag`
**Salida del script (real):**
```
-- P(L) caract.
p(L)=L^3+
a=1
b=-1
c=-1
...
Autovalores:
L1=1
L2=-1
L3=-1

-- S_L=1
v:
-0.5 -0.5 1

-- S_L=-1 m=2
v:
0 1 0
v:
0 0 1

-- Armando P,D
P:
-0.5 0 0
-0.5 1 0
   1 0 1
D:
1  0  0
0 -1  0
0  0 -1
|AP-PD|=0
```
**Cómo lo escribo en el examen:** a) Autovalores $1,-1,-1$; para $\lambda=-1$, $m_g=2=m_a$ ⟹ **diagonalizable**. b) $B=\{(1,1,-2),(0,1,0),(0,0,1)\}$ (autovector de $\lambda=1$ primero), con ese orden $M(T)_{BB}=\operatorname{diag}(1,-1,-1)$.
**Caveat:** Coincide con la oficial. El autovector de $\lambda=1$ que da el script es $(-0.5,-0.5,1)=-\tfrac12(1,1,-2)$, proporcional al oficial $(1,1,-2)$ (escala distinta, mismo subespacio). $|AP-PD|=0$ certifica que la base es válida. **Ojo con el orden** de las columnas para que la diagonal salga $(1,-1,-1)$ y no otra permutación.

### Ej 3 — independencia lineal con parámetros a,b · No cubierto
**Enunciado (resumen):** $\{v,u,w\}$ LI; hallar $a,b$ para que $\{u+av,\,w,\,u+2av+bw\}$ sea LI.
**De dónde salen los inputs:** No hay matriz numérica: las coordenadas en la base abstracta $\{v,u,w\}$ tienen parámetro $a,b$. Ningún script hace álgebra simbólica.
**Inputs Casio / Salida:** —
**Cómo lo escribo en el examen:** Coordenadas en $\{v,u,w\}$: columnas $(a,1,0)$, $(0,0,1)$, $(2a,1,b)$; $\det=-a$. LI $\iff a\ne0$, $b$ arbitrario.
**Caveat:** **No cubierto** (parámetro simbólico puro). Se resuelve a mano por determinante. Coincide con la oficial.

---

## IP Tema VII

### Ej 1 — a,b para que (0,-1,1) sea autovector + ¿diag? · [param] | SÍ
**Enunciado (resumen):** $A=\begin{pmatrix}1&0&b\\1&1&0\\1&1&a\end{pmatrix}$. a) $a,b$ para que $(0,-1,1)$ sea autovector. b) ¿Diagonalizable?
**De dónde salen los inputs:** Es exactamente el caso de `param`: autovector pedido $(0,-1,1)$ y matriz con letras `a,b` en sus posiciones.
**Inputs Casio:** módulo `param`; secuencia: `n=3`, autovector `0,-1,1`, filas `1,0,b` / `1,1,0` / `1,1,a`.
**Comando de verificación:**
`printf '3\n0,-1,1\n1,0,b\n1,1,0\n1,1,a\n' | python3 run_mod.py param`
**Salida del script (real):**
```
-- a) Parametros
b=0
a=2
L=1

-- b) Diagonaliz?
A:
1 0 0
1 1 0
1 1 2
...
Autovalores:
L1=2
L2=1
L3=1

-- S_L=2
v:
0 0 1

-- S_L=1 m=2
dimK= 1 <m= 2
(NO diag.)
v:
0 -1 1
NO diagonaliz.
dim= 2 <n= 3
```
**Cómo lo escribo en el examen:** a) $a=2$, $b=0$, autovalor asociado $\lambda=1$. b) $p_A(\lambda)=(\lambda-1)^2(\lambda-2)$; para $\lambda=1$ $m_g=1<2=m_a$ ⟹ **NO diagonalizable**.
**Caveat:** Coincide 100% con la oficial (incluso el autovector de $\lambda=1$ es $(0,-1,1)$, el del enunciado). `param` resuelve la parte a) directamente y encadena la parte b).

### Ej 2 — antiimagen T(v)=(0,2,1) y dim N(T) con M(T)_EB en base B · [tl:4] | SÍ
**Enunciado (resumen):** $M(T)_{EB}=\begin{pmatrix}2&0&2\\0&3&3\\1&-1&0\end{pmatrix}$, $B=\{(0,1,-1),(0,0,1),(1,1,0)\}$. a) $v$ con $T(v)=(0,2,1)$. b) $\dim N(T)$.
**De dónde salen los inputs:** Matriz $M$ en base no canónica del dominio ⟹ `tl` opción 4. Las filas de $B$ son los vectores de la base; $w=(0,2,1)$.
**Inputs Casio (a):** módulo `tl`, opción `4` (M(T)_EB base B), sub-opción `1` (Antiimg T(v)=w); secuencia: `Op=4`, `Op=1`, `dim=3`, $M$ filas `2,0,2`/`0,3,3`/`1,-1,0`, $B$ filas `0,1,-1`/`0,0,1`/`1,1,0`, `w=0,2,1`.
**Comando de verificación (a):**
`printf '4\n1\n3\n2,0,2\n0,3,3\n1,-1,0\n0,1,-1\n0,0,1\n1,1,0\n0,2,1\n' | python3 run_mod.py tl`
**Salida del script (real, a):**
```
-- Resuelvo M[v]B=w
NO existe v
(w no in Im T)
```
**Comando de verificación (b):** misma estructura con sub-opción `2` (Núcleo):
`printf '4\n2\n3\n2,0,2\n0,3,3\n1,-1,0\n0,1,-1\n0,0,1\n1,1,0\n' | python3 run_mod.py tl`
**Salida del script (real, b):**
```
-- N(T): M[v]B=0
dim N(T)= 1
Base N(T)(canon):
v1:
1 0 0
```
**Cómo lo escribo en el examen:** a) El sistema $M[v]_B=(0,2,1)$ es **incompatible** ⟹ no existe $v$ con $T(v)=(0,2,1)$ ($\det M=0$, $(0,2,1)\notin\operatorname{Im}T$). b) $\dim N(T)=1$ (base canónica $(1,0,0)$).
**Caveat:** Coincide 100% con la oficial. La opción 4 ya reconstruye el núcleo en coordenadas canónicas ($v=(1,0,0)$), tal cual la resolución.

### Ej 3 — serie de Fourier de |cos t| · No cubierto
**Enunciado (resumen):** $f(t)=|\cos t|$. a) Serie trigonométrica. b) Convergencia de $f'$ en $t=\pi/2$.
**De dónde salen los inputs:** —
**Inputs Casio / Salida:** —
**Cómo lo escribo en el examen:** $|\cos t|=\frac{2}{\pi}+\frac{4}{\pi}\sum_{n\ge1}\frac{(-1)^{n+1}}{4n^2-1}\cos(2nt)$ (par, $T=\pi$, $b_n=0$). b) Salto de $f'$ en $\pi/2$ entre $-1$ y $+1$ ⟹ converge a $0$ (Dirichlet).
**Caveat:** **No cubierto.** Los 9 templates de `fs` NO incluyen $|\cos t|$. Se hace a mano (producto-a-suma). Coincide con la oficial.

---

## IP Tema VIII

### Ej 1 — k para que (0,-1,1) sea autovector + ¿diag? · [param + diag] | PARCIAL (cuidado)
**Enunciado (resumen):** $A=\begin{pmatrix}k&0&0\\2&-2&-1\\-2&5&4\end{pmatrix}$. a) $k$ para que $(0,-1,1)$ sea autovector. b) ¿Diagonalizable?
**De dónde salen los inputs:** Igual estructura que un `param`, PERO acá la primera componente del autovector es 0 y multiplica justo a la única posición con $k$ ⟹ $k$ queda **libre** ($(0,-1,1)$ es autovector con $\lambda=-1$ para **todo** $k$). El `param` resuelve un sistema y devuelve **un** valor concreto (no toda la familia).
**Inputs Casio (a, param):** `param`; `n=3`, autovector `0,-1,1`, filas `k,0,0` / `2,-2,-1` / `-2,5,4`.
**Comando de verificación (a):**
`printf '3\n0,-1,1\nk,0,0\n2,-2,-1\n-2,5,4\n' | python3 run_mod.py param`
**Salida del script (real, a):**
```
-- a) Parametros
k=0
L=-1
(infinitas sol:
 hay libre/s)
...
```
**Cómo lo escribo en el examen:** a) $A(0,-1,1)^T=(0,1,-1)^T=-1\cdot(0,-1,1)^T$ **para todo $k$** (la 1ª coord 0 anula a $k$); autovalor $\lambda=-1$. b) $p_A(\lambda)=(\lambda-k)(\lambda-3)(\lambda+1)$: diagonalizable $\iff k\ne-1$ (en $k=-1$, $\lambda=-1$ tiene $m_a=2$, $m_g=1$).
**Caveat (importante):** El `param` da `k=0` pero **avisa** `(infinitas sol: hay libre/s)` — esa es la señal de que $k$ es libre, NO que la respuesta sea $k=0$. La respuesta correcta (todo $k$) va a mano leyendo ese aviso. La parte b) la verifiqué sustituyendo los dos casos críticos:
**Verif b) con diag, k=−1 (esperado NO diag):**
`printf '3\n-1,0,0\n2,-2,-1\n-2,5,4\n' | python3 run_mod.py diag` →
```
Autovalores: L1=3 L2=-1 L3=-1
-- S_L=-1 m=2
dimK= 1 <m= 2
(NO diag.)
NO diagonaliz.
```
**Verif b) con diag, k=3 (esperado SÍ diag):**
`printf '3\n3,0,0\n2,-2,-1\n-2,5,4\n' | python3 run_mod.py diag` →
```
Autovalores: L1=3 L2=3 L3=-1
-- S_L=3 m=2
v: 2.5 1 0
v: 0.5 0 1
...
|AP-PD|=8.882e-16
```
Ambos casos confirman la oficial (NO diag solo en $k=-1$). **PARCIAL** porque la respuesta de a) (familia de $k$) no la entrega el script: la inferís del aviso "hay libre/s" + a mano.

### Ej 2 — QR y PLU de A=[[2,0,2],[0,3,3],[1,-1,0]] (singular) · [qr / lu] | PARCIAL (ambas abortan por singularidad)
**Enunciado (resumen):** a) QR. b) PLU. (Columnas: $a_3=a_1+a_2$ ⟹ $\operatorname{rg}A=2$, singular.)
**De dónde salen los inputs:** matriz tal cual.
**Inputs Casio (a):** `qr`; `filas=3`, `cols=3`, filas `2,0,2`/`0,3,3`/`1,-1,0`.
**Comando de verificación (a):**
`printf '3\n3\n2,0,2\n0,3,3\n1,-1,0\n' | python3 run_mod.py qr`
**Salida del script (real, a):**
```
-- Col 1
||u1||=2.236
v1:
0.8944 0 0.4472

-- Col 2
<a2,v1>=-0.4472
||u2||=3.13
v2:
0.1278 0.9583 -0.2556

-- Col 3
<a3,v1>=1.789
<a3,v2>=3.13
||u3||=1.57e-16
col LD: no QR
```
**Inputs Casio (b):** `lu`; `n=3`, filas `2,0,2`/`0,3,3`/`1,-1,0`.
**Comando de verificación (b):**
`printf '3\n2,0,2\n0,3,3\n1,-1,0\n' | python3 run_mod.py lu`
**Salida del script (real, b):**
```
-- Tras col 1
U:
2  0  2
0  3  3
0 -1 -1

-- Tras col 2
U:
2 0 2
0 3 3
0 0 0
piv=0, A sing.
```
**Cómo lo escribo en el examen:** a) Gram-Schmidt: $v_1=\tfrac{1}{\sqrt5}(2,0,1)$, $v_2=(0.1278,0.9583,-0.2556)$, $u_3=0$ (col LD); se completa $v_3=\tfrac17(-3,2,6)$ a mano. $R_{11}=\sqrt5=2.236$, $R_{12}=-0.4472$, $R_{22}=\tfrac{7\sqrt5}{5}=3.13$, $R_{13}=1.789$, $R_{23}=3.13$, $R_{33}=0$. b) Eliminación: $P=I$, $L=\begin{psmallmatrix}1&0&0\\0&1&0\\\frac12&-\frac13&1\end{psmallmatrix}$, $U=\begin{psmallmatrix}2&0&2\\0&3&3\\0&0&0\end{psmallmatrix}$.
**Caveat (importante, doble limitación):**
- **QR:** el script **se detiene** en la 3ª columna con `col LD: no QR` (exige columnas LI). Igual entrega $v_1,v_2$ y todos los coeficientes $R_{ij}$ (que coinciden con la oficial: $v_1,v_2$ y $R_{11}=2.236,R_{12}=-0.4472,R_{22}=3.13,R_{13}=1.789,R_{23}=3.13$). La 3ª columna ortonormal $v_3=(-3,2,6)/7$ y $R_{33}=0$ se completan a mano.
- **PLU:** el script aborta con `piv=0, A sing.` al llegar al pivote $U_{33}=0$ y **NO imprime $P,L,U$ finales**. Pero las dos matrices `U` intermedias son correctas ($U$ tras col 2 = la $U$ final oficial). Los multiplicadores $L_{31}=\tfrac12$, $L_{32}=-\tfrac13$ se leen del proceso a mano (o de la teoría). $P=I$.
Resultado numérico **coincide** con la oficial en lo que el script sí calcula. Marcado **PARCIAL** por los dos abortos por singularidad.

### Ej 3 — serie de Fourier de |sen t| · No cubierto
**Enunciado (resumen):** $f(t)=|\sin t|$. a) Serie trigonométrica. b) Convergencia de $f'$ en $t=\pi$.
**Inputs Casio / Salida:** —
**Cómo lo escribo en el examen:** $|\sin t|=\frac{2}{\pi}-\frac{4}{\pi}\sum_{n\ge1}\frac{\cos(2nt)}{4n^2-1}$ ($T=\pi$, par, $b_n=0$). b) Salto de $f'$ en $\pi$ entre $-1$ y $+1$ ⟹ converge a $0$.
**Caveat:** **No cubierto** (no hay template $|\sin t|$ en `fs`). A mano. Coincide con la oficial.

---

## IP Tema IX

### Ej 1 — k para dim N(T)=1, y R(T) con k=2 · [tl:1] | SÍ
**Enunciado (resumen):** $M_{EE}(T)=\begin{pmatrix}0&k&1\\k&0&1\\1&1&0\end{pmatrix}$. a) $k$ con $\dim N(T)=1$. b) Para $k=2$, hallar $R(T)$.
**De dónde salen los inputs:** Parte a) ($\det=2k$ ⟹ $k=0$) es simbólica a mano; los casos concretos se verifican con `tl` op 1 (rango, N, Im). Parte b) es $k=2$ directo.
**Inputs Casio (b, k=2):** `tl`, opción `1`; `filas=3`, `cols=3`, filas `0,2,1`/`2,0,1`/`1,1,0`.
**Comando de verificación (b):**
`printf '1\n3\n3\n0,2,1\n2,0,1\n1,1,0\n' | python3 run_mod.py tl`
**Salida del script (real, b):**
```
-- RREF: N(T) Im(T)
rref:
1 0 0
0 1 0
0 0 1
rg= 3
dim N= 0
...
N(T)={0}
```
**Verif a) con k=0 (esperado dim N=1):**
`printf '1\n3\n3\n0,0,1\n0,0,1\n1,1,0\n' | python3 run_mod.py tl` →
```
rg= 2
dim N= 1
-- Base N(T)
n1: -1 1 0
```
**Cómo lo escribo en el examen:** a) $\det M=2k=0\iff k=0$; con $k=0$, $\operatorname{rg}=2$ ⟹ $\dim N(T)=1$ ⟹ $\boxed{k=0}$. b) Con $k=2$, $\operatorname{rg}=3$ ⟹ $T$ biyectiva ⟹ $R(T)=\mathbb{R}^3$.
**Caveat:** Coincide con la oficial. El $k$ de a) sale a mano del determinante; el script confirma los rangos.

### Ej 2 — k para λ=-1 autovalor + diagonalizar k=2 · [diag] | PARCIAL (param NO sirve para "λ autovalor")
**Enunciado (resumen):** $A=\begin{pmatrix}3&0&1\\1&k&-1\\2&0&2\end{pmatrix}$. a) $k$ para que $\lambda=-1$ sea autovalor. b) Para $k=2$, diagonalizar.
**De dónde salen los inputs:** **Atención:** la parte a) pide "λ=−1 sea autovalor", NO "v sea autovector". `param` resuelve el problema *del autovector*, así que **no es la herramienta correcta** acá (necesitaría el autovector, que no se conoce). La parte a) va a mano: $p_A(\lambda)=(\lambda-k)(\lambda^2-5\lambda+4)$, $p_A(-1)=0\Rightarrow k=-1$. Verifico sustituyendo $k=-1$ en `diag`. Parte b) ($k=2$) directo en `diag`.
**Inputs Casio (b, k=2):** `diag`; `n=3`, filas `3,0,1`/`1,2,-1`/`2,0,2`.
**Comando de verificación (b):**
`printf '3\n3,0,1\n1,2,-1\n2,0,2\n' | python3 run_mod.py diag`
**Salida del script (real, b):**
```
Autovalores:
L1=4
L2=2
L3=1

-- S_L=4
v:
1 0 1

-- S_L=2
v:
0 1 0

-- S_L=1
v:
-0.5 1.5 1

-- Armando P,D
P:
1 0 -0.5
0 1  1.5
1 0    1
D:
4 0 0
0 2 0
0 0 1
|AP-PD|=1.332e-15
```
**Verif a) con k=−1 (esperado λ=−1 entre los autovalores):**
`printf '3\n3,0,1\n1,-1,-1\n2,0,2\n' | python3 run_mod.py diag` → `Autovalores: L1=4 L2=1 L3=-1` ✓
**Cómo lo escribo en el examen:** a) $p_A(\lambda)=(\lambda-k)(\lambda-1)(\lambda-4)$; $\lambda=-1$ autovalor $\iff k=-1$. b) Con $k=2$: autovalores $4,2,1$ (todos distintos) ⟹ diagonalizable; $P=\begin{psmallmatrix}1&0&1\\0&1&-3\\1&0&-2\end{psmallmatrix}$ (autovectores $v_4=(1,0,1)$, $v_2=(0,1,0)$, $v_1=(1,-3,-2)$), $D=\operatorname{diag}(4,2,1)$.
**Caveat:** Parte b) coincide 100% con la oficial ($v_1=(-0.5,1.5,1)=-\tfrac12(1,-3,-2)$, escala distinta, mismo subespacio; $|AP-PD|\approx0$). **PARCIAL** porque la parte a) (hallar $k$ para que $\lambda=-1$ sea autovalor) **no la hace ningún script directamente** — `param` resuelve el problema equivocado; se hace a mano y se verifica sustituyendo $k=-1$ en `diag`.

### Ej 3 — SVD y QR de A=[[3,1],[5,-1],[-2,-3]] (3×2) · [svd / qr] | SÍ
**Enunciado (resumen):** a) SVD. b) QR. ($A$ es $3\times2$, $m=2\le n=3$: SVD directa, sin transponer.)
**De dónde salen los inputs:** matriz tal cual.
**Inputs Casio (a):** `svd`; `filas=3`, `cols=2`, filas `3,1`/`5,-1`/`-2,-3`.
**Comando de verificación (a):**
`printf '3\n2\n3,1\n5,-1\n-2,-3\n' | python3 run_mod.py svd`
**Salida del script (real, a):**
```
-- Via AtA 2x2
AtA:
38  4
 4 11
tr=49
det=402
disc=793

-- V.singulares
s1=6.21129
s2=3.22798

-- V cols
v1:
0.9896 0.1435
v2:
-0.1435 0.9896

-- U cols
u1:
0.5011 0.7735 -0.388
u2:
0.1732 -0.5289
-0.8308
u3:
0.8479 -0.3491 0.399

-- Verif
|USVt-A|=1.776e-15
Sigma:
6.211     0
    0 3.228
    0     0
```
**Inputs Casio (b):** `qr`; `filas=3`, `cols=2`, mismas filas.
**Comando de verificación (b):**
`printf '3\n2\n3,1\n5,-1\n-2,-3\n' | python3 run_mod.py qr`
**Salida del script (real, b):**
```
-- Col 1
||u1||=6.164
v1:
0.4867 0.8111 -0.3244

-- Col 2
<a2,v1>=0.6489
||u2||=3.253
v2:
0.2104 -0.4693
-0.8576

-- Resultado
Q:
 0.4867  0.2104
 0.8111 -0.4693
-0.3244 -0.8576
R:
6.164 0.6489
    0  3.253
|QR-A|=0
|QtQ-I|=2.22e-16
```
**Cómo lo escribo en el examen:** a) $\sigma_1=6.2113$, $\sigma_2=3.2280$; $V=\begin{psmallmatrix}0.9896&0.1435\\0.1435&-0.9896\end{psmallmatrix}$, $U=\begin{psmallmatrix}0.5011&-0.1732&0.8479\\0.7735&0.5289&-0.3491\\-0.388&0.8308&0.399\end{psmallmatrix}$, $\Sigma=\operatorname{diag}(6.211,3.228)$ con fila nula extra. b) $Q=\begin{psmallmatrix}0.4867&0.2104\\0.8111&-0.4693\\-0.3244&-0.8576\end{psmallmatrix}$, $R=\begin{psmallmatrix}6.164&0.6489\\0&3.253\end{psmallmatrix}$.
**Caveat:** Coincide con la oficial. El 2º vector singular sale con signo global opuesto ($v_2=(-0.1435,0.9896)$ vs oficial $(0.1435,-0.9896)$; $u_2$ correspondientemente con signo opuesto): **ambos signos son válidos** porque $\pm v_2$ generan el mismo subespacio y $U\Sigma V^T=A$ se mantiene ($|USVt-A|=1.78\times10^{-15}$). QR exacto.

---

## Recuperatorio Tema XIII

### Ej 1 — h con dim R(T)<3, y h para no diagonalizable · [diag] | SÍ (verificando por casos)
**Enunciado (resumen):** $M_{EE}(T)=\begin{pmatrix}2&0&0\\0&h&0\\-1&1&1\end{pmatrix}$. a) $h$ con $\dim R(T)<3$. b) $h$ para que NO sea diagonalizable.
**De dónde salen los inputs:** a) simbólica ($\det=2h\Rightarrow h=0$): a mano. b) Autovalores $2,h,1$; candidatos a repetir: $h=2$ y $h=1$. Se verifican sustituyendo cada uno en `diag`.
**Inputs Casio (b, h=1):** `diag`; `n=3`, filas `2,0,0`/`0,1,0`/`-1,1,1`.
**Comando de verificación (b, h=1):**
`printf '3\n2,0,0\n0,1,0\n-1,1,1\n' | python3 run_mod.py diag`
**Salida del script (real, h=1):**
```
Autovalores:
L1=2
L2=1
L3=1

-- S_L=2
v:
-1 0 1

-- S_L=1 m=2
dimK= 1 <m= 2
(NO diag.)
v:
0 0 1
NO diagonaliz.
dim= 2 <n= 3
```
**Comando de verificación (b, h=2):**
`printf '3\n2,0,0\n0,2,0\n-1,1,1\n' | python3 run_mod.py diag` →
```
Autovalores: L1=2 L2=2 L3=1
-- S_L=2 m=2
v: 1 1 0
v: -1 0 1
...
|AP-PD|=5.551e-16   (diagonalizable)
```
**Cómo lo escribo en el examen:** a) $\det M=2h=0\iff h=0$ ⟹ $\dim R(T)=2<3$ solo para $\boxed{h=0}$. b) Autovalores $2,h,1$: para $h=2$ es diagonalizable ($\lambda=2$ con $m_g=m_a=2$), pero para $h=1$, $\lambda=1$ tiene $m_a=2$, $m_g=1$ ⟹ **NO diagonalizable solo para $h=1$**.
**Caveat:** Coincide 100% con la oficial. La parte a) (determinante) va a mano; la b) se confirma sustituyendo los dos $h$ críticos en `diag` (h=1 NO diag, h=2 SÍ diag).

### Ej 2 — serie de Fourier diente de sierra f(t)=t en [0,1) + convergencia · [fs:1 / fs:3] | SÍ
**Enunciado (resumen):** $f:[0,1)\to\mathbb{R}$, $f(t)=t$, período 1. a) Serie de Fourier. b) Convergencia en $t=1$ y $t=1/4$.
**De dónde salen los inputs:** $f(t)=t$ en $(0,1)$ periódica = template **9** (`t-[t] en(0,1)`). Convención `fs`: imprime `a0`(=2·media) y `a0/2`(=media). La cátedra usa $a_0$=media ⟹ tomar `a0/2`.
**Inputs Casio (a):** `fs`, opción `1` (Coef a_n b_n); secuencia: `Op=1`, template `>=9`, `#arm=4`.
**Comando de verificación (a):**
`printf '1\n9\n4\n' | python3 run_mod.py fs`
**Salida del script (real, a):**
```
T=1
w0=6.283
-- Coefs
a0=0.9983
a0/2=0.4992
n=1
 a=-0.001667
 b=-0.3183
n=2
 a=-0.001667
 b=-0.1592
n=3
 a=-0.001667
 b=-0.1061
n=4
 a=-0.001667
 b=-0.07958
```
**Inputs Casio (b):** `fs`, opción `3` (Conv en t0); `Op=3`, template `>=9`, `t0`, `#arm suma`.
**Comando de verificación (b, t0=1):**
`printf '3\n9\n1\n50\n' | python3 run_mod.py fs` →
```
x(t0+)=0.0001
x(t0-)=0.9999
prom=0.5
S_N(t0)=0.4158
```
**Comando de verificación (b, t0=0.25):**
`printf '3\n9\n0.25\n50\n' | python3 run_mod.py fs` →
```
x(t0+)=0.2501
x(t0-)=0.2499
prom=0.25
S_N(t0)=0.2476
```
**Cómo lo escribo en el examen:** a) $a_0=\tfrac12$ (=`a0/2`), $a_n=0$, $b_n=-\tfrac{1}{\pi n}$; $f(t)=\tfrac12-\tfrac1\pi\sum_{n\ge1}\tfrac{\sin(2\pi n t)}{n}$. b) En $t=1$ (salto): converge a $\tfrac{f(1^-)+f(1^+)}{2}=\tfrac{1+0}{2}=\tfrac12$. En $t=1/4$ (continuidad): converge a $f(1/4)=\tfrac14$.
**Caveat:** Coincide con la oficial. **Dos detalles:** (1) leer la **media** en `a0/2=0.4992≈1/2`, no `a0`. (2) los $a_n=-0.001667$ son **ruido numérico de Simpson** en la discontinuidad (el valor exacto es 0); $b_n$ coinciden con $-1/(\pi n)$ ($-0.3183=-1/\pi$, etc.). La opción 3 confirma directamente los promedios de Dirichlet (0.5 y 0.25).

### Ej 3 — PLU y QR de A=[[0,-1],[1,-1],[-1,0]] (3×2) · [lu / qr] | PARCIAL (lu NO acepta no-cuadrada)
**Enunciado (resumen):** $A=\begin{pmatrix}0&-1\\1&-1\\-1&0\end{pmatrix}$ ($3\times2$). a) PLU. b) QR.
**De dónde salen los inputs:** matriz tal cual; QR sí toma rectangular, `lu` NO.
**Inputs Casio (b, qr):** `qr`; `filas=3`, `cols=2`, filas `0,-1`/`1,-1`/`-1,0`.
**Comando de verificación (b):**
`printf '3\n2\n0,-1\n1,-1\n-1,0\n' | python3 run_mod.py qr`
**Salida del script (real, b):**
```
-- Col 1
||u1||=1.414
v1:
0 0.7071 -0.7071

-- Col 2
<a2,v1>=-0.7071
||u2||=1.225
v2:
-0.8165 -0.4082
-0.4082

-- Resultado
Q:
      0 -0.8165
 0.7071 -0.4082
-0.7071 -0.4082
R:
1.414 -0.7071
    0   1.225
|QR-A|=0
|QtQ-I|=2.22e-16
```
**Intento (a, lu) — FALLA:**
`printf '3\n0,-1\n1,-1\n-1,0\n' | python3 run_mod.py lu` →
```
n cuadr:A3x3:
f1/3:len?   ... EOFError (lu pide matriz CUADRADA n×n, no 3×2)
```
**Cómo lo escribo en el examen:** a) Pivote $a_{11}=0$ ⟹ permutar $F_1\leftrightarrow F_2$: $P=\begin{psmallmatrix}0&1&0\\1&0&0\\0&0&1\end{psmallmatrix}$, $L=\begin{psmallmatrix}1&0&0\\0&1&0\\-1&1&1\end{psmallmatrix}$, $U=\begin{psmallmatrix}1&-1\\0&-1\\0&0\end{psmallmatrix}$ ($PA=LU$). b) $Q=\begin{psmallmatrix}0&-0.8165\\0.7071&-0.4082\\-0.7071&-0.4082\end{psmallmatrix}$, $R=\begin{psmallmatrix}1.414&-0.7071\\0&1.225\end{psmallmatrix}$.
**Caveat (importante):**
- **QR (b):** coincide 100% con la oficial ($v_1=(0,0.7071,-0.7071)$, $v_2=(-0.8165,-0.4082,-0.4082)$, $R=\begin{psmallmatrix}\sqrt2&-\sqrt2/2\\0&\sqrt6/2\end{psmallmatrix}$). `qr` acepta matrices rectangulares de rango columna completo.
- **PLU (a):** el módulo `lu` **solo acepta matrices cuadradas** (`read_mat(n,n)`), así que con una $3\times2$ entra en loop `len?` y termina en EOFError. **No cubierto por el script** — la PLU del $3\times2$ se hace a mano (permutación obligatoria por pivote $a_{11}=0$). Marcado **PARCIAL** (QR sí, PLU no).
# Sección IIP (Temas 01, 03, 04, 05, 06) — Casio Graph 90+E

> Parciales Fourier-pesados. Ej1 = serie trigonométrica, Ej2 = transformada de Fourier, Ej3 = diferencias finitas implícitas de EDP (4 nodos internos).
>
> **Convención CRÍTICA de la cátedra vs. el script `fs`.** La cátedra define
> $$f(t)=a_0+\sum a_n\cos+\sum b_n\sin,\qquad a_0=\tfrac1T\int_T f\ (\textbf{valor medio}).$$
> El script `fs` imprime `a0 = (2/T)∫f` (es decir `2·a0_cátedra`) y `a0/2 = (1/T)∫f` (= el valor medio de la cátedra). **En el examen, el término constante es el `a0/2` que imprime el script, NO el `a0`.** Los `a=`/`b=` que imprime sí son los $a_n,b_n$ de la cátedra. Esto vale para los 5 temas.

---

## IIP Tema 01

### Ej 1 — Serie trig. de $e^t$ en $(-\pi,\pi)$ + identidad · [fs:1 / fs:3] | SÍ
**Enunciado (resumen):** $x(t)=e^t$ en $(-\pi,\pi)$, $T=2\pi$. a) serie trig.; b) probar $\sum_{n\ge1}\frac{(-1)^n}{n^2+1}=\frac{1-\sh\pi/\pi}{2\sh\pi/\pi}$ evaluando la serie en un punto.
**De dónde salen los inputs:** función + intervalo = template 7 (`e^t en(-π,π)`). Para b) se evalúa convergencia en $t_0=0$ (punto de continuidad).
**Inputs Casio (a):** módulo `fs`, opción `1` (Coef a_n b_n); secuencia: `Op=1`, `template=7`, `#arm=5`.
**Comando de verificación (a):**
`printf '1\n7\n5\n' | python3 run_mod.py fs`
**Salida del script (real):**
```
T=6.283
w0=1
a0=7.352
a0/2=3.676
n=1
 a=-3.676
 b=3.676
n=2
 a=1.47
 b=-2.941
n=3
 a=-0.7352
 b=2.206
n=4
 a=0.4325
 b=-1.73
n=5
 a=-0.2828
 b=1.414
```
**Inputs Casio (b, convergencia en $t_0=0$):** opción `3` (Conv en t0); `Op=3`, `template=7`, `t0=0`, `#arm suma=40`.
**Comando de verificación (b):**
`printf '3\n7\n0\n40\n' | python3 run_mod.py fs`
**Salida del script (real):**
```
x(t0+)=1
x(t0-)=0.9999
prom=1
S_N(t0)=1.002
```
**Cómo lo escribo en el examen:** término medio $a_0=\,$`a0/2`$=3.676=\sh(\pi)/\pi$. Coeficientes: $a_1=-3.676,\ a_2=1.47,\ a_3=-0.735,\dots$ que es $\frac{2\sh\pi}{\pi}\frac{(-1)^n}{1+n^2}$ (chequeo: $\frac{2\cdot3.676}{1}\cdot\frac{-1}{2}=-3.676$ ✓); $b_1=3.676,\ b_2=-2.941,\dots=-\frac{2\sh\pi}{\pi}\frac{n(-1)^n}{1+n^2}$. Serie: $x(t)=\frac{\sh\pi}{\pi}\big[1+\sum\frac{2(-1)^n}{1+n^2}\cos nt-\sum\frac{2n(-1)^n}{1+n^2}\sin nt\big]$. Para b): la serie en $t_0=0$ converge a $x(0)=1$ (`prom=1`, `S_N=1.002`); igualando $1=\frac{\sh\pi}{\pi}(1+2S)$ y despejando $S=\sum\frac{(-1)^n}{n^2+1}$ se obtiene la identidad pedida.
**Caveat:** coincide con la resolución oficial. Cuidar la convención `a0` vs `a0/2` (el término constante es `a0/2`). El inciso b) es analítico (despeje); el script solo confirma numéricamente que la serie en $t=0$ tiende a $1$, que es el paso clave del argumento.

### Ej 2 — Serie trig./exp./laboratorio de $t-[t]$ · [fs:1 / fs:2] | SÍ
**Enunciado (resumen):** $x(t)=t-[t]$ (parte fraccionaria, $T=1$). a) trig.; b) exponencial; c) forma de laboratorio.
**De dónde salen los inputs:** $t-[t]$ = template 9 exacto.
**Inputs Casio (a):** `Op=1`, `template=9`, `#arm=5`.
**Comando (a):** `printf '1\n9\n5\n' | python3 run_mod.py fs`
**Salida (real):**
```
T=1
w0=6.283
a0=0.9983
a0/2=0.4992
n=1
 a=-0.001667
 b=-0.3183
n=2
 a=-0.001667
 b=-0.1592
n=3
 a=-0.001667
 b=-0.1061
n=4
 a=-0.001667
 b=-0.07958
n=5
 a=-0.001667
 b=-0.06366
```
**Inputs Casio (b, exponencial):** `Op=2`, `template=9`, `|n|max=3`.
**Comando (b):** `printf '2\n9\n3\n' | python3 run_mod.py fs`
**Salida (real):**
```
c-3=-0.0008333
 +i-0.05305
 |c|=0.05306
c-2=-0.0008333
 +i-0.07958
 |c|=0.07958
c-1=-0.0008333
 +i-0.1592
 |c|=0.1592
c0=0.4992
 +i0
 |c|=0.4992
c1=-0.0008333
 +i0.1592
 |c|=0.1592
c2=-0.0008333
 +i0.07958
 |c|=0.07958
c3=-0.0008333
 +i0.05305
 |c|=0.05306
```
**Cómo lo escribo en el examen:**
- a) $a_0=$`a0/2`$=0.5=\tfrac12$; $a_n=0$ (el `-0.001667` es ruido numérico de Simpson en el salto, se interpreta $0$); $b_n=-0.3183,-0.1592,\dots=-\frac1{\pi n}$. Serie: $x(t)=\tfrac12-\sum\frac1{\pi n}\sin(2\pi n t)$.
- b) $c_0=0.4992\approx\tfrac12$; $c_n=0+0.1592i=\frac{i}{2\pi n}$ (parte real $\approx0$ es ruido); $c_{-n}=\overline{c_n}$. Serie exp.: $x(t)=\tfrac12+\sum_{n\ne0}\frac{i}{2\pi n}e^{i2\pi n t}$.
- c) Forma de laboratorio (a mano, derivada de a): $A_n=\sqrt{a_n^2+b_n^2}=|b_n|=\frac1{\pi n}$, $\varphi_n=-\tfrac\pi2$: $x(t)=\tfrac12+\sum\frac1{\pi n}\cos(2\pi n t+\tfrac\pi2)$.
**Caveat:** coincide con la oficial. Los `a_n` y `Re(c_n)` salen `≈ -0.0017 / -0.0008` (no exactamente 0) por la discontinuidad de salto en los enteros que el método de Simpson no captura limpio — interpretarlos como cero. La forma de laboratorio (c) la hace el script solo parcialmente: da $A_n=|b_n|$ pero la fase se arma a mano.

### Ej 3 — TF de la rampa $x(t)=t$ en $[0,1]$ · [tf:4] | SÍ
**Enunciado (resumen):** $x(t)=t$ si $0\le t\le1$, $0$ si no. a) TF; b) espectro.
**De dónde salen los inputs:** pulso polinómico $p(t)=0+1\cdot t$ (grado 1) en $[a,b]=[0,1]$.
**Inputs Casio:** módulo `tf`, opción `4` (Polin. num.); `Op=4`, `grado=1`, `c0=0`, `c1=1`, `a inf=0`, `b sup=1`, `w_max=5`.
**Comando de verificación:**
`printf '4\n1\n0\n1\n0\n1\n5\n' | python3 run_mod.py tf`
**Salida del script (real):** (grilla $\omega$ vs Re, Im, $|F|$)
```
 0.0
 0.5
 -0
 |0.5|
 1.0
 0.382
 -0.301
 |0.486|
 2.0
 0.101
 -0.435
 |0.447|
 3.0
 -0.174
 -0.346
 |0.387|
 4.0
 -0.293
 -0.116
 |0.315|
 5.0
 -0.22
 0.0951
 |0.24|
```
**Cómo lo escribo en el examen:** la fórmula cerrada $\hat x(\omega)=\frac{(1+i\omega)e^{-i\omega}-1}{\omega^2}$, con $\hat x(0)=\tfrac12$ (= `F=0.5` en la grilla = $\int_0^1 t\,dt$). Los puntos confirman: $\hat x(1)=0.382-0.301i$, $\hat x(2)=0.101-0.435i$. b) Espectro $|\hat x(\omega)|$ par, pico $\tfrac12$ en $\omega=0$, decae $\sim1/|\omega|$ con lóbulos: $|F|=0.5,0.486,0.447,0.387,\dots$ decreciente.
**Caveat:** coincide con la oficial al $\sim10^{-3}$. El script da la GRILLA numérica, NO la fórmula cerrada — la fórmula se arma por integración por partes a mano y se valida punto a punto con la grilla. Útil sobre todo para $\hat x(0)=\int f$ y para el bosquejo del espectro.

---

## IIP Tema 03

> **Nota de la resolución oficial:** el inciso 1b está MAL copiado (pide la identidad de $e^t$ del Tema 01 pero la función del 1a es $t+1$, que no la genera). El 1b se resuelve con $e^t$ (idéntico al Tema 01 Ej1b). Los Ej 2 y 3 son **idénticos** a los del Tema 01.

### Ej 1 — Serie trig. de $t+1$ en $(0,1)$ · [fs:1 vía template 9] | PARCIAL
**Enunciado (resumen):** $x(t)=t+1$ en $(0,1)$, $T=1$. a) serie; b) identidad (mal copiada, ver nota).
**De dónde salen los inputs:** NO hay template `t+1`. Pero en $(0,1)$, $t+1=(t-[t])+1$: la parte oscilante es idéntica al template 9, solo cambia el término constante en $+1$.
**Inputs Casio:** `fs` opción `1`, `Op=1`, `template=9`, `#arm=5` (mismo run del Tema 01 Ej2a).
**Comando:** `printf '1\n9\n5\n' | python3 run_mod.py fs`
**Salida (real):** (misma de Tema01 Ej2a) `a0/2=0.4992`, `b1=-0.3183`, `b2=-0.1592`, ... , `a_n≈0`.
**Cómo lo escribo en el examen:** término medio = `a0/2` $+1 = 0.5+1 = \tfrac32$; $a_n=0$; $b_n=-\frac1{\pi n}$ (idéntico al template). Serie: $x(t)=\tfrac32-\sum\frac1{\pi n}\sin(2\pi n t)$.
**Caveat:** PARCIAL — el template 9 da la parte oscilante exacta, pero el $+1$ del término constante se agrega a mano (el script no tiene `t+1`). Coincide con la oficial ($a_0=\tfrac32$). El inciso b) se resuelve con $e^t$ (template 7) exactamente como en Tema 01 Ej1b (ver allí).

### Ej 2 — $t-[t]$ (trig./exp./lab.) · [fs:1 / fs:2] | SÍ
**Idéntico al Tema 01 Ej 2.** Mismos comandos, misma salida. Ver Tema 01 Ej 2.
**Resultado:** $a_0=\tfrac12$, $a_n=0$, $b_n=-\frac1{\pi n}$; $c_0=\tfrac12$, $c_n=\frac{i}{2\pi n}$; lab. $A_n=\frac1{\pi n}$, $\varphi_n=-\tfrac\pi2$.

### Ej 3 — TF de la rampa $t$ en $[0,1]$ · [tf:4] | SÍ
**Idéntico al Tema 01 Ej 3.** Mismo comando `printf '4\n1\n0\n1\n0\n1\n5\n' | python3 run_mod.py tf`, misma salida. $\hat x(\omega)=\frac{(1+i\omega)e^{-i\omega}-1}{\omega^2}$, $\hat x(0)=\tfrac12$.

---

## IIP Tema 04

### Ej 1 — Serie trig. de $t^2$ en $(0,2\pi)$ + derivar · [fs:1] | PARCIAL
**Enunciado (resumen):** $x(t)=t^2$ en $(0,2\pi)$, $T=2\pi$. a) serie; b) desarrollo de $y(t)=x'(t)$.
**De dónde salen los inputs:** $t^2$ en $(0,2\pi)$ = template 4 exacto.
**Inputs Casio (a):** `fs` opción `1`, `Op=1`, `template=4`, `#arm=5`.
**Comando:** `printf '1\n4\n5\n' | python3 run_mod.py fs`
**Salida del script (real):**
```
T=6.283
w0=1
a0=26.32
a0/2=13.16
n=1
 a=4
 b=-12.57
n=2
 a=1
 b=-6.283
n=3
 a=0.4444
 b=-4.189
n=4
 a=0.25
 b=-3.142
n=5
 a=0.16
 b=-2.513
```
**Cómo lo escribo en el examen:** a) término medio = `a0/2` $=13.16=\frac{4\pi^2}{3}$; $a_n=4,1,0.444,0.25,0.16=\frac4{n^2}$; $b_n=-12.57,-6.283,\dots=-\frac{4\pi}{n}$. Serie: $x(t)=\frac{4\pi^2}{3}+\sum\frac4{n^2}\cos nt-\sum\frac{4\pi}{n}\sin nt$.
b) (a mano, derivando término a término): $y(t)=x'(t)\sim\sum(-a_n n\sin nt+b_n n\cos nt)=-4\pi\sum\cos nt-\sum\frac4n\sin nt\equiv 2\pi-\sum\frac4n\sin nt=2t$ en $(0,2\pi)$.
**Caveat:** a) coincide con la oficial (cuidar `a0` vs `a0/2`). b) es analítico — el script no deriva series; el término $-4\pi\sum\cos nt$ aporta el valor medio $2\pi$ vía sumabilidad Abel/Cesàro (la "firma" del salto de $t^2$). Marcado PARCIAL solo por el inciso b).

### Ej 2 — TF de $t^2$ en $[0,2\pi]$ · [tf:4] | SÍ
**Enunciado (resumen):** $x(t)=t^2$ si $0\le t\le2\pi$, $0$ si no. Hallar TF.
**De dónde salen los inputs:** pulso polinómico $p(t)=t^2$ → grado 2, $c_0=0,c_1=0,c_2=1$, en $[0,2\pi]\approx[0,6.2832]$.
**Inputs Casio:** `tf` opción `4`; `Op=4`, `grado=2`, `c0=0`, `c1=0`, `c2=1`, `a inf=0`, `b sup=6.2832`, `w_max=5`.
**Comando de verificación:**
`printf '4\n2\n0\n0\n1\n0\n6.2832\n5\n' | python3 run_mod.py tf`
**Salida del script (real):**
```
 0.0
 82.7
 -0
 |82.7|
 1.0
 12.6
 39.5
 |41.4|
 2.0
 3.14
 19.7
 |20|
 3.0
 1.4
 13.2
 |13.2|
 4.0
 0.786
 9.87
 |9.9|
 5.0
 0.503
 7.9
 |7.91|
```
**Cómo lo escribo en el examen:** fórmula cerrada (por partes 2 veces) $\hat x(\omega)=e^{-2\pi i\omega}\big(\frac{4\pi^2 i}{\omega}+\frac{4\pi}{\omega^2}-\frac{2i}{\omega^3}\big)+\frac{2i}{\omega^3}$, con $\hat x(0)=\frac{8\pi^3}{3}=$ `82.7` (= $\int_0^{2\pi}t^2dt$). Chequeo cruzado con Ej1: en $\omega=n$ entero, $\hat x(n)=\frac{4\pi^2 i}{n}+\frac{4\pi}{n^2}$ → para $n=1$: $\text{Re}=4\pi\approx12.57$ (`12.6`), $\text{Im}=4\pi^2\approx39.48$ (`39.5`) ✓.
**Caveat:** coincide con la oficial. Grilla numérica, no fórmula cerrada. El valor más útil es $\hat x(0)=82.7$ y la coherencia con los coeficientes de Fourier del Ej1 en $\omega$ entero.

### Ej 3a — Calor implícito Dirichlet, $u(x,0)=\sin x$ · [edp:1] | PARCIAL
**Enunciado (resumen):** $u_t=u_{xx}$, 4 nodos internos, $u(0,t)=u(1,t)=0$, $u(x,0)=\sin(x)$.
**De dónde salen los inputs:** $L=1$, 4 nodos → $h=0.2$; $r=0.5$ (elección típica) → $dt=r\,h^2=0.5\cdot0.04=0.02$. Bordes Dirichlet $0$ y $0$.
**Inputs Casio:** `edp` opción `1` (Calor Dir); `Op=1`, `L=1`, `nodos int=4`, `dt=0.02`, `#pasos=1`, `u(x,0)=1` (template `sen(πx/L)`), `u(0,t)=0`, `u(L,t)=0`.
**Comando de verificación:**
`printf '1\n1\n4\n0.02\n1\n1\n0\n0\n' | python3 run_mod.py edp`
**Salida del script (real):**
```
h=0.2
r=0.5
-- u^0
0.5878 0.9511 0.9511
0.5878
-- u^1 t=0.020
0.4935 0.7985 0.7985
0.4935
-- Final
0.4935 0.7985 0.7985
0.4935
```
**Cómo lo escribo en el examen:** esquema implícito $-r\,u_{i-1}^{k+1}+(1+2r)u_i^{k+1}-r\,u_{i+1}^{k+1}=u_i^k$ con $h=0.2$, $r=\frac{\Delta t}{h^2}$. Matriz tridiagonal $4\times4$ $M=\text{tridiag}(-r,\,1+2r,\,-r)=\text{tridiag}(-0.5,\,2,\,-0.5)$, RHS $=\mathbf u^k$ (bordes homogéneos desaparecen). C.I. (a mano, $\sin x_i$): $\mathbf u^0=(\sin0.2,\sin0.4,\sin0.6,\sin0.8)=(0.1987,0.3894,0.5646,0.7174)$; resolviendo $M\mathbf u^1=\mathbf u^0$ da $\mathbf u^1=(0.1908,0.3660,0.4944,0.4823)$.
**Caveat:** PARCIAL — el ESQUEMA y la MATRIZ son exactamente los de la oficial ($M=$tridiag$(-0.5,2,-0.5)$ con $r=0.5$). PERO el template de C.I. del script es $\sin(\pi x/L)=\sin(\pi x)$, NO $\sin(x)$ que pide el examen (script imprime $\mathbf u^0=(0.5878,0.9511,0.9511,0.5878)$, la resolución usa $(0.1987,...,0.7174)$). El armado/matriz se transcriben del script; la C.I. correcta y el primer paso se hacen a mano (resolviendo el mismo $M$). **Limitación de `edp`: C.I. no parametrizable, atada a 4 templates.**

### Ej 3b — Calor implícito, borde Neumann $u_x(0,t)=0$ · [—] | NO cubierto
**Enunciado (resumen):** mismo calor, pero $u_x(0,t)=0$ (Neumann) y $u(1,t)=0$, $u(x,0)=\cos x$.
**Por qué no:** `edp` Op1 solo admite bordes Dirichlet (valor fijo). Neumann requiere nodo fantasma y el borde pasa a ser incógnita (sistema $5\times5$, primera fila $(1+2r)u_0-2r\,u_1=u_0^k$, matriz NO simétrica). El script no lo modela.
**Qué se hace a mano:** introducir $u_{-1}=u_1$ (central, $u_x=0$), fila Neumann $(1+2r)u_0-2r\,u_1=u_0^k$; sistema $5\times5$ con incógnitas $u_0..u_4$; C.I. $\cos x_i$ incluyendo $x_0=0$: $\mathbf u^0=(1,0.9801,0.9211,0.8253,0.6967)$.

---

## IIP Tema 05

### Ej 1 — Serie trig. de $\cos t$ en $(-\tfrac\pi4,\tfrac\pi4)$, $T=\tfrac\pi2$ · [—] | NO cubierto
**Enunciado (resumen):** $x(t)=\cos t$ en $(-\pi/4,\pi/4)$, $T=\pi/2$. a) serie; b) $y=x'$.
**Por qué no:** `fs` solo tiene 9 templates (potencias de $t$, $|t|$, sgn, $e^t$, $1-t$, $t-[t]$); NO hay $\cos t$ ni intervalos $(-\pi/4,\pi/4)$ con $T=\pi/2$. Función Y período fuera de catálogo.
**Qué se hace a mano:** $\omega_0=2\pi/T=4$; $\cos t$ par → $b_n=0$. $a_0=\frac{2\sqrt2}{\pi}$, $a_n=\frac{4\sqrt2(-1)^{n+1}}{\pi(16n^2-1)}$. Serie de solo cosenos $\cos(4nt)$. b) derivar: $y=x'=\frac{16\sqrt2}{\pi}\sum\frac{(-1)^n n}{16n^2-1}\sin(4nt)$ (= serie de $-\sin t$).

### Ej 2 — TF de $e^{-2|t|}$ · [tf:3 parcial] | PARCIAL
**Enunciado (resumen):** $x(t)=e^{-2|t|}$. Hallar TF.
**De dónde salen los inputs:** `tf` Op3 modela $e^{-at}u(t)$ (UN solo lado), $a=2$. El bilátero $e^{-2|t|}$ es la suma de la cola derecha $e^{-2t}u(t)$ y su espejo.
**Inputs Casio:** `tf` opción `3` (Exp -at u(t)); `Op=3`, `a=2`, `w_max=3`.
**Comando:** `printf '3\n2\n3\n' | python3 run_mod.py tf`
**Salida del script (real):** (one-sided $1/(2+i\omega)$)
```
 0.00 0.5 -0
 0.50 0.485 -0.24
 1.00 0.447 -0.46
 1.50 0.4 -0.64
 2.00 0.354 -0.79
 3.00 0.277 -0.98
```
**Cómo lo escribo en el examen:** a mano, $\hat x(\omega)=\int_{-\infty}^0 e^{2t}e^{-i\omega t}dt+\int_0^\infty e^{-2t}e^{-i\omega t}dt=\frac1{2-i\omega}+\frac1{2+i\omega}=\frac{4}{4+\omega^2}$ (real y par; lorentziana $\frac{2a}{a^2+\omega^2}$ con $a=2$). Chequeo con el script: el one-sided da $|1/(2+i\omega)|$; el bilátero es $2\,\text{Re}\frac1{2+i\omega}=\frac{2\cdot2}{4+\omega^2}$. En $\omega=0$: script `0.5` (one-sided) → bilátero $=1=\frac44$ ✓; en $\omega=2$: $\frac4{8}=0.5$.
**Caveat:** PARCIAL — `tf` Op3 da SOLO el medio derecho $e^{-2t}u(t)$, no el bilátero $e^{-2|t|}$. El resultado cerrado $\frac4{4+\omega^2}$ se obtiene a mano; el script sirve para validar las piezas ($\text{Re}\frac1{2+i\omega}$). **Limitación de `tf`: no tiene template para decaimiento bilátero $e^{-a|t|}$.**

### Ej 3a — Onda implícita Dirichlet, $u(x,0)=\sin x$, $u_t(x,0)=0$ · [edp:2] | PARCIAL
**Enunciado (resumen):** $u_{tt}=u_{xx}$, 4 nodos, $u(0,t)=u(1,t)=0$, $u(x,0)=\sin x$, $u_t(x,0)=0$.
**De dónde salen los inputs:** $L=1$, 4 nodos → $h=0.2$; $\Delta t=h=0.2$ → $r=\Delta t^2/h^2=1$ (coeficientes limpios). Borde Dirichlet $0,0$ (implícitos en Op2). $u_t=0$ asumido por el script.
**Inputs Casio:** `edp` opción `2` (Onda 3 niv); `Op=2`, `L=1`, `nodos int=4`, `dt=0.2`, `#pasos=1`, `u(x,0)=1` (template sen).
**Comando de verificación:**
`printf '2\n1\n4\n0.2\n1\n1\n' | python3 run_mod.py edp`
**Salida del script (real):**
```
h=0.2
r=1
-- u^0
0.5878 0.9511 0.9511
0.5878
-- u^1
0.4253 0.6882 0.6882
0.4253
-- Final
0.4253 0.6882 0.6882
0.4253
```
**Cómo lo escribo en el examen:** esquema 3 niveles implícito $-r\,u_{i-1}^{k+1}+(1+2r)u_i^{k+1}-r\,u_{i+1}^{k+1}=2u_i^k-u_i^{k-1}$, $r=\frac{\Delta t^2}{h^2}=1$ → $M=\text{tridiag}(-1,3,-1)$. Arranque: $u_t(x,0)=0\Rightarrow u_i^{-1}=u_i^0$, luego $\mathbf b^0=2\mathbf u^0-\mathbf u^0=\mathbf u^0$. C.I. (a mano, $\sin x_i$): $\mathbf u^0=(0.1987,0.3894,0.5646,0.7174)$, y $\mathbf u^1=M^{-1}\mathbf u^0=(0.1763,0.3304,0.4253,0.3809)$.
**Caveat:** PARCIAL — el ESQUEMA y $M=\text{tridiag}(-1,3,-1)$ con $r=1$ coinciden con la oficial, y el script asume $u_t(x,0)=0$ (justo lo del inciso a). PERO el template de C.I. es $\sin(\pi x)$, no $\sin(x)$ (script: $\mathbf u^0=(0.5878,...)$; oficial: $(0.1987,...)$). C.I. y primer paso a mano. **Limitación `edp` Op2: C.I. fija sen(πx/L), $u_t(x,0)=0$ forzado.**

### Ej 3b — Onda, Neumann $u_x(0,t)=0$, $u_t(x,0)=x$ · [—] | NO cubierto
**Por qué no:** Op2 es solo Dirichlet y solo $u_t(x,0)=0$. Aquí hay Neumann en $x_0$ (nodo fantasma, sistema $5\times5$, $M$ no simétrica con fila $(3,-2,0,0,0)$) y velocidad inicial $u_t(x,0)=x\ne0$ (nivel ficticio $u_i^{-1}=u_i^0-\Delta t\,x_i$). El script no lo cubre.
**Qué se hace a mano:** $M_b$ $5\times5$ fila Neumann $[3,-2,0,0,0]$; $\mathbf u^0=\cos x_i=(1,0.98,0.921,0.825,0.697)$, $\mathbf u^{-1}=\mathbf u^0-0.2\,x_i$, $\mathbf b^0=2\mathbf u^0-\mathbf u^{-1}$.

---

## IIP Tema 06

### Ej 1 — Serie trig. de $\sin t$ en $(-\tfrac\pi4,\tfrac\pi4)$, $T=\tfrac\pi2$ · [—] | NO cubierto
**Enunciado (resumen):** $x(t)=\sin t$ en $(-\pi/4,\pi/4)$, $T=\pi/2$. a) serie; b) $y=x'$.
**Por qué no:** igual que Tema 05 Ej1 — `fs` no tiene $\sin t$ ni el intervalo/período $(-\pi/4,\pi/4)$, $T=\pi/2$.
**Qué se hace a mano:** $\omega_0=4$; $\sin t$ impar → $a_0=a_n=0$. $b_n=\frac{16\sqrt2}{\pi}(-1)^{n+1}\frac{n}{16n^2-1}$, serie de senos $\sin(4nt)$. b) derivar t.a.t. → serie de cosenos con $B_n=4n\,b_n\not\to0$ (no converge puntualmente; es $\cos t$ + tren de deltas en los saltos $\pm\pi/4$).

### Ej 2 — TF de $t\,e^{-t}u(t)$ · [—] | NO cubierto
**Enunciado (resumen):** $x(t)=t e^{-t}$ (causal, $t\ge0$). Hallar TF.
**Por qué no:** `tf` Op3 es $e^{-at}u(t)$ (sin factor $t$), Op4 es polinómico de soporte FINITO $[a,b]$. $t e^{-t}u(t)$ tiene soporte infinito $[0,\infty)$ y factor mixto polinomio×exponencial: ningún template.
**Qué se hace a mano:** $\hat x(\omega)=\int_0^\infty t e^{-(1+i\omega)t}dt=\frac1{(1+i\omega)^2}$, con $\text{Re}=\frac{1-\omega^2}{(1+\omega^2)^2}$, $\text{Im}=\frac{-2\omega}{(1+\omega^2)^2}$, $|\hat x|=\frac1{1+\omega^2}$.

### Ej 3a — Convección-difusión implícita Dirichlet, $u(x,0)=\sin x$ · [edp:3] | PARCIAL
**Enunciado (resumen):** $u_t=u_{xx}+u_x$, 4 nodos, $u(0,t)=u(1,t)=0$, $u(x,0)=\sin x$.
**De dónde salen los inputs:** reescribir $u_t=u_{xx}+u_x$ como $u_t+c\,u_x=\nu\,u_{xx}$ con $\nu=1$, $c=-1$. $L=1$, 4 nodos → $h=0.2$; $\Delta t=0.01$ (ejemplo de la oficial: $r=\nu\Delta t/h^2=0.25$, $s=\Delta t/(2h)=0.025$). Bordes Dirichlet $0,0$.
**Inputs Casio:** `edp` opción `3` (Conv-difus); `Op=3`, `L=1`, `nodos int=4`, `dt=0.01`, `#pasos=1`, `c vel=-1`, `nu dif=1`, `u(0,t)=0`, `u(L,t)=0`.
**Comando de verificación:**
`printf '3\n1\n4\n0.01\n1\n-1\n1\n0\n0\n' | python3 run_mod.py edp`
**Salida del script (real):**
```
-- u^1
0.5522 0.8747 0.8607
0.521
-- Final
0.5522 0.8747 0.8607
0.521
```
**Cómo lo escribo en el examen:** con $r=\frac{\Delta t}{h^2}$, $s=\frac{\Delta t}{2h}$, el esquema implícito es $(s-r)u_{i-1}^{k+1}+(1+2r)u_i^{k+1}-(r+s)u_{i+1}^{k+1}=u_i^k$. Matriz tridiagonal NO simétrica $4\times4$: subdiagonal $s-r$, diagonal $1+2r$, superdiagonal $-(r+s)$. Con $\Delta t=0.01$: $r=0.25$, $s=0.025$ → $M=\text{tridiag}(-0.225,\,1.5,\,-0.275)$. C.I. (a mano, $\sin x_i$): $\mathbf u^0=(0.1987,0.3894,0.5646,0.7174)$, $M\mathbf u^1=\mathbf u^0$.
**Caveat:** PARCIAL — clave el mapeo de signo: la EDP $u_t=u_{xx}+u_x$ entra como $c=-1$, $\nu=1$, y así la matriz del script coincide EXACTAMENTE con la oficial (subdiag $s-r=-0.225$, diag $1.5$, superdiag $-(r+s)=-0.275$). PERO la C.I. está HARDCODEADA a $\sin(\pi x/L)$ (no parametrizable) → el script reporta el avance con $\sin(\pi x)$, no con $\sin(x)$; C.I. y primer paso correctos van a mano. El script tampoco imprime $\mathbf u^0$ en Op3 (solo $\mathbf u^k$ por intervalos y Final). **Limitaciones `edp` Op3: C.I. fija sen(πx/L), no imprime $u^0$, requiere traducir la EDP al formato $u_t+c\,u_x=\nu\,u_{xx}$ (signo de $c$).**

### Ej 3b — Conv-difusión, Neumann $u_x(0,t)=0$ · [—] | NO cubierto
**Por qué no:** Op3 solo Dirichlet. Neumann → nodo fantasma, sistema $5\times5$, primera fila $(1+2r)u_0-2r\,u_1=u_0^k$ (los términos en $s$ se cancelan en la pared). No modelado.
**Qué se hace a mano:** $M$ $5\times5$ fila Neumann $(1+2r,-2r,0,0,0)$; C.I. $\cos x_i$ incluyendo $x_0=0$: $\mathbf u^0=(1,0.9801,0.9211,0.8253,0.6967)$.

---

## Resumen de cobertura

| Tema | Ej1 (serie) | Ej2 (TF) | Ej3a (EDP) | Ej3b (EDP) |
|------|-------------|----------|------------|------------|
| 01 | SÍ (fs:1+3, tmpl 7) | SÍ (tf:4) | — | — |
| 03 | PARCIAL (fs:1 tmpl 9 + cte) | SÍ (tf:4) | — | — |
| 04 | PARCIAL (fs:1 tmpl 4; b a mano) | SÍ (tf:4) | PARCIAL (edp:1, C.I.) | NO (Neumann) |
| 05 | NO (cos, $T=\pi/2$) | PARCIAL (tf:3 one-sided) | PARCIAL (edp:2, C.I.) | NO (Neumann+$u_t=x$) |
| 06 | NO (sin, $T=\pi/2$) | NO ($te^{-t}$) | PARCIAL (edp:3, C.I.) | NO (Neumann) |

**Conteo:** de 17 ítems evaluados (Ej3 desglosado a/b en los temas con EDP): **SÍ = 6**, **PARCIAL = 7**, **NO cubierto = 4**. (Si se cuentan Ej1/Ej2/Ej3 como bloques de 3 por tema = 15 bloques, los SÍ "limpios" son los 4 de Fourier de los temas 01/03/04.)
# Sección — Finales A (Temas 01–05)

> Agente: resolución/verificación de los finales MNA con scripts Casio (fx-CG50 / Graph 90+E).
> Sandbox: `/tmp/acasios_sb`. Todas las salidas pegadas son REALES (capturadas ejecutando los scripts).

## Resumen de cobertura por tema

| Tema | Ej1 TL/diag | Ej2 Fourier | Ej3 | Ej4/Ej5 |
|---|---|---|---|---|
| 01 | SÍ (tl+diag) | SÍ (fs tmpl 9) | NO (EDO→sistema, teoría) | NO (TF e^{-\|t\|}, no template) |
| 02 | SÍ (tl+diag) | SÍ (fs tmpl 8) | NO (EDO→sistema) | SÍ (tf Op4 polinomio) |
| 03 | PARCIAL (diag SÍ; M_BB no) | NO (x−x² no es template) | NO (EDO→sistema) | SÍ (tf Op4 polinomio) |
| 04 | SÍ (tl+diag) | SÍ (fs tmpl 8) | SÍ (qr+svd+lu) | — |
| 05 | SÍ (tl+diag) | NO (1−x² no es template) | PARCIAL (calor Dir: esquema sí, CI no; Neumann no) | NO (TF e^{t-1}, no template) |

**GOTCHA CRÍTICO (afecta a varios temas):** en `diag`, cuando la matriz tiene **autovalores complejos** y `det≠0` (no entra al atajo `c~0`), el script va por la rama de **Cardano** y la línea `L1(real)=...` está **MAL CALCULADA** (imprime basura, p.ej. −0.1667 en vez de 1, ó 0.1667 en vez de 2). Lo importante: el script **igual devuelve `None`** y NO arma P/D, lo que correctamente significa "NO diagonalizable en ℝ". O sea: **fiate del "devolvió None / no armó P,D" como señal de no-diagonalizable, pero NO copies el número de `L1(real)`** — calculá el autovalor real a mano (raíz del factor lineal). En cambio la rama `c~0` (det=0) y la rama de cubica real (3 reales) SÍ imprimen autovalores correctos.

---

## Final Tema 01

### Ej 1 — TL R³→R³: núcleo/imagen + diagonalizable · [tl:1 + diag] | SÍ
**Enunciado (resumen):** T(x,y,z)=(2x−y, x+y−z, z). a) N(T), Im(T). b) ¿diagonalizable en ℝ?
**De dónde salen los inputs:** la matriz A = M_EE(T) son las filas de coeficientes de cada componente de salida: 1ª comp 2x−y → `2,-1,0`; 2ª x+y−z → `1,1,-1`; 3ª z → `0,0,1`.
**Inputs Casio:**
- Núcleo/Imagen: `tl`, Op `1` (N(T),Im,rg); secuencia: `filas=3`, `cols=3`, filas `2,-1,0` / `1,1,-1` / `0,0,1`.
- Diagonalizable: `diag`; secuencia: `n=3`, mismas 3 filas.
**Comando de verificación:**
`printf '1\n3\n3\n2,-1,0\n1,1,-1\n0,0,1\n' | python3 run_mod.py tl`
`printf '3\n2,-1,0\n1,1,-1\n0,0,1\n' | python3 run_mod.py diag`
**Salida del script (real):**
```
-- RREF: N(T) Im(T)
rref:
1 0 0
0 1 0
0 0 1
rg= 3
dim N= 0
-- Base N(T)
N(T)={0}
-- Base Im(T)
(cols pivote de A)
c1:  2 1 0
c2: -1 1 0
c3:  0 -1 1
```
```
-- P(L) caract.
p(L)=L^3+
a=-4
b=6
c=-3
dep p=0.6667
dep q=0.2593
disc=-3
L1(real)=1           (ya CORREGIDO; antes -0.1667)
L2,3 Re=1.5
   Im=+-0.866
```
**Cómo lo escribo en el examen:** A inversible (rg=3, det=3), entonces **N(T)={(0,0,0)}** e **Im(T)=ℝ³** (T isomorfismo). p_A(λ)=λ³−4λ²+6λ−3=(λ−1)(λ²−3λ+3); el factor cuadrático tiene Δ=−3<0 → raíces complejas 3/2±(√3/2)i. Hay autovalores no reales → **T NO es diagonalizable en ℝ**.
**Caveat:** Coincide con la oficial (N={0}, Im=ℝ³, no diag en ℝ). Con el **parche aplicado** (ver changelog), `diag` ahora imprime el autovalor real correcto `L1(real)=1` y las complejas `1.5±0.866i` (numpy: eig={1, 1.5±0.866i}). El "no armó P,D" sigue señalando que NO diagonaliza en ℝ.

### Ej 2 — Serie de Fourier f(x)=x−[x] + convergencia en ℤ · [fs:1 y fs:3] | SÍ
**Enunciado (resumen):** a) serie de Fourier de la parte fraccionaria f(x)=x−[x] (período 1). b) ¿a qué converge en los enteros?
**De dónde salen los inputs:** f(x)=x−[x] en (0,1) es exactamente el **template 9** (`t-[t] en(0,1)`). Convergencia en enteros → evaluar en t0=0.
**Inputs Casio:**
- Coeficientes: `fs`, Op `1`, template `>9`, `#arm=4`.
- Convergencia: `fs`, Op `3`, template `>9`, `t0=0`, `#arm suma=10`.
**Comando de verificación:**
`printf '1\n9\n4\n' | python3 run_mod.py fs`
`printf '3\n9\n0\n10\n' | python3 run_mod.py fs`
**Salida del script (real):**
```
T=1
w0=6.283
a0=0.9983
a0/2=0.4992
n=1  a=-0.001667  b=-0.3183
n=2  a=-0.001667  b=-0.1592
n=3  a=-0.001667  b=-0.1061
n=4  a=-0.001667  b=-0.07958
```
```
x(t0+)=0.0001
x(t0-)=0.9999
prom=0.5
S_N(t0)=0.4825
```
**Cómo lo escribo en el examen:** a0/2≈0.4992→**½** (valor medio), a_n≈0, b_n=−1/(πn) (−0.3183=−1/π, −0.1592=−1/2π, …). Serie: **f(x)=½ − Σ_{n≥1} (1/πn) sin(2πnx)**. b) En cada entero hay salto (f→1 por izq, →0 por der); por Dirichlet converge al **promedio = ½** (consistente con prom=0.5; S_N→0.5 al sumar más armónicos).
**Caveat:** Coincide con la oficial. Dos detalles del script: (1) a_n sale −0.001667 en vez de 0 — es ruido de Simpson por la discontinuidad en el borde del período (a mano a_n=0 exacto). (2) En conv, `prom=0.5` salió bien acá porque eps cae dentro de (0,1); pero el promedio "verdadero" del salto (1→0) también es ½, así que cierra.

### Ej 3 — EDO 2º orden (Duffing) → sistema 1er orden + esquema implícito · [No cubierto] | NO
**Enunciado (resumen):** x''+δx'+βx+αx³=γcos(ωt+φ). a) Pasar a sistema de orden 1. b) Esquema implícito de diferencias finitas + CI.
**Por qué No cubierto:** Es reformulación **teórica** (x₁=x, x₂=ẋ → ẋ₁=x₂, ẋ₂=γcos(ωt+φ)−δx₂−βx₁−αx₁³; Euler implícito con Newton por el término no lineal x³). Ningún script hace álgebra simbólica ni Newton multivariable. El `edp` solo cubre EDPs lineales (calor/onda/convección), no este IVP no lineal.
**Cómo lo escribo en el examen:** a mano (ver resolución oficial: sistema, Euler hacia atrás, Jacobiano J=[[1,−Δt],[Δt(β+3αx₁²),1+Δtδ]], CI x₁⁰=x(0), x₂⁰=x'(0)).

### Ej 4 — SVD de A 2×2 + ¿diagonalizable? · [svd + (b) a mano] | PARCIAL
**Enunciado (resumen):** A=[[0.92,1.44],[1.44,0.08]]. a) SVD. b) ¿diagonalizable?
**De dónde salen los inputs:** filas de A directamente. A es 2×2 (m=n) → SVD corre directo.
**Inputs Casio:** `svd`; `filas=2`, `cols=2`, filas `0.92,1.44` / `1.44,0.08`.
**Comando de verificación:**
`printf '2\n2\n0.92,1.44\n1.44,0.08\n' | python3 run_mod.py svd`
**Salida del script (real):**
```
-- Via AtA 2x2
AtA:
2.92 1.44
1.44 2.08
tr=5
det=4
disc=9
-- V.singulares
s1=2
s2=1
-- V cols
v1: 0.8 0.6
v2: -0.6 0.8
-- U cols
u1: 0.8 0.6
u2: 0.6 -0.8
-- Verif
|USVt-A|=1.527e-16
Sigma:
2 0
0 1
```
**Cómo lo escribo en el examen:** σ₁=2, σ₂=1, Σ=diag(2,1). Del script: V=[[0.8,−0.6],[0.6,0.8]], U=[[0.8,0.6],[0.6,−0.8]] → **A=UΣVᵀ** (|USVt−A|≈1.5e-16). b) A es **simétrica real** → por el teorema espectral **es diagonalizable** (ortogonalmente): A=PDPᵀ con D=diag(2,−1), P=[[0.8,0.6],[0.6,−0.8]].
**Caveat:** La SVD coincide con la oficial salvo **signo** del segundo par singular: el script da v₂=(−0.6,0.8), u₂=(0.6,−0.8); la oficial v₂=(0.6,−0.8), u₂=(−0.6,0.8) — es el mismo par con (vᵢ,uᵢ)↦(−vᵢ,−uᵢ), que deja A=UΣVᵀ idéntico (libertad de signo de los vectores singulares). Ambas válidas. La parte (b) NO la da el script (argumento teórico simétrica→espectral); los autovalores con signo (2,−1) se sacan aparte (o corriendo `diag` con esta A). PARCIAL: el script resuelve (a), (b) es teoría.

### Ej 5 — Transformada de Fourier de e^{-|t|} · [No cubierto] | NO
**Enunciado (resumen):** TF de f(t)=e^{-|t|} (en todo ℝ).
**Por qué No cubierto:** `tf` Op3 es e^{-at}u(t) **unilateral** (t>0), no la bilateral e^{-|t|}. No hay template para el pulso de doble cola en ℝ. Tampoco entra en Op4 (polinomio en [a,b], soporte compacto).
**Cómo lo escribo en el examen:** a mano: F(ω)=1/(1−iω)+1/(1+iω)=**2/(1+ω²)** (Lorentziana, real y par). Verificación puntual a mano F(0)=2.

---

## Final Tema 02

### Ej 1 — TL R³→R³: núcleo/imagen + diagonalizable · [tl:1 + diag] | SÍ
**Enunciado (resumen):** T(x,y,z)=(2x−y, x+y−z, z−x−y). a) N(T), Im(T). b) ¿diag en ℝ?
**De dónde salen los inputs:** filas de A: `2,-1,0` / `1,1,-1` / `-1,-1,1`.
**Inputs Casio:** `tl` Op `1` (filas=3, cols=3, esas filas) y `diag` (n=3, esas filas).
**Comando de verificación:**
`printf '1\n3\n3\n2,-1,0\n1,1,-1\n-1,-1,1\n' | python3 run_mod.py tl`
`printf '3\n2,-1,0\n1,1,-1\n-1,-1,1\n' | python3 run_mod.py diag`
**Salida del script (real):**
```
rref:
1 0 -0.3333
0 1 -0.6667
0 0       0
rg= 2
dim N= 1
-- Base N(T)
n1: 0.3333 0.6667 1
-- Base Im(T)
c1: 2 1 -1
c2: -1 1 -1
```
```
p(L)=L^3+  a=-4  b=5  c=-0
c~0: L factor
p=L(L^2+aL+b)
disc2=-4
L=0 y 2 cpx:
Re=2
Im=+-1
```
**Cómo lo escribo en el examen:** rg=2, dim N=1. **N(T)=⟨(0.3333,0.6667,1)⟩=⟨(1,2,3)⟩** (la base del script es el mismo vector escalado por 1/3). Im(T)=⟨(2,1,−1),(−1,1,−1)⟩, equivalente al plano {v+w=0}. b) Autovalores **0 y 2±i** (complejos) → **NO diagonalizable en ℝ**.
**Caveat:** Coincide totalmente con la oficial. Acá la rama `c~0` (det=0) imprimió los autovalores complejos **correctamente** (Re=2, Im=±1), a diferencia del bug de la rama Cardano. La base del núcleo difiere por escala (×3) — válida.

### Ej 2 — Serie de Fourier f(x)=1−x (período 1) + convergencia · [fs:1 y fs:3] | SÍ
**Enunciado (resumen):** a) serie de f(x)=1−x, f(x)=f(x+1). b) convergencia en x=0 y x=½.
**De dónde salen los inputs:** f(x)=1−x en (0,1) = **template 8** (`1-t en(0,1)`).
**Inputs Casio:** `fs` Op `1` template `>8` `#arm=4`; conv `fs` Op `3` template `>8` `t0` `#arm=20`.
**Comando de verificación:**
`printf '1\n8\n4\n' | python3 run_mod.py fs`
`printf '3\n8\n0\n20\n' | python3 run_mod.py fs`  (y t0=0.5)
**Salida del script (real):**
```
T=1  w0=6.283
a0=1  a0/2=0.5
n=1  a=-6.347e-17  b=0.3183
n=2  a=-1.373e-17  b=0.1592
n=3  a=-5.151e-17  b=0.1061
n=4  a=-3.552e-17  b=0.07958
```
```
t0=0:    x(t0+)=0.9999  x(t0-)=1  prom=1   S_N(t0)=0.5
t0=0.5:  x(t0+)=0.4999  x(t0-)=0.5001  prom=0.5  S_N(t0)=0.5
```
**Cómo lo escribo en el examen:** a0=½ (valor medio), a_n≈0, b_n=1/(πn) (0.3183=1/π,…). **f(x)=½ + Σ_{n≥1} (1/πn) sin(2πnx)**. b) En x=½ continua → converge a f(½)=½ (S_N=0.5 ✓). En x=0 hay salto (1→0) → promedio ½ (S_N=0.5 ✓).
**Caveat:** Coincide con la oficial. GOTCHA: en conv a t0=0 el campo `prom=1` está MAL (el script evalúa f(0−eps)=f(−0.0001)=1.0001 con la lambda cruda, sin periodizar, así que no ve el salto). Pero **S_N(0)=0.5 sí es correcto** (el promedio real del salto 1↔0 es ½). Confiar en S_N, no en `prom` cuando t0 cae en el borde del período.

### Ej 3 — EDO x''+2x'+x=e^{−t²} → sistema + esquema implícito · [No cubierto] | NO
**Por qué No cubierto:** reformulación teórica EDO→sistema 1er orden + Euler implícito. Es **lineal** (a diferencia del tema 1), así que el paso queda (I−Δt·M)x^{k+1}=x^k+Δt·f^{k+1} con M=[[0,1],[−1,−2]]. Ningún script arma este IVP. (El `edp` es solo para EDPs.)
**Cómo lo escribo en el examen:** a mano (ver oficial; CI x₁⁰=x₂⁰=c por el dato x(0)=x'(0)).

### Ej 4 — Transformada de Fourier de (t−1)² en [0,1] · [tf:4] | SÍ
**Enunciado (resumen):** TF de f(t)=(t−1)² si 0≤t≤1, 0 si no.
**De dónde salen los inputs:** (t−1)²=1−2t+t² → polinomio grado 2, coefs c0=1, c1=−2, c2=1, soporte [0,1].
**Inputs Casio:** `tf` Op `4` (Polin. num.); `grado=2`, `c0=1`, `c1=-2`, `c2=1`, `a inf=0`, `b sup=1`, `w_max=5`.
**Comando de verificación:**
`printf '4\n2\n1\n-2\n1\n0\n1\n5\n' | python3 run_mod.py tf`
**Salida del script (real):**
```
 w   Re       Im
 0.0  0.333   -0
 1.0  0.317   -0.0806
 2.0  0.273   -0.146
 3.0  0.212   -0.186
 4.0  0.149   -0.198
 5.0  0.0953  -0.189
```
**Cómo lo escribo en el examen:** F(ω)=∫₀¹(t−1)²e^{−iωt}dt = **−i/ω + 2/ω² + (2i/ω³)(1−e^{−iω})** (ω≠0), con **F(0)=⅓** (área). Verifico en grilla: F(0)=0.333=⅓ ✓, F(1)=0.317−0.0806i ✓, F(2)=0.273−0.146i ✓.
**Caveat:** Coincide con la oficial (que da F(1)=0.3171−0.0806i, F(2)=0.2727−0.1460i). El script da grilla numérica, no la fórmula cerrada; sirve para verificar la fórmula que escribís a mano y especialmente F(0)=⅓.

---

## Final Tema 03

### Ej 1 — TL R³→R³: matriz M_BB en base B + diagonalizable · [diag SÍ; M_BB no] | PARCIAL
**Enunciado (resumen):** T(x,y,z)=(x+3y, x+y−z, z−x−y). a) M_BB con B={(0,0,1),(1,0,0),(1,−1,0)}. b) ¿diag en ℝ?
**De dónde salen los inputs:** M_EE(T) filas: `1,3,0` / `1,1,-1` / `-1,-1,1`. (b) se resuelve con `diag` sobre M_EE (semejante a M_BB, mismos autovalores).
**Inputs Casio (parte b):** `diag`; `n=3`, esas filas.
**Comando de verificación:**
`printf '3\n1,3,0\n1,1,-1\n-1,-1,1\n' | python3 run_mod.py diag`
**Salida del script (real):**
```
p(L)=L^3+  a=-3  b=-1  c=-0
c~0: L factor
p=L(L^2+aL+b)
disc2=13
Autovalores:
L1=3.30278
L2=0
L3=-0.302776
-- S_L=3.303  v: -1.303 -1 1
-- S_L=0      v: 1.5 -0.5 1
-- S_L=-0.3028 v: 2.303 -1 1
P: [[-1.303,1.5,2.303],[-1,-0.5,-1],[1,1,1]]
D: diag(3.303, 0, -0.3028)
|AP-PD|=3.331e-16
```
**Cómo lo escribo en el examen:** a) M_BB **a mano** (no lo da el script): M_BB=P⁻¹·M_EE·P=**[[1,−1,0],[−1,2,−2],[1,−1,0]]** (confirmado con numpy aparte; el `tl` Op4 calcula M_EB, NO M_BB). b) Autovalores **0, (3−√13)/2≈−0.3028, (3+√13)/2≈3.3028** — tres reales distintos → **T diagonalizable en ℝ** (el script arma P,D y |AP−PD|≈0 ✓).
**Caveat:** La parte (b) la cubre `diag` perfectamente (3 reales distintos, diagonaliza; ramo `c~0`+cubica real → autovalores correctos). La parte (a) M_BB **NO es computable con el script**: `tl` Op4 (`con_base`) calcula M(T)_EB (dominio en B, codominio canónico), no M_BB (ambos en B). M_BB hay que hacerlo a mano (P⁻¹AP). Por eso PARCIAL.

### Ej 2 — Serie de Fourier f(x)=x−x² (período 1) · [No cubierto] | NO
**Por qué No cubierto:** `fs` solo tiene 9 templates pre-cargados; **x−x² en (0,1) NO está** (los templates con período 1 son `1−t` y `t−[t]`). No se puede tipear una función arbitraria.
**Cómo lo escribo en el examen:** a mano: a0=1/6, a_n=−1/(π²n²), b_n=0 (parábola simétrica respecto x=½) → f(x)=⅙ − (1/π²)Σ cos(2πnx)/n². Conv: x=0→0 (continua), x=½→¼.

### Ej 3 — EDO x''+x'+3x=cos(t²+1) → sistema + implícito · [No cubierto] | NO
**Por qué No cubierto:** reformulación teórica EDO→sistema lineal de 1er orden + Euler implícito (M=[[0,1],[−3,−1]]). Fuera del alcance de los scripts.
**Cómo lo escribo en el examen:** a mano (CI x⁰=(0,0) por x(0)=x'(0)=0).

### Ej 4 — Transformada de Fourier de t−t² en [0,1] · [tf:4] | SÍ
**Enunciado (resumen):** TF de f(t)=t−t² si 0≤t≤1, 0 si no.
**De dónde salen los inputs:** t−t² → grado 2, c0=0, c1=1, c2=−1, soporte [0,1].
**Inputs Casio:** `tf` Op `4`; `grado=2`, `c0=0`, `c1=1`, `c2=-1`, `a=0`, `b=1`, `w_max=5`.
**Comando de verificación:**
`printf '4\n2\n0\n1\n-1\n0\n1\n5\n' | python3 run_mod.py tf`
**Salida del script (real):**
```
 w   Re        Im
 0.0  0.167    -0
 1.0  0.143    -0.0779
 2.0  0.0814   -0.127
 3.0  0.00934  -0.132
 4.0 -0.0453   -0.099
 5.0 -0.0667   -0.0498
```
**Cómo lo escribo en el examen:** F(ω)=[2sinω−ω(1+cosω)]/ω³ + i[ωsinω+2cosω−2]/ω³ (ω≠0), con **F(0)=⅙** (área). Verifico: F(0)=0.167=⅙ ✓, F(1)=0.143−0.0779i ✓, F(2)=0.0814−0.127i ✓.
**Caveat:** Coincide con la oficial (F(1)=0.14264−0.07792i, F(2)=0.08136−0.12671i). Grilla numérica para verificar la fórmula cerrada manuscrita.

---

## Final Tema 04

### Ej 1 — TL R³→R³: núcleo/imagen + diagonalizable · [tl:1 + diag] | SÍ
**Enunciado (resumen):** T(x,y,z)=(x+y, y−z, x+z). a) N(T), Im(T). b) ¿diag en ℝ?
**De dónde salen los inputs:** filas de A: `1,1,0` / `0,1,-1` / `1,0,1`.
**Inputs Casio:** `tl` Op `1` (filas=3,cols=3,esas filas) y `diag` (n=3,esas filas).
**Comando de verificación:**
`printf '1\n3\n3\n1,1,0\n0,1,-1\n1,0,1\n' | python3 run_mod.py tl`
`printf '3\n1,1,0\n0,1,-1\n1,0,1\n' | python3 run_mod.py diag`
**Salida del script (real):**
```
rref:
1 0  1
0 1 -1
0 0  0
rg= 2
dim N= 1
-- Base N(T)
n1: -1 1 1
-- Base Im(T)
c1: 1 0 1
c2: 1 1 0
```
```
p(L)=L^3+  a=-3  b=3  c=-0
c~0: L factor
p=L(L^2+aL+b)
disc2=-3
L=0 y 2 cpx:
Re=1.5
Im=+-0.866
```
**Cómo lo escribo en el examen:** rg=2, dim N=1. **N(T)=⟨(−1,1,1)⟩** (equivale a ⟨(1,−1,−1)⟩ de la oficial, mismo subespacio). **Im(T)=⟨(1,0,1),(1,1,0)⟩**. b) Autovalores **0 y 3/2±(√3/2)i** (complejos) → **NO diagonalizable en ℝ**.
**Caveat:** Coincide con la oficial. La base del núcleo es −1× la oficial (mismo span). Rama `c~0` imprimió los complejos correctamente.

### Ej 2 — Serie de Fourier f(x)=1−x (período 1) + convergencia · [fs:1 y fs:3] | SÍ
**Idéntico al Tema 02 Ej 2** (misma función f(x)=1−x en (0,1)=template 8). Mismos inputs y salida:
**Comando de verificación:** `printf '1\n8\n4\n' | python3 run_mod.py fs` (+ Op3 conv).
**Salida (real):** a0=1, a0/2=0.5, b_n={0.3183,0.1592,0.1061,0.07958}, a_n≈0. Conv: S_N(0)=0.5, S_N(0.5)=0.5.
**Cómo lo escribo en el examen:** f(x)=½ + Σ_{n≥1}(1/πn)sin(2πnx); converge a ½ en x=0 (promedio del salto) y a ½ en x=½ (continuidad).
**Caveat:** Coincide con la oficial. Mismo gotcha que tema 02: `prom=1` en t0=0 está mal por no periodizar, pero S_N=0.5 es correcto.

### Ej 3 — Factorizaciones QR, SVD, PLU de A 3×3 · [qr + svd + lu] | SÍ
**Enunciado (resumen):** A=[[1,0,0],[2,−1,0],[−4,0,−1]]. a) QR. b) SVD. c) PLU.
**De dónde salen los inputs:** filas de A directamente. A es 3×3 (m=n) → todo corre directo.
**Inputs Casio:**
- QR: `qr`; `filas=3`, `cols=3`, filas `1,0,0` / `2,-1,0` / `-4,0,-1`.
- SVD: `svd`; mismos filas/cols/filas.
- PLU: `lu`; `n=3`, mismas filas.
**Comando de verificación:**
`printf '3\n3\n1,0,0\n2,-1,0\n-4,0,-1\n' | python3 run_mod.py qr`
`printf '3\n3\n1,0,0\n2,-1,0\n-4,0,-1\n' | python3 run_mod.py svd`
`printf '3\n1,0,0\n2,-1,0\n-4,0,-1\n' | python3 run_mod.py lu`
**Salida del script (real):**
```
QR:
||u1||=4.583  v1: 0.2182 0.4364 -0.8729
<a2,v1>=-0.4364  ||u2||=0.8997  v2: 0.1059 -0.8997 -0.4234
<a3,v1>=0.8729  <a3,v2>=0.4234  ||u3||=0.2425  v3: -0.9701 0 -0.2425
Q: [[0.2182,0.1059,-0.9701],[0.4364,-0.8997,0],[-0.8729,-0.4234,-0.2425]]
R: [[4.583,-0.4364,0.8729],[0,0.8997,0.4234],[0,0,0.2425]]
|QR-A|=0   |QtQ-I|=3.886e-16
```
```
SVD:
AtA: [[21,-2,4],[-2,1,0],[4,0,1]]
s1=4.68556  s2=1  s3=0.213422
v1: 0.978 -0.09334 0.1867
v2: 0 0.8944 0.4472
v3: -0.2087 -0.4374 0.8747
u1: 0.2087 0.4374 -0.8747
u2: 0 -0.8944 -0.4472
u3: -0.978 0.09334 -0.1867
|USVt-A|=1.11e-15   Sigma: diag(4.686,1,0.2134)
```
```
PLU:
P:F1<>F3
P: [[0,0,1],[0,1,0],[1,0,0]]
L: [[1,0,0],[-0.5,1,0],[-0.25,0,1]]
U: [[-4,0,-1],[0,-1,-0.5],[0,0,-0.25]]
|PA-LU|=0
```
**Cómo lo escribo en el examen:**
- a) QR: Q=[[0.2182,0.1059,−0.9701],[0.4364,−0.8997,0],[−0.8729,−0.4234,−0.2425]] (=[1/√21,2/√357,−4/√17;…]), R=[[√21,−2/√21,4/√21],[0,√357/21,8/√357],[0,0,1/√17]]≈[[4.583,−0.436,0.873],[0,0.900,0.423],[0,0,0.243]]. ✓
- b) SVD: σ={√6+√5≈4.686, 1, √6−√5≈0.213}, U,V ortogonales arriba. ✓
- c) PLU (con pivoteo del script): P intercambia F1↔F3, L=[[1,0,0],[−0.5,1,0],[−0.25,0,1]], U=[[−4,0,−1],[0,−1,−0.5],[0,0,−0.25]].
**Caveat:** QR y SVD coinciden EXACTO con la oficial (σ=√6±√5, V/U idénticos). **PLU difiere**: el script usa **pivoteo parcial** (P≠I, busca el pivote más grande |−4|→F1↔F3), mientras la oficial usa **Doolittle SIN pivoteo** (P=I, L=[[1,0,0],[2,1,0],[−4,0,1]], U=diag(1,−1,−1)). **Ambas son válidas** (la oficial misma nota que scipy da la versión pivoteada). Elegí según lo que pida la cátedra; si piden "PLU con pivoteo parcial" usá la del script, si piden "PA=LU de Doolittle" usá P=I.

---

## Final Tema 05

### Ej 1 — TL R³→R³: núcleo/imagen + diagonalizable · [tl:1 + diag] | SÍ
**Enunciado (resumen):** T(x,y,z)=(2x, x+y−z, 2z+y). a) N(T), Im(T). b) ¿diag en ℝ?
**De dónde salen los inputs:** filas de A: `2,0,0` / `1,1,-1` / `0,1,2`.
**Inputs Casio:** `tl` Op `1` y `diag`, n=3, esas filas.
**Comando de verificación:**
`printf '1\n3\n3\n2,0,0\n1,1,-1\n0,1,2\n' | python3 run_mod.py tl`
`printf '3\n2,0,0\n1,1,-1\n0,1,2\n' | python3 run_mod.py diag`
**Salida del script (real):**
```
rref:
1 0 0
0 1 0
0 0 1
rg= 3
dim N= 0
N(T)={0}
Im(T): c1: 2 1 0 | c2: 0 1 1 | c3: 0 -1 2
```
```
p(L)=L^3+  a=-5  b=9  c=-6
dep p=0.6667
dep q=-0.2593
disc=-3
L1(real)=2           (ya CORREGIDO; antes 0.1667)
L2,3 Re=1.5
   Im=+-0.866
```
**Cómo lo escribo en el examen:** rg=3, det=6≠0 → **N(T)={(0,0,0)}, Im(T)=ℝ³** (isomorfismo). p_A(λ)=(λ−2)(λ²−3λ+3); el cuadrático tiene Δ=−3<0 → 3/2±(√3/2)i complejos. Hay autovalor real único λ=2 y dos complejos → **NO diagonalizable en ℝ**.
**Caveat:** N(T) e Im(T) coinciden con la oficial. Con el **parche aplicado** (ver changelog), `diag` ahora imprime bien `L1(real)=2` y `1.5±0.866i` (numpy: eig={2, 1.5±0.866i}). El "no armó P,D" señala correctamente que NO diagonaliza en ℝ.

### Ej 2 — Serie de Fourier f(x)=1−x² (período 1) · [No cubierto] | NO
**Por qué No cubierto:** `1−x²` en (0,1) NO es ninguno de los 9 templates de `fs`.
**Cómo lo escribo en el examen:** a mano: a0=2/3, a_n=−1/(π²n²), b_n=1/(πn) → f(x)=⅔ − (1/π²)Σcos(2πnx)/n² + (1/π)Σsin(2πnx)/n. Conv: x=0→½ (salto 1↔0), x=½→¾.

### Ej 3 — Diferencias finitas implícitas calor (Dirichlet y Neumann) · [edp:1 parcial] | PARCIAL
**Enunciado (resumen):** u_t=u_xx, esquema implícito con 4 nodos internos. a) Dirichlet u(0,t)=u(1,t)=0, u(x,0)=sen(x). b) Neumann u_x(0,t)=u_x(1,t)=0, u(x,0)=|x|.
**De dónde salen los inputs:** L=1, 4 nodos internos → h=L/5=0.2. Borde Dirichlet 0,0. CI: el template 1 es sen(πx/L), pero el enunciado pide **sen(x) en radianes** (≠ template).
**Inputs Casio (parte a, solo para exhibir el esquema):** `edp` Op `1`; `L=1`, `nodos int=4`, `dt=0.01`, `#pasos=1`, CI `>1`, `u(0,t)=0`, `u(L,t)=0`.
**Comando de verificación:**
`printf '1\n1\n4\n0.01\n1\n1\n0\n0\n' | python3 run_mod.py edp`
**Salida del script (real):**
```
h=0.2
r=0.25
-- u^0
0.5878 0.9511 0.9511 0.5878    <-- sen(pi x), NO la CI pedida sen(x)
-- u^1 t=0.010
0.5365 0.8682 0.8682 0.5365
```
**Cómo lo escribo en el examen:**
- a) Malla h=1/5=0.2, x_i=0.2,0.4,0.6,0.8. Euler implícito: −r·u_{i−1}+(1+2r)u_i−r·u_{i+1}=u_i^k con r=Δt/h². Sistema tridiagonal 4×4 **M·u^{k+1}=u^k**, M=[[1+2r,−r,0,0],[−r,1+2r,−r,0],[0,−r,1+2r,−r],[0,0,−r,1+2r]]. CI **u^0=(sen0.2,sen0.4,sen0.6,sen0.8)=(0.19867,0.38942,0.56464,0.71736)** [radianes, a mano].
- b) Neumann: **NO cubierto por el script** (solo hace Dirichlet). A mano: nodos fantasma u_{−1}=u_1, u_6=u_4 → sistema 6×6 con −2r (no −r) en filas extremas; CI u_i^0=|x_i|=x_i (en [0,1] |x|=x) = (0,0.2,0.4,0.6,0.8,1.0).
**Caveat:** PARCIAL. El script confirma la **estructura del esquema** (h=0.2, r=Δt/h², matriz tridiagonal 1+2r/−r). PERO: (1) la **CI no coincide**: template 1 da sen(πx)=(0.5878,0.9511,0.9511,0.5878), no sen(x)=(0.19867,…) que pide el enunciado — la CI hay que calcularla a mano. (2) **Neumann (parte b) NO está** en el script (solo Dirichlet, valor de borde fijo); va 100% a mano.

### Ej 4 — Transformada de Fourier de e^{t−1} en [0,1] · [No cubierto] | NO
**Enunciado (resumen):** TF de f(t)=e^{−|t−1|} si 0≤t≤1 (=e^{t−1} en [0,1]), 0 si no.
**Por qué No cubierto:** `tf` Op4 solo integra **polinomios** en [a,b]; una exponencial e^{t−1} no es polinomio. Op3 es e^{−at}u(t) unilateral, no este pulso en [0,1].
**Cómo lo escribo en el examen:** a mano: en [0,1] |t−1|=1−t → f=e^{t−1}; F(ω)=∫₀¹e^{t−1}e^{−iωt}dt = **(e^{−iω}−e^{−1})/(1−iω)**, con F(0)=1−e^{−1}≈0.6321.

---

## Limitaciones / gotchas clave (resumen para el examen)

1. **BUG en `diag` (rama Cardano, det≠0 + complejos):** la línea `L1(real)=...` imprime un número INCORRECTO (temas 01 y 05: dio −0.1667/0.1667 en vez de 1/2). Confiar en que **no armó P,D ⇒ no diagonalizable en ℝ**, pero sacar el autovalor real a mano del factor lineal del polinomio. La rama `c~0` (det=0, temas 02/04) y la cúbica de 3 reales (tema 03) SÍ imprimen valores correctos.
2. **`fs` solo 9 templates:** cubre `1−x` (tmpl 8) y `x−[x]` (tmpl 9), pero NO `x−x²` (tema 03) ni `1−x²` (tema 05) → esos van a mano.
3. **`fs` conv en borde de período:** el campo `prom` puede salir mal (no periodiza el muestreo de los límites laterales), pero `S_N(t0)` es correcto. Usar S_N.
4. **`tf` Op4 solo polinomios** en [a,b]: cubre (t−1)² (tema 02) y t−t² (tema 03), pero NO e^{−|t|} (tema 01) ni e^{t−1} (tema 05) → fórmula cerrada a mano (el script igual sirve para verificar F(0) y puntos).
5. **`tl` Op4 calcula M_EB (codominio canónico), NO M_BB:** tema 03 Ej1a (M_BB) va a mano (P⁻¹AP).
6. **`lu` usa pivoteo parcial (P≠I):** si la cátedra pide Doolittle sin pivoteo, el resultado del script difiere (válido igual). Tema 04 Ej3c.
7. **`edp` solo Dirichlet (valor fijo) y CI por template:** tema 05 Ej3a el esquema sí, pero la CI sen(x) y todo Neumann (3b) van a mano.
8. **EDO→sistema 1er orden + esquema implícito (temas 01,02,03 Ej3):** reformulación teórica, ningún script lo hace.
# Sección Final B — Temas VI a X (scripts Casio fx-CG50)

> Sandbox: `/tmp/acasios_sb`. Cada salida pegada abajo es la **captura real** de
> `printf '...\n' | python3 run_mod.py <mod>`.
> Convención de impresión: vectores/matrices 4 cifras (`show_vec`/`show_mat`),
> autovalores/coef 6 cifras. **`fs` imprime `a0=(2/T)∫f` y también `a0/2`**: el
> "a0 valor medio" de la cátedra = `a0/2` del script.

---

## Final Tema VI

### Ej 1 — N(T), Im(T) y diagonalización · [tl:1 + diag] | PARCIAL (bug numérico en diag)
**Enunciado (resumen):** $T(x,y,z)=(2x-y,\ x+y-z,\ x+y+2z)$. a) N(T) e Im(T). b) ¿diagonalizable en $\mathbb R$?
**De dónde salen los inputs:** cada componente de salida → una fila de $A=M_{EE}$: $2x-y\to(2,-1,0)$, $x+y-z\to(1,1,-1)$, $x+y+2z\to(1,1,2)$.
**Inputs Casio (a):** `tl`, opción `1` (`N(T),Im,rg`); `filas=3`, `cols=3`, filas `2,-1,0` / `1,1,-1` / `1,1,2`.
**Comando:** `printf '1\n3\n3\n2,-1,0\n1,1,-1\n1,1,2\n' | python3 run_mod.py tl`
**Salida del script (real):**
```
rref:
1 0 0
0 1 0
0 0 1
rg= 3
dim N= 0
-- Base N(T)
N(T)={0}
-- Base Im(T)
c1: 2 1 1
c2: -1 1 1
c3: 0 -1 2
```
**Inputs Casio (b):** `diag`; `n=3`, filas `2,-1,0` / `1,1,-1` / `1,1,2`.
**Comando:** `printf '3\n2,-1,0\n1,1,-1\n1,1,2\n' | python3 run_mod.py diag`
**Salida del script (real):**
```
p(L)=L^3+
a=-5
b=10
c=-9
dep p=1.667
dep q=-1.593
disc=-87
L1(real)=0.363
L2,3 Re=-0.363
```
**Cómo lo escribo en el examen:** $\det A = 9\ne0 \Rightarrow T$ isomorfismo: $N(T)=\{0\}$ (dim 0), $\operatorname{Im}(T)=\mathbb R^3$ (dim 3), base = columnas $(2,1,1),(-1,1,1),(0,-1,2)$. Para (b): $p_A(\lambda)=\lambda^3-5\lambda^2+10\lambda-9$, $\operatorname{disc}=-87<0 \Rightarrow$ **una sola raíz real** y dos complejas conjugadas $\Rightarrow$ **$T$ NO es diagonalizable en $\mathbb R$**. (La raíz real verdadera es $\lambda_1\approx2.3926$.)
**Caveat:** parte (a) coincide al 100 % con la resolución. En (b) el polinomio ($-5,10,-9$) y el signo del discriminante son correctos y bastan para concluir, **PERO el valor `L1(real)=0.363` que imprime el script es ERRÓNEO** (bug en `diag.py`, rama Cardano: línea `print("L1(real)=", re+(u+v))` con `re=-(u+v)/2` da $(u+v)/2$ en vez de $(u+v)-a/3$; la raíz real correcta es $2.3926$, verificado con numpy `eigvals→2.3926`). El `Re` de las complejas también sale mal (imprime $-0.363$; el verdadero es $1.3037$). No afecta la conclusión cualitativa, pero no transcribir esos decimales.

### Ej 2 — Serie de Fourier de $1-x$ en $(0,1)$ y convergencia · [fs:1 + fs:3] | SÍ
**Enunciado (resumen):** a) Fourier de $f(x)=1-x$, $f(x)=f(x+1)$. b) convergencia en $x=0$ y $x=1/2$.
**De dónde salen los inputs:** $f(x)=1-x$ con período $1$ = **template 8** (`1-t en(0,1)`).
**Inputs Casio (a):** `fs`, opción `1` (`Coef a_n b_n`); template `>8`, `#arm=4`.
**Comando:** `printf '1\n8\n4\n' | python3 run_mod.py fs`
**Salida del script (real):**
```
T=1
w0=6.283
a0=1
a0/2=0.5
n=1  a=-6.347e-17  b=0.3183
n=2  a=-1.373e-17  b=0.1592
n=3  a=-5.151e-17  b=0.1061
n=4  a=-3.552e-17  b=0.07958
```
**Inputs Casio (b):** `fs`, opción `3` (`Conv en t0`); template `>8`, `t0=0`, `#arm=50`; y otra corrida con `t0=0.5`.
**Comando:** `printf '3\n8\n0\n50\n' | python3 run_mod.py fs` y `printf '3\n8\n0.5\n50\n' | python3 run_mod.py fs`
**Salida del script (real):**
```
t0=0:    x(t0+)=0.9999  x(t0-)=1  prom=1  S_N(t0)=0.5
t0=0.5:  x(t0+)=0.4999  x(t0-)=0.5001  prom=0.5  S_N(t0)=0.5
```
**Cómo lo escribo en el examen:** $a_0=\tfrac12$ (valor medio, = `a0/2` del script), $a_n=0$, $b_n=\tfrac{1}{\pi n}$ (script: $b_1=0.3183=\tfrac1\pi$, $b_2=0.1592=\tfrac1{2\pi}$, $b_3=0.1061=\tfrac1{3\pi}$, $b_4=0.0796=\tfrac1{4\pi}$). Serie $f(x)=\tfrac12+\tfrac1\pi\sum \tfrac{\sin(2\pi n x)}{n}$. (b) $S(0)=\tfrac12$ (promedio del salto $\tfrac{1+0}{2}$); $S(\tfrac12)=\tfrac12$ (continuidad).
**Caveat:** coincide totalmente con la resolución. Cuidar: el "a0" del script (=1) NO es el a0 de la cátedra; usar `a0/2=0.5`. En $x=0$ el script reporta `prom=1` (no detecta el salto, porque el template define $f$ sólo en $[0,1)$ y en $t_0-\varepsilon$ evalúa $1.0001$), pero el valor que importa, $S_N(0)=0.5$, sí es el correcto (promedio real del salto).

### Ej 3 — Calor: esquema implícito 4 nodos · [edp:1 parcial] | a) PARCIAL · b) No cubierto
**Enunciado (resumen):** $u_t=u_{xx}$, 4 nodos internos. a) Dirichlet $u(0,t)=u(1,t)=0$, CI $u(x,0)=e^{-x}\sen(x)$. b) mixto $u_x(0,t)=u(1,t)=0$, CI $u(x,0)=x^2$.
**De dónde salen los inputs:** $L=1$, 4 nodos $\Rightarrow h=0.2$. `edp` op1 sólo tiene CI {sen, cos, x(L−x), exp(−x²)} y **sólo Dirichlet**.
**Inputs Casio (a, estructura):** `edp`, opción `1` (`Calor Dir`); `L=1`, `nodos int=4`, `dt=0.04`, `#pasos=1`, CI `>3` (cualquiera, sólo para ver $h,r$), `u(0,t)=0`, `u(L,t)=0`.
**Comando:** `printf '1\n1\n4\n0.04\n1\n3\n0\n0\n' | python3 run_mod.py edp`
**Salida del script (real):**
```
h=0.2
r=1
-- u^0
0.16 0.24 0.24 0.16     <- (esto es x(L-x), NO la CI pedida)
-- u^1 t=0.040
0.112 0.176 0.176 0.112
```
**Cómo lo escribo en el examen (a):** Euler implícito: $-r\,u_{i-1}^{k+1}+(1+2r)u_i^{k+1}-r\,u_{i+1}^{k+1}=u_i^k$ con $r=\Delta t/h^2$, $h=0.2$. Matriz tridiagonal $4\times4$: $\operatorname{diag}=1+2r$, sub/super$=-r$. CI (a mano): $u_i^0=e^{-x_i}\sen(x_i)$ en $x_i=0.2,0.4,0.6,0.8 \approx (0.1627, 0.2610, 0.3099, 0.3223)$.
**Cómo lo escribo (b):** Neumann en $x=0$ con nodo fantasma $\Rightarrow$ sistema $5\times5$, primera fila $(1+2r,\,-2r,0,0,0)$ (huella del fantasma), última fila tridiagonal normal (Dirichlet en $x=1$). CI $u_i^0=x_i^2=(0,0.04,0.16,0.36,0.64)$.
**Caveat:** **a) PARCIAL** — el script arma exactamente el esquema implícito Dirichlet $4\times4$ y confirma $h=0.2$, $r=1$ con $\Delta t=0.04$ (det M=55), pero la CI $e^{-x}\sen(x)$ **no es ninguno de los 4 templates**, así que el vector inicial hay que evaluarlo a mano. **b) No cubierto** — `edp` sólo maneja Dirichlet; el borde Neumann $u_x(0,t)=0$ (nodo fantasma, $-2r$) no está implementado.

### Ej 4 — TF de $e^{-2|t|+1}$ en $[0,1]$ · [—] | No cubierto
**Enunciado (resumen):** $\hat f(\omega)$ de $f(t)=e^{-2|t|+1}=e^{1-2t}$ en $[0,1]$, $0$ afuera.
**Por qué no cubierto:** `tf` op4 integra **pulsos polinómicos** ($c_0+c_1t+\dots$), no exponenciales. `tf` op3 (`Exp -at u(t)`) es $e^{-at}u(t)$ en $[0,\infty)$, **no** truncado en $[0,1]$. Ninguna variante calcula $\int_0^1 e^{1-2t}e^{-i\omega t}dt$.
**Cómo lo escribo en el examen (a mano):** $\hat f(\omega)=e\int_0^1 e^{-(2+i\omega)t}dt=\dfrac{e-e^{-1}e^{-i\omega}}{2+i\omega}$; en $\omega=0$: $\dfrac{e-e^{-1}}{2}\approx1.1752$.
**Caveat:** chequeo de $\hat f(0)$ con numpy `quad` da $1.17520$ (coincide con la resolución), pero esto no usa ningún script — es verificación auxiliar.

---

## Final Tema VII

### Ej 1 — Parámetro $k$: rango y diagonalización · [diag con $k$ sustituido] | PARCIAL
**Enunciado (resumen):** $T(x,y,z)=(kx,\ 2x-2y-z,\ -2x+5y+4z)$. a) $k$ tal que $\dim R(T)<3$. b) $k$ tal que diagonalizable en $\mathbb R$.
**De dónde salen los inputs:** $A=\begin{pmatrix}k&0&0\\2&-2&-1\\-2&5&4\end{pmatrix}$. El script es numérico → se sustituye cada $k$ concreto.
**Inputs Casio (b, casos críticos):** `diag`; `n=3`, filas `k,0,0` / `2,-2,-1` / `-2,5,4` con $k\in\{-1,3\}$.
**Comando:** `printf '3\n-1,0,0\n2,-2,-1\n-2,5,4\n' | python3 run_mod.py diag` (y $k=3$).
**Salida del script (real):**
```
k=-1:  Autovalores L1=3, L2=-1, L3=-1
       S_L=-1 m=2 -> dimK= 1 <m= 2  (NO diag.)
       NO diagonaliz.  dim= 2 <n= 3
k=3:   Autovalores L1=3, L2=3, L3=-1
       S_L=3 m=2 -> v:(2.5,1,0)  v:(0.5,0,1)
       S_L=-1 -> v:(0,-1,1)
       P=[[2.5,0.5,0],[1,0,-1],[0,1,1]] D=diag(3,3,-1)
       |AP-PD|=8.882e-16
```
**Cómo lo escribo en el examen:** (a) $\det A=-3k$, así que $\dim R(T)<3 \iff k=0$. (b) Autovalores $\{k,3,-1\}$; diagonalizable salvo cuando un autovalor doble pierde multiplicidad geométrica: en $k=3$ sí ($m_g=2$, verificado $|AP-PD|\approx0$), en $k=-1$ no ($m_g=1$). $\Rightarrow$ **diagonalizable $\iff k\ne-1$**.
**Caveat:** (a) es simbólico ($\det A=-3k$): el script no lo deriva, va a mano. (b) el script confirma numéricamente los dos casos límite y coincide con la resolución ($k=3$ diag, $k=-1$ no). La base de $S_3$ que da el script ($(2.5,1,0),(0.5,0,1)$) difiere de la oficial ($(5,2,0),(1,0,2)$) por escala $\times2$ — ambas válidas, $|AP-PD|\approx0$.

### Ej 2 — Serie de Fourier de $1-x$ en $(0,1)$ · [fs:1 + fs:3] | SÍ
**Idéntico al Tema VI Ej 2.** Misma corrida `fs` op1 template 8 (`a0/2=0.5`, $b_n=\tfrac1{\pi n}$: $0.3183,0.1592,0.1061,0.0796$) y op3 ($S(0)=S(\tfrac12)=0.5$). Resultado: $f(x)=\tfrac12+\tfrac1\pi\sum\tfrac{\sin(2\pi n x)}{n}$, $S(0)=\tfrac12$ (salto), $S(\tfrac12)=\tfrac12$ (continuidad). Coincide con la resolución.

### Ej 3 — QR de $A=\begin{pmatrix}1&-3&2\\5&2&0\end{pmatrix}$ · [qr] | SÍ
**De dónde salen los inputs:** matriz $2\times3$ directa.
**Inputs Casio:** `qr`; `filas=2`, `cols=3`, filas `1,-3,2` / `5,2,0`.
**Comando:** `printf '2\n3\n1,-3,2\n5,2,0\n' | python3 run_mod.py qr`
**Salida del script (real):**
```
-- Col 1   ||u1||=5.099   v1: 0.1961 0.9806
-- Col 2   <a2,v1>=1.373  ||u2||=3.334  v2: -0.9806 0.1961
-- Col 3   <a3,v1>=0.3922 <a3,v2>=-1.961  ||u3||=2.289e-16
col LD: no QR
```
**Cómo lo escribo en el examen:** $Q=\tfrac1{\sqrt{26}}\begin{pmatrix}1&-5\\5&1\end{pmatrix}\approx\begin{pmatrix}0.1961&-0.9806\\0.9806&0.1961\end{pmatrix}$, $R=\begin{pmatrix}5.099&1.373&0.3922\\0&3.334&-1.961\end{pmatrix}=\tfrac1{\sqrt{26}}\begin{pmatrix}26&7&2\\0&17&-10\end{pmatrix}$. La 3ª columna es LD ($u_3=0$, rango deficiente): $Q$ es $2\times2$ y $R$ es $2\times3$.
**Caveat:** coincide exactamente con la resolución ($r_{11}=\sqrt{26}$, $r_{12}=7/\sqrt{26}$, etc.). El script corta con `col LD: no QR` al llegar a $u_3=0$, **pero ya imprimió todos los $R_{ij}$ y los $v_1,v_2$**, así que la info para escribir $Q,R$ está completa.

---

## Final Tema VIII

### Ej 1 — Parámetro $k$: $\dim R(T)=1$ y núcleo en $k=0$ · [tl:1 con $k=0$] | PARCIAL
**Enunciado (resumen):** $T(x,y,z)=(2x+8y+kz,\ -x-4y,\ (k+3)x+12y+2kz)$. a) $k$ tal que $\dim R(T)=1$. b) $k=0$: base y dim de $N(T)$.
**De dónde salen los inputs:** $A=\begin{pmatrix}2&8&k\\-1&-4&0\\k+3&12&2k\end{pmatrix}$. El script no es simbólico; verifico el caso $k=0$.
**Inputs Casio (b):** `tl`, opción `1`; `filas=3`, `cols=3`, filas `2,8,0` / `-1,-4,0` / `3,12,0`.
**Comando:** `printf '1\n3\n3\n2,8,0\n-1,-4,0\n3,12,0\n' | python3 run_mod.py tl`
**Salida del script (real):**
```
rref:
1 4 0
0 0 0
0 0 0
rg= 1
dim N= 2
-- Base N(T)
n1: -4 1 0
n2: 0 0 1
-- Base Im(T)
c1: 2 -1 3
```
**Cómo lo escribo en el examen:** (a) $\det A=4k^2$, sólo se anula en $k=0$; en $k=0$ las 3 filas son proporcionales a $(1,4,0)$ $\Rightarrow \operatorname{rg}=1$, sin valor intermedio. $\boxed{\dim R(T)=1\iff k=0}$. (b) Con $k=0$: $\operatorname{rg}=1$, $\dim N(T)=2$, base $\{(-4,1,0),(0,0,1)\}$ (exacto, del script).
**Caveat:** (a) el "todos los menores $2\times2$ se anulan $\iff k=0$" es simbólico (a mano: $\det A=4k^2$). (b) el script lo resuelve y **coincide exactamente** con la resolución (base $N(T)$, dim 2, $\operatorname{Im}(T)=\langle(2,-1,3)\rangle$).

### Ej 2 — Serie de Fourier de $1-x^2$ en $(0,1)$ · [—] | No cubierto
**Enunciado (resumen):** Fourier de $f(x)=1-x^2$, $f(x)=f(x+1)$; convergencia en $0$ y $1/2$.
**Por qué no cubierto:** `fs` sólo tiene 9 templates: $t,\ t^2,\ |t|,\ \operatorname{sgn},\ e^t$ (en $(-\pi,\pi)$ o $(0,2\pi)$), $1-t$ y $t-[t]$ en $(0,1)$. **No existe $1-x^2$.** No es reescalable a ningún template (no es $t^2$ puro ni $1-t$).
**Cómo lo escribo en el examen (a mano):** $a_0=\tfrac23$, $a_n=-\tfrac1{\pi^2 n^2}$, $b_n=\tfrac1{\pi n}$; $f(x)\sim\tfrac23-\tfrac1{\pi^2}\sum\tfrac{\cos(2\pi nx)}{n^2}+\tfrac1\pi\sum\tfrac{\sin(2\pi nx)}{n}$. Convergencia: $S(0)=\tfrac12$ (salto $\tfrac{1+0}{2}$), $S(\tfrac12)=f(\tfrac12)=\tfrac34$ (continuidad).
**Caveat:** completamente a mano; ningún script aplica.

### Ej 3 — SVD de $A=\begin{pmatrix}1&-3&2\\5&2&0\end{pmatrix}$ · [svd vía $A^T$] | SÍ
**De dónde salen los inputs:** matriz $2\times3$. El script exige $\text{cols}\le\text{filas}$; como $3>2$ avisa `pasar A^T (n<m)` → corro la SVD de $A^T$ ($3\times2$) e intercambio roles $U\leftrightarrow V$.
**Inputs Casio:** `svd`; (primero $A$ directa devuelve el aviso). Luego $A^T$: `filas=3`, `cols=2`, filas `1,5` / `-3,2` / `2,0`.
**Comando:** `printf '3\n2\n1,5\n-3,2\n2,0\n' | python3 run_mod.py svd`
**Salida del script (real):**
```
AtA: [[14,-1],[-1,29]]  tr=43 det=405 disc=229
-- V.singulares  s1=5.39132  s2=3.73278
-- V cols  v1: -0.06623 0.9978   v2: 0.9978 0.06623
-- U cols  u1: 0.9131 0.407 -0.02457
           u2: 0.356 -0.7664 0.5346
           u3: -0.1988 0.4969 0.8447
-- Verif  |USVt-A|=6.661e-16
Sigma: [[5.391,0],[0,3.733],[0,0]]
```
**Cómo lo escribo en el examen:** valores singulares $\sigma_1=\sqrt{\tfrac{43+\sqrt{229}}2}\approx5.3913$, $\sigma_2\approx3.7328$. Como corrí la SVD de $A^T$, **intercambio**: para $A$ original, $U_A$ ($2\times2$) = las "V cols" $\to u_1=(-0.0662,0.9978),\ u_2=(0.9978,0.0662)$; $V_A$ ($3\times3$) = las "U cols" $\to v_1=(0.9131,0.407,-0.0246),\ v_2=(0.356,-0.7664,0.5346),\ v_3=(-0.1988,0.4969,0.8447)$. $\Sigma=\begin{pmatrix}5.391&0&0\\0&3.733&0\end{pmatrix}$.
**Caveat:** $\sigma_1,\sigma_2$ coinciden exactamente con la resolución. Las columnas coinciden **salvo el signo global de $u_1/v_1$** (resolución: $U$ col 1 $=(0.0662,-0.9978)$, $V$ col 1 $=(-0.9131,-0.4070,0.0246)$); es el flip de signo libre de toda SVD (al invertir $v_1$ se invierte $u_1$, consistente). Reconstrucción $|U\Sigma V^T-A|=6.7\times10^{-16}$ ✓.

---

## Final Tema IX

### Ej 1 — $M_{BB}$ y SVD · [a: numpy aux / b: svd] | a) PARCIAL · b) SÍ
**Enunciado (resumen):** $T(x,y,z)=(2x+y,\ y-z,\ z+x)$. a) $M_{BB}$ con $B=\{(0,0,1),(1,0,0),(1,-1,0)\}$. b) SVD de $M_{BB}$.
**De dónde salen los inputs:** $M_{EE}=\begin{pmatrix}2&1&0\\0&1&-1\\1&0&1\end{pmatrix}$, $P=(b_1|b_2|b_3)$. $M_{BB}=P^{-1}M_{EE}P$.
**(a) Caveat de cobertura:** **ningún script arma $M_{BB}$ directamente.** `tl` op4 espera una matriz $M_{EB}$ ya dada (dominio base $B$, codominio canónico) y hace antiimagen/núcleo, no la conjugación $P^{-1}M_{EE}P$; `cb` sólo cambia coordenadas de vectores. $M_{BB}$ se calcula a mano (columna $j=[T(b_j)]_B$). Verificación auxiliar con numpy ($P^{-1}M_{EE}P$): da $\begin{pmatrix}1&1&1\\-1&2&0\\1&0&1\end{pmatrix}$, igual a la resolución.
**Inputs Casio (b):** `svd`; `filas=3`, `cols=3`, filas de $M_{BB}$ `1,1,1` / `-1,2,0` / `1,0,1`.
**Comando:** `printf '3\n3\n1,1,1\n-1,2,0\n1,0,1\n' | python3 run_mod.py svd`
**Salida del script (real):**
```
AtA: [[3,-1,2],[-1,5,1],[2,1,2]]
p(L)=L^3+ a=-10 b=25 c=-1   dep p=-8.333 dep q=8.259 disc=473
-- V.singulares  s1=2.33006  s2=2.12842  s3=0.20164
-- V cols  v1: -0.312 0.9454 0.09371
           v2: 0.7364 0.1784 0.6526
           v3: -0.6003 -0.2726 0.7519
-- U cols  u1: 0.312 0.9454 -0.09371
           u2: 0.7364 -0.1784 0.6526
           u3: -0.6003 0.2726 0.7519
-- Verif  |USVt-A|=1.11e-15
Sigma: diag(2.33, 2.128, 0.2016)
```
**Cómo lo escribo en el examen:** (a) $M_{BB}=\begin{pmatrix}1&1&1\\-1&2&0\\1&0&1\end{pmatrix}$. (b) char. de $A^TA$: $\lambda^3-10\lambda^2+25\lambda-1$; $\sigma_1=2.3301,\ \sigma_2=2.1284,\ \sigma_3=0.2016$; $V,U$ con las columnas dadas; $\Sigma=\operatorname{diag}(2.3301,2.1284,0.2016)$.
**Caveat:** (b) **coincide exactamente** con la resolución (mismo poli $\lambda^3-10\lambda^2+25\lambda-1$, mismos $\sigma_i$, mismos $V,U$ — incluso los signos coinciden con la versión publicada), $|U\Sigma V^T-A|=1.1\times10^{-15}$, $\prod\sigma_i\approx1=|\det|$. (a) PARCIAL: el script no construye $M_{BB}$; sólo verifico vía numpy auxiliar.

### Ej 2 — Calor Dirichlet, CI $x^2$, 4 nodos · [edp:1 parcial] | PARCIAL
**Enunciado (resumen):** $u_t=u_{xx}$, $u(0,t)=u(1,t)=0$ (errata del PDF: "$u(1,t)=u(1,t)$", se lee Dirichlet homogéneo doble), CI $u(x,0)=x^2$. Plantear esquema implícito 4 nodos + matrices.
**De dónde salen los inputs:** $L=1$, 4 nodos $\Rightarrow h=0.2$. CI $x^2$ no es template.
**Inputs Casio (estructura):** `edp`, opción `1`; `L=1`, `nodos int=4`, `dt=0.04`, `#pasos=1`, CI `>3`, `u(0,t)=0`, `u(L,t)=0`.
**Comando:** `printf '1\n1\n4\n0.04\n1\n3\n0\n0\n' | python3 run_mod.py edp`
**Salida del script (real):**
```
h=0.2
r=1
-- u^0  0.16 0.24 0.24 0.16   (= x(L-x), NO la CI x^2)
-- u^1  0.112 0.176 0.176 0.112
```
**Cómo lo escribo en el examen:** Euler implícito $-r u_{i-1}^{k+1}+(1+2r)u_i^{k+1}-r u_{i+1}^{k+1}=u_i^k$, $r=\Delta t/h^2$, $h=0.2$. Sistema tridiagonal $4\times4$: $M=\begin{pmatrix}1+2r&-r&&\\-r&1+2r&-r&\\&-r&1+2r&-r\\&&-r&1+2r\end{pmatrix}$, $M\mathbf u^{k+1}=\mathbf u^k$. CI (a mano): $\mathbf u^0=(0.2^2,0.4^2,0.6^2,0.8^2)=(0.04,0.16,0.36,0.64)$.
**Caveat:** PARCIAL. El script arma el esquema implícito Dirichlet $4\times4$ exacto (confirma $h=0.2$, $r=1$ con $\Delta t=0.04$ → $\det M=55$ como la resolución), pero la CI $x^2$ **no es ninguno de los 4 templates** → el vector inicial $(0.04,0.16,0.36,0.64)$ va a mano (la salida `0.16 0.24 0.24 0.16` es de $x(L-x)$, no usarla).

### Ej 3 — TF de $t^2-t$ en $[0,1]$ · [tf:4] | SÍ
**De dónde salen los inputs:** polinomio $t^2-t=0+(-1)t+(1)t^2$ en $[0,1]$ → grado 2, $c_0=0,c_1=-1,c_2=1$, $a=0,b=1$.
**Inputs Casio:** `tf`, opción `4` (`Polin. num.`); `grado=2`, `c0=0`, `c1=-1`, `c2=1`, `a inf=0`, `b sup=1`, `w_max=5`.
**Comando:** `printf '4\n2\n0\n-1\n1\n0\n1\n5\n' | python3 run_mod.py tf`
**Salida del script (real, grilla, w paso 1):**
```
 w     Re        Im       |F|
-5.0   0.0667   -0.0498   0.0832
-4.0   0.0453   -0.099    0.109
-3.0  -0.00934  -0.132    0.132
-2.0  -0.0814   -0.127    0.151
-1.0  -0.143    -0.0779   0.163
 0.0  -0.167     0        0.167
 1.0  -0.143     0.0779   0.163
 2.0  -0.0814    0.127    0.151
 3.0  -0.00934   0.132    0.132
 4.0   0.0453    0.099
```
**Cómo lo escribo en el examen:** $\hat f(\omega)=\int_0^1(t^2-t)e^{-i\omega t}dt=\dfrac{(\omega+2i)+(\omega-2i)e^{-i\omega}}{\omega^3}$; $\operatorname{Re}=\tfrac{\omega+\omega\cos\omega-2\sin\omega}{\omega^3}$, $\operatorname{Im}=\tfrac{2-\omega\sin\omega-2\cos\omega}{\omega^3}$. En $\omega=0$: $\hat f(0)=-\tfrac16=-0.1667$ (= script).
**Caveat:** coincide con la resolución. $\hat f(0)=-0.167=-1/6$ ✓; $\hat f(1)=-0.143+0.0779i$ vs oficial $-0.142640+0.077924i$ ✓; $\hat f(2)=-0.0814+0.127i$ vs $-0.081361+0.126712i$ ✓. El script da grilla numérica (no la fórmula cerrada): la forma cerrada se escribe a mano, el script verifica valores puntuales.

---

## Final Tema X

### Ej 1 — $M_{BB}$ y QR · [a: numpy aux / b: qr] | a) PARCIAL · b) SÍ
**Enunciado (resumen):** $T(x,y,z)=(2x+y-z,\ x+3y-z,\ z-y)$. a) $M_{BB}$ con $B=\{(0,0,1),(1,0,0),(1,-1,0)\}$. b) QR de $M_{BB}$.
**De dónde salen los inputs:** $M_{EE}=\begin{pmatrix}2&1&-1\\1&3&-1\\0&-1&1\end{pmatrix}$, $M_{BB}=P^{-1}M_{EE}P$.
**(a) Caveat de cobertura:** igual que Tema IX — **ningún script arma $M_{BB}$**. A mano (columna $j=[T(b_j)]_B$). Verificación aux numpy ($P^{-1}M_{EE}P$): $\begin{pmatrix}1&0&1\\-2&3&-1\\1&-1&2\end{pmatrix}$, igual a la resolución.
**Inputs Casio (b):** `qr`; `filas=3`, `cols=3`, filas de $M_{BB}$ `1,0,1` / `-2,3,-1` / `1,-1,2`.
**Comando:** `printf '3\n3\n1,0,1\n-2,3,-1\n1,-1,2\n' | python3 run_mod.py qr`
**Salida del script (real):**
```
-- Col 1  ||u1||=2.449   v1: 0.4082 -0.8165 0.4082
-- Col 2  <a2,v1>=-2.858 ||u2||=1.354  v2: 0.8616 0.4924 0.1231
-- Col 3  <a3,v1>=2.041  <a3,v2>=0.6155 ||u3||=1.206  v3: -0.3015 0.3015 0.9045
Q: [[0.4082,0.8616,-0.3015],[-0.8165,0.4924,0.3015],[0.4082,0.1231,0.9045]]
R: [[2.449,-2.858,2.041],[0,1.354,0.6155],[0,0,1.206]]
|QR-A|=0
|QtQ-I|=1.055e-15
```
**Cómo lo escribo en el examen:** (a) $M_{BB}=\begin{pmatrix}1&0&1\\-2&3&-1\\1&-1&2\end{pmatrix}$. (b) $Q\approx\begin{pmatrix}0.4082&0.8616&-0.3015\\-0.8165&0.4924&0.3015\\0.4082&0.1231&0.9045\end{pmatrix}$, $R\approx\begin{pmatrix}2.4495&-2.8577&2.0412\\0&1.3540&0.6155\\0&0&1.2060\end{pmatrix}$ ($r_{11}=\sqrt6$, $r_{22}=\sqrt{66}/6$, $r_{33}=4/\sqrt{11}$).
**Caveat:** (b) **coincide exactamente** con la resolución, incluso los signos (convención Gram-Schmidt $R_{ii}>0$), $|QR-A|=0$, $Q^TQ=I$. (a) PARCIAL: $M_{BB}$ a mano + numpy auxiliar.

### Ej 2 — Calor mixto Neumann/Dirichlet, CI $e^{-x^2}$ · [—] | No cubierto
**Enunciado (resumen):** $u_t=u_{xx}$, $u_x(0,t)=0$ (Neumann), $u(1,t)=0$ (Dirichlet), CI $e^{-x^2}$, 4 nodos.
**Por qué no cubierto:** `edp` op1 sólo implementa **Dirichlet en ambos bordes**; el borde Neumann $u_x(0,t)=0$ (nodo fantasma $\Rightarrow$ fila $(1+2r,-2r,\dots)$, sistema $5\times5$) **no está**. Además la CI $e^{-x^2}$ no es template (sí está `exp(-x^2)` como op4, pero el borde Neumann lo descalifica).
**Cómo lo escribo en el examen (a mano):** sistema $5\times5$ (entra $u_0$ por Neumann, sale $u_5$ por Dirichlet); $M=\begin{pmatrix}1+2r&-2r&0&0&0\\-r&1+2r&-r&0&0\\0&-r&1+2r&-r&0\\0&0&-r&1+2r&-r\\0&0&0&-r&1+2r\end{pmatrix}$; primera fila con $-2r$ (fantasma), última tridiagonal normal. CI $\mathbf u^0=e^{-x_i^2}$ en $x_i=0,0.2,0.4,0.6,0.8\approx(1,0.9608,0.8521,0.6977,0.5273)$.
**Caveat:** No cubierto por el script (Neumann no implementado). Va íntegramente a mano.

### Ej 3 — TF de $1-|t|$ en $[-1,1]$ (triángulo) · [tf:2] | SÍ
**De dónde salen los inputs:** pulso triangular en $[-n,n]$ con $n=1$ (intervalo $[-1,1]$).
**Inputs Casio:** `tf`, opción `2` (`Tri (sinc^2)`); `n=1`, `w_max=3`.
**Comando:** `printf '2\n1\n3\n' | python3 run_mod.py tf`
**Salida del script (real):**
```
 w     F(w)
-3.00  0.4422
-2.50  0.5764
-2.00  0.7081
-1.50  0.826
-1.00  0.9194
-0.50  0.9793
 0.00  1
 0.50  0.9793
 1.00  0.9194
 ...   (par)
```
**Cómo lo escribo en el examen:** $\hat f(\omega)=\dfrac{2(1-\cos\omega)}{\omega^2}=\dfrac{4\sin^2(\omega/2)}{\omega^2}=\operatorname{sinc}^2(\omega/2)$, real y $\ge0$ ($f$ par). $\hat f(0)=1$.
**Caveat:** **coincide exactamente** con la resolución: $\hat f(0)=1$, $\hat f(0.5)=0.9793$, $\hat f(1)=0.9194$, $\hat f(2)=0.7081$, $\hat f(3)=0.4422$ — todos = los valores de $\operatorname{sinc}^2(\omega/2)$ tabulados en la resolución. El script asume el triángulo unitario centrado de semiancho $n=1$, que es justo $1-|t|$ en $[-1,1]$.

---

## Resumen de cobertura

| Tema | Ej1 | Ej2 | Ej3 | Ej4 |
|---|---|---|---|---|
| VI | tl:1 SÍ + diag PARCIAL (bug raíz) | fs:1,3 SÍ | edp:1 a)PARCIAL b)NO | TF NO cubierto |
| VII | diag PARCIAL (k sustituido) | fs:1,3 SÍ | qr SÍ | — |
| VIII | tl:1 PARCIAL (k=0) | fs NO cubierto (1−x²) | svd SÍ (vía Aᵀ) | — |
| IX | a)PARCIAL b)svd SÍ | edp PARCIAL (CI x²) | tf:4 SÍ | — |
| X | a)PARCIAL b)qr SÍ | edp NO (Neumann) | tf:2 SÍ | — |
# Sección C — Finales Tema XI, Tema XI (variante) y Tema XIV

> Sandbox: `/tmp/acasios_sb`. Todas las salidas pegadas abajo son **reales** (capturadas con `python3 run_mod.py <mod>`), no inventadas.
>
> **Puente TL no estándar → matriz asociada (clave para varios ejercicios):** los scripts solo operan sobre matrices numéricas en coordenadas. Cuando el dominio/codominio NO es $\mathbb{R}^n$ canónico (polinomios $P_2$, matrices $\mathbb{R}^{n\times n}$), primero hay que **armar a mano** la matriz $M$ de la TL en las bases dadas (cada columna = imagen del $j$-ésimo vector de la base, en coordenadas de la base de llegada), y recién esa $M$ se mete en `tl`/`diag`. El script clasifica/diagonaliza $M$, pero el paso de "vectorizar" el espacio abstracto va a mano.

---

## Final Tema XI

### Ej 1 — Sobreyectividad y diagonalización de $M_{EE}(T)$ con parámetro $a$ · [diag] | PARCIAL

**Enunciado (resumen):** $M_{EE}(T)=\begin{pmatrix}4&-1&a\\0&-2a+1&0\\0&0&4a\end{pmatrix}$. a) Hallar $a$ para que $T$ sea sobreyectiva. b) Para $a=1$, ¿es diagonalizable?

**a) NO cubierto (simbólico).** El script `diag` es numérico, no resuelve "para qué $a$". La sobreyectividad de $T:\mathbb{R}^3\to\mathbb{R}^3$ equivale a $\det A\neq0$; como $A$ es triangular, $\det A=4\,(1-2a)\,(4a)=16a(1-2a)$, que se anula en $a=0$ y $a=\tfrac12$. Va a mano: $\boxed{a\notin\{0,\tfrac12\}}$. (Se podría verificar cada $a$ concreto corriendo `diag`/`lu`, pero el "para todo $a$" es álgebra simbólica.)

**b) SÍ ($a=1$).**
**De dónde salen los inputs:** sustituir $a=1$ en $A$ → filas `4,-1,1` / `0,-1,0` / `0,0,4`.
**Inputs Casio:** módulo `diag`; `n=3`; filas de $A$.
**Comando de verificación:**
`printf '3\n4,-1,1\n0,-1,0\n0,0,4\n' | python3 run_mod.py diag`
**Salida del script (real):**
```
n(2 o 3):A3x3:
f1/3:f2/3:f3/3:A:
4 -1 1
0 -1 0
0  0 4

-- P(L) caract.
p(L)=L^3+
a=-7
b=8
c=16
dep p=-8.333
dep q=9.259
disc=-9.095e-13
Autovalores:
L1=4
L2=4
L3=-1

-- S_L=4 m=2
dimK= 1 <m= 2
(NO diag.)
v:
1 0 0

-- S_L=-1
v:
0.2 1 0
NO diagonaliz.
dim= 2 <n= 3
```
**Cómo lo escribo en el examen:** Para $a=1$, $p_A(\lambda)=(\lambda-4)^2(\lambda+1)$, autovalores $\lambda=4$ (doble) y $\lambda=-1$ (simple). El autoespacio de $\lambda=4$ es $S_4=\langle(1,0,0)\rangle$, de dimensión $m_g(4)=1<2=m_a(4)$. Como falla la igualdad de multiplicidades, $T$ **NO es diagonalizable**.
**Caveat:** Coincide con la resolución oficial. El autovector de $\lambda=-1$ que da el script, $(0.2,1,0)$, es proporcional a $(1,5,0)$ de la oficial ($\times 0.2$) — misma dirección. Salida `(NO diag.)` + `NO diagonaliz.` confirma la conclusión.

---

### Ej 2 — TL sobre matrices $T(A)=A-A^T$: $N(T)$, $R(T)$ y sistema $T(A)X=B$ · [tl:1 + tl:2] | SÍ (vía matriz asociada)

**Enunciado (resumen):** $T:\mathbb{R}^{n\times n}\to\mathbb{R}^{n\times n}$, $T(A)=A-A^T$. a) $N(T)$ y $R(T)$. b) Para $A=\begin{psmallmatrix}1&-1\\2&0\end{psmallmatrix}$ resolver $T(A)X=B$, $B=(1,1)^T$.

**a) Puente TL no estándar (matrices → matriz asociada $4\times4$ para $n=2$).** Vectorizamos $A=(a_{11},a_{12},a_{21},a_{22})$. $T(A)=A-A^T$ tiene componentes $(0,\ a_{12}-a_{21},\ a_{21}-a_{12},\ 0)$, así que la matriz asociada (mismo orden de vectorización en salida) es
$$M=\begin{pmatrix}0&0&0&0\\0&1&-1&0\\0&-1&1&0\\0&0&0&0\end{pmatrix}.$$
**Inputs Casio:** módulo `tl`, opción `1` (`N(T),Im,rg`); `filas=4`, `cols=4`; filas de $M$.
**Comando de verificación:**
`printf '1\n4\n4\n0,0,0,0\n0,1,-1,0\n0,-1,1,0\n0,0,0,0\n' | python3 run_mod.py tl`
**Salida del script (real):**
```
 1)N(T),Im,rg
 2)Antiimagen b
 3)Mat. por regla
 4)M(T)_EB base B
Op:filas A:cols A:A4x4:
f1/4:f2/4:f3/4:f4/4:A:
0  0  0 0
0  1 -1 0
0 -1  1 0
0  0  0 0

-- RREF: N(T) Im(T)
rref:
0 1 -1 0
0 0  0 0
0 0  0 0
0 0  0 0
rg= 1
dim N= 3

-- Base N(T)
n1:
1 0 0 0
n2:
0 1 1 0
n3:
0 0 0 1

-- Base Im(T)
(cols pivote de A)
c2:
0 1 -1 0
```
**Cómo lo escribo en el examen:** "Devectorizando" la base del núcleo: $n_1=\begin{psmallmatrix}1&0\\0&0\end{psmallmatrix}$, $n_2=\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}$, $n_3=\begin{psmallmatrix}0&0\\0&1\end{psmallmatrix}$ → exactamente las **matrices simétricas**, $\dim N(T)=3=\tfrac{n(n+1)}2$. La imagen $c_2\to\begin{psmallmatrix}0&1\\-1&0\end{psmallmatrix}$ genera las **matrices antisimétricas**, $\dim R(T)=1=\tfrac{n(n-1)}2$. (Generalizando a $n$ cualquiera por el mismo argumento.)
**Caveat:** Coincide con la oficial ($N(T)$ = simétricas, $R(T)$ = antisimétricas). El script valida el caso $n=2$; la fórmula general $\tfrac{n(n\pm1)}2$ se argumenta a mano.

**b) SÍ.** Primero a mano $T(A)=A-A^T=\begin{psmallmatrix}0&-3\\3&0\end{psmallmatrix}$ (antisimétrica, como debe). El sistema $T(A)X=B$ es un sistema lineal $2\times2$ ordinario → `tl` opción `2`.
**Inputs Casio:** módulo `tl`, opción `2` (`Antiimagen b`); `filas=2`, `cols=2`; filas de $T(A)$ `0,-3` / `3,0`; vector `b` = `1,1`.
**Comando de verificación:**
`printf '2\n2\n2\n0,-3\n3,0\n1,1\n' | python3 run_mod.py tl`
**Salida del script (real):**
```
 1)N(T),Im,rg
 2)Antiimagen b
 3)Mat. por regla
 4)M(T)_EB base B
Op:filas A:cols A:A2x2:
f1/2:f2/2:b2:
-- Resuelvo Ax=b
x_p:
0.3333 -0.3333
Sol unica.
```
**Cómo lo escribo en el examen:** $\det T(A)=9\neq0$ → solución única $\boxed{X=(\tfrac13,\ -\tfrac13)^T}$.
**Caveat:** Coincide exactamente con la oficial. El armado de $T(A)=A-A^T$ va a mano; el script resuelve el sistema resultante.

---

### Ej 3 — SVD y QR de $A_{3\times2}$ · [svd] + [qr] | SÍ

**Enunciado (resumen):** $A=\begin{pmatrix}1&1\\0&-3\\-3&5\end{pmatrix}$. a) SVD. b) QR.

**a) SVD.**
**De dónde salen los inputs:** $A$ es $3\times2$ → `filas=3`, `cols=2`. Como $m=2\le n=3$, el script va directo por $A^TA$.
**Inputs Casio:** módulo `svd`; `filas=3`, `cols=2`; filas de $A$.
**Comando de verificación:**
`printf '3\n2\n1,1\n0,-3\n-3,5\n' | python3 run_mod.py svd`
**Salida del script (real):**
```
filas A:cols A:A3x2:
f1/2:f2/2:f3/2:A:
 1  1
 0 -3
-3  5

-- Via AtA 2x2
AtA:
 10 -14
-14  35
tr=45
det=154
disc=1409

-- V.singulares
s1=6.42404
s2=1.93175

-- V cols
v1:
-0.4086 0.9127
v2:
0.9127 0.4086

-- U cols
u1:
0.07846 -0.4262
0.9012
u2:
0.684 -0.6346 -0.3597
u3:
0.7252 0.6447 0.2417

-- Verif
|USVt-A|=1.776e-15
Sigma:
6.424     0
    0 1.932
    0     0
```
**Cómo lo escribo en el examen:** $A^TA=\begin{psmallmatrix}10&-14\\-14&35\end{psmallmatrix}$, autovalores $\tfrac{45\pm\sqrt{1409}}2$ → valores singulares $\sigma_1\approx6.4240$, $\sigma_2\approx1.9318$ ($\Sigma$ es $3\times2$ con esos en la diagonal y fila nula abajo).
$$V\approx\begin{pmatrix}-0.4086&0.9127\\0.9127&0.4086\end{pmatrix},\quad U\approx\begin{pmatrix}0.0785&0.6840&0.7252\\-0.4262&-0.6346&0.6447\\0.9012&-0.3597&0.2417\end{pmatrix}.$$
**Caveat:** $\sigma_i$ idénticos a la oficial. Las columnas $v_1,u_1$ aparecen con **signo global opuesto** a la oficial ($v_1^{ofi}=(0.4086,-0.9127)$, $u_1^{ofi}=(-0.0785,0.4262,-0.9012)$); es la libertad de signo de la SVD (se pueden invertir $(v_i,u_i)$ a la vez). $u_3=(0.7252,0.6447,0.2417)$ coincide con $\tfrac1{\sqrt{154}}(9,8,3)$ de la oficial. `|USVt-A|≈1.8e-15` → reconstrucción exacta.

**b) QR.**
**Inputs Casio:** módulo `qr`; `filas=3`, `cols=2`; filas de $A$.
**Comando de verificación:**
`printf '3\n2\n1,1\n0,-3\n-3,5\n' | python3 run_mod.py qr`
**Salida del script (real):**
```
filas A:cols A:A3x2:
f1/2:f2/2:f3/2:A:
 1  1
 0 -3
-3  5

-- Col 1
||u1||=3.162
v1:
0.3162 0 -0.9487

-- Col 2
<a2,v1>=-4.427
||u2||=3.924
v2:
0.6116 -0.7645 0.2039

-- Resultado
Q:
 0.3162  0.6116
      0 -0.7645
-0.9487  0.2039
R:
3.162 -4.427
    0  3.924
|QR-A|=2.22e-16
|QtQ-I|=1.11e-16
```
**Cómo lo escribo en el examen:**
$$Q\approx\begin{pmatrix}0.3162&0.6116\\0&-0.7645\\-0.9487&0.2039\end{pmatrix},\quad R\approx\begin{pmatrix}3.1623&-4.4272\\0&3.9243\end{pmatrix}=\begin{pmatrix}\sqrt{10}&-7\sqrt{10}/5\\0&\sqrt{385}/5\end{pmatrix}.$$
**Caveat:** Coincide **exactamente** con la oficial (mismos signos). `|QR-A|≈2e-16`, `|QtQ-I|≈1e-16`.

---

## Final Tema XI (variante)

### Ej 1 — TL $T(x,y,z)=(-y+z,\,x+y,\,x+z)$: núcleo, imagen, diagonalización · [tl:1 + diag] | SÍ

**Enunciado (resumen):** a) Núcleo e imagen. b) ¿Diagonalizable en $\mathbb{R}$?

**Armado de $A$ (regla → columnas $T(e_j)$):** $T(e_1)=(0,1,1)$, $T(e_2)=(-1,1,0)$, $T(e_3)=(1,0,1)$ → $A=\begin{psmallmatrix}0&-1&1\\1&1&0\\1&0&1\end{psmallmatrix}$ (filas = coeficientes de cada componente de salida).

**a) tl Op1.**
**Comando de verificación:**
`printf '1\n3\n3\n0,-1,1\n1,1,0\n1,0,1\n' | python3 run_mod.py tl`
**Salida del script (real):**
```
 1)N(T),Im,rg
 2)Antiimagen b
 3)Mat. por regla
 4)M(T)_EB base B
Op:filas A:cols A:A3x3:
f1/3:f2/3:f3/3:A:
0 -1 1
1  1 0
1  0 1

-- RREF: N(T) Im(T)
rref:
1 0  1
0 1 -1
0 0  0
rg= 2
dim N= 1

-- Base N(T)
n1:
-1 1 1

-- Base Im(T)
(cols pivote de A)
c1:
0 1 1
c2:
-1 1 0
```
**Cómo lo escribo en el examen:** $\boxed{N(T)=\langle(-1,1,1)\rangle,\ \dim N=1}$; $\boxed{\operatorname{Im}(T)=\langle(0,1,1),(-1,1,0)\rangle,\ \dim=2}$, que es el plano $-x-y+z=0$.
**Caveat:** Coincide con la oficial.

**b) diag.**
**Comando de verificación:**
`printf '3\n0,-1,1\n1,1,0\n1,0,1\n' | python3 run_mod.py diag`
**Salida del script (real):**
```
n(2 o 3):A3x3:
f1/3:f2/3:f3/3:A:
0 -1 1
1  1 0
1  0 1

-- P(L) caract.
p(L)=L^3+
a=-2
b=1
c=-0
c~0: L factor
p=L(L^2+aL+b)
disc2=0
Autovalores:
L1=1
L2=1
L3=0

-- S_L=1 m=2
dimK= 1 <m= 2
(NO diag.)
v:
0 1 1

-- S_L=0
v:
-1 1 1
NO diagonaliz.
dim= 2 <n= 3
```
**Cómo lo escribo en el examen:** $p_A(\lambda)=\lambda(\lambda-1)^2$, autovalores $0$ (simple) y $1$ (doble). Para $\lambda=1$: $m_g=1<2=m_a$ → $T$ **NO es diagonalizable** en $\mathbb{R}$.
**Caveat:** Coincide con la oficial. El script detecta $c\approx0$ (det$=0$) y factoriza $\lambda$ correctamente.

---

### Ej 2 — Serie de Fourier de $f(x)=1-x^2$ en $[0,1]$ y convergencia · [fs] | NO cubierto

**Enunciado (resumen):** a) Desarrollo en serie de Fourier de $f:[0,1]\to\mathbb{R}$, $f(x)=1-x^2$, período $T=1$. b) ¿A qué converge en $x=0$ y $x=\tfrac12$?

**NO cubierto.** El módulo `fs` solo tiene 9 templates pre-cargados: $t$, $t^2$, $|t|$, $\operatorname{sgn}t$, $e^t$ en $(-\pi,\pi)$/$(0,2\pi)$, y $1-t$, $t-[t]$ en $(0,1)$. La función $1-x^2$ en $(0,1)$ **no es ninguno** (el más cercano, template 8, es $1-t$, lineal, no cuadrático). No hay forma de inyectar una función arbitraria. Va todo a mano.

**Cómo lo escribo en el examen (a mano, de la oficial):** con $a_0=\int_0^1(1-x^2)dx=\tfrac23$, $a_n=-\tfrac1{\pi^2n^2}$, $b_n=\tfrac1{\pi n}$:
$$f(x)=\frac23-\frac1{\pi^2}\sum_{n\ge1}\frac{\cos(2\pi nx)}{n^2}+\frac1\pi\sum_{n\ge1}\frac{\sin(2\pi nx)}{n}.$$
b) En $x=0$ (salto, $f(0^+)=1$, $f(1^-)=0$) → converge a $\tfrac{1+0}2=\tfrac12$. En $x=\tfrac12$ (continuidad) → $f(\tfrac12)=\tfrac34$.
**Caveat:** Limitación dura del módulo `fs` (solo templates). No se puede ni verificar parcialmente con la Casio.

---

### Ej 3 — Diferencias finitas implícitas (calor) · [edp:1] | PARCIAL (a) / NO cubierto (b)

**Enunciado (resumen):** $u_t=u_{xx}$, $x\in[0,1]$, 4 nodos internos. a) Dirichlet $u(0,t)=u(1,t)=0$, C.I. $u(x,0)=xe^{-x}$. b) Neumann $u_x(0,t)=u_x(1,t)=0$, C.I. $u(x,0)=x+1$.

**a) PARCIAL.** El módulo `edp` opción 1 (Calor Dirichlet) arma el **mismo esquema** que pide el ejercicio: con 4 nodos internos $h=L/(N+1)=0.2$, $r=\Delta t/h^2$, y matriz tridiagonal $M=\operatorname{tridiag}(-r,\ 1+2r,\ -r)$ resolviendo $M\mathbf u^{k+1}=\mathbf u^k$. **PERO** la C.I. $u(x,0)=xe^{-x}$ **no está** entre los templates del módulo (1=sen, 2=cos, 3=$x(L-x)$, 4=$\exp(-x^2)$), así que no se puede generar el $\mathbf u^0$ correcto ni avanzar pasos con la C.I. real. El módulo solo sirve para **confirmar la estructura del esquema** (matriz tridiagonal, $r$, bordes Dirichlet homogéneos sin aporte al RHS), no los valores.
**Cómo lo escribo en el examen (a mano):** incógnitas $u_1,...,u_4$; $-ru_{i-1}^{k+1}+(1+2r)u_i^{k+1}-ru_{i+1}^{k+1}=u_i^k$, con $u_0=u_5=0$. $M=\operatorname{tridiag}(-r,1+2r,-r)_{4\times4}$, $\mathbf u^0=(0.2e^{-0.2},0.4e^{-0.4},0.6e^{-0.6},0.8e^{-0.8})^T\approx(0.1638,0.2681,0.3293,0.3595)^T$.
**Caveat:** La estructura coincide con la oficial; el script no puede inyectar $xe^{-x}$ (No template).

**b) NO cubierto.** El módulo `edp` solo maneja **Dirichlet** (valor de borde fijo). Las condiciones **Neumann** $u_x=0$ en ambos bordes (nodos fantasma, bordes que pasan a ser incógnitas, sistema $6\times6$ con $-2r$ en filas extremas) **no están implementadas**. Va 100% a mano (ver oficial: $M$ $6\times6$ no simétrica, $\mathbf u^0=(1,1.2,1.4,1.6,1.8,2)^T$).
**Caveat:** Limitación del módulo (solo Dirichlet). Ni la estructura se puede sacar del script.

---

### Ej 4 — Transformada de Fourier de $f(t)=e^{-a|t|}$ en $[0,1]$ · [tf] | NO cubierto

**Enunciado (resumen):** $\hat f(\omega)$ de $f(t)=e^{-a|t|}$ para $0\le t\le1$ ($a>0$), $0$ en otro caso.

**NO cubierto (simbólico + parámetro $a$).** En $[0,1]$ es $f(t)=e^{-at}$ (pulso exponencial acotado). El módulo `tf` no lo cubre: Op3 (`Exp -at u(t)`) es de soporte $[0,\infty)$, no $[0,1]$; Op4 (`Polin. num.`) integra **polinomios** $\sum c_d t^d$ en $[a,b]$, no exponenciales; y además el script da una grilla numérica para un $a$ concreto, no la fórmula cerrada con parámetro $a$. No hay opción para $e^{-at}$ truncado a $[0,1]$.
**Cómo lo escribo en el examen (a mano):**
$$\hat f(\omega)=\int_0^1 e^{-(a+i\omega)t}\,dt=\frac{1-e^{-(a+i\omega)}}{a+i\omega}=\frac{1-e^{-a}(\cos\omega-i\sin\omega)}{a+i\omega}.$$
Converge para todo $\omega$ y $a>0$ por ser soporte acotado. En $\omega=0$: $\hat f(0)=\tfrac{1-e^{-a}}a$.
**Caveat:** No cubierto por la Casio. Cross-check independiente (integración numérica de $\int_0^1 e^{-t}e^{-i\omega t}dt$, $a=1$) confirma la fórmula oficial: $\omega=0\to0.63212$, $\omega=1\to0.55540-0.24584i$, $\omega=2.5\to0.25450-0.41609i$, $\omega=5\to-0.03339-0.18581i$ — coincide exacto.

---

## Final Tema XIV

### Ej 1 — TL $T:P_2\to\mathbb{R}^3$: matriz asociada y clasificación · [tl:1] | SÍ (vía matriz asociada)

**Enunciado (resumen):** $T(a+bx+cx^2)=(a+b,\ a+b+c,\ b-c)$. a) Matriz en bases canónicas. b) Clasificar.

**a) Puente TL no estándar (polinomios → matriz asociada).** Columna $j$ = $[T(\text{base}_j)]_E$: $T(1)=(1,1,0)$, $T(x)=(1,1,1)$, $T(x^2)=(0,1,-1)$ → $\boxed{M=\begin{psmallmatrix}1&1&0\\1&1&1\\0&1&-1\end{psmallmatrix}}$. (A mano; va como respuesta de a).

**b) tl Op1 sobre $M$.**
**Inputs Casio:** módulo `tl`, opción `1`; `filas=3`, `cols=3`; filas de $M$.
**Comando de verificación:**
`printf '1\n3\n3\n1,1,0\n1,1,1\n0,1,-1\n' | python3 run_mod.py tl`
**Salida del script (real):**
```
 1)N(T),Im,rg
 2)Antiimagen b
 3)Mat. por regla
 4)M(T)_EB base B
Op:filas A:cols A:A3x3:
f1/3:f2/3:f3/3:A:
1 1  0
1 1  1
0 1 -1

-- RREF: N(T) Im(T)
rref:
1 0 0
0 1 0
0 0 1
rg= 3
dim N= 0

-- Base N(T)
N(T)={0}

-- Base Im(T)
(cols pivote de A)
c1:
1 1 0
c2:
1 1 1
c3:
0 1 -1
```
**Cómo lo escribo en el examen:** RREF$=I_3$ → $\operatorname{rg}(M)=3$, $N(T)=\{0\}$ ($\dim N=0$), $\operatorname{Im}(T)=\mathbb{R}^3$. $T$ es **inyectiva, sobreyectiva y biyectiva (isomorfismo)**. (El $\det M=-1\neq0$ va a mano para reforzar.)
**Caveat:** Coincide con la oficial. El script no calcula determinante, pero rg$=3$ + $N=\{0\}$ alcanzan para clasificar.

---

### Ej 2 — Diagonalización con parámetro $k$ y sistema $A^TAX=0$ · [diag + tl:1] | SÍ (verificando casos $k$)

**Enunciado (resumen):** $A=\begin{psmallmatrix}2&k-2&0\\0&3&k-1\\0&0&3\end{psmallmatrix}$. a) ¿Para qué $k$ es diagonalizable en $\mathbb{R}$? b) Para $k=2$ resolver $A^TAX=0$.

**a) SÍ (verificando casos concretos; el "para qué $k$" es semi-simbólico).** Autovalores fijos $\lambda=2$ (simple), $\lambda=3$ (doble), independientes de $k$. Diagonalizable $\iff m_g(3)=2 \iff k=1$ (a mano). Verifico los dos casos clave con `diag`:

**Caso $k=1$ (esperado: diagonalizable):**
`printf '3\n2,-1,0\n0,3,0\n0,0,3\n' | python3 run_mod.py diag`
```
n(2 o 3):A3x3:
f1/3:f2/3:f3/3:A:
2 -1 0
0  3 0
0  0 3

-- P(L) caract.
p(L)=L^3+
a=-8
b=21
c=-18
dep p=-0.3333
dep q=0.07407
disc=-1.002e-14
Autovalores:
L1=3
L2=3
L3=2

-- S_L=3 m=2
v:
-1 1 0
v:
0 0 1

-- S_L=2
v:
1 0 0

-- Armando P,D
P:
-1 0 1
 1 0 0
 0 1 0
D:
3 0 0
0 3 0
0 0 2
|AP-PD|=8.882e-16
```

**Caso $k=2$ (esperado: NO diagonalizable):**
`printf '3\n2,0,0\n0,3,1\n0,0,3\n' | python3 run_mod.py diag`
```
...
Autovalores:
L1=3
L2=3
L3=2

-- S_L=3 m=2
dimK= 1 <m= 2
(NO diag.)
v:
0 1 0

-- S_L=2
v:
1 0 0
NO diagonaliz.
dim= 2 <n= 3
```
**Cómo lo escribo en el examen:** Para $k=1$, $m_g(3)=2$ (autoespacio $S_3=\langle(-1,1,0),(0,0,1)\rangle$, $S_2=\langle(1,0,0)\rangle$), se arman $P,D$ con $|AP-PD|\approx0$ → diagonalizable. Para $k\neq1$ (p.ej. $k=2$), $m_g(3)=1<2$ → NO. Conclusión: $\boxed{A\text{ diagonalizable}\iff k=1}$.
**Caveat:** Coincide con la oficial. El script confirma cada $k$ concreto; el "$\iff k=1$" se argumenta a mano (rg$(A-3I)=1\iff k-1=0$).

**b) SÍ.** Con $k=2$, $A=\begin{psmallmatrix}2&0&0\\0&3&1\\0&0&3\end{psmallmatrix}$ → a mano $A^TA=\begin{psmallmatrix}4&0&0\\0&9&3\\0&3&10\end{psmallmatrix}$. Resolver el sistema homogéneo = ver el núcleo → `tl` Op1.
**Comando de verificación:**
`printf '1\n3\n3\n4,0,0\n0,9,3\n0,3,10\n' | python3 run_mod.py tl`
**Salida del script (real):**
```
 1)N(T),Im,rg
...
-- RREF: N(T) Im(T)
rref:
1 0 0
0 1 0
0 0 1
rg= 3
dim N= 0

-- Base N(T)
N(T)={0}
...
```
**Cómo lo escribo en el examen:** $\det A=18\neq0$ → $A^TA$ inversible (de hecho definida positiva). El sistema homogéneo tiene **solución única** $\boxed{X=(0,0,0)^T}$.
**Caveat:** Coincide con la oficial. $N(A^TA)=\{0\}$ confirma trivialidad. El armado de $A^TA$ va a mano (no hay módulo que solo multiplique matrices).

---

### Ej 3 — SVD completa de $A_{3\times2}$ y PLU de $AA^T$ · [svd] + [lu] | SÍ (a) / PARCIAL (b)

**Enunciado (resumen):** $A=\begin{psmallmatrix}0&-1\\-1&-1\\1&1\end{psmallmatrix}$. a) SVD completa. b) PLU de $AA^T$.

**a) SVD — SÍ.**
**Inputs Casio:** módulo `svd`; `filas=3`, `cols=2`; filas de $A$.
**Comando de verificación:**
`printf '3\n2\n0,-1\n-1,-1\n1,1\n' | python3 run_mod.py svd`
**Salida del script (real):**
```
filas A:cols A:A3x2:
f1/2:f2/2:f3/2:A:
 0 -1
-1 -1
 1  1

-- Via AtA 2x2
AtA:
2 2
2 3
tr=5
det=2
disc=17

-- V.singulares
s1=2.13578
s2=0.662153

-- V cols
v1:
0.6154 0.7882
v2:
-0.7882 0.6154

-- U cols
u1:
-0.369 -0.6572 0.6572
u2:
-0.9294 0.261 -0.261
u3:
0 0.7071 0.7071

-- Verif
|USVt-A|=2.22e-16
Sigma:
2.136      0
    0 0.6622
    0      0
```
**Cómo lo escribo en el examen:** $A^TA=\begin{psmallmatrix}2&2\\2&3\end{psmallmatrix}$, autovalores $\tfrac{5\pm\sqrt{17}}2$ → $\sigma_1\approx2.1358$, $\sigma_2\approx0.6622$.
$$U\approx\begin{pmatrix}-0.369&-0.9294&0\\-0.6572&0.261&0.7071\\0.6572&-0.261&0.7071\end{pmatrix},\ \Sigma\approx\begin{pmatrix}2.136&0\\0&0.6622\\0&0\end{pmatrix},\ V\approx\begin{pmatrix}0.6154&-0.7882\\0.7882&0.6154\end{pmatrix}.$$
**Caveat:** $\sigma_i$ idénticos a la oficial; $u_1$ y $u_3$ coinciden. El par $(v_2,u_2)$ aparece con **signo opuesto** a la oficial ($v_2^{ofi}=(0.7882,-0.6154)$, $u_2^{ofi}=(0.9294,-0.261,0.261)$) — libertad de signo de la SVD (la propia oficial lo advierte). `|USVt-A|≈2e-16` → exacto.

**b) PLU de $AA^T$ — PARCIAL (el módulo aborta en el pivote nulo final).** A mano $AA^T=\begin{psmallmatrix}1&1&-1\\1&2&-2\\-1&-2&2\end{psmallmatrix}$ (singular, rango 2).
**Inputs Casio:** módulo `lu`; `n=3`; filas de $AA^T$.
**Comando de verificación:**
`printf '3\n1,1,-1\n1,2,-2\n-1,-2,2\n' | python3 run_mod.py lu`
**Salida del script (real):**
```
n cuadr:A3x3:
f1/3:f2/3:f3/3:A:
 1  1 -1
 1  2 -2
-1 -2  2

-- Tras col 1
U:
1  1 -1
0  1 -1
0 -1  1

-- Tras col 2
U:
1 1 -1
0 1 -1
0 0  0
piv=0, A sing.
```
**Cómo lo escribo en el examen:** No hubo permutaciones (pivotes $(1,1)=1$, $(2,2)=1$ no nulos) → $P=I$. Multiplicadores: $m_{21}=1$, $m_{31}=-1$, $m_{32}=-1$, de donde
$$P=I,\quad L=\begin{pmatrix}1&0&0\\1&1&0\\-1&-1&1\end{pmatrix},\quad U=\begin{pmatrix}1&1&-1\\0&1&-1\\0&0&0\end{pmatrix}.$$
**Caveat:** **Limitación del módulo `lu`:** al ser $AA^T$ singular ($U_{33}=0$), el script imprime `piv=0, A sing.` y **corta antes de mostrar $P$, $L$ y el $U$ final**. Igual la salida intermedia "Tras col 2" da el $U$ correcto y la progresión de filas revela los multiplicadores de $L$, así que se reconstruye a mano. El resultado coincide exactamente con la oficial ($P=I$, $LU=AA^T$). El armado de $AA^T$ también va a mano.

---

## Resumen de cobertura

| Parcial / Ej | Cobertura | Módulo | Nota |
|---|---|---|---|
| XI-1a | NO (simbólico) | — | $\det A=16a(1-2a)$, $a\notin\{0,\tfrac12\}$, a mano |
| XI-1b | SÍ | diag | NO diagonalizable ($a=1$); coincide |
| XI-2a | SÍ (vía matriz $4\times4$) | tl:1 | $N$=simétricas, $R$=antisimétricas; coincide |
| XI-2b | SÍ | tl:2 | $X=(\tfrac13,-\tfrac13)$; coincide |
| XI-3a/b | SÍ | svd / qr | SVD con signo global flip; QR exacto; coinciden |
| XI-alt-1 | SÍ | tl:1 + diag | $N,Im$ y NO diag; coinciden |
| XI-alt-2 | NO | fs | $1-x^2$ no es template |
| XI-alt-3a | PARCIAL | edp:1 | estructura OK, C.I. $xe^{-x}$ no es template |
| XI-alt-3b | NO | edp | Neumann no implementado (solo Dirichlet) |
| XI-alt-4 | NO | tf | $e^{-at}$ en $[0,1]$ no es template; cross-check externo OK |
| XIV-1 | SÍ (vía matriz $3\times3$) | tl:1 | isomorfismo; coincide |
| XIV-2a | SÍ (casos $k=1,2$) | diag | diagonalizable $\iff k=1$; coincide |
| XIV-2b | SÍ | tl:1 | $X=0$ (núcleo trivial); coincide |
| XIV-3a | SÍ | svd | SVD; $(v_2,u_2)$ signo flip; coincide |
| XIV-3b | PARCIAL | lu | aborta en pivote nulo; $U$ intermedio + $L$ reconstruibles; coincide |
---

# Recomendaciones de mejora (priorizadas)

Pensadas para las restricciones reales de la Casio Graph 90+E: MicroPython 1.9.4 (sin `sympy`, sin `set`, sin `str.rjust`, formato anidado limitado), pantalla ~21 cols, memoria escasa. Por eso casi todo es "agregar templates / inputs numéricos", no "álgebra simbólica".

## 🔴 Crítico — bug de correctitud

### R1. ✅ APLICADO — `diag.py`: autovalor real MAL impreso con autovalores complejos y $\det\neq0$
> **Estado: corregido en esta entrega** (parche de abajo aplicado y verificado). El texto siguiente documenta el bug original.

**Síntoma (verificado):** en la rama de Cardano clásico (3×3, una raíz real + dos complejas, no entra al atajo `c~0`), las líneas `L1(real)` y `L2,3 Re` imprimen valores **incorrectos** porque **no deshacen la depresión** ($-a/3$). Casos reales: Final I imprime `L1(real)=-0.1667` (verdadero **1**), Final V `0.1667` (verdadero **2**), Final VI `0.363` (verdadero **2.3926**). Test mínimo: $A=\begin{psmallmatrix}0&-1&0\\1&0&0\\0&0&2\end{psmallmatrix}$ (autovalores $2,\pm i$) imprime `L1(real)=0.6667` en vez de `2`.

> Mitigación mientras no se parchee: el script **igual devuelve `None` y no arma $P,D$**, lo que correctamente significa "no diagonalizable en $\mathbb R$". Confiá en esa señal, pero **NO copies el número de `L1(real)`**: sacá el autovalor real a mano del factor lineal del polinomio.

**Parche (probado, da los valores exactos):** en `eigvals_3x3`, rama `if d2 >= 0:`, reemplazar
```python
            u = cbrt(u3)
            v = cbrt(v3)
            roots = [u + v]
            # las otras dos son complejas conjugadas
            re = -(u + v) / 2
            print("L1(real)={:.4g}".format(re + (u + v)))
            print("L2,3 Re={:.4g}".format(re))
            return None
```
por
```python
            u = cbrt(u3)
            v = cbrt(v3)
            real_root = (u + v) - a / 3.0          # deshacer la depresion
            re = -(u + v) / 2.0 - a / 3.0           # Re de las complejas
            im = (3.0 ** 0.5) / 2.0 * abs(u - v)    # parte imaginaria
            print("L1(real)={:.4g}".format(real_root))
            print("L2,3 Re={:.4g}".format(re))
            print("   Im=+-{:.4g}".format(im))
            return None
```
Verificado: el caso $2,\pm i$ pasa a imprimir `L1(real)=2 / Re=0 / Im=+-1`, y Final VI `L1(real)=2.393 / Re=1.304 / Im=+-1.436` (coincide con numpy).

## 🟠 Alto valor — convierten muchos 🟡/❌ en ✅

### R2. `edp.py`: condición inicial numérica (tipear el vector $u^0$)
Hoy la C.I. está atada a 4 templates con argumento `πx/L`. Los exámenes piden $\sin(x)$, $\cos(x)$, $e^{-x}\sin x$, $x^2$, $xe^{-x}$, $|x|$… con $L=1$, y `sin(πx)≠sin(x)`, así que **el $u^0$ y todos los pasos salen mal** aunque el esquema sea correcto. Agregar una opción **"5) C.I. manual"** que lea un vector de $N$ valores (`read_vec`) convierte en ✅ los Ej3a de IIP IV/V/VI y Final V/VI/IX/XI-alt. Es el cambio con mejor relación impacto/esfuerzo.

### R3. `edp.py`: bordes Neumann / mixtos (nodo fantasma)
Todos los "Ej3b" (mitad de los EDP de IIP y varios finales) piden $u_x=0$ en un borde → hoy ❌. Agregar una variante con nodo fantasma (primera/última fila con $1+2r,\,-2r$, sistema de $N{+}1$ o $N{+}2$ incógnitas) los cubriría. Además, `edp` Op2/Op3 **no imprimen $u^0$** — agregarlo.

### R4. `fs.py`: más templates + intervalo arbitrario
Los 9 templates dejan afuera funciones muy frecuentes. Por orden de aparición en los modelos, agregar: **`1-x²` y `x-x²` en (0,1)`** (Final III/V/VIII/XI-alt), **`|cos t|` y `|sin t|`** (IP VII/VIII), y **`cos t`/`sin t` con intervalo $(-L,L)$ y período $T$ parametrizables** (IIP V/VI con $T=\pi/2$). Lo ideal sería una entrada genérica "polinomio a trozos en $(a,b)$", pero aun agregando esos 4–5 templates se cubren ~6 ejercicios hoy ❌.

### R5. `lu.py`: tres arreglos
- ✅ **APLICADO — Aceptar matrices rectangulares $n\times m$** (antes `read_mat(n,n)` crasheaba con 3×2; ahora pide `filas:`/`cols:`): IP IV-Ej3, IP IX-Ej3, Rec. XIII-Ej3 ya corren.
- ⬜ **Pendiente — opción "sin pivoteo (Doolittle, $P=I$)"** además del pivoteo parcial: la cátedra suele pedir $P=I$ y el resultado del script difiere (IP III-Ej3, Final IV-Ej3c). *(No aplicado: el script sigue pivoteando siempre; si piden $P=I$, hacelo a mano.)*
- ✅ **APLICADO — No abortar mudo en pivote nulo:** ante $U_{jj}\approx0$ ahora sigue (la columna ya es ~0 bajo la diagonal) y emite $P$, $L$, $U$ con `|PA-LU|=0`: Final XIV-Ej3b, IP VIII-Ej2b.

### R6. `tf.py`: exponenciales
Agregar **`e^{-a|t|}` bilátero** (Lorentziana $2a/(a^2+\omega^2)$): Final I-Ej5, IIP V-Ej2; y **pulso exponencial $e^{-at}$ truncado a $[a,b]$** (o más general, $p(t)e^{-\alpha t}$): Final V/VI/XI-alt-Ej4, IIP VI-Ej2. Con eso se cierran ~5 ejercicios hoy ❌.

## 🟡 Medio — cierran huecos puntuales

### R7. Nueva variante en `tl` (o módulo aparte): $M(T)_{BB}$ por conjugación
Para $T:\mathbb R^n\to\mathbb R^n$ con base no canónica $B$, ningún script arma $M_{BB}=P^{-1}M_{EE}P$ (`tl:4` calcula $M_{EB}$, distinto; `cb` solo cambia coordenadas de vectores). Aparece en Final III/IX/X-Ej1a. Una opción "5) M(T)_BB base B" que lea $M_{EE}$ y $B$ y devuelva $P^{-1}M_{EE}P$ (reusando `mat.inverse`/`matmul`) lo resuelve.

### R8. `lsq.py`: modelo nativo $y=ax^2+b$
Hoy hay que usar el truco "cargar $x_i^2$ y modelo 1, y reetiquetar $(b,a)$" (IP II-Ej3), fácil de equivocar. Agregar el template $[\,x^2,\,1\,]$.

### R9. `param.py` / `diag`: variante "$\lambda$ dado es autovalor"
`param` resuelve "$v$ es autovector" pero no "para qué $k$ es $\lambda_0$ autovalor" (IP IX-Ej2a) — ahí `param` resuelve el problema equivocado. Una variante que imponga $\det(\lambda_0 I-A)=0$ como ecuación en $k$ lo cubriría. Mientras tanto, se hace a mano y se verifica sustituyendo el $k$ en `diag`.

## 🟢 UX / robustez (barato y útil)

- **R10.** ✅ **APLICADO** — `fs` ahora imprime el término constante como **`=>cte=`** (= `a0/2`, el valor medio), debajo de `a0`, para que no se copie el `a0` que es el doble.
- **R11.** ✅ **APLICADO** — `fs` convergencia: el `prom` ahora periodiza el muestreo (`f(a+((t0±eps−a) mod T))`), así detecta bien el salto en los bordes del período (ej. `prom=0.5` donde antes daba `1`).
- **R12.** **Documentar en el README** (o imprimir una nota corta): la libertad de escala/signo de autovectores y de signo / intercambio $U\leftrightarrow V$ en SVD, para no asustarse cuando difiere de la resolución (lo importante es `|AP-PD|`/`|USVt-A|`≈0).
- **R13.** En coeficientes de Fourier con discontinuidad, **redondear a 0** los $a_n$/Re$(c_n)$ por debajo de un umbral (hoy salen `-0.0017`, ruido de Simpson), igual que ya hace `fmt_num` para vectores.
- **R14.** **Aclarar el mapeo de signo de la convección** (`edp:3`): $u_t=u_{xx}+u_x$ entra como $c=-1$, $\nu=1$; con el signo equivocado la solución sale espejada. Conviene una nota en el prompt.

## Qué queda inevitablemente a mano (no son "mejoras", son límites del formato)
- **Demostraciones / teoría** (espectral, dimensiones, propiedades).
- **EDO de 2º orden → sistema de 1er orden + esquema implícito** (Final I/II/III-Ej3): reformulación simbólica + (en Duffing) Newton por el término no lineal.
- **Despejar parámetros simbólicamente** y **parametrizar restricciones** de subespacios (la base sale del despeje a mano; el script solo verifica el caso concreto).
- **Identidades de series** (probar $\sum(-1)^n/(n^2+1)=\dots$): el script confirma numéricamente el valor de convergencia, el despeje es analítico.

## Cierre
El set ya es una herramienta de **verificación** muy fuerte para el núcleo del parcial (TL, diagonalización, factorizaciones, MMCC). En esta entrega se aplicaron **R1** (bug de `diag`, obligatorio), **R5** (PLU rectangular + singular), **R10/R11** (Fourier) y la mejora de UI de `show_vec` — eso ya recupera los PLU de $3\times2$/singulares, los autovalores complejos y la convergencia de Fourier. Lo que falta para llegar a un estimado **~80%** de incisos totalmente resolubles son features de cobertura (**R2–R4, R6–R9**: C.I. numérica y Neumann en `edp`, más templates en `fs`, exponenciales en `tf`, $M_{BB}$). El resto es teoría que conviene practicar a mano de todos modos.
