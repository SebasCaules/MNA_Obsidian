#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ejercicio (MNA):

        | 1  0  b |
    A = | 1  1  0 |
        | 1  1  a |

    a) Hallar a, b en R para que (0, -1, 1) sea autovector de A.
    b) Para esos valores, decidir si A es diagonalizable en R.

Resolucion simbolica con sympy (verifica la solucion hecha a mano).
Correr:  python3 ej_autovector_diag.py
"""

import sympy as sp


def main():
    a, b, lam = sp.symbols("a b lambda", real=True)

    A = sp.Matrix([[1, 0, b],
                   [1, 1, 0],
                   [1, 1, a]])
    v = sp.Matrix([0, -1, 1])

    # ------------------------------------------------------------------
    # a) (0,-1,1) autovector  <=>  A v = lam v  para algun lam
    # ------------------------------------------------------------------
    print("=" * 56)
    print("a) Hallar a, b para que (0,-1,1) sea autovector")
    print("=" * 56)

    Av = A * v
    print("A·v =", list(Av))                 # (b, -1, a-1)
    print("Pido  A·v = λ·v = (0, -λ, λ):")

    # Sistema A v - lam v = 0 (3 ecuaciones, incognitas a, b, lam)
    eqs = list(Av - lam * v)
    for i, e in enumerate(eqs):
        print("   comp {}:  {} = 0".format(i + 1, sp.simplify(e)))

    sol = sp.solve(eqs, [a, b, lam], dict=True)[0]
    print("\n=> b = {},  λ = {},  a = {}".format(sol[b], sol[lam], sol[a]))

    # Matriz con los valores hallados
    A0 = A.subs({a: sol[a], b: sol[b]})
    print("\nA con a={}, b={}:".format(sol[a], sol[b]))
    sp.pprint(A0)

    # ------------------------------------------------------------------
    # b) Diagonalizable en R ?
    # ------------------------------------------------------------------
    print("\n" + "=" * 56)
    print("b) ¿Es diagonalizable en R?")
    print("=" * 56)

    # Polinomio caracteristico p(lam) = det(A - lam I)
    M = A0 - lam * sp.eye(3)
    print("A - λI =")
    sp.pprint(M)
    detM = sp.factor(M.det())
    print("\np(λ) = det(A - λI) =", detM)
    print("       (forma monica det(λI-A) =", sp.factor((lam * sp.eye(3) - A0).det()), ")")

    # Autovalores con multiplicidad algebraica
    eig = A0.eigenvals()           # {valor: mult_algebraica}
    print("\nAutovalores y multiplicidad ALGEBRAICA:")
    for val, m in sorted(eig.items(), key=lambda kv: float(kv[0])):
        print("   λ = {}   m_alg = {}".format(val, m))

    # Autoespacios -> multiplicidad geometrica
    print("\nAutoespacios y multiplicidad GEOMETRICA (= dim ker(A-λI)):")
    diag_ok = True
    for val, m_alg, space in sorted(A0.eigenvects(), key=lambda t: float(t[0])):
        m_geo = len(space)
        base = [list(s) for s in space]
        marca = "OK" if m_geo == m_alg else "FALLA (g<m)"
        if m_geo != m_alg:
            diag_ok = False
        print("   λ = {}:  m_alg = {}, m_geo = {}  -> {}".format(val, m_alg, m_geo, marca))
        print("            base del autoespacio: {}".format(base))

    n = A0.shape[0]
    suma_geo = sum(len(t[2]) for t in A0.eigenvects())
    print("\nSuma de mult. geometricas = {}  (n = {})".format(suma_geo, n))
    print("Criterio (g=m en todos / suma_geo=n):",
          "DIAGONALIZABLE" if diag_ok else "NO diagonalizable")
    print("sympy is_diagonalizable():", A0.is_diagonalizable())


if __name__ == "__main__":
    main()
