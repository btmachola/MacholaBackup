# -*- coding: utf-8 -*-
"""
Created on Fri Jul  4 13:57:13 2025

@author: B MACHOLA
"""
#prime checker
m=int(input('enter a number'))
fm=[]
for i in range(1,m+1):
    if (m%i)==0:
        fm.append(i)
        
if len(fm)==2:
    print('m is a prime')
else:
    print('m is not prime')