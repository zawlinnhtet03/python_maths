from sympy import *
from sympy.plotting import plot

# Define the symbols
t = symbols('t')

# Define the Heaviside step function
heaviside_function = Heaviside(t)

# Plot the function
plot(heaviside_function)
