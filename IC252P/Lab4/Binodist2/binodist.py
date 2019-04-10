# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:37:29 2019
@author: prakhar
"""

import matplotlib.pyplot as plt
import numpy as np

def fact(n):
    if n==0: return 1
    else: return n*fact(n-1)

def comb(n,k):
    return fact(n)/(fact(k)*fact(n-k))

N,n =500,10

x=[]
for p in [0.2,0.8]:
    f=open("binomial_N_n_"+str(p)+".dat",'w',encoding="utf8")
    d=list(np.random.binomial(n,p,size=N))
    x.append(d)
    for i in d: f.writelines(str(i)+"\n")
    f.close()

p1,p2=0.2,0.8

data=np.array([[comb(n,i)*(p1**i)*((1-p1)**(n-i)) for i in x[0]],
               [comb(n,i)*(p2**i)*((1-p2)**(n-i)) for i in x[0]],
               [comb(n,i)*(p1**i)*((1-p1)**(n-i)) for i in x[1]],
               [comb(n,i)*(p2**i)*((1-p2)**(n-i)) for i in x[1]]])

plt.grid()
for lis in data: 
    print(lis)
    plt.hist(lis)