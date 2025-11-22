# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 09:49:19 2025

@author: B MACHOLA
"""

import numpy as np
from scipy.fftpack import fft
from scipy.io import wavfile

fs,data= wavfile.read('C:/Users/B MACHOLA/Desktop/lv10.wav')
fsl, data1 = wavfile.read('C:/Users/B MACHOLA/Desktop/harvard.wav')

data2=[]
data2=data1[1:80000]+data1[1:80000]
data3=data2+data2
data4=data2/2

wavfile.write('mahesh3.wav',20000,data3)
b=[]
c=fft(data)
b.append(np.argmax(abs(c)))
print(b)