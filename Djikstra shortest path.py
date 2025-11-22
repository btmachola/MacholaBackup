# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 09:07:05 2025

@author: B MACHOLA
"""

import sys

class Graph():
    def __init__(self, vertices):
        self.V=vertices
        self.edges= [[0 for column in range(vertices)] 
                     for row in range(vertices)]
        self.bp= [[0 for column in range(vertices)] 
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
    bp= [0 for column in range(self.V)]
    
    for cout in range(self.V):
        x=self.minDistance(dist,tset)
        tset[x]=True
        print(dist)
        for y in range(self.V):
            if self.edges[x][y]>0 and tset[y]==False and dist[y]>dist[x]+self.edges[x][y]:
                dist[y]=dist[x]+self.edges[x][y]
                bp[y]=x
    self.printSolution(dist)
    print(bp)
    
g=Graph(9)
g.edges=[ [0,2,8,7,0,0,0,0,0],
              [3,0,0,0,1,0,0,0,0],
              [0,0,0,7,0,76,0,0,0],
              [0,0,2,0,0,0,8,0,0],
              [0,3,0,0,0,0,0,15,0],
              [0,0,27,0,4,0,0,5,0],
              [0,0,0,0,0,2,0,0,0],
              [0,0,0,0,0,1,0,0,10],
              [0,0,0,0,0,0,1,0,0]
        ]
djikstra(g, 0)