# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 09:21:22 2025

@author: B MACHOLA
"""

import sys

class Graph():
    def __init__(self, vertices):
        self.V=vertices
        self.edges= [[0 for column in range(vertices)] 
                     for row in range(vertices)]
        