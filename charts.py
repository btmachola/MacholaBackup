# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 11:09:39 2025

@author: B MACHOLA
"""

#printing Graphs
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(1,11)
y=np.array([7,12,9,2,5,6,15,8,2,8])
plt.plot(x,y)
#plt.bar(x,y,color='r')
#plt.barh(x,y,color='green')
plt.pie(y)
names=['Mahesh','Ramesh','Suresh','Naresh',
       'Rajesh','Ram','Bhim','Som','Arjun','Yagesh']
me=[0.3,0,0,0,0,0,0.2,0,0,0]
plt.pie(y,labels=names)
plt.pie(y,labels=names,explode=me)

       
