import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

def computeProb(d,num):
    return(d['T'][:num][d['C']+d['T']>8][d['T']>=4].count())/(d['T'][:num][d['C']+d['T']>8].count())

# Generate a DataFrame to hold the data. T is for turbine defect, C for compressor defect
d = pd.DataFrame({'T':np.random.randint(1,7,100000),'C':np.random.randint(1,7,100000)})

numTrials = sorted([int(10**i) for i in range(1,6)]+[int((10**i)/2) for i in range(1,6)])
plt.plot([math.log10(i) for i in numTrials],[computeProb(d,i) for i in numTrials])
plt.grid()