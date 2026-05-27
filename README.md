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

## Stats

- 70 PDFs en `raw/` (~3 MB total)
- 73 páginas markdown en `wiki/` (auditoría 2026-05-27 ✅ cero gaps críticos)
- 17 archivos Python en `study/casio/` (1.5K líneas)
- Cheatsheet HTML 1.7K líneas, A4 imprimible ~30 páginas
