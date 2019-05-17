"""
Created on Tue May 16 16:56:46 2019
@author: Prakhar
"""
import math
import random
import numpy as np
import matplotlib.pyplot as plt

def N(x, u, s): return 1./(math.sqrt(2.*math.pi)*s)*np.exp(-np.power((x - u)/s, 2.)/2)

def cdf(b):
    N,a=1000,-4

    CDx,CDy=[random.uniform(a,b) for i in range(N)],[random.uniform(0,0.40) for i in range(N)]
    datax,datay=[],[]
    
    for i in range(N):
        gauss=((1/((2*math.pi)**.5))*math.exp((-1)*((CDx[i]**2)/2)))
        if (CDy[i]<gauss):
            datax.append(CDx[i])
            datay.append(CDy[i])
        else:
            continue
    return round((len(datax)/N)*((b-a)*0.4),3)

def Table():
    A=np.arange(-4,4,0.001)
    return A,[cdf(A[i]) for i in range(len(A))]

def inverse(N):
    A,B=Table()
    Sample=[]
    for i in range(N):
        a=round(np.random.uniform(0,1),3)
        if (a in B): Sample.append(A[B.index(a)])
    return(Sample)




n=int(input("Enter n:"))
r=inverse(n)
plt.hist(r)
plt.show()