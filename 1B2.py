import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import *
x = linspace(0, 7, 70)
y = cos(x)

import matplotlib.pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $sin(x)$')
plt.plot(x, y, color='#FF0000')

y1=x
plt.plot(x, y1, color='#04B45F')

y2=x - x*x*x/(1*2*3)
plt.plot(x, y2, color='#610B4B')

y3=x - x*x*x/(1*2*3)+x*x*x*x*x/(1*2*3*4*5)
plt.plot(x, y3, color='#FF33CC')

y4=x - x*x*x/(1*2*3)+x*x*x*x*x/(1*2*3*4*5)-x*x*x*x*x*x*x/(1*2*3*4*5*6*7)
plt.plot(x, y4, color='#663300')
plt.show()
