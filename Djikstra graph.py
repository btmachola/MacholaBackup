# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 09:38:41 2025

@author: B MACHOLA
"""

import sys

class Graph():
    def __init__(self, vertices):
        self.V=vertices
        self.edges= [[0 for column in range(vertices)] 
                     for row in range(vertices)]
        
    def printSolution(self,dist):
        print("vertex distance from source")
        for node in range(self.V):
            print(node,"\t\t", dist[node])
                
    def minDistance(self,dist,tset):
        infi=sys.maxsize
        for u in range(self.V):
            if dist[u]<infi and tset[u] ==False:
                infi=dist[u]
                min_index=u
        return min_index
       
def djikstra(self,src):
    dist=[sys.maxsize]* self.V 
    dist[src]=0
    tset=[False]*self.V
    
    for cout in range(self.V):
        x=self.minDistance(dist,tset)
        tset[x]=True
        print(dist)
        for y in range(self.V):
            if self.edges[x][y]>0 and tset[y]==False and dist[y]>dist[x]+self.edges[x][y]:
                dist[y]=dist[x]+self.edges[x][y]
    
    self.printSolution(dist)
    
g=Graph(6)
g.edges=[ [0,3,2,0,0,0],
              [0,0,0,3,1,0],
              [0,0,0,2,4,5],
              [0,0,0,0,0,6],
              [0,0,0,0,0,2],
              [0,0,0,1,0,0]
        ]
djikstra(g, 0)
    