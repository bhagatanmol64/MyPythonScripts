# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 11:11:59 2019
@author: Prakhar
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import multivariate_normal


def mean(c): return sum(c)/len(c)
def vterm(c): return [i-mean(c) for i in c]
def cov(c1,c2): return sum([(c1[i]-mean(c1))*(c2[i]-mean(c2)) for i in range(len(c1))])/(len(c1)-1)
def std(c): return cov(c,c)**(1/2)
def r(c1,c2): return cov(c1,c2)/(std(c1)*std(c2))

f=open("data.txt","r")
data=f.read().split()
f.close()
data=[[float(i.split(',')[0]),float(i.split(',')[1])] for i in data]
x=[i[0] for i in data]
y=[i[1] for i in data]

plt.scatter(x,y)
plt.show()

print("Mean:\n",np.array([mean(x),mean(y)]).reshape(2,1),"\n")
print("Covariance Matrix:\n",np.array([cov(i,j) for j in [x,y] for i in [x,y]]).reshape(2,2))

gx,gy=np.random.multivariate_normal(np.array([0,0]),np.array([[1,0],[0,1]]),100).T
fx,fy=np.random.multivariate_normal(np.array([2.5,2.5]),np.array([[0.5,0],[0,0.5]]),100).T

d1 = multivariate_normal(mean=[0,0], cov=[[1,0],[0,1]])
pdf1=[(d1.pdf(i)) for i in data]
plt.scatter([i for i in range(2000)],pdf1)

d2 = multivariate_normal(mean=[2.5,2.5], cov=[[0.5,0],[0,0.5]])
pdf2=[(d2.pdf(i)) for i in data]
plt.scatter([i for i in range(2000)],pdf2)