from sympy import *

# Initialize pretty printing
init_printing()

# Define the symbols
t, s = symbols('t s')
a = symbols('a', real=True, positive=True)

# Define the function
f = exp(-a*t)
print("The function f(t) is:", f)

# Calculate the Laplace transform
L = integrate(f * exp(-s * t), (t, 0, oo))
print("The Laplace transform L(s) is:", L)
