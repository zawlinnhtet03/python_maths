from sympy import *

# Define the function
f = 5 * symbols('t')
print("Original function f(t):", f)

# Laplace transform (t->s)
F = laplace_transform(f, symbols('t'), symbols('s'), noconds=True)
print("Laplace transform F(s):", F)

# Inverse Laplace transform (s->t)
invF = inverse_laplace_transform(F, symbols('s'), symbols('t'))
print("Inverse Laplace transform invF(t):", invF)
