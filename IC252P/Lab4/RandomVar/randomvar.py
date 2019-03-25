# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 17:31:33 2019
@author: prakhar
"""

import numpy as np

Y=[]
for i in [int(np.random.random()*10)+1 for i in range(1000)]:
    if i==1:        Y.append(1)
    if i>1 and i<4: Y.append(2)
    if i>=4:        Y.append(3)

for i in range(1,4):
  print(i,"occurs with probabiity",Y.count(i)/len(Y))