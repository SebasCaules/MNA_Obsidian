# Log

## [2026-05-26] setup | estructura inicial
Creadas carpetas `raw/` (Teoricas, Practicas) y `wiki/`. Schema en `CLAUDE.md`.

## [2026-05-26] ingest A1 | MNA_Unidad_I_Numeros_Complejos_Clase_I_v4.pdf
Unidad I completa: unidad imaginaria, definicion y operaciones en C, axiomas de orden, modulo, argumento, forma polar (elemental/trigonometrica/exponencial), De Moivre, radicacion, logaritmacion, potencia compleja y conjugacion. Output: wiki/teoria/01-numeros-complejos.md.

## [2026-05-26] ingest A1 | MNA_Unidad_II_Espacios_Vectoriales_P_I_v1.pdf
Unidad II Parte I: vectores en K^n, igualdad/adicion/multiplicacion por escalar, producto interno y propiedades, Cauchy-B-Schwarz, normas (euclidiana/1/p/infinito), angulo, paralelismo y perpendicularidad. Output: wiki/teoria/02-vectores-cn-rn.md.

## [2026-05-26] ingest A1 | MNA_Unidad_II_Espacios_Vectoriales_P_II_v1.pdf
Unidad II Parte II: matrices, adicion, multiplicacion por escalar, multiplicacion matricial (con ejemplo 2x3 * 3x2), potenciacion, transpuesta, identidad, inversa y propiedades, clasificacion (simetricas, antisimetricas, triangulares, diagonales, escalares, idempotentes, involutivas, nilpotentes, ortogonales). Output: wiki/teoria/03-matrices.md.

## [2026-05-26] ingest A1 | MNA_Unidad_II_Espacios_Vectoriales_P_III_v2.pdf
Unidad II Parte III: formas multilineales alternadas y sus propiedades, definicion de determinante, menor y cofactor, regla de Laplace; nota sobre Sarrus (no desarrollado en el slide). Output: wiki/teoria/04-determinantes.md.

## [2026-05-26] ingest A5 | Modelos de Examenes (IP + IIP + Parcial + Finales)
Procesados 30 PDFs: 9 IP (3 con resolucion: I, V, IX), 5 IIP (I, III, IV, V, VI), 1 recuperatorio (XIII) y 13 finales (I-XI, XIV mas variante XI(1)). Output: 22 paginas en wiki/parciales/ (16 enunciados + 3 resoluciones + 2 finales extra + patrones.md). Detectados patrones: TL R3->R3 en ~all parciales, factorizaciones QR/PLU/SVD recurrentes, EDP del calor con 4 nodos internos en casi todos los IIP/finales con EDP, varias matrices y bases que se repiten textualmente entre parciales.

## [2026-05-26] ingest A4 | guias TP + ejercicios resueltos
Procesados 9 guias TP (I-IX) y 6 PDFs de ejercicios resueltos. Output: 9 paginas en wiki/guias/ (complejos, vec-mat-det, espacios-vectoriales, transformaciones-lineales, diagonalizacion, qr-lu, svd-mmcc, fourier-series, tf) y 6 paginas en wiki/resueltos/ (complejos, algebra, diagonalizacion, svd, pseudoinversa, fourier). Total: 11+17+15+10+8+8+10+14+2 = 95 ejercicios en guias, ~27 resueltos paso a paso.

## [2026-05-26] ingest A2 | clase-2026-03-12
Slides Espacios Vectoriales Parte I (vectores en K^n, producto interno, normas 1/p/inf, Cauchy-Schwarz) y Parte II (matrices, operaciones, transpuesta, inversa, matrices con nombre propio). Referencia a teoria/02 y teoria/03 (sin anotaciones extras: los xs son las mismas slides).

## [2026-05-26] ingest A2 | clase-2026-03-19
Slide Determinantes (ref teoria/04) + anotaciones manuscritas: ejemplos de idempotente/nilpotente/involutiva/ortogonal, calculo de inversa via sistema, ejemplo det 3x3 por Laplace (det = -161), matriz adjunta/cofactor, aplicacion a sistemas AX=B.

## [2026-05-26] ingest A2 | clase-2026-03-26
Espacios vectoriales generales, axiomas (V,+) y (V,K,.), subespacios, combinacion lineal, dependencia/independencia, base y dimension. Ejercicios: subespacios de R^2/R^3/R^2x2/P_2, CL con parametro k (matriz 3x3 con determinante k-1).

## [2026-05-26] ingest A2 | clase-2026-04-09
Espacios euclideos: producto interno generalizado (bilinealidad, simetria hermitica, positividad), ejemplos en R^n / R^nxn (con tr(AB^T)) / P_n(C) (con integral). Proyeccion ortogonal, BON, formula v = sum<v,v_k>v_k, Gram-Schmidt, L^1 y L^2.

## [2026-05-26] ingest A2 | clase-2026-04-16
TL: inyectividad via nucleo, sobreyectividad, biyectividad, teorema dimensiones (dim V = dim N(T) + dim R(T)). Ejercicios: T(A) = rg(A) no es TL, T(A) = A + A^T es TL (nucleo = antisimetricas), TL definida por imagenes con casos existe-unica / existe-no-unica / no-existe.

## [2026-05-26] ingest A2 | clase-2026-04-23
Coordenadas en base como isomorfismo V ~ K^n, matriz asociada M_{B2 B1}(T). Ejemplo T: P_2 -> R^2x2. Inicio autovalores/autovectores, semejanza de matrices, polinomio caracteristico p_A(lambda) = det(lambda I - A), diagonalizacion.

## [2026-05-26] ingest A2 | clase-2026-04-30
Diagonalizacion con parametros: multiplicidad algebraica vs geometrica. Tres ejercicios resueltos: M 3x3 con parametro a (diagonalizable salvo a=1), A 3x3 con autovector dado (1,2,3) -> a=2, autovector (1,0,1) en bases no canonicas con A=M_{B2 B1}(T) -> k=4, matriz de cambio de base B1->B2.

## [2026-05-26] ingest A2 | clase-2026-05-07
Factorizacion de matrices: idea general "invertir sin invertir". LU via Doolittle (multiplicadores m_ij, ejemplo 3x3 con resultado L y U), PLU con matrices de permutacion (ejemplos de izq vs der), proposicion PA=LU para A regular. Inicio QR: inversas a izq/der, matriz ortogonal, construccion Q via Gram-Schmidt, R = Q^T A.

## [2026-05-26] ingest A2 | clase-2026-05-14
SVD: teorema A = U S V^T con sigma_i >= 0, A^T A = V S^T S V^T y A A^T = U S S^T U^T. Caracterizacion via bases ortonormales (A v_i = sigma_i u_i). Definida positiva => autovalores > 0. Procedimiento de calculo (Caso I via A^T A, Caso II via A A^T). Aplicacion a minimos cuadrados: ecuaciones normales A^T A X = A^T B y pseudoinversa de Moore-Penrose A^+ = (A^T A)^{-1} A^T.

## [2026-05-26] ingest A3 | pizarron-clase-1
Numeros complejos: forma binomica/polar/exponencial, formula de Euler, modulo y argumento, producto y potencias en polar, raices n-esimas (ej w^4 = i), ejercicios 4 (z^n = bar z), 5 (Re/Im como combinacion de z y bar z), 8.k (z^2 + |z|^2 = i bar z), 10 (|z|=1, z^4 (z-i)^4 = 1) y 11.a (logaritmo complejo e^w = sqrt(3) - i sqrt(3)).

## [2026-05-26] ingest A3 | pizarron-clase-2
Vectores en C^n (parte real/imaginaria), CL en R^3, sistema Ax=b clasificado (SCD/SCI/SI) con solucion particular + homogenea, escalonamiento Gauss, ejercicio 7 con triangulacion (alpha,beta,gamma), y matrices idempotentes 2x2 (caso b=c=0 y caso tr(A)=1 con a^2 - a + bc = 0).

## [2026-05-26] ingest A3 | pizarron-clase-3
Determinantes por Sarrus (3x3, det = -57) y por cofactores (4x4 desarrollado por columna 4, det = 0). Propiedades de det aplicadas a det(3/4 A^-1 B^T) y det(2/3 B^-1 A^2). Matrices singulares paramétricas (k=3 v k=-5; k!=0 y k!=-3/2 para invertibilidad). Discusion de sistemas paramétricos por compatibilidad (SCD/SCI/SI segun a, b, k).

## [2026-05-26] ingest A3 | pizarron-clase-4
Cierre ej 1.10 (k=-2 SCI), espacios vectoriales: V={f:R->R} con 8 axiomas verificados, subespacio A={(0, x2)} en R^2, S={alpha i} es subespacio de (C,+;R,.) pero NO de (C,+;C,.), ejercicio 6.a sobre independencia lineal con parametro k (LI si k!=1, LD si k=1).

## [2026-05-26] ingest A3 | pizarron-clase-5
Cierre subespacios (matrices singulares NO son subespacio; polinomios con dos restricciones lineales si). Completar a base de R_3[x] el conjunto {x^3-2x+1, x^3+3x} (agregar x^2 y 1, det=-5). Producto interno: angulo, norma, proyeccion (ejs en R^2). Minimizar |b - alpha a|^2 con alpha optimo = <b,a>/|a|^2 y demostracion vector error perpendicular a a. Ortogonalidad <cos(kx), sen(nx)>_{L^2[0,2pi]} = 0.

## [2026-05-26] ingest A3 | pizarron-clase-6
TLs: verificacion linealidad f(x)=Ax y D:P_2->P_2 (D(p)=p'). Coordenadas en base, matriz asociada [D]_EE (3x3) construida con D(x^2), D(x), D(1). Aplicacion: D(2x^2-x+3)=4x-1 via [D]_EE [p]_E. Nucleo (constantes) e imagen (P_1), teorema de la dimension (3 = 1 + 2). Existencia y unicidad de TL desde su accion sobre una base. Matriz de cambio de base B_1->B_2 (uso bidireccional).

## [2026-05-26] ingest A3 | pizarron-clase-6-tl-matriz-asociada
Interpretacion geometrica de TLs en R^2: proyeccion (1,0;0,0), reflexion (1,0;0,-1), rotacion (cos,-sin;sin,cos). Cambio de base con P (con caveat de transcripcion). Existencia/unicidad de TL: contraejemplo con 3 condiciones inconsistentes. Nucleo de F:R^3->P_1 con matriz no canonica. Coordenadas en C^2 (base compleja). Diagonalizacion completa de A=(3,-1,1;0,2,0;1,-1,3): autovalores 2 (MA=MG=2) y 4 (MA=MG=1), A=PDP^-1.

## [2026-05-26] ingest A3 | pizarron-clase-8
Factorizacion PA=LU: definicion, 2 ejemplos completos (uno con permutacion F_3 -> F_1 y otro sin permutacion), aplicacion a Ax=b (forward sustitucion en Lz=Pb, backward en Ux=z). Verificacion det(A) via det(L)det(U). Factorizacion QR via Gram-Schmidt: definicion, formula recursiva u_k, ejemplos 2x2 (A=(1,2;3,4)), 3x2 y 3x3. Aplicacion: Ax=b -> Rx = Q^T b (sistema escalonado).

## [2026-05-26] ingest A3 | pizarron-repaso
Repaso integrador: TL paramétrica con M(k) cuyo det = 2k (rango 2 para k=0, R(T)=R^3 para k=2). Autovalor lambda=-1 dado -> k=-1. Diagonalizacion de A 3x3 (k=2) con 3 autovalores distintos 2,1,4. SVD de A=(1,-1;0,1;1,0) (3x2): valores singulares sqrt(3) y 1, U 3x2 forma reducida y 3x3 forma completa (u_3 via producto vectorial). QR de la misma matriz con R triangular superior 2x2 (con cero abajo en forma 3x2).

## [2026-05-26] ingest A3 | pizarron-svd
SVD detallada en 3 ejemplos: matriz 4x3 (con autovalores 36 doble y 0, U 4x2/4x4, Sigma con bloque diag); vector columna A=(1,3)^T (caso 2x1 con sigma=sqrt(10) y pseudo-inversa A^+ = (1/10)(1,3)); matriz C 2x3 (sigmas 5 y 3, V 3x3 completada via producto vectorial, pseudoinversa C^+ = (1/45)(7,2;2,7;10,-10)).

## [2026-05-27] consolidacion | index + mapa-temas
Reescritos wiki/index.md (catalogo de 73 paginas) y wiki/00-mapa-temas.md (tabla cruzada Tema -> Teoria/Clase/Pizarron/Guia/Resueltos/Parciales con priorizacion para el parcial central).

## [2026-05-27] entregable | study/MNA_Cheatsheet.html
Guia imprimible (font 11.5pt, A4, ~30-35 paginas). Contiene: mapa del parcial, cronograma de 5 dias, 12 recetas paso a paso, 8 ejercicios resueltos con cuentas completas (TL con parametro, diagonalizacion clase 30/04, cambio de base, LU, QR, SVD, MMCC, SF de t en [-pi,pi], TF pulso rectangular, calor 4 nodos, subespacio P2), formulario denso 2-col, tabla integrales/derivadas, 15 trampas + 6 matrices recurrentes identificadas como alta probabilidad de aparecer en el parcial. Single-file con MathJax CDN.

## [2026-05-27] entregable | study/casio/ (16 archivos)
Scripts MicroPython para Casio fx-CG50/9750GIII. main.py + io_util.py + mat.py + 12 modulos por tema (tl, diag, cb, lu, qr, svd, pinv, lsq, cplx, fs, tf, edp) + README.md. Arquitectura hibrida menu + modulos, entrada fila por fila por display chico (21x7), imprime pasos intermedios. Smoke test CPython: matmul/det/solve/GS/Cardano 3x3/QR coinciden con valores esperados.

## [2026-05-29] resolucion | wiki/parciales/ip-tema-02-resolucion.md
Resolucion completa del Primer Parcial Tema II: TL R3->R3 (nucleo trivial via det=10, Im=R3, antiimagen (8/5,2/5,4/5)), SVD+QR de [[0.55,1.1],[1.1,0.8]] (sigma=1.7821,0.4321; Q=(1/sqrt5)[[1,2],[2,-1]]), y cuadrados minimos y=ax^2+b por QR (a=98/65~1.5077, b=399/650~0.6138, ||r||~0.2824). Verificado con numpy (solve, svd, qr, lstsq) y fracciones exactas.

## [2026-05-29] resolucion | wiki/parciales/ip-tema-03-resolucion.md
Resolucion completa del Primer Parcial Tema III: (1) TL R3->R3 con parametro k, dim R(T)=1 sii k=0 (columnas proporcionales c1=c2/4, c3=0), nucleo para k=0 base {(-4,1,0),(0,0,1)} dim 2; (2) diagonalizacion de triangular sup con autovals 2,3,3, diagble sii k=1 (mg(3)=2), para k=0 NO diagble (solo 2 autovecs (1,0,0) y (-2,1,0)); (3) PLU con P=I (no requiere permutar) L=[[1,0,0],[2,1,0],[-1,3,1]] U=[[1,3,-1],[0,2,6],[0,0,-23]], y QR Gram-Schmidt v1=(1,2,-1)/sqrt6, v2=(1,8,17)/sqrt354, v3=(-7,3,-1)/sqrt59. Verificado con numpy/scipy y fracciones exactas (rg, AP=PD, LU=A, QR=A, QtQ=I).

## [2026-05-29] resolucion | MNA_IIP_Tema_I.pdf
Resolucion completa del IIP Tema I (Fourier). Ej1: serie trig. de e^t en (-pi,pi) e identidad sum (-1)^n/(n^2+1) via Dirichlet en t=0. Ej2: diente de sierra t-[t], serie trig/exp y forma de laboratorio. Ej3: TF de la rampa t en [0,1] y espectro |x_hat(w)|. Coeficientes e identidades verificados numericamente con scipy/sympy. Output: wiki/parciales/iip-tema-01-resolucion.md.

## [2026-05-29] resolucion | MNA_IIP_Tema_IV.pdf
Resolucion completa del IIP Tema IV (Fourier + diferencias finitas). Ej1: serie trig. de x=t^2 en (0,2pi) T=2pi (a0=4pi^2/3, an=4/n^2, bn=-4pi/n) y derivada t-a-t -> y=2t; punto sutil: el termino -4pi*sum cos(nt) suma (Abel) a 2pi recuperando el valor medio de 2t (firma del salto periodico). Ej2: TF de t^2 en [0,2pi], xhat(w)=e^{-2pi i w}(4pi^2 i/w + 4pi/w^2 - 2i/w^3)+2i/w^3, xhat(0)=8pi^3/3, control xhat(n)=pi(an - i bn). Ej3: calor implicito h=1/5; (a) Dirichlet homogeneo -> M tridiag 4x4 (1+2r)/-r, CI sin(0.2..0.8); (b) Neumann en x0 (fantasma u_{-1}=u1) + Dirichlet en x5 -> M 5x5 NO simetrica con fila 0 (1+2r,-2r,...), CI cos(0,0.2..0.8). Coeficientes, forma cerrada de la TF y sistemas verificados con sympy/numpy/scipy (residuos ~1e-14). Output: wiki/parciales/iip-tema-04-resolucion.md.

## [2026-05-29] resolucion | MNA_Final_Tema_V.pdf
Resolucion completa del Final Tema V. Ej1: TL R3->R3 T(x,y,z)=(2x,x+y-z,2z+y), det=6 => iso (N(T)={0}, Im=R3), p_A(l)=(l-2)(l^2-3l+3), discriminante -3<0 => unico autoval real l=2 => NO diagonalizable en R (si en C). Ej2: serie de Fourier de 1-x^2 en [0,1] periodo 1: a0=2/3, an=-1/(pi^2 n^2), bn=1/(pi n); converge a 1/2 en x=0 (salto f(1-)=0,f(0+)=1) y a 3/4 en x=1/2. Ej3: calor implicito 4 nodos internos: (a) Dirichlet homog -> tridiag 4x4 (1+2r diag,-r off), CI sin(x_i); (b) Neumann ambos bordes -> nodos fantasma, sistema 6x6 con -2r en filas 1 y 6, CI |x|=x_i, masa conservada. Ej4: TF de e^{-|t-1|} en [0,1]: |t-1|=1-t => e^{t-1}, f_hat(w)=e^-1 (e^{1-iw}-1)/(1-iw)=(e^{-iw}-e^-1)/(1-iw), f_hat(0)=1-e^-1. Todo verificado con numpy/scipy/sympy. Output: wiki/parciales/final-tema-05-resolucion.md.

## [2026-05-29] resolucion | MNA_IIP_Tema_VI.pdf
Resolucion completa del IIP Tema VI (Fourier + diferencias finitas). Ej1: serie trig. de x=sen(t) en (-pi/4,pi/4) T=pi/2 (impar -> solo senos, w0=4); bn=(16√2/pi)(-1)^{n+1} n/(16n^2-1). Punto sutil: derivada t-a-t da serie de cosenos con Bn=4n·bn que NO->0 (|Bn|->2√2·2/pi=1.8006) => NO converge puntualmente; la extension periodica salta -√2 en ±pi/4, asi x'=cos(t) menos tren de deltas (Cesaro recupera cos en interior). Ej2: TF de t·e^{-t} ASUMIENDO causal (t>=0; si no, diverge): xhat(w)=1/(1+iw)^2=(1-w^2-2iw)/(1+w^2)^2, |xhat|=1/(1+w^2). Ej3: conveccion-difusion u_t=u_xx+u_x implicito h=1/5, r=dt/h^2, s=dt/(2h). Stencil verificado simbolo a simbolo: (s-r)u_{i-1}+(1+2r)u_i-(r+s)u_{i+1}=u_i^k (tridiag NO simetrica; el brief tenia las off-diagonales con signo invertido -> corregido y confirmado: signo correcto da O(dt)~6e-4 vs MoL, signo invertido ~4e-2). (a) Dirichlet homog -> M 4x4, CI sen(0.2..0.8). (b) Neumann en x0 (fantasma u_{-1}=u1) + Dirichlet x5 -> M 5x5, fila 0 = (1+2r)u0-2r·u1=u0^k (el termino s se CANCELA en la pared), CI cos(0,0.2..0.8). Coeficientes/forma cerrada/sistemas verificados con sympy/numpy/scipy. Output: wiki/parciales/iip-tema-06-resolucion.md.

## [2026-05-29] resolucion | final-tema-07
Resolucion completa del Final Tema VII (3 ejercicios), verificada con numpy/sympy. Ej1: TL R3->R3 parametrica T(x,y,z)=(kx, 2x-2y-z, -2x+5y+4z); det=-3k -> dim R(T)<3 sse k=0; autovalores {k,3,-1}; diagonalizable sse k!=-1 (en k=3 el autoespacio doble es genuino m_g=2, en k=-1 colapsa m_g=1 porque el autovector movil (k+1,2,-2) se alinea con el del bloque). Ej2: serie de Fourier diente de sierra f(x)=1-x, T=1: a0=1/2, an=0, bn=1/(pi n); converge a 1/2 en x=0 (salto) y x=1/2 (continuidad). Ej3: QR de A 2x3 -> 3 columnas en R^2, la tercera dependiente da u3=0; Q 2x2 ortogonal, R 2x3. Output: wiki/parciales/final-tema-07-resolucion.md.

## [2026-05-29] resolucion | MNA_Final_Tema_VI.pdf
Resolucion completa del Final Tema VI (4 ejercicios), verificada con numpy/sympy/scipy. Ej1: TL R3->R3 T(x,y,z)=(2x-y, x+y-z, x+y+2z); det(A)=9 (isomorfismo -> N(T)={0}, Im=R3); p_A(l)=l^3-5l^2+10l-9, irreducible sobre Q, sin raices racionales; argumento limpio: p'(l)=3l^2-10l+10 con disc=-20<0 -> p estrictamente creciente -> UNA sola raiz real (~2.3926, en (2,3)) + par complejo conjugado (1.3037+-1.4359i) => NO diagonalizable en R. Ej2: serie de Fourier diente de sierra f(x)=1-x, T=1: a0=1/2, an=0, bn=1/(pi n); converge a 1/2 en x=0 (salto) y a 1/2 en x=1/2 (continuidad, coincidencia: razones distintas). Ej3: calor implicito h=1/5 r=dt/h^2. (a) Dirichlet-Dirichlet homog -> M 4x4 tridiag, CI e^{-x}sen(x) en x=0.2..0.8 = (0.162657,0.261035,0.309882,0.322329). (b) MIXTO Neumann en x0 (fantasma u_{-1}=u1, fila0=(1+2r)u0-2r·u1=u0^k) + Dirichlet en x5 -> sistema 5x5 (entra u0, sale u5; NO 6x6); ultima fila SIN -2r (Dirichlet); CI x^2 en x=0..0.8 = (0,0.04,0.16,0.36,0.64); det M_a=55, M_b=123 a r=1. Ej4: TF de e^{-2|t|+1} en [0,1] (|t|=t): fhat(w)=e·(1-e^{-(2+iw)})/(2+iw)=(e-e^{-1}e^{-iw})/(2+iw); w=0 -> (e-e^{-1})/2~1.17520; Re/Im cerradas verificadas vs scipy.quad a ~1e-16. Output: wiki/parciales/final-tema-06-resolucion.md.

## [2026-05-29] resolucion | final-tema-08
Resolucion completa del Final Tema VIII (3 ejercicios), verificada con numpy/sympy. Ej1: TL R3->R3 parametrica T(x,y,z)=(2x+8y+kz, -x-4y, (k+3)x+12y+2kz); det(A)=4k^2 -> rango baja de 3 solo en k=0, y ahi todos los menores 2x2 se anulan -> dim R(T)=1 sse k=0 (NO hay valor con rango 2); para k=0 las filas son proporcionales a (1,4,0), N(T)=gen{(-4,1,0),(0,0,1)}, dim N(T)=2 (teorema dim 2+1=3 ✓). Ej2: serie de Fourier de f(x)=1-x^2 en [0,1], T=1: a0=2/3, an=-1/(pi^2 n^2), bn=1/(pi n) (no hay paridad porque el intervalo no es simetrico); converge a 1/2 en x=0 (salto entre f(0+)=1 y f(1-)=0) y a 3/4 en x=1/2 (continuidad, =f(1/2)). Ej3: SVD de A 2x3 via AA^T=[[14,-1],[-1,29]]; autovalores IRRACIONALES lambda=(43+-sqrt229)/2 -> sigma1~5.3913, sigma2~3.7328 (chequeo trace=43, det=405, sigma1·sigma2=9sqrt5); v_i=A^T u_i/sigma_i, v3 base de N(A)=(-4,10,17)/9sqrt5; U 2x2, Sigma 2x3, V 3x3; U Sigma V^T=A exacto, U^TU=I, V^TV=I verificados. Output: wiki/parciales/final-tema-08-resolucion.md.

## [2026-05-29] resolucion | MNA_Final_Tema_XI.pdf
Resolucion completa del Final Tema XI (3 ejercicios), verificada con numpy/sympy. Ej1: TL R3->R3 triangular superior M_EE con parametro a; det=16a(1-2a) -> sobreyectiva (=inyectiva=iso, dominio=codominio) sse a!=0 y a!=1/2. En a=1 M=[[4,-1,1],[0,-1,0],[0,0,4]], autovalores 4 (doble) y -1; p(l)=(l-4)^2(l+1); m_g(4)=dim N(4I-M)=1<2=m_a -> NO diagonalizable (bloque de Jordan en direcciones x,z por el acople (1,3)=1); autovec lambda=4 es (1,0,0), lambda=-1 es (1,5,0). Ej2: T(A)=A-A^T sobre R^{nxn}: N(T)=simetricas (dim n(n+1)/2), R(T)=antisimetricas (dim n(n-1)/2; toda antisim S=T(S/2)); chequeo dim n^2. Para A=[[1,-1],[2,0]] -> T(A)=[[0,-3],[3,0]] (det=9, no singular), sistema T(A)X=(1,1)^T tiene solucion unica X=(1/3,-1/3). Ej3: A 3x2=[[1,1],[0,-3],[-3,5]]. SVD via A^TA=[[10,-14],[-14,35]], p(l)=l^2-45l+154 -> autovalores (45+-sqrt(1409))/2 NO lindos, sigma1~6.4240 sigma2~1.9318 (cross-check sigma1·sigma2=sqrt(154)=sqrt(detA^TA)); V de autovectores ortonormales; u_i=Av_i/sigma_i; u3 completa U desde N(A^T) -> (9,8,3)/sqrt(154); U Sigma V^T=A ✓. QR por Gram-Schmidt SI exacto: r11=sqrt(10), r12=-7sqrt(10)/5, r22=sqrt(385)/5, u2=(12/5,-3,4/5); Q^TQ=I, QR=A ✓. Output: wiki/parciales/final-tema-11-resolucion.md.

## [2026-05-29] resolucion | MNA_Final_Tema_X.pdf
Resolucion completa del Final Tema X (3 ejercicios), verificada con numpy/sympy. Ej1: TL R3->R3 T(x,y,z)=(2x+y-z, x+3y-z, z-y). M_EE=[[2,1,-1],[1,3,-1],[0,-1,1]]. Base B={(0,0,1),(1,0,0),(1,-1,0)} -> P=cols(b_j), M_BB=P^-1 M_EE P = [[1,0,1],[-2,3,-1],[1,-1,2]] (cada col j = [T(b_j)]_B; det=4). QR por Gram-Schmidt exacto: r11=sqrt6, r12=-7sqrt6/6, r22=sqrt66/6, r13=5sqrt6/6, r23=5sqrt66/66, r33=4sqrt11/11; Q^TQ=I y QR=M_BB exactos (sympy). OJO: numpy.qr invierte signos de col1,col2 (no fuerza R_ii>0); la convencion catedra si. Ej2: calor u_t=u_xx con bordes MIXTOS u_x(0)=0 (Neumann) y u(1)=0 (Dirichlet), u(x,0)=e^{-x^2}. h=0.2. Neumann en x0 -> x0 incognita + fantasma u_{-1}=u1 -> fila0 (1+2r)u0-2r u1=u0^k; Dirichlet en x5 -> u5=0 sale del sistema. Sistema 5x5 (incognitas u0..u4), NO 4x4 ni 6x6. CI=(1,0.9608,0.8521,0.6977,0.5273); det M(r=1)=123. Ej3: TF del pulso triangular f=1-|t| en [-1,1]. f par -> TF real = 2 int_0^1 (1-t)cos(wt)dt = 2(1-cos w)/w^2 = 4 sin^2(w/2)/w^2 = sinc^2(w/2); en w=0 -> 1 (area del triangulo). Im=0 a precision maquina; formula coincide con scipy.quad ~1e-8. Output: wiki/parciales/final-tema-10-resolucion.md.

## [2026-05-29] resolucion | final-tema-11-alt
Resolucion completa de la VARIANTE del Final Tema XI (segundo archivo MNA_Final_Tema_XI(1).pdf, 4 ejercicios), verificada con numpy/sympy/scipy. Ej1: TL R3->R3 T(x,y,z)=(-y+z, x+y, x+z); M_EE=[[0,-1,1],[1,1,0],[1,0,1]], det=0 (no inyectiva); N(T)=gen{(-1,1,1)} dim1; Im(T)=gen{(0,1,1),(-1,1,0)}={z=x+y} (plano -x-y+z=0) dim2; p_A(l)=l(l-1)^2, autovalores 0 (simple) y 1 (m_a=2); para l=1 rg(I-A)=2 -> m_g=1<2 => NO diagonalizable en R (sympy is_diagonalizable=False). Ej2: serie de Fourier de f(x)=1-x^2 en [0,1] T=1: a0=2/3, an=-1/(pi^2 n^2), bn=1/(pi n) (intervalo no simetrico -> sin paridad); converge a 1/2 en x=0 (salto f(0+)=1, f(1-)=0) y a 3/4 en x=1/2 (continuidad, =f(1/2)); sumas parciales N=5000 confirman. Ej3: calor implicito h=1/5, r=dt/h^2, esquema -r u_{i-1}+(1+2r)u_i-r u_{i+1}=u_i^k. (a) Dirichlet-Dirichlet homog -> M 4x4 tridiag, CI x e^{-x} en x=0.2..0.8 = (0.16375,0.26813,0.32929,0.35946). (b) Neumann-Neumann en AMBOS bordes (fantasmas u_{-1}=u1, u6=u4) -> sistema 6x6, primera/ultima fila con -2r ((1+2r)u0-2r u1=u0^k); matriz NO simetrica; CI x+1 en x=0..1 = (1,1.2,1.4,1.6,1.8,2). Ej4: TF de e^{-a|t|} en [0,1] (|t|=t -> e^{-at}): fhat(w)=(1-e^{-(a+iw)})/(a+iw); soporte acotado -> converge para todo w,a>0; Re/Im cerradas dadas y verificadas vs scipy.quad a=1 (w=0,1,2.5,5) coincidencia ~1e-16; w=0 -> (1-e^{-a})/a. Output: wiki/parciales/final-tema-11-alt-resolucion.md.

## [2026-05-29] resolucion | parciales (lote completo)
Se completaron las resoluciones de TODOS los modelos de examen sin resolver: 6 nuevas IP (II, III, IV, VI, VII, VIII) + se completaron las truncadas IP I (ej. 3-5) e IP IX (ej. 3); 5 IIP (I, III, IV, V, VI); 13 Finales (I-XI, XI-variante, XIV); 1 recuperatorio (Tema XIII). Total: 28 archivos *-resolucion.md, todos verificados numericamente con numpy/sympy (QR/LU/SVD/PLU, AP=PD, antiimagenes, coeficientes de Fourier y esquemas de diferencias finitas). Convenciones de la catedra: p_A(l)=det(lI-A), serie de Fourier con a0=valor medio, TF con e^{-iwt}, esquema implicito Euler-atras h=1/5. Hallazgos: IP III/Final XIV diagonalizable solo k=1; Parcial XIII no diagonalizable solo h=1 (h=2 si); Final IV/VII antiimagen (0,2,1) incompatible; varias TL con autovalores complejos no diagonalizables en R; correccion de signo en stencil conveccion-difusion (IIP VI). Se actualizo wiki/index.md y se marco tiene_resolucion: true + puntero en cada enunciado.
