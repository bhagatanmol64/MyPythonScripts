# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 14:28:59 2018

@author: prakhar
"""

import matplotlib.pyplot as plt
import numpy as np
import random as rd

def Dice():
    x=int(rd.random()*6+1)
    if x==6:
        x+=int(rd.random()*6+1)
        if x==12:
            x+=int(rd.random()*6+1)
            if x==18:
                return 0
    return x


'''
Some other things I might add later:
'''
#series=[]
#n=100
#
#for j in range(n):
#    player1=0
#    player2=0
#    
#    for i in range(216):
#        player1+=(Dice())
#        player2+=(Dice())
#    
#        if(player1>=100): 
#            #print("Player1 Wins!")
#            series.append(0)
#            break
#        elif(player2>=100): 
#            #print("Player2 Wins!") 
#            series.append(1)
#            break
#
#print(series)
#print(int(100*sum(series)/n),"vs",int(100*(1-sum(series)/n)))