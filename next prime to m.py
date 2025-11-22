# -*- coding: utf-8 -*-
"""
Created on Sat Jul  5 09:00:53 2025

@author: B MACHOLA
"""
#next prime to m
m=int(input('enter a number'))

i=m
#///while True:
#for i in range(1,m):
 #   mf=[]
 #   for j in range (1,i+1):
 #       #find all factors
 #       if (i%j==0):
  #          mf.append(j)
    #check if array has a third number - a prime will have 2       
   # if len (mf)>2:
        
#        i=i+1
 #       print(i)
#    else:
       # break
#print(i)////
        
m = int(input("Enter a number: "))
i = m + 1  # Start checking from the next number

while True:
    mf = []
    for j in range(1, i + 1):
        if i % j == 0:
            mf.append(j)

    if len(mf) == 2:  # Prime numbers have exactly 2 factors: 1 and itself
        break
    else:
        i += 1

print("Next prime number is:", i)