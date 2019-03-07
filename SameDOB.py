# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 15:01:14 2019

@author: prakhar
"""

import matplotlib.pyplot as plt
import numpy as np

def f(n):
    if n==0:
        return 1
    else:
        return n*f(n-1)

def f365(n):
    return 1-float(((f(365)/(f(365-n))))/(365**n))

x=list(np.arange(1,366,1))
y=[]

print(f365(365)%100000007)

#for n in x:
#    y.append(f365(n))
#    
#plt.scatter(x,y,marker='.')