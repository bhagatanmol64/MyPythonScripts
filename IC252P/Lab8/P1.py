"""
Created on Tue May 14 22:03:46 2019
@author: Prakhar
"""
import math
import matplotlib.pyplot as plt
import numpy as np

"""PDF of Gaussian distribution"""
def N(x, u, s): return 1./(math.sqrt(2.*math.pi)*s)*np.exp(-np.power((x - u)/s, 2.)/2)

"""Taking the inputs."""
n=int(input("Enter the number of data points:"));a,b=map(int,input("Enter the boundaries of interval(a&b):\n").split())

"""Monte Carlo Sampling over n data points."""
sx=[[np.random.random()*(max(a,b)-min(a,b))+min(a,b),np.random.random()] for i in range(n)]
uc,ac=[sx[i] for i in range(n) if sx[i][1]<=N(sx[i][0],0,1)],[sx[i] for i in range(n) if sx[i][1]> N(sx[i][0],0,1)]

"""Plotting the distribution and data points."""
plt.scatter([i[0] for i in ac],[i[1] for i in ac],color="yellow");plt.scatter([i[0] for i in uc],[i[1] for i in uc],color="red")
plt.plot(np.linspace(-4, 4, 1000),N(np.linspace(-4, 4, 1000), 0,1))
print("\nThe area under the curve is",len(uc)*(max(a,b)-min(a,b))/n)