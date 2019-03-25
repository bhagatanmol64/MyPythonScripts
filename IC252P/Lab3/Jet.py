import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

def computeProb(d,num):
    #returning the required conditional probability ie Count of Turbines failing the scrutiny
    #Under the condition when compressor passing the scrutiny
    
    return(d['T'][:num][d['T']>=4][d['C']<4].count())/num

# Generate a DataFrame to hold the data. T is for turbine defect, C for compressor defect
d = pd.DataFrame({'T':np.random.randint(1,7,100000),'C':np.random.randint(1,7,100000)})

#Creating list of number of trials

numTrials = sorted([int(10**i) for i in range(1,6)]+[int((10**i)/2) for i in range(2,6)])

#plotting the graph for various number of trials and their corresponding required probabilities
plt.plot([math.log10(i) for i in numTrials],[computeProb(d,i) for i in numTrials],marker='.')

plt.grid()
plt.xlabel('log(numberoftrials) ==>')
plt.ylabel('Cond. Probab. for particular number of trials==>')
plt.axhline(0.25,linestyle='dashed',alpha=0.5)
plt.text(3.3, 0.25, '0.25', fontsize=10, va='center', ha='center')
plt.title('Experiment',fontsize=20)
