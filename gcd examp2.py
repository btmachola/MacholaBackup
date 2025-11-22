# -*- coding: utf-8 -*-
"""
Created on Fri Jul  4 13:22:00 2025

@author: B MACHOLA
"""

def gcd(m,n,i):
    if m<n:
        (m,n)=(n,m)
        
    print('count',i)  
    print('first number',m)
    print('second number',n)
    i=i+1
    
    if (m%n==0):
        return(n)
    else:
        return(gcd(n,m%n,i))
    