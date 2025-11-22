# -*- coding: utf-8 -*-
"""
Created on Sat Jul  5 09:32:08 2025

@author: B MACHOLA
"""

x=int(input('enter your monthly sub'))
y=int(input('enter a interest rate'))
z=int(input('enter duration, in months'))
amount=0
for i in range (1,z+1):
    amount = amount+x*(1+y/1200)**i
    
print(round(amount,-1))
    