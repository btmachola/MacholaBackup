# -*- coding: utf-8 -*-
"""
Created on Fri Jul  4 12:39:57 2025

@author: B MACHOLA
"""

def gcd(m,n):
    for i in range(1,min(m,n)+1):
        if (m%i) ==0 and (n%i)==0:
            mahesh=i
    return (mahesh)