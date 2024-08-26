from sympy import *

t = symbols('t')
s = symbols('s')
# Define the function
f = 5 * t
print("Original function f(t):", f)

# Laplace transform (t->s)
F = laplace_transform(f, t, s, noconds=True)
print("Laplace transform F(s):", F)

# Inverse Laplace transform (s->t)
invF = inverse_laplace_transform(F, s, t)
print("Inverse Laplace transform invF(t):", invF)