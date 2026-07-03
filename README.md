# MNA — Wiki + cheatsheet + scripts Casio

Material de estudio para **Métodos Numéricos Avanzados** (ITBA, 26-1C), construido sobre el patrón [LLM Wiki](https://github.com/karpathy/llm-wiki-pattern).

## Estructura

```
raw/             # Fuentes inmutables (PDFs de cátedra)
  Teoricas/
    Anotaciones_Clases/   # 9 tar.gz con scans/anotaciones
    Slides/               # 4 PDFs (Unidad I y II)
  Practicas/
    Ejercicios_Resueltos/ # 6 PDFs con resoluciones
    Guias_TP2026/         # 9 guías TP
    Modelos_Examenes/     # 30 modelos (IP + IIP + Final + recup)
    Pizarrones/           # 10 fotos de pizarrón

wiki/            # Generado a partir de raw/ (Claude-owned)
  index.md, log.md, AUDIT_REPORT.md, 00-mapa-temas.md
  teoria/        # 4 páginas — Unidad I, vectores, matrices, det
  clases/        # 9 páginas cronológicas (12 mar → 14 may)
  pizarrones/    # 10 transcripciones
  guias/         # 9 guías con todos los enunciados
  resueltos/     # 6 archivos con resoluciones paso a paso
  parciales/     # 30+ exámenes + patrones.md (análisis transversal)

study/           # Entregables para estudiar
  MNA_Cheatsheet.html  # Guía imprimible A4 con 12 recetas + 8 ejs resueltos
  acasios/             # Scripts MicroPython para fx-CG50 / fx-9750GIII
    main.py, mat.py, io_util.py
    tl.py diag.py cb.py lu.py qr.py svd.py pinv.py lsq.py
    cplx.py fs.py tf.py edp.py
    README.md (cómo transferir a la calc)

CLAUDE.md        # Schema del wiki (workflows ingest/query/lint)
```

## Cómo se usa

1. **Estudio rápido**: abrir `study/MNA_Cheatsheet.html` en un browser → `Cmd+P` para imprimir o leer en pantalla. 12 recetas con ejercicios resueltos.
2. **Drill mecánico con la calc**: transferir `study/acasios/*.py` al fx-CG50 (modo USB), correr `main.py`. Verificar ejercicios a mano contra el script.
3. **Profundizar un tema**: ir a `wiki/00-mapa-temas.md` → ubicar el tema → seguir los links a teoría / clase / pizarrón / guía / parcial correspondiente.
4. **Agregar fuente nueva**: dropear PDF en `raw/`, pedirle a Claude "ingestar X". Se actualiza el wiki automáticamente.

### Scripts Casio: inputs documentados (prompts exactos)

Convenciones: `read_mat(r,c,"A")` imprime `A<r>x<c>:` (ej. `A3x2:`) y luego pide cada fila con `f1/<c>:`, `f2/<c>:`, ...; `read_vec(n,"v")` pide `v<n>:` (ej. `v3:`). Todos los vectores son CSV con punto decimal.

| Archivo | Prompts (en orden) |
|---|---|
| `main.py` | 1) `Op(0=fin):` si hay una sola pagina, o `Op(0=fin n=pgX):` si hay varias.<br>2) `n` o Enter vacio = siguiente pagina; numero = ejecutar modulo; `0` = salir. |
| `tl.py` | 1) Menu de variantes, prompt `Op:`.<br>2) Variante 1: `filas A:`, `cols A:`, `A<r>x<c>:` y filas `f1/<c>:`, ...<br>3) Variante 2: `filas A:`, `cols A:`, `A<r>x<c>:` y filas `f1/<c>:`, ...; luego `b<r>:`.<br>4) Variante 3: `dim dom:`, `dim cod:`, luego `T(e1)<m>:`, `T(e2)<m>:`, ... hasta `T(en)<m>:`. |
| `diag.py` | 1) `n(2 o 3):`.<br>2) `A<n>x<n>:` y filas `f1/<n>:`, `f2/<n>:`, ... |
| `cb.py` | 1) `dim:`.<br>2) `B1<n>x<n>:` y filas `f1/<n>:`, ...<br>3) `B2<n>x<n>:` y filas `f1/<n>:`, ...<br>4) `v(can)<n>:`. |
| `lu.py` | 1) `n cuadr:`.<br>2) `A<n>x<n>:` y filas `f1/<n>:`, ... |
| `qr.py` | 1) `filas A:`.<br>2) `cols A:`.<br>3) `A<r>x<c>:` y filas `f1/<c>:`, ... |
| `svd.py` | 1) `filas A:`.<br>2) `cols A:`.<br>3) `A<r>x<c>:` y filas `f1/<c>:`, ... |
| `pinv.py` | 1) `filas:`.<br>2) `cols:`.<br>3) `A<r>x<c>:` y filas `f1/<c>:`, ... |
| `lsq.py` | 1) `#ptos:`.<br>2) Para cada punto i: prompt `p{i}2:` (ej. `p12:`) con `x,y` en una linea.<br>3) Seleccion de modelo con prompt `>`. |
| `cplx.py` | 1) Menu de variantes, prompt `Op:`.<br>2) Bin->polar: `a:`, `b:`.<br>3) Polar->bin: `rho:`, `th(rad):`.<br>4) Raices: `Re(z):`, `Im(z):`, `n:`.<br>5) Potencia: `a:`, `b:`, `n:`. |
| `fs.py` | 1) Menu de variantes, prompt `Op:`.<br>2) Seleccion de template con prompt `>`.<br>3) Coef trig: `#arm:`.<br>4) Coef exp: `|n|max:`.<br>5) Convergencia: `t0:`, `#arm suma:`. |
| `tf.py` | 1) Menu de variantes, prompt `Op:`.<br>2) Rect: `a(|t|<a/2):`, `w_max:`.<br>3) Tri: `n([-n,n]):`, `w_max:`.<br>4) Exp: `a(>0):`, `w_max:`.<br>5) Polin. num.: `grado(0-3):`, luego `c0:`, `c1:`, ... `cd:`; despues `a inf:`, `b sup:`, `w_max:`. |
| `edp.py` | 1) Menu de variantes, prompt `Op:`.<br>2) Calor: `L:`, `nodos int:`, `dt:`, `#pasos:`, init con prompt `>`, `u(0,t):`, `u(L,t):`.<br>3) Onda: `L:`, `nodos int:`, `dt:`, `#pasos:`, init con prompt `>`.<br>4) Conv-difus: `L:`, `nodos int:`, `dt:`, `#pasos:`, `c vel:`, `nu dif:`, `u(0,t):`, `u(L,t):`. |
| `io_util.py` | Define los prompts usados: `ask_int(prompt)` (default `n:`), `ask_float(prompt)` (default `x:`), `read_vec(n,prompt)` (prompt `prompt<n>:`), `read_mat(r,c,prompt)` (muestra `prompt<r>x<c>:` y pide `f1/<c>:`, ...). |
| `mat.py` | No pide inputs. |

## Descargar a tu computadora

El repo es **privado** → git necesita auth. Configuración una sola vez:

```bash
# si nunca usaste gh, instalalo y logueate (deja el token en el keychain)
brew install gh && gh auth login
gh auth setup-git              # le dice a git que use ese token
```

(Alternativa sin `gh`: configurar SSH con `ssh-keygen` y subir la pubkey a GitHub, y usar `git@github.com:SebasCaules/MNA_Obsidian.git` en los comandos de abajo.)

### Clonar todo el repo (recomendado)

```bash
git clone https://github.com/SebasCaules/MNA_Obsidian.git
cd MNA_Obsidian
```

Para actualizarlo después: `git pull` desde la carpeta.

### Bajar solo los scripts Casio (sparse-checkout)

```bash
git clone --depth 1 --filter=blob:none --sparse \
  https://github.com/SebasCaules/MNA_Obsidian.git MNA_casio
cd MNA_casio
git sparse-checkout set study/acasios
ls study/acasios/        # main.py, mat.py, io_util.py + 12 módulos + README.md
```

Te deja un repo livianito con solo los 17 archivos `.py` + el README. Cuando quieras actualizar: `git pull`.

### Bajar solo el cheatsheet HTML

```bash
git clone --depth 1 --filter=blob:none --sparse \
  https://github.com/SebasCaules/MNA_Obsidian.git MNA_html
cd MNA_html
git sparse-checkout set study/MNA_Cheatsheet.html
open study/MNA_Cheatsheet.html   # se abre en tu browser default
```

### Bajar solo el wiki (markdown) para consulta offline

```bash
git clone --depth 1 --filter=blob:none --sparse \
  https://github.com/SebasCaules/MNA_Obsidian.git MNA_wiki
cd MNA_wiki
git sparse-checkout set wiki
```

Abrilo con Obsidian (`File → Open vault → MNA_wiki`) o con cualquier editor de markdown.

### Transferir los scripts a la Casio fx-CG50

1. Conectar la calculadora por USB.
2. En la calc: `MENU → LINK → F4 (CABLE)` → elegir "USB Mass Storage".
3. En la PC la calc aparece como pendrive. Arrastrar todo el contenido de la carpeta `study/acasios/` a la raíz del pendrive (o a una subcarpeta `PYTHON/`).
4. Eject seguro. Desconectar.
5. En la calc: `MENU → PYTHON → seleccionar main → EXE`.

## Stats

- 70 PDFs en `raw/` (~3 MB total)
- 73 páginas markdown en `wiki/` (auditoría 2026-05-27 ✅ cero gaps críticos)
- 17 archivos Python en `study/acasios/` (1.5K líneas)
- Cheatsheet HTML 1.7K líneas, A4 imprimible ~30 páginas
