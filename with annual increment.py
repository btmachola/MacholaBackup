# -*- coding: utf-8 -*-
"""
Created on Sat Jul  5 09:53:51 2025

@author: B MACHOLA
"""
#annual increment
x=int(input('enter your monthly sub'))
y=int(input('enter a interest rate'))
z=int(input('enter duration, in months'))
w=int(input('enter annual increment in subscription'))
amount=0
for i in range (1,z):
    if(i%12==0):
        x=x+w
    amount = amount+x*((1+y/1200)**i)
    print(amount)

print('Total amount you receive in', z+1,'month is', amount)
    
 
 