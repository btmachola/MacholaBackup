# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 09:51:03 2025

@author: B MACHOLA
"""

#complex equations
#2x**2-5x+3=0
L=int(input('enter lower limit'))
U=int(input('enter upper limit'))
#d=float(input('enter the size of the strip'))

sol=[]
import math as mt


for i in range (L*100,U*100):
    i=i/10
    print(i)
    f= i**3-3*i**2-i+3
    if round(f,2)==0:
        sol.append(i)
    
print(sol)