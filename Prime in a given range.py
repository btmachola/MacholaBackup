# -*- coding: utf-8 -*-
"""
Created on Sat Jul  5 08:42:02 2025

@author: B MACHOLA
"""

#prime checker2 in range
m=int(input('enter a number'))
n=int(input('enter a 2nd number'))
nf=[]
for i in range(m,n+1):
    mf=[]
    for j in range (1,i+1): 
        if (i%j==0):
            #append all factors 
            mf.append(j)
    # check if prime    
    if len(mf)==2:
        nf.append(i)

print(nf)