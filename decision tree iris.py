# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 10:33:36 2025

@author: B MACHOLA
"""

from sklearn import tree
from sklearn .datasets import load_iris

iris = load_iris()
X=iris.data
y=iris.target

clf = tree.DecisionTreeClassifier()
clf= clf.fit(X,y)
tree.plot_tree(clf)
print(clf.predict([[7,2,2,1],[3,9,7,2]]))
