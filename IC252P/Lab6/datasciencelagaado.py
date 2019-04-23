# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 15:01:16 2019
@author: prakhar
"""
import pandas as pd
import numpy as np
import scipy.stats as st

def vterm(c): return data[col[c]]-data[col[c]].mean()
def cov(c1,c2): return sum(vterm(c1)*vterm(c2))/(n-1)
def std(c): return cov(c,c)**(1/2)
def r(c1,c2): return cov(c1,c2)/(std(c1)*std(c2))
def line(): return("\n-------------------------")
def is_ind(c1,o1,v1,c2,o2,v2,data):
    if o1=="<=" and o2=="<=":A,B,AB=data[data[c1]<=v1][c1].count(),data[data[c2]<=v2][c2].count(),data["Date"][(data[c1]<=v1) & (data[c2]<=v2)].count()
    elif o1=="<=" and o2==">":A,B,AB=data[data[c1]<=v1][c1].count(),data[data[c2]>v2][c2].count(),data["Date"][(data[c1]<=v1) & (data[c2]>v2)].count()
    elif o1==">" and o2=="<=":A,B,AB=data[data[c1]>v1][c1].count(),data[data[c2]<=v2][c2].count(),data["Date"][(data[c1]>v1) & (data[c2]<=v2)].count()
    elif o1==">" and o2==">":A,B,AB=data[data[c1]>v1][c1].count(),data[data[c2]>v2][c2].count(),data["Date"][(data[c1]>v1) & (data[c2]>v2)].count()
    if(A*B==n*AB): print("Event("+c1+o1+str(v1)+") and Event("+c2+o2+str(v2)+") are independent.")
    else: print("Event("+c1+o1+str(v1)+") \tand Event("+c2+o2+str(v2)+")\t are dependent.")

data=pd.read_csv("medical_expenditure.csv")#Reading from the CSV file.
col=list(data.columns)#Indexing the columns of data.
n=data["Date"].count()#Counting the number of rows in data.

'''Checking the independence'''
print("\nChecking the Independence:-"+line())
is_ind("Nmale","<=",93,col[21],"<=",504,data)
is_ind("Nfemale","<=",131,col[21],"<=",504,data)
is_ind("Nage-group2","<=",25,col[21],">",504,data)
is_ind("Nage-group2","<=",25,col[21],">",504,data)
is_ind("Nregion5","<=",53,col[21],">",504,data)

'''Finding the covariances'''
print("\nValues of covariance:-"+line())
for i in [1,2,13,14,16]: print("cov("+col[i]+","+col[21]+"):\t",cov(i,21))
print("\nValues of covariance using numpy.cov():-"+line())
for i in [1,2,13,14,16]: print("cov("+col[i]+","+col[21]+"):\t",np.cov(list(data[col[i]]),list(data[col[21]]))[0][1])

'''Finding Pearson's Correlation Coefficients'''
print("\nCorrelation coefficients:-"+line())
for i in [1,2,13,14,16]: print("r("+col[i]+","+col[21]+"):\t",r(i,21))
print("\nCorrelation coefficients using scipy.stats.pearsonr():-"+line())
for i in [1,2,13,14,16]: print("r("+col[i]+","+col[21]+"):\t",st.pearsonr((data[col[i]]),(data[col[21]]))[0])