# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 11:15:21 2025

@author: B MACHOLA
"""

INF =999
def floydwarshall(dist):
    V=len(dist)
    for k in range(V):
        for i in range(V):
            for j in range(V):
                
                dist[i][j]=min(dist[i][j], dist[i][k]+dist[k][j])
    return(dist)

dist =[[0,3,7,INF,INF],
      [INF,0,1,INF,INF],
      [INF,4,0,INF,4],
      [8,INF,2,0,1],
      [INF,INF,INF,3,0]
      ]

print( floydwarshall(dist))
        