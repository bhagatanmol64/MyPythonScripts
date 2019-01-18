# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 22:21:26 2019

@author: prakhar
"""
'''
This script extracts all the current news headline articles present on the site of The Hindu Newspaper.
'''
import pandas as pd

from urllib.request import urlopen
from bs4 import BeautifulSoup

url="https://www.thehindu.com"
html=urlopen(url)

soup = BeautifulSoup(html, 'lxml')

hyps=soup.find_all('a')
l=[]
for link in hyps:
        a=str(link.get('href'))
        for i in range(len(a)):
            if a[i:i+4]=='.ece':
                l.append(a[24:])
                break
        

head=[]
for i in l:
    n=len(i)
    for j in range(len(i)):
        if i[n-1-j]=='/':
            a=j
            break
    for j in range(a+1,len(i)):
        if i[n-1-j]=='/':
            b=j
            break    
    head.append(i[n-b:n-1-a])

nhead=[]
for word in head:
    sen=word.split('-')
    temp=''
    for i in range(len(sen)):
        temp+=sen[i]
        temp+=' '
    nhead.append(temp)

nset=set(nhead)
nlist=list(nset)

data=pd.Series(data=nlist,index=None,dtype=str)
print(data)