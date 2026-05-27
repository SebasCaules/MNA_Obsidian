# MNA Obsidian — Wiki schema

Personal knowledge base for **Métodos Numéricos Avanzados** (ITBA, 2026 1C).
Built on the LLM Wiki pattern: the user curates sources in `raw/`; Claude builds and maintains `wiki/`.

## Layout

```
raw/                          # source of truth — never modify, only read
  Teoricas/
    Anotaciones_Clases/       # class notes (handwritten scans, markdown, etc.)
    Slides/                   # lecture slides (pdf)
  Practicas/
    Ejercicios_Resueltos/     # solved exercises
    Guias_TP2026/             # problem set guides for this term
    Pizarrones/               # whiteboard photos
    Modelos_Examenes/         # past exams

wiki/                         # Claude-owned — generated pages
  index.md                    # catalog of all wiki pages
  log.md                      # append-only chronological log
  ...                         # topic, concept, method, exercise pages (TBD)
```

Wiki structure is **not pre-decided**. Once enough material lands in `raw/`, organize the wiki around the actual topics that show up (e.g. SVD, PCA, iterative methods, FFT, optimization — whatever the course covers). Don't over-engineer the structure up front.

## Workflows

### Ingest
When the user drops new files in `raw/` and asks to ingest:
1. Read the source(s).
2. Briefly discuss key takeaways with the user before writing.
3. Create/update wiki pages: topic pages, method pages, worked-example pages.
4. Cross-link with `[[wiki-link]]` style.
5. Update `wiki/index.md`.
6. Append a line to `wiki/log.md`: `## [YYYY-MM-DD] ingest | <source name>` + 1-line summary.

### Query
When the user asks a question:
1. Read `wiki/index.md` first to locate relevant pages.
2. Read those pages; drill into `raw/` only if the wiki is insufficient.
3. Answer with citations to wiki pages (and raw sources when relevant).
4. If the answer is non-trivial and reusable, offer to file it as a new wiki page.

### Lint
On request, health-check the wiki: contradictions, stale claims, orphan pages, missing cross-references, concepts mentioned without their own page, gaps worth filling.

## Conventions

- **Language**: Spanish (course is in Spanish). Math in LaTeX (`$...$`, `$$...$$`).
- **Filenames**: kebab-case, descriptive (`descomposicion-svd.md`, not `svd1.md`).
- **Links**: Obsidian-style `[[page-name]]`.
- **Frontmatter** (optional, add when useful for Dataview):
  ```yaml
  ---
  tags: [teoria, svd]
  fuentes: [clase-03, slides-cap2]
  ---
  ```
- **Log entries**: always start with `## [YYYY-MM-DD] <op> | <subject>` so they're greppable.

## Current state

Empty wiki. Waiting for the user to populate `raw/`.
