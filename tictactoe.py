import random

startingboard = {1 : " ", 2 : " ", 3 : " ", 4 : " ", 5 : " ", 6 : " ", 7 : " ", 8 : " ", 9 : " ",}

def printboard():
    global board 
    board = f" {startingboard[1]} | {startingboard[2]} | {startingboard[3]} \n___|___|___\n   |   |   \n {startingboard[4]} | {startingboard[5]} | {startingboard[6]} \n___|___|___\n   |   |   \n {startingboard[7]} | {startingboard[8]} | {startingboard[9]} "
    print(board)

def playerselect():
    playerchoice = int(input("What square would you like to choose? (1-9, left to right, top to bottom)"))
    if startingboard[playerchoice] != " ":
        print("Square already taken, choose again!")
        playerselect()
    else:
        startingboard[playerchoice] = "X"


def computerselect():
    computerchoice = random.randint(1, 9)
    if startingboard[computerchoice] != " ":
        computerselect()
    else:
        startingboard[computerchoice] = 'O'

def main():
    gameover = False
    while not gameover:
        if startingboard[1] == startingboard[2] == startingboard[3] == 'X' or startingboard[4] == startingboard[5] == startingboard[6] == 'X' or startingboard[7] == startingboard[8] == startingboard[9] == 'X' or startingboard[1] == startingboard[5] == startingboard[9] == 'X' or startingboard[3] == startingboard[5] == startingboard[7] == 'X' or startingboard[1] == startingboard[4] == startingboard[7] == 'X' or startingboard[2] == startingboard[5] == startingboard[8] == 'X' or startingboard[3] == startingboard[6] == startingboard[9] == 'X':
            print("\n\n")
            print(board)
            print("You win!!")
            gameover = True
            
        elif startingboard[1] == startingboard[2] == startingboard[3] == 'O' or startingboard[4] == startingboard[5] == startingboard[6] == 'O' or startingboard[7] == startingboard[8] == startingboard[9] == 'O' or startingboard[1] == startingboard[5] == startingboard[9] == 'O' or startingboard[3] == startingboard[5] == startingboard[7] == 'O' or startingboard[1] == startingboard[4] == startingboard[7] == 'O' or startingboard[2] == startingboard[5] == startingboard[8] == 'O' or startingboard[3] == startingboard[6] == startingboard[9] == 'O':
            print("\n\n")
            print(board)
            print("You lose!!")
            gameover = True

        elif startingboard[1] != " " and startingboard[2] != " " and startingboard[3] != " " and startingboard[4] != " " and startingboard[5] != " " and startingboard[6] != " " and startingboard[7] != " " and startingboard[8] != " " and startingboard[9] != " ":
            print("\n\n")
            print(board)
            print("It's a tie!!")
            gameover = True

        else:
            playerselect()
            computerselect()
            printboard()

main()