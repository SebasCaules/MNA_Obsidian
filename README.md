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
  casio/               # Scripts MicroPython para fx-CG50 / fx-9750GIII
    main.py, mat.py, io_util.py
    tl.py diag.py cb.py lu.py qr.py svd.py pinv.py lsq.py
    cplx.py fs.py tf.py edp.py
    README.md (cómo transferir a la calc)

CLAUDE.md        # Schema del wiki (workflows ingest/query/lint)
```

## Cómo se usa

1. **Estudio rápido**: abrir `study/MNA_Cheatsheet.html` en un browser → `Cmd+P` para imprimir o leer en pantalla. 12 recetas con ejercicios resueltos.
2. **Drill mecánico con la calc**: transferir `study/casio/*.py` al fx-CG50 (modo USB), correr `main.py`. Verificar ejercicios a mano contra el script.
3. **Profundizar un tema**: ir a `wiki/00-mapa-temas.md` → ubicar el tema → seguir los links a teoría / clase / pizarrón / guía / parcial correspondiente.
4. **Agregar fuente nueva**: dropear PDF en `raw/`, pedirle a Claude "ingestar X". Se actualiza el wiki automáticamente.

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
git sparse-checkout set study/casio
ls study/casio/        # main.py, mat.py, io_util.py + 12 módulos + README.md
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
3. En la PC la calc aparece como pendrive. Arrastrar todo el contenido de la carpeta `study/casio/` a la raíz del pendrive (o a una subcarpeta `PYTHON/`).
4. Eject seguro. Desconectar.
5. En la calc: `MENU → PYTHON → seleccionar main → EXE`.

## Stats

- 70 PDFs en `raw/` (~3 MB total)
- 73 páginas markdown en `wiki/` (auditoría 2026-05-27 ✅ cero gaps críticos)
- 17 archivos Python en `study/casio/` (1.5K líneas)
- Cheatsheet HTML 1.7K líneas, A4 imprimible ~30 páginas
