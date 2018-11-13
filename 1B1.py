"""
from numpy import *
x = linspace(0,7,70)
y = cos(x)


import matplotlib.pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija$cos(x)$')
plt.plot(x, y)
plt.show()

"""

from numpy import *
x = linspace(0,7,70)
y2 = sin(x)


import matplotlib.pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija$cos(x)$')
plt.plot(x, y2, color = "#04B45F")
plt.show()

