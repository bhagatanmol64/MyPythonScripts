# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 20:46:25 2019

@author: prakhar
"""
import math

'''File Driver Code'''
x=input("Enter the file code(A or B):")
if x=='A':
    y='_time_mach'
else :
    y='_jane_eyre'
f=open('file'+x+y+'.txt','r',encoding="utf8")
data=f.read()
f.close()

letters={}
for i in range(26):
    letters[chr(65+i)]=0

for l in data:
    if (ord(l)>=65 and ord(l)<91):
        letters[l]+=1
    elif (ord(l)>=97 and ord(l)<123):
        m=chr(ord(l)-32)
        letters[m]+=1


m=sorted(list(letters.values()))
s=sum(m)

num=10

p=[]

for i in range(num):
    n=m[25-i]
    for j in range(26):
        if letters[chr(65+j)]==n:
            print(chr(65+j),"= ", end='')
            print('%.5f' %(n/s))

for i in range(26):
    prob=m[i]/s
    p.append(prob*math.log2(prob))

H=-(sum(p))
print("The Entropy of alphabets in the given file is: ",end='')
print('%.5f'%H)

print("For equiprobableness, Entropy= ",end='')
print('%.5f' %math.log2(26))