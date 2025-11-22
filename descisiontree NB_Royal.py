# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 08:45:17 2025

@author: B MACHOLA
"""


import math as mt

def ent2(a,b):
    p,q = a/(a+b), b/(a+b)
    return -(p*mt.log2(p)+q*mt.log2(q))
    
def gini2(a,b):
    p,q = a/(a+b), b/(a+b)
    return 1-p*2-q*2

def ent3(a,b,c):
    p,q,r = a/(a+b+c), b/(a+b+c), c/(a+b+c)
    return -(p*mt.log2(p)+q*mt.log2(q)+r*mt.log2(r))

def gini3(a,b,c):
    p,q,r = a/(a+b+c), b/(a+b+c), c/(a+b+c)
    return 1-p*2-q**2-r*2