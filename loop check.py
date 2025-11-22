# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 10:03:30 2025

@author: B MACHOLA
"""

INF=9999

G =[[0,3,2,0,0],
   [3,0,5,1,0],
   [2,5,0,2,8],
   [0,1,2,0,3],
   [0,0,8,3,0]]

V=len (G)
ed=[]
ed1=[]

for i in range(1,V):
    for j in range(V):
        if (G[i][j]):
                 ed.append(G[i][j])
                 ed1.append((i))
ed2 =[val for _, val in sorted(zip(ed,ed1))]
ed3 = sorted(ed)
 
MST=[]