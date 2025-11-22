# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 08:53:51 2025

@author: B MACHOLA
"""
#integration of area under a graph
L=int(input('enter lower limit'))
U=int(input('enter upper limit'))
d=float(input('enter the size of the strip'))

import math as mt
N=int(1/d)
sum=0

for i in range (L*N,U*N):
    i=i/N
    print(i)
    f1=mt.exp(i**2)
    f2=mt.exp((i+d)**2)
    sum=sum+d*(f1+f2)/2
    
print(sum)