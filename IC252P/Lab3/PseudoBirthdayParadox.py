import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

c=input("Choose an option(A,B,C,D):")


if c=='A':
    num=365
    d=list(np.random.randint(1,366,365))
    f=[len(list(filter(None,["*"*(d[:n].count(el)-1) for el in set(d[:n])]))) for n in range(1,num+1)]
    plt.plot(np.arange(1,num+1,1),f)

    print("The value of c at n=23:",f[23])

elif c=='B':
    num=365
    d=list((np.random.randint(0,514,365)%365)+1)
    f=[len(list(filter(None,["*"*(d[:n].count(el)-1) for el in set(d[:n])]))) for n in range(1,num+1)]
    plt.plot(np.arange(1,num+1,1),f)
    
elif c=='C':
    num=365
    d=list(np.random.randint(1,688,365))
    f=[len(list(filter(None,["*"*(d[:n].count(el)-1) for el in set(d[:n])]))) for n in range(1,num+1)]
    plt.plot(np.arange(1,num+1,1),f)
    
    print("The value of c at n=33:",f[33])
    
elif c=='D':
    p=0
    for c in range(100):
        d=list(np.random.randint(1,366,365))
        if len(list(filter(None,["*"*(d[:50].count(el)-1) for el in set(d[:50])])))>=1: p+=1
        
    print("The probability of c>=1 in n=50 is:",p/100)