# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 10:40:36 2025

@author: B MACHOLA
"""

import pandas
df = pandas.read_csv("C:/Users/B MACHOLA/dsop.csv")

df['roi']=4.00
df['net amount']=0
for i in range(12,120):
    roi=0.000
    for j in  range (0,12):
        roi=roi+df.iloc[i+j-12,1]
    df.loc[i,'roi']=4.00+round(roi/50,2)
    
aa=0
for i in range(0,120):
     aa=aa+df.loc[i,'gpf_subs']
     aa = aa - (df.loc[i,'gpf_withdrawal']) * (1 + df.loc[i,'roi'] / 1200)
     df.loc[i, 'net amount'] = round(aa, -1)

TS = df.iloc[:,2].sum(axis=0)
TW = df.iloc[:,3].sum(axis=0)
 
print('TOTAL SUBSCRIPTION IS ',TS) 
print('TOTAL withdrawal IS ',TW) 
print('BALANCE IS ',round(aa,1)) 