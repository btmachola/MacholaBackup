# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 10:17:50 2025

@author: B MACHOLA
"""

#printing Graphs
import numpy as np
import matplotlib.pyplot as plt
t=np.arange(-10,10,0.1)
sinamp=np.sin(t)
cosamp=np.cos(t)

plt.plot(t,sinamp,color='r')
plt.plot(t,cosamp)
plt.title('sin(t) and cos(t) graph')
plt.xlabel('t')
plt.ylabel('sin(t) and cos(t)')
plt.grid(axis='y')
plt.axhline(y=0, color='r')
plt.axvline(x=0, color='g')
plt.legend(["sin(t)","cos(t)"])
plt.ylim(-2,2)