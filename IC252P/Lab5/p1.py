# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 23:33:09 2019
@author: prakhar
"""

import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

#Creating the sample data to be transmitted.
p,q=0.25,0.35
sample = [np.random.randint(2) for i in range(10000)]

#Creating the Channel which follows the assigned probabilities.
out=[int((i and np.random.rand()/q>=1) or ((not i) and np.random.rand()/p<1)) for i in sample]

sig=[0,1]
results=[1-(sum(out)/len(out)),sum(out)/len(out)]

custm=st.rv_discrete(name='custm', values=(sig, results))
fig, ax = plt.subplots(1, 1)
ax.plot(sig, custm.pmf(sig), 'ro', ms=8, mec='r')
ax.vlines(sig, 0, custm.pmf(sig), colors='r', linestyles='-', lw=3)
plt.title('PMF of Y')
plt.ylabel('Probability')
plt.show()

#Printing The Probabilites of recieved data.
print("p(Y = 0) = p(Y = 0|X = 0)p(X = 0) + p(Y = 0|X = 1)p(X = 1)=0.55")
print("p(Y = 1) = p(Y = 1|X = 0)p(X = 0) + p(Y = 1|X = 1)p(X = 1)=0.45")
print()
print("P(Y=0) according to the data:",results[0])
print("P(Y=1) according to the data:",results[1])