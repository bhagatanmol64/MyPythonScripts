# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 00:15:35 2019

@author: prakhar
"""
def fact(n):
    if(n==0):
        return(1)
    else:
        return(n*fact(n-1))
def com(n,r):
    return(fact(n)/(fact(r)*fact(n-r)))
su=0

for i in range(300):
    su+=com(1800,i)/pow(5,i)
su*=pow(5/6,1800)
print(1-su)