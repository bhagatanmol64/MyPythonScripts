# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:37:29 2019
@author: prakhar
"""

import matplotlib.pyplot as plt
import numpy as np

n=int(input("Enter n:"))
p=float(input("Enter p:"))
N=int(input("Enter N:"))

f=open("binomial_N_n_p.dat",'w',encoding="utf8")
for i in list(np.random.binomial(n,p,size=N)): f.writelines(str(i)+"\n")
f.close()

print("For the given n and N:")
for p in [0.1,0.5,0.9]:
    print("\nHistogram at ",p," is:")
    plt.grid()
    plt.hist(list(np.random.binomial(n,p,size=N)),bins=[i for i in range(0,n,2)])
    plt.show()