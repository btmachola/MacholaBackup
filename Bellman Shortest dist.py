# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 10:20:27 2025

@author: B MACHOLA
"""

import sys


class Graph():
    def __init__(self, vertices):
        self.V=vertices
        self.edges= [[0 for _ in range(vertices)] 
                     for _ in range(vertices)]
        
    def printArr(self,dist):   
        print("vertex distance from source")
        for i in range(self.V):
            print("Node",i,"Shortest distance", dist[i])

def Bellmanford(graph,src):
    V=graph.V
    dist=[sys.maxsize]*V
    best_path=[None]*V
    dist[src]=0
    
    for _ in range(V-1):
        for u in range(V):
            for v in range(V):
                if graph.edges[u][v]!=0 and dist[u]!=sys.maxsize:
                    if dist[u]+graph.edges[u][v]<dist[v]:
                        dist[v]=dist[u]+graph.edges[u][v]
                        best_path[v]=u
                        
    for u in range(V):
        for v in range(V):
            if graph.edges[u][v]!=0 and dist[u]!=sys.maxsize:
                if dist[u]+graph.edges[u][v]<dist[v]:
                    print("cyclic redundancy")
                    
    print("shortest distance:",dist)
    print("predecossor:",best_path)

g=Graph(9)
'''g.edges=[[0,3,2,0,0,0],
         [0,0,0,3,1,0],
         [0,0,0,2,4,5],
         [0,0,0,0,0,6],
         [0,0,0,0,0,2],
         [0,0,0,1,0,0],
    ]'''
g.edges=[[0,2,8,7,0,0,0,0,0],
         [3,0,0,0,1,0,0,0,0],
         [0,0,0,7,0,76,0,0,0],
         [0,0,2,0,0,0,8,0,0],
         [0,3,0,0,0,0,0,15,0],
         [0,0,27,0,4,0,0,5,0],
         [0,0,0,0,0,2,0,0,0],
         [0,0,0,0,0,1,0,0,10],
         [0,0,0,0,0,0,1,0,0]
    ]
    
Bellmanford(g,0)
