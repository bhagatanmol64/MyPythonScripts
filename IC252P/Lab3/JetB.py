import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

def computeProb(d,num):
    return(d['T'][:num][d['T']>=4][d['C']<4].count())/num

# Generate a DataFrame to hold the data. T is for turbine defect, C for compressor defect
d = pd.DataFrame({'T':np.random.randint(1,16,100000),'C':np.random.randint(1,16,100000)})
d['T'][d['T']>6],d['C'][d['C']>6]=4,4

numTrials = sorted([int(10**i) for i in range(1,6)]+[int((10**i)/2) for i in range(1,6)])
plt.plot([math.log10(i) for i in numTrials],[computeProb(d,i) for i in numTrials])
plt.grid()