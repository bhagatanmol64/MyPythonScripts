# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 00:24:39 2019
@author: prakhar
"""

import numpy as np

#Creating the sample data to be transmitted.
p,q=0.25,0.35
smp = [np.random.randint(2) for i in range(10000)]

#Creating the Channel which follows the assigned probabilities.
out=[int((i and np.random.rand()/q>=1) or ((not i) and np.random.rand()/p<1)) for i in smp]

s1,s2=[],[]
for i in range(10000):
    if smp[i]==0:
        if out[i]==0: s1.append(0)
        else: s1.append(1)
    else:
        if out[i]==1: s2.append(0)
        else: s2.append(1)
                
print(sum(s1)/len(s1),1-(sum(s1)/len(s1)))
print(sum(s2)/len(s2),1-(sum(s2)/len(s2)))