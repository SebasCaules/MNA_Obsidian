# Scripts MNA — Casio fx-CG50 / fx-9750GIII

Conjunto de scripts MicroPython optimizados para la pantalla y memoria de la Casio (MicroPython 1.9.4). Resuelven los temas centrales de la cursada de Métodos Numéricos Avanzados (ITBA).

## Estructura

```
acasios/
  main.py        # punto de entrada (este es el que se ejecuta)
  io_util.py     # IO + captura de salida
  mat.py         # algebra de matrices
  diag.py        # diagonalizacion (dependencia base)
  ...            # resto de los modulos (cb, lu, qr, svd, ...)
  README.md
```

> **Importante**: todos los `.py` van **juntos en una misma carpeta**, sin subcarpetas. La app PYTHON de la Casio **no importa desde subcarpetas** (los `import` son planos), así que tienen que estar todos al mismo nivel.

## Instalación y Transferencia

1. **Conexión**: En la calculadora, ir a `MENU → LINK → F4 (CABLE) → F1 (USB Flash)`. Conectar a la PC.
2. **Copia**: Copiar TODOS los `.py` **juntos en una misma carpeta** (raíz o `PYTHON/`) de la unidad montada. **Es fundamental incluir `main.py`, `mat.py`, `io_util.py` y `diag.py`**, ya que son las dependencias base. NO uses subcarpetas: la Casio no importa desde ellas.
3. **Ejecución**: En la calculadora, ir a `MENU → PYTHON`, seleccionar **`main.py`** y presionar `F1 (EXE)`.

## Uso del Menú Principal

El script `main.py` centraliza todas las funciones en un menú paginado. 
- Al arrancar pregunta **`ej(1-5):`** → el número de ejercicio del parcial que estás resolviendo. Solo acepta `1`–`5`; define el nombre del archivo de salida (`ej1.py` … `ej5.py`).
- Tipear el **número** de la opción y presionar **EXE**.
- Para cambiar de página (si hay más de 6 opciones), presionar **EXE** sin escribir nada o escribir `n`.
- **Importante**: Al terminar un ejercicio, el script se detiene para permitir el **scroll vertical** y revisar los pasos. Para iniciar otro, ejecutar `main` nuevamente.

### Guardado de la resolución (`ejN.py`)
Al finalizar, **toda la salida** del ejercicio se vuelca a un archivo `ejN.py` (donde `N` es el número que ingresaste) **afuera de la carpeta de los scripts** (`../`; si el sistema de archivos no lo permite, lo deja al lado). El script imprime `guardado: <ruta>` para confirmar.

- **Para qué**: la *shell* solo scrollea vertical y corta a 21 columnas; en cambio el **editor de Python** (`MENU → PYTHON`, abrir `ejN.py`) scrollea **izquierda/derecha**, así revisás la resolución cómodo.
- El archivo es solo texto para **visualizar** (empieza con `# Ej N - <técnica>`): **no es Python válido**, no intentes ejecutarlo.
- Si volvés a hacer el **mismo** número de ejercicio, `ejN.py` se **sobrescribe**.
- ⚠️ La escritura de archivos depende del OS de la Casio. **Verificá en la calculadora real** que aparezca `guardado:` y que el archivo se vea en el menú PYTHON; el cálculo en pantalla funciona igual aunque el guardado falle.

## Guía de Entradas (Inputs)

### Formatos Obligatorios
- **Vectores**: Se ingresan en una línea separando valores por comas (ej: `1, -0.5, 2`).
- **Matrices**: La calculadora pedirá las filas una por una. Ingresar cada fila como un vector (ej: `Fila 1: 1,0,0`).
- **Decimales**: Usar exclusivamente el punto (`.`). La coma (`,`) se reserva para separar elementos.
- **Fracciones**: Resolver la división antes (ej: para $1/3$ ingresar `0.3333`).

---

## Referencia de Módulos con Ejemplos Concisos

### 1. TL (`tl.py`)
*   **Para qué sirve**: Núcleo, imagen, rangos, antiimágenes $A x = b$, matriz por regla, y **TL con matriz en base no canónica** ($M(T)_{EB}$). Menú interno con 4 variantes.
*   **Ejemplo (Antiimagen)**: Resolver $A x = b$ para $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ y $b = \begin{pmatrix} 5 \\ 11 \end{pmatrix}$.
    *   *Inputs*: `Op:` $\rightarrow$ `2`. `filas A:` $\rightarrow$ `2`, `cols A:` $\rightarrow$ `2`. `f1/2:` $\rightarrow$ `1,2`, `f2/2:` $\rightarrow$ `3,4`. `b2:` $\rightarrow$ `5,11`.
    *   *Salida*: `x_p: 1 2` ($x = 1, y = 2$). `Sol unica.`
*   **Variante `M(T)_EB base B` (opción 4)**: para una TL dada por su matriz $M(T)_{EB}$ con el **dominio en base $B$** (no canónica) y el **codominio en la canónica $E$**. Como $E$ es canónica, $T(v)=M\,[v]_B$; el script resuelve en coordenadas $B$ y devuelve los vectores en **coordenadas canónicas** ($v=C_B\,[v]_B$). Hace **antiimagen** ($T(v)=w$) y **núcleo** ($\dim N(T)$ + base).
*   **Ejemplo**: $M(T)_{EB}=\begin{pmatrix}2&0&2\\0&3&3\\1&-1&0\end{pmatrix}$, $B=\{(0,1,-1),(0,0,1),(1,1,0)\}$.
    *   *Inputs (núcleo)*: `Op:` $\rightarrow$ `4`, luego `Op:` $\rightarrow$ `2`. `dim n:` $\rightarrow$ `3`. `M` $\rightarrow$ `2,0,2` / `0,3,3` / `1,-1,0`. `B` (un vector por fila) $\rightarrow$ `0,1,-1` / `0,0,1` / `1,1,0`.
    *   *Salida*: `dim N(T)= 1`, base $N(T)$ canónica `v1: 1 0 0`.
    *   *Antiimagen $T(v)=(0,2,1)$*: `Op:` $\rightarrow$ `4`, `Op:` $\rightarrow$ `1`, misma `M` y `B`, `w3:` $\rightarrow$ `0,2,1`. Salida: `NO existe v` (no está en la imagen).

### 2. Diagonalización (`diag.py`)
*   **Para qué sirve**: Autovalores y autovectores de matrices 2x2 o 3x3.
*   **Ejemplo**: Diagonalizar $A = \begin{pmatrix} 4 & 0 & 0 \\ 3 & -2 & 3 \\ 3 & -6 & 7 \end{pmatrix}$.
    *   *Inputs*: `n(2 o 3):` $\rightarrow$ `3`. `f1/3:` $\rightarrow$ `4,0,0`, `f2/3:` $\rightarrow$ `3,-2,3`, `f3/3:` $\rightarrow$ `3,-6,7`.
    *   *Salida*: `L1=4, L2=4, L3=1`. `S_L=4 m=2` $\rightarrow$ `v: 2 1 0` y `v: 0 1 2`. `S_L=1` $\rightarrow$ `v: 0 1 1`.
*   **Matriz singular ($\det A = 0$)**: Si el término independiente es $\approx 0$, el script detecta que $\lambda$ es factor común y muestra el polinomio **factorizado**: para 3x3 `p=L(L^2+aL+b)` (resuelve el cuadrático restante de forma exacta, sin Cardano) y para 2x2 `p(L)=L(L-tr)`. Imprime `c~0: L factor` (o `det~0: L factor`) como aviso. Esto da raíces exactas cuando $0$ es autovalor.

### 3. Param x autovector (`param.py`)
*   **Para qué sirve**: Hallar parámetros de una matriz para que un vector dado sea **autovector**, y luego decidir si esa matriz **diagonaliza**. Resuelve el típico "Hallar $a,b$ para que $v$ sea autovector de $A$ + ¿es diagonalizable?".
*   **Cómo**: la condición $Av = \lambda v$ se arma como **sistema lineal** en las incógnitas (parámetros y $\lambda$) y se resuelve numéricamente (no usa sympy). Las entradas de la matriz pueden ser **números o letras** (los parámetros): `1,0,b`. Después arma la $A$ numérica y reutiliza el análisis de `diag`.
*   **Ejemplo**: $A = \begin{pmatrix} 1 & 0 & b \\ 1 & 1 & 0 \\ 1 & 1 & a \end{pmatrix}$, pedir que $(0,-1,1)$ sea autovector.
    *   *Inputs*: `n(2 o 3):` $\rightarrow$ `3`. `v3:` $\rightarrow$ `0,-1,1`. Matriz: `f1/3:` $\rightarrow$ `1,0,b`, `f2/3:` $\rightarrow$ `1,1,0`, `f3/3:` $\rightarrow$ `1,1,a`.
    *   *Salida*: a) `b=0, a=2, L=1`. b) arma $A=\begin{pmatrix}1&0&0\\1&1&0\\1&1&2\end{pmatrix}$, autovalores `2,1,1`, y para $\lambda=1$ avisa `dimK=1 <m=2` → `NO diagonaliz.`.
*   **Notas**: cada celda es un número o un parámetro con coeficiente opcional (`a`, `-a`, `2a`); un mismo parámetro puede repetirse en varias celdas. Si el sistema es incompatible imprime `v NO es autovec`; si quedan grados de libertad, `infinitas sol`.

### 4. Cambio de Base (`cb.py`)
*   **Para qué sirve**: Halla la matriz de pasaje $M_{B_2 B_1}(\text{id})$ y cambia coordenadas.
*   **Ejemplo**: $B_1 = \{(1,0), (0,1)\}$ (Canónica), $B_2 = \{(1,1), (1,-1)\}$.
    *   *Inputs*: `dim:` $\rightarrow$ `2`. `B1` $\rightarrow$ `f1/2:` `1,0`, `f2/2:` `0,1`. `B2` $\rightarrow$ `f1/2:` `1,1`, `f2/2:` `1,-1`.
    *   *Salida*: `P:` `[[0.5, 0.5], [0.5, -0.5]]`.

### 5. Factorización LU (`lu.py`)
*   **Para qué sirve**: Descomposición $PA = LU$ con pivoteo parcial. Acepta matrices **rectangulares** $n\times m$ (no solo cuadradas) y **singulares** (en pivote $\approx 0$ no aborta: sigue y arma $P,L,U$ completos, $U$ con fila/s nula/s).
*   **Ejemplo**: Factorizar $A = \begin{pmatrix} 0 & 2 \\ 1 & 3 \end{pmatrix}$.
    *   *Inputs*: `filas:` $\rightarrow$ `2`, `cols:` $\rightarrow$ `2`. `f1/2:` $\rightarrow$ `0,2`, `f2/2:` $\rightarrow$ `1,3`.
    *   *Salida*: `P: [[0, 1], [1, 0]]` (intercambió filas), `L: [[1, 0], [0, 1]]`, `U: [[1, 3], [0, 2]]`.

### 6. Factorización QR (`qr.py`)
*   **Para qué sirve**: Descomposición $A = QR$ usando Gram-Schmidt clásico.
*   **Ejemplo**: Factorizar $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \\ 1 & 0 \end{pmatrix}$.
    *   *Inputs*: `filas A:` $\rightarrow$ `3`, `cols A:` $\rightarrow$ `2`. `f1/2:` $\rightarrow$ `1,1`, `f2/2:` $\rightarrow$ `0,1`, `f3/2:` $\rightarrow$ `1,0`.
    *   *Salida*: `Q: [[0.7071, 0.4082], [0, 0.8165], [0.7071, -0.4082]]`, `R: [[1.414, 0.7071], [0, 1.225]]`.

### 7. SVD (`svd.py`)
*   **Para qué sirve**: Descomposición en Valores Singulares para matrices de hasta 4x4.
*   **Ejemplo**: SVD de $A = \begin{pmatrix} 3 & 0 \\ 0 & 2 \end{pmatrix}$.
    *   *Inputs*: `filas A:` $\rightarrow$ `2`, `cols A:` $\rightarrow$ `2`. `f1/2:` $\rightarrow$ `3,0`, `f2/2:` $\rightarrow$ `0,2`.
    *   *Salida*: `s1=3, s2=2`. `V cols` $\rightarrow$ `v1: 1 0`, `v2: 0 1`. `U cols` $\rightarrow$ `u1: 1 0`, `u2: 0 1`.

### 8. Pseudoinversa (`pinv.py`)
*   **Para qué sirve**: Inversa de Moore-Penrose $A^+$ de matrices no cuadradas por ec. normales.
*   **Ejemplo**: Hallar $A^+$ para $A = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$.
    *   *Inputs*: `filas:` $\rightarrow$ `2`, `cols:` $\rightarrow$ `1`. `f1/1:` $\rightarrow$ `1`, `f2/1:` $\rightarrow$ `2`.
    *   *Salida*: `A+: [[0.2, 0.4]]` (Matriz de 1x2 ya que $(A^T A)^{-1}A^T = [1/5, 2/5]$).

### 9. Cuadrados Mínimos (`lsq.py`)
*   **Para qué sirve**: Ajuste de curvas con 5 modelos pre-cargados.
*   **Ejemplo**: Ajustar $(0,1)$, $(1,3)$ a una recta ($y = a + bx$).
    *   *Inputs*: `#ptos:` $\rightarrow$ `2`. `p1:` $\rightarrow$ `0,1`, `p2:` $\rightarrow$ `1,3`. `Modelo >` $\rightarrow$ `1` (`y=a+bx`).
    *   *Salida*: `coef: 1 2` ($a = 1, b = 2 \rightarrow y = 1 + 2x$). `||Ax-b||=0` (ajuste perfecto).

### 10. Complejos (`cplx.py`)
*   **Para qué sirve**: Operaciones con números complejos (Raíces, potencias, pasajes).
*   **Ejemplo (Raíces n-ésimas)**: Hallar las raíces cuadradas de $z = 4$ ($4 + 0i$).
    *   *Inputs*: Seleccionar `Raices n-esim`. `Re(z):` $\rightarrow$ `4`, `Im(z):` $\rightarrow$ `0`, `n:` $\rightarrow$ `2`.
    *   *Salida*: `w0=2 +i*0` ($2$), `w1=-2 +i*0` ($-2$).

### 11. Series de Fourier (`fs.py`)
*   **Para qué sirve**: Coeficientes trigonométricos/exponenciales utilizando Simpson.
*   **Ejemplo**: Coeficientes trigonométricos para $f(t) = t$ en $(-\pi, \pi)$ con 1 armónico.
    *   *Inputs*: Seleccionar `Coef a_n b_n`. `Templates >` $\rightarrow$ `1` (`t en(-pi,pi)`). `#arm:` $\rightarrow$ `1`.
    *   *Salida*: `a0=0`. `n=1` $\rightarrow$ `a=0`, `b=2` ($b_1 = 2 \rightarrow S_1(t) = 2\sin(t)$).

### 12. Transformada de Fourier (`tf.py`)
*   **Para qué sirve**: Pares analíticos y cálculo numérico para pulsos polinómicos custom.
*   **Ejemplo (Numérica)**: TF de $f(t) = 1$ (grado 0) en $[-1, 1]$ (pulso rectangular de ancho 2).
    *   *Inputs*: Seleccionar `Polin. num.`. `grado(0-3):` $\rightarrow$ `0`. `c0:` $\rightarrow$ `1`. `a inf:` $\rightarrow$ `-1`, `b sup:` $\rightarrow$ `1`. `w_max:` $\rightarrow$ `2`.
    *   *Salida*: Imprime grilla. En `w=0` muestra `|F|=2`. En `w=2` muestra `|F|=1.818` ($2\sin(2)/2$).

### 13. EDPs (`edp.py`)
*   **Para qué sirve**: Resolución implícita temporal de ecuaciones de calor, onda y advección.
*   **Ejemplo (Calor Dirichlet)**: Dominio $L=1$, 2 nodos internos ($\Delta x = 0.333$), $\Delta t = 0.1$, 1 paso, bordes en 0.
    *   *Inputs*: Seleccionar `Calor Dir`. `L:` $\rightarrow$ `1`, `nodos int:` $\rightarrow$ `2`, `dt:` $\rightarrow$ `0.1`, `#pasos:` $\rightarrow$ `1`. `C.Inicial >` $\rightarrow$ `3` ($x(1-x)$). `u(0,t):` $\rightarrow$ `0`, `u(L,t):` $\rightarrow$ `0`.
    *   *Salida*: `u^0: 0.2222 0.2222` (nodos iniciales). `u^1 t=0.100: 0.0617 0.0617` (vector difundido).

---

## Limitaciones Técnicas
- **Precisión**: Se utiliza integración de Simpson (400 paneles) para Fourier y TF numérica.
- **Memoria**: En matrices grandes ($> 5 \times 5$), el tiempo de cómputo y el scroll pueden verse afectados.
- **Diagonalización**: Autovalores 3x3 por método trigonométrico/Cardano. Si hay un autovalor real y dos complejos conjugados, imprime `L1(real)`, `L2,3 Re` y `Im=+-...` (parte imaginaria) y **no** arma $P,D$ (señal de no diagonalizable en $\mathbb{R}$). La salida de `show_vec` compacta los vectores cortos en una sola línea (`v: 2 1 0`) para ahorrar filas en la pantalla.

## Estrategia para el Parcial
Los scripts están diseñados para **validar**, no para reemplazar el razonamiento. Se recomienda:
1. Plantear el ejercicio en papel.
2. Usar el script para verificar valores intermedios (ej: ver si el autovalor que hallaste es correcto antes de buscar el autovector).
3. Utilizar las verificaciones finales (`|PA-LU|`, `|QR-A|`, etc.) para asegurar que no hubo errores de signo o aritmética.