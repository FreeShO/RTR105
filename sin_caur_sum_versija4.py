# -*- coding: utf-8 -*-
from math import sin

x = float(input("Lietotaj,lūdzu, ievadi argmentu (x): "))

y = sin(x)

print ("sin(%6.2f) = %6.2f")%(x,y)

k = 0
a = (-1)**0*x**1/(1)
S = a

print "a0 = %6.2f S0 = %6.2f"%(a,S)

k = k + 1
a = a * (-1)*x*x/(2*k)*(2*k+1)
S = S + a

print "a%d = %6.2f a%d = %6.2f"%(k,a,k,S)

k = k + 1
a = a * (-1)*x*x/(2*k)*(2*k+1)
S = S + a

print "a%d = %6.2f a%d = %6.2f"%(k,a,k,S)

k = k + 1
a = a * (-1)*x*x/(2*k)*(2*k+1)
S = S + a

print "a%d = %6.2f a%d = %6.2f"%(k,a,k,S)


  
               
 
