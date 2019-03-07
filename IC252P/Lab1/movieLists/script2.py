# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 23:32:41 2019

@author: prakhar
"""
x=input("Which file would you like to open?(1,2,3): ")
f=open('list'+x+'.txt','r',encoding="utf8")
data=f.read()
f.close()

data=data.split('\n')
#print(data)

st=[]
et=[]

for l in data:
    if len(l)!=0:
        st.append(l[3:7])
        et.append(l[8:12])

#print(st)
#print(et)
        
m=1

for i in range(i,n)