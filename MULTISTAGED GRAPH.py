# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 09:42:00 2025

@author: B MACHOLA
"""

def shortestDist(graph):
    dist =[0]*N
    for i in range (N-2,-1,-1):
        dist[i]=INF
        for j in range(N):
            if graph[i][j]==INF:
                continue
            
            dist[i]= min(dist[i],graph[i][j]+dist[j])
    
    
    return dist[0]

N=16
INF=99999

graph =[[INF,2,1,5,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF],
        [INF,INF,INF,INF,9,1,7,3,INF,INF,INF,INF,INF,INF,INF,INF,INF],
        [INF,INF,INF,INF,3,9,0,7,INF,INF,INF,INF,INF,INF,INF,INF],
        [INF,INF,INF,INF,3,5,2,1,INF,INF,INF,INF,INF,INF,INF,INF],
        [INF,INF,INF,INF,INF,INF,INF,3,2,9,5,INF,INF,INF,INF,INF],
        [INF,INF,INF,INF,INF,INF,INF,5,6,4,1,INF,INF,INF,INF,INF],
        [INF,INF,INF,INF,INF,INF,INF,10,19,7,24,INF,INF,INF,INF,INF],
        [INF,INF,INF,INF,INF,INF,INF,8,0,4,2,INF,INF,INF,INF,INF,INF],
        [INF,INF,INF,INF,INF,INF,INF,INF,INF,4,7,6,INF,INF,INF,INF],
        [INF,INF,INF,INF,INF,INF,INF,INF,INF,8,12,2,INF,INF,INF,INF],
        [INF,INF,INF,INF,INF,INF,INF,INF,INF,11,10,4,INF,INF,INF,INF],
        [INF,INF,INF,INF,INF,INF,INF,INF,INF,5,6,17,INF,INF,INF,INF],
        [INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,8,INF,INF],
        [INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,15,INF,INF],
        [INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,7,INF,INF],
        [INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF]
        ]