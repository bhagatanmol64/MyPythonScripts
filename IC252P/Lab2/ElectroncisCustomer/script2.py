# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 15:51:43 2019

@author: prakhar
"""

import pandas as pd

data=pd.read_csv('AllElectronicsCustomer.csv')

'''a)'''
yes=data[data['Class: Buys_Computer']=='Yes']
no=data[data['Class: Buys_Computer']=='No']
print("Prior probability of Buy's computer:Yes",yes['Class: Buys_Computer'].count()/data['Age'].count())
print("Prior probability of Buy's computer:No ",no['Class: Buys_Computer'].count()/data['Age'].count())
print()

'''b)'''
name=list(data.columns)[1:-1]
parameters=list(set(data[i]) for i in name)

i=0
for x in parameters:
    for y in x:
        ayes=yes[name[i]][yes[name[i]]==y].count()
        ano=no[name[i]][no[name[i]]==y].count()
        print("Prob. of ",name[i]+":",y,"given Buy's computer:Yes= ","%.4f" %(ayes/yes[name[i]].count()))
        print("Prob. of ",name[i]+":",y,"given Buy's computer:No = ","%.4f" %(ano/no[name[i]].count()))
        print()
    i+=1