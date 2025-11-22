# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 11:07:28 2025

@author: B MACHOLA
"""

import numpy as np
import scipy.linalg as lg

A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 5], [4, 7]])

C = A + B         # Matrix addition
D = A - B         # Matrix subtraction
P = A.dot(B)      # Matrix multiplication

TR = A.T          # Transpose of A
DET = lg.det(A)   # Determinant of A
inver = lg.inv(A) # Inverse of A

eigv, eigvec = lg.eig(A)  # Eigenvalues and Eigenvectors