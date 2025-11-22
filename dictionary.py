# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 10:28:24 2025

@author: B MACHOLA
"""

OACT1=['rahul','dinesh','rajanish','deepak']
OACT2=('rahul','dinesh','rajanish','deepak')
OACT3={'rahul','dinesh','rajanish','deepak'}

OACT3.add('suresh')
OACT3.remove('rajanish')
OACT1.insert(2,'rama')
OACT1.remove('rama')       

CSDEPT={
        100:'PRAMAD',
        20: 'Harmeet',
        3:'Anuj',
        25:'Palash',
        5:'Mahesh'
        } 

for keys,values in CSDEPT.items():
    if values=='Palash':
        print(keys)
        
CSDK= list(CSDEPT.keys())
CSDK.sort()
CSDEPT_NEW={i: CSDEPT[i] for i in CSDK}
Number=['43561','2391','32559','64393','98266']
Name=['Ramesh','Suresh','Naresh','Mahesh','Rajesh']
FEL=dict(zip(Number,Name))
FEL.pop('2391')
FEL['IC2391']='Vijay'
movies={'kushi':(2000,'pk','bhumika','surya'),
        'kushi2':(2045,'pk','bhumika','surya'),
        'kushi3':(2001,'pk','bhumika','surya')     
        }

for key,value in movies.items():
    if value[0]<2005:
        print(key)