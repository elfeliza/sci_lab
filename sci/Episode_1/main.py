import sympy as sym

l, ro, mu = sym.symbols('l, ro, mu')

matr = sym.Matrix.zeros(9, 9)

matr[0, 3] = -1 / ro
matr[1, 4] = -1 / ro
matr[2, 5] = -1 / ro
matr[3, 0] = -(l + 2*mu)
matr[4, 1] = -mu
matr[5, 2] = -mu
matr[6, 0] = -l
matr[8, 0] = -l

print(matr.eigenvals())
