from sympy import *

# Define the function in the Laplace domain
s, t = symbols('s t')
f = 5 * (s + 1) / (s + 3)**2
print("Original function F(s):", f)

# Laplace transform (t->s)
F = laplace_transform(f, t, s, noconds=True)
print("Laplace transform F(s):", F)

# Inverse Laplace transform (s->t)
invF = inverse_laplace_transform(F, s, t)
print("Inverse Laplace transform invF(t):", invF)
