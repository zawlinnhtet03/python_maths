from sympy import *

# Define the function in the Laplace domain
s = symbols('s')
t = symbols('t')

f = 5 * (s + 1) / (s + 3)**2
print("Original function F(s):", f)

# Laplace transform (t->s)
F = simplify(laplace_transform(f, t, s, noconds=True))
print("Laplace transform F(s):", F)

# Inverse Laplace transform (s->t)
invF = simplify(inverse_laplace_transform(F, s, t))
print("Inverse Laplace transform invF(t):", invF)
