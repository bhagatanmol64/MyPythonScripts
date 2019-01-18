# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 20:21:53 2019

@author: prakhar
"""
'''
This script demonstrates the basics of web scraping in Python.
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.hubertiming.com/results/2017GPTR10K"
html = urlopen(url)

soup = BeautifulSoup(html, 'lxml')

print("What would you like to do?")
print("1.Print the title of the webpage!")
print("2.Print all the links present on the webpage.")
print("3.Print first 10 rows of the table.")


n=int(input())

if n==1:
    title=soup.title
    print(title)

elif n==2:
    hyps=soup.find_all('a')
    for link in hyps:
        print(link.get("href"))
        
elif n==3:
    rows=soup.find_all('tr')
    #print(rows[:10])
    
    for row in rows:
        row_td=row.find_all('td')
    
    print(row_td)