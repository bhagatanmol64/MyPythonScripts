# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 00:48:00 2019
@author: prakhar
"""

import random
import math

card_faces=[str(i) for i in range(2,11)]+["J","Q","K","A"]
suits=["❤️","♦️","♣️","♠️"]
    
    
deck=[card+suit for suit in suits for card in card_faces]

#Code to find Probability of Winning in this game.
"""
shuffled_deck=deck.copy()
counter=0
for i in range(10000):
    random.shuffle(shuffled_deck)
    for i in range(52):
        if shuffled_deck[i]==deck[i]:
            counter+=1
            break
"""

print("Welcome to the game of:")
print("----------------------")
print("||CARD'S PLACE VALUE||")
print("----------------------")

print("\nAccording to what we have studied in our Probability course, the probability of finding a card in its orginal position in a reshuffled deck can be found by using the Inclusion-Exclusion principle.")
print("First, sum the probabilities of the 'i'th card being in its position then subtract the probabilites of both 'i'th and 'j'th card being in their position. Then once again add the probabilities of 'i'th,'j'th and 'k'th cards being in their original position and so on..")
print("This calculation yields the required probability to be equal to around "+str(1-math.exp(-1))+".")

print("\nNow I am giving you a deck of cards:")
for cards in deck: print(cards,end=' ')

print("\n\nThere is a function in Python which can shuffle this deck.")
print("Like this:")
shuffled_deck=deck.copy()
random.shuffle(shuffled_deck)
for cards in shuffled_deck: print(cards,end=' ')

print("\n\nSo what you have to do is shuffle the deck as many times as you want and then stop anytime.")
print("If there would be a card that is in its original position(as shown in the first deck) then you win. Your score would be equal to the position index of the first card that is in its right position.")
print("So ready? Here we go!")

num=0
while(True):
    num+=1
    print(str(num)+") Shuffle or Play?(S/P)",end="")
    decision=input()
    if decision=="S":
        random.shuffle(shuffled_deck)
        
    elif decision=="P":
        flag=1
        for i in range(52):
            if shuffled_deck[i]==deck[i]:
                print("YOU WIN! Your Score is "+str(i)+"!!")
                flag=0
                break
        if(flag): print("YOU LOSE!")
        break
    
    else: print("I don't get it!")
    
Leaderboard=[]
f=open("Leaderboard.dat","r")
data=f.read().split()
print(data)
f.close()
for d in range(0,len(data)-1,2): Leaderboard.append([d,d+1])

if (not flag):
    decision=input("Would you like to save your score and take a look at your position in our leaderboard?(Y/N)")
    if decision=="Y":
        name=input("Please Enter your 6 characters long username:")
        Leaderboard.append([str(i),name])
        sorted(Leaderboard,key=lambda l:int(l[0]), reverse=True)
        f=open("Leaderboard.dat","w")
        #print(Leaderboard)
        for l in range(len(Leaderboard)): f.write(str(Leaderboard[l][0])+" "+str(Leaderboard[l][1])+"\n")
        f.close()