from sympy import *
import matplotlib.pyplot as plt
#from sympy.plotting import plot

x = symbols('x')
y = symbols('y')

x = [1,2,3,4,5]
y = [2,4,6,8,10]

plt.plot(x,y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Plot")
plt.show()