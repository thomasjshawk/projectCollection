import random

startingboard = {1 : " ", 2 : " ", 3 : " ", 4 : " ", 5 : " ", 6 : " ", 7 : " ", 8 : " ", 9 : " ",}

def printboard():
    board = f" {startingboard[1]} | {startingboard[2]} | {startingboard[3]} \n___|___|___\n   |   |   \n {startingboard[4]} | {startingboard[5]} | {startingboard[6]} \n___|___|___\n   |   |   \n {startingboard[7]} | {startingboard[8]} | {startingboard[9]} "
    print(board)

def playerselect():
    playerchoice = int(input("What square would you like to choose? (1-9, left to right, top to bottom)"))
    startingboard[playerchoice] = 'X'

playerselect()
printboard()