# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 08:54:26 2025

@author: B MACHOLA
"""

import numpy as np
import scipy.linalg as lg

A = np.array([[2,3,10,-7], [1, -2,7,2],[7,5,1,-6],[-3,1,-2,15]])
B = np.array([[100], [27],[68],[215]])

C = A + B         # Matrix addition
D = A - B         # Matrix subtraction
P = A.dot(B)      # Matrix multiplication

TR = A.T          # Transpose of A
DET = lg.det(A)   # Determinant of A
inver = lg.inv(A) # Inverse of A

#eigv, eigvec = lg.eig(A)  # Eigenvalues and Eigenvectors
AI= lg.inv(A)
x=AI.dot(B)