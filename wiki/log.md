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
