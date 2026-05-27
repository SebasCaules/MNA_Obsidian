# Scripts MNA — Casio fx-CG50 / fx-9750GIII

Conjunto de scripts MicroPython para resolver mecánicamente los ejercicios típicos del parcial central de MNA (ITBA).

## Cómo transferir a la calculadora

1. Conectar la calc por USB. En la calc: `MENU → LINK → F4 (CABLE)`.
2. En la PC se monta como pendrive. Copiar TODOS los `.py` (incluyendo `main.py`) a la raíz o a `PYTHON/`.
3. Desconectar (eject seguro).
4. En la calc: `MENU → PYTHON → seleccionar main → EXE`.

## Uso

Correr `main.py` — abre un menú con 12 herramientas. Tipear el número y Enter.

Cada herramienta:
- Pide entradas **fila por fila** (CSV: `1,2,3` Enter).
- Muestra **pasos intermedios** (cada paso = una pantalla, Enter para avanzar).
- Imprime el resultado final + verificación numérica.

## Inventario

| # | Archivo | Para qué sirve | Receta |
|---|---------|---------------|--------|
| 1 | `tl.py` | TL: núcleo, imagen, antiimagen, matriz por regla | R1 |
| 2 | `diag.py` | Diagonalización 2×2/3×3 (Cardano + autovec por Gauss) | R2 |
| 3 | `cb.py` | Cambio de base $M_{B_2 B_1}(\text{id})$ + coordenadas | R3 |
| 4 | `lu.py` | Factorización PA = LU (Doolittle + pivoteo parcial) | R4 |
| 5 | `qr.py` | QR por Gram-Schmidt clásico con todos los pasos | R5 |
| 6 | `svd.py` | SVD vía $A^TA$ con autoval, autovec, $U$, $V$ | R6 |
| 7 | `pinv.py` | Pseudoinversa Moore-Penrose | R7 |
| 8 | `lsq.py` | Cuadrados mínimos: 5 modelos pre-cargados | R8 |
| 9 | `cplx.py` | Complejos: binómica↔polar, raíces, potencias | — |
| 10 | `fs.py` | Series de Fourier: 9 funciones pre-cargadas + custom | R9 |
| 11 | `tf.py` | TF: pares estándar + pulso polinómico numérico | R10 |
| 12 | `edp.py` | EDPs diferencias finitas: calor / onda / convección | R11 |

## Convenciones de entrada

- **Vector**: `1, 2, 3` (separar con coma).
- **Matriz**: una fila por línea, mismo formato.
- **Decimales**: punto, no coma. `1.5`, no `1,5`.
- **Fracciones**: no soportadas como entrada directa. Convertir: `1/3` → `0.3333`.

## Limitaciones

- Sin `numpy` → toda álgebra implementada a mano en `mat.py`.
- Matrices máximo prácticas: 4×4. La SVD pelea con 4×4 pero anda.
- Polinomio cúbico (3×3 diagonalización): asume autovalores reales. Si caen complejos avisa pero no resuelve.
- Series de Fourier: usa **integración numérica Simpson** con 400 paneles. Suficiente para 4 decimales en los templates incluidos. Para funciones con discontinuidades el error puede ser mayor cerca del salto.
- EDPs: implementadas ec. del calor con Dirichlet, onda con $u_t(x,0)=0$, y convección-difusión con Dirichlet. Si el parcial pide Neumann o BC mixtas, hay que adaptar la primera/última fila de la matriz tridiagonal a mano.

## Tests rápidos (verificar instalación)

Al cargar `main.py`:

1. **Diagonalización**: cargar `[[4,0,0],[3,-2,3],[3,-6,7]]` (clase 30/04 Ej. 2). Debería dar $\lambda \in \{1, 4, 4\}$, $S_4 = \langle(2,1,0),(0,1,2)\rangle$, $S_1=\langle(0,1,1)\rangle$.

2. **QR**: cargar $A = \pmat{1&1\\0&1\\1&0}$. Debería dar $R = \pmat{\sqrt 2 & 1/\sqrt 2 \\ 0 & \sqrt{3/2}}$ ≈ `[[1.414, 0.707], [0, 1.225]]`.

3. **MMCC**: puntos $(0,1),(\pi/2,0),(\pi,-1)$ con modelo `y = a cos x + b sen x`. Debería dar $a=1, b=0$.

## Estrategia para el parcial

1. Hacer cada ejercicio **primero a mano** en el papel.
2. Si te trabás o el resultado parece raro, abrir el script correspondiente y cargarle los mismos datos.
3. Comparar tu cuenta con la del script paso por paso. El script imprime todos los intermedios (autovalores, $u_i$ antes de normalizar, $\langle a, v\rangle$, etc.), así que podés ubicar dónde te equivocaste.
4. NO copiar el resultado del script — el examen se corrige por proceso, no por número final. Pero verificar con el script te ahorra perder puntos por errores aritméticos.
