# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 10:23:26 2025

@author: B MACHOLA
"""

from sklearn import tree

X=([[82,76],[83,74],[81,78],[85,73],[87,82],[79,78],[77,76],[79,69]])

Y=([1,0,1,0,1,0,0,0])

model = tree.DecisionTreeClassifier()
model = model.fit(X,Y)
tree.plot_tree(model)