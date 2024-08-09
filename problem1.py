from sympy import *

# Define the Laplace transform function
def L(f):
    return laplace_transform(f, t, s, noconds=True)

# Define the symbols
t, s = symbols('t, s')
a = symbols('a', real=True, positive=True)
omega = Symbol('omega', real=True)

# Define shorthand functions
exp = exp
sin = sin
cos = cos

# Define the list of functions
functions = [
    1,
    t,
    exp(-a*t),
    t**2 * exp(-a*t),
    sin(omega*t),
    cos(omega*t),
    1 - exp(-a*t),
    exp(-a*t) * sin(omega*t),
    exp(-a*t) * cos(omega*t)
]

# Print the list of functions
print("Functions:")
for f in functions:
    print(f)

print("---------")

# Compute the Laplace transforms
Fs = [L(f) for f in functions]

# Print the Laplace transforms
print("Laplace Transforms:")
for F in Fs:
    print(F)
