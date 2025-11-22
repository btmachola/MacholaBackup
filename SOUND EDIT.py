# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 08:43:59 2025

@author: B MACHOLA
"""

import numpy as np
from scipy.fftpack import fft
from scipy.io import wavfile

fs,data= wavfile.read('C:/Users/B MACHOLA/Desktop/lv10.wav')
fsl, data1 = wavfile.read('C:/Users/B MACHOLA/Desktop/hv10.wav')

data2=[]
data2=data[1:80000]+data[1:80000]

wavfile.write('mahesh.wav',40000,data2)
b=[]
c=fft(data)
b.append(np.argmax(abs(c)))
print(b)