# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 10:48:25 2025

@author: B MACHOLA
"""

#printing Graphs
import numpy as np
import matplotlib.pyplot as plt
t=np.arange(-10,10,0.1)
y1=np.sin(t)
y2=np.cos(t)
y3=np.sin(t)**2
y4=np.exp(t)

figure, axis = plt.subplots(2,2)

axis[0,0].plot(t,y1)
axis[0,0].set_title("sine Function")

axis[0,1].plot(t,y2)
axis[0,1].set_title("Cosine Function")

axis[1,0].plot(t,y3)
axis[1,0].set_title(" square of ine Function")

axis[1,1].plot(t,y4)
axis[1,1].set_ttle("exp Function")


