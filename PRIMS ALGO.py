# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 09:02:31 2025

@author: B MACHOLA
"""
INF=9999

#G =[[0,99,75,0,0],
 #   [99,0,95,19,42],
 #   [75,95,5,1,66],
 #   [0,19,51,0,31],
 #   [0,42,66,31,0]]
 
 
 
 

G =[[0,3,2,0,0],
   [3,0,5,1,0],
   [2,5,0,2,8],
   [0,1,2,0,3],
   [0,0,8,3,0]]

V=len (G)
selected=[0,0,0,0,0]
no_edge=0
selected[0]=True
print("Edge: Weight \n")
while(no_edge<V-1):
    
    minimum=INF
    x=0
    y=0
    
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if ((not selected[j]) and G[i][j]):
                    if minimum > G[i][j]:
                        minimum= G[i][j]
                        x=i
                        y=j
    print((str(x))+"-"+ str(y)+":" +str(G[x][y]))
    selected[y]=True
    no_edge+=1
    