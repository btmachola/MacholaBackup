# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 11:02:09 2025

@author: B MACHOLA
"""
import numpy as np
import scipy.linalg as lg

A=np.array([[0,1,1,0,0,0],
           [0,0,1,1,0,1],
           [0,0,0,0,1,0],
           [0,0,0,0,1,0],
           [0,0,1,0,0,1],
           [0,0,0,0,0,0],
           ])

A2= A.dot(A)
A3= A2.dot(A)
A4= A3.dot(A)

print(A4)