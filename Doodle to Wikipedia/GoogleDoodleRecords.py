# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 01:03:15 2019

@author: prakhar
"""

import datetime as dt

from urllib.request import urlopen
from bs4 import BeautifulSoup

url="https://www.google.co.in"
html=urlopen(url)

soup = BeautifulSoup(html, 'lxml')

hyps=soup.find_all('a')

l=[]
for link in hyps:
        a=str(link.get('href'))
        for i in range(len(a)):
            if a[i:i+11]=='search?site':
                l.append(a)

sense=[]
for link in l:
    for i in range(len(link)):
        if link[i:i+2]=='q=':
            flag=i
            break
    phrase=''
    for j in range(flag+2,len(link)):
        if link[j]=='&': break
        
        if link[j]=='+': phrase+='_'
        else: phrase+=link[j]
    
    sense.append(phrase)
        
with open('wiki.dat','a') as file:
    file.write(str(dt.date.today())+": ")
    file.write("https://en.wikipedia.org/wiki/"+sense[0]+'\n')
