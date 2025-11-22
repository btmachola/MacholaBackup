# -*- coding: utf-8 -*-
"""
Created on Sat Jul  5 10:22:57 2025

@author: B MACHOLA
"""
#finding x
#x=int(input('enter your monthly sub'))
y=int(input('enter a interest rate'))
z=int(input('enter duration, in months'))
w=int(input('enter annual increment in subscription'))

for x in range (10000,50000,10):
    print(x)
    amount=0
    for i in range (1,z):
        if(i%12==0):
            x=x+w
        amount = amount+x*((1+y/1200)**i)
    
    if amount>50000000:
        break
    