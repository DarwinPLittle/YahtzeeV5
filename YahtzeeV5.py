# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 15:12:16 2021

@author: darwi
"""

from random import *

def Roll():
    global roll
    roll = [randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)]
    
def Result():
    global roll
    roll.sort()
    print(roll)
    
def Reroll():
    print("Please input the positions of the dice you wish to reroll.")
    user = input()
    user = user.split()
    for i in user:
        try:
            i = int(i)
            if i > 0 and i < 6:
                roll[i - 1] = randint(1, 6)
                print("Successfully rerolled.")
            else:
                print("Input falls outside of range (1 throught 5).")
        except:
            print("Error, input was not a number.")
            
def Card1():
    print("[0] Ones", score1[0])
    print("[1] Twos", score1[1])
    print("[2] Threes", score1[2])
    print("[3] Fours", score1[3])
    print("[4] Fives", score1[4])
    print("[5] Sixes", score1[5])
    print("... Bonus", score1[6])
    print("[7] Three-of-a-Kind", score1[7])
    print("[8] Four-of-a-Kind", score1[8])
    print("[9] Full House", score1[9])
    print("[10]Sm. Straight", score1[10])
    print("[11]Lg. Straight", score1[11])
    print("[12]Chance", score1[12])
    print("[13]Yahtzee!", score1[13])
    print("[14]Bonus Yahtzee!", score1[14])
    
def Card2():
    print("[0] Ones", score2[0])
    print("[1] Twos", score2[1])
    print("[2] Threes", score2[2])
    print("[3] Fours", score2[3])
    print("[4] Fives", score2[4])
    print("[5] Sixes", score2[5])
    print("... Bonus", score2[6])
    print("[7] Three-of-a-Kind", score2[7])
    print("[8] Four-of-a-Kind", score2[8])
    print("[9] Full House", score2[9])
    print("[10]Sm. Straight", score2[10])
    print("[11]Lg. Straight", score2[11])
    print("[12]Chance", score2[12])
    print("[13]Yahtzee!", score2[13])
    print("[14]Bonus Yahtzee!", score2[14])  
    
    
score1 = ["__", "__", "__", "__", "__", "__", 0, "__", "__", "__", "__", "__", "__", "__", "__"]
yahtzee1 = False
score2 = ["__", "__", "__", "__", "__", "__", 0, "__", "__", "__", "__", "__", "__", "__", "__"]
yahtzee2 = False

while score1.count("__") > 0:
    print("Player 1's turn!")
    print("Score card:")
    Card1()
    
    Roll()
    Result()
    Reroll()
    Result()
    Reroll()
    Result()
    spread = [roll.count(1), roll.count(2), roll.count(3), roll.count(4), roll.count(5), roll.count(6)]
    

    assign = float("inf")
    while assign == float("inf"):
        print("Please choose where to assign your dice:")
        Card1()
        assign = input()
        try:
            assign = int(assign)
            if assign == 6:
                print("You cannot assign a score to bonus.")
                assign = float("inf")
            else:
                if assign >= 0 and assign <= 14:
                    if score1[assign] == "__":
                        print("Successfully assigned.")
                    else:
                        print("That spot is already filled.")
                        assign = float("inf")
                else:
                    print("Input falls outside of range.")
                    assign = float("inf")
        except:
            print("Input was not a number.")
            assign = float("inf")
            
#The following is the bulk of the program.
#It is a series of tests for each possible position.

    if assign <= 5:
        score1[assign] = spread[assign] * (assign + 1)
        
    if score1[0: 6].count("__") == 0:
        if sum(score1[0: 6]) >= 63:
            score1[6] = 35
        
    if assign == 7:
        spread.sort()
        sixth = spread[5]
        if sixth >= 3:
            score1[7] = sum(roll)
        else:
            score1[7] = 0
           
    if assign == 8:
        spread.sort()
        sixth= spread[5]
        if sixth >= 4:
            score1[8] = sum(roll)
        else:
            score1[8] = 0
        
    if assign == 9:
        spread.sort()
        sixth = spread[5]
        fifth = spread[4]
        if sixth == 3 and fifth == 2:
            score1[9] = 25
        else:
            score1[9] = 0
            
    if assign == 10:
        #Test if roll has (1, 2, 3, 4), (2, 3, 4, 5), or (3, 4, 5, 6)
        if (spread[0] > 0 and spread[1] > 0 and spread[2] > 0 and spread[3] > 0) or (spread[1] > 0 and spread[2] > 0 and spread[3] > 0 and spread[4] > 0) or (spread[2] > 0 and spread[3] > 0 and spread[4] > 0 and spread[5] > 0):
            score1[10] = 30
        else:
            score1[10] = 0
            
    if assign == 11:
        #Test if roll has (1, 2, 3, 4, 5) or (2, 3, 4, 5, 6)
        if (spread[0] > 0 and spread[1] > 0 and spread[2] > 0 and spread[3] > 0 and spread[4] > 0) or (spread[1] > 0 and spread[2] > 0 and spread[3] > 0 and spread[4] > 0 and spread[5] > 0):
            score1[11] = 40
        else:
            score1[11] = 0
            
    if assign == 12:
        score1[12] = sum(roll)
        
    if assign == 13:
        spread.sort()
        sixth = spread[5]
        if sixth == 5:
            score1[13] = 50
            yahtzee1 = True
        else:
            score1[13] = 0
            
    if assign == 14:
        spread.sort()
        sixth = spread[5]
        if sixth == 5 and yahtzee1 == True:
            score1[14] = 100
        else:
            score1[14] = 0
            
    #Player 2's turn is a duplicate except the variables score and yahtzee change
    
    print("Player 2's turn!")
    print("Score card:")
    Card2()
    
    Roll()
    Result()
    Reroll()
    Result()
    Reroll()
    Result()
    spread = [roll.count(1), roll.count(2), roll.count(3), roll.count(4), roll.count(5), roll.count(6)]
    

    assign = float("inf")
    while assign == float("inf"):
        print("Please choose where to assign your dice:")
        Card2()
        assign = input()
        try:
            assign = int(assign)
            if assign >= 0 and assign <= 14:
                if score2[assign] == "__":
                    print("Successfully assigned.")
                else:
                    print("That spot is already filled.")
                    assign = float("inf")
            else:
                print("Input falls outside of range.")
                assign = float("inf")
        except:
            print("Input was not a number.")
            assign = float("inf")
            
#The following is the bulk of the program.
#It is a series of tests for each possible position.

    if assign <= 5:
        score2[assign] = spread[assign] * (assign + 1)
        
    if score1[0: 6].count("__") == 0:        
        if sum(score2[0: 6]) >= 63:
            score2[6] = 35
        
    if assign == 7:
        spread.sort()
        sixth = spread[5]
        if sixth >= 3:
            score2[7] = sum(roll)
        else:
            score2[7] = 0
           
    if assign == 8:
        spread.sort()
        sixth = spread[5]
        if sixth >= 4:
            score2[8] = sum(roll)
        else:
            score2[8] = 0
        
    if assign == 9:
        spread.sort()
        sixth = spread[5]
        fifth = spread[4]
        if sixth == 3 and fifth == 2:
            score2[9] = 25
        else:
            score2[9] = 0
            
    if assign == 10:
        #Test if roll has (1, 2, 3, 4), (2, 3, 4, 5), or (3, 4, 5, 6)
        if (spread[0] > 0 and spread[1] > 0 and spread[2] > 0 and spread[3] > 0) or (spread[1] > 0 and spread[2] > 0 and spread[3] > 0 and spread[4] > 0) or (spread[2] > 0 and spread[3] > 0 and spread[4] > 0 and spread[5] > 0):
            score2[10] = 30
        else:
            score2[10] = 0
            
    if assign == 11:
        #Test if roll has (1, 2, 3, 4, 5) or (2, 3, 4, 5, 6)
        if (spread[0] > 0 and spread[1] > 0 and spread[2] > 0 and spread[3] > 0 and spread[4] > 0) or (spread[1] > 0 and spread[2] > 0 and spread[3] > 0 and spread[4] > 0 and spread[5] > 0):
            score2[11] = 40
        else:
            score2[11] = 0
            
    if assign == 12:
        score2[12] = sum(roll)
        
    if assign == 13:
        spread.sort()
        sixth = spread[5]
        if sixth == 5:
            score2[13] = 50
            yahtzee2 = True
        else:
            score2[13] = 0
            
    if assign == 14:
        spread.sort()
        sixth = spread[5]
        if sixth == 5 and yahtzee2 == True:
            score2[14] = 100
        else:
            score2[14] = 0
            
Card1()
print("Player 1's final score is", sum(score1))
Card2()
print("Player 2's final score is", sum(score2))

if sum(score1) > sum(score2):
    print("Player 1 is the winner!")
elif sum(score1) < sum(score2):
    print("Player 2 is the winner!")
else:
    print("There is a tie!")