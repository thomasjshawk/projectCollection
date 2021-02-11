import random
from calculator import replay


starting_board = 'none'
marker_player = 'none'
marker_computer = 'none'
board = 'none'

def markerSelection():
    global marker_player
    global marker_computer
    marker_computer = 'none'
    marker_player = 'none'
    marker_player = input("Would you like Xs or Os?")

    if marker_player == 'X' or marker_player == 'x':
        marker_player = 'X'
        marker_computer = 'O'

    elif marker_player == 'O' or marker_player == 'o':
        marker_player = 'O'
        marker_computer = 'X'

def printboard():
    global board 
    board = f" {starting_board[1]} | {starting_board[2]} | {starting_board[3]} \n___|___|___\n   |   |   \n {starting_board[4]} | {starting_board[5]} | {starting_board[6]} \n___|___|___\n   |   |   \n {starting_board[7]} | {starting_board[8]} | {starting_board[9]} "
    print(board)

def playerselect():
    playerchoice = int(input("What square would you like to choose? (1-9, left to right, top to bottom)"))
    if starting_board[playerchoice] != " ":
        print("Square already taken, choose again!")
        playerselect()
    else:
        starting_board[playerchoice] = marker_player


def computerselect():
    computerchoice = random.randint(1, 9)
    if starting_board[computerchoice] != " ":
        computerselect()
    else:
        starting_board[computerchoice] = marker_computer


def game():
    global starting_board
    starting_board = {1 : " ", 2 : " ", 3 : " ", 4 : " ", 5 : " ", 6 : " ", 7 : " ", 8 : " ", 9 : " "}
    gameover = False
    markerSelection()
    while not gameover:
        if starting_board[1] == starting_board[2] == starting_board[3] == marker_player or starting_board[4] == starting_board[5] == starting_board[6] == marker_player or starting_board[7] == starting_board[8] == starting_board[9] == marker_player or starting_board[1] == starting_board[5] == starting_board[9] == marker_player or starting_board[3] == starting_board[5] == starting_board[7] == marker_player or starting_board[1] == starting_board[4] == starting_board[7] == marker_player or starting_board[2] == starting_board[5] == starting_board[8] == marker_player or starting_board[3] == starting_board[6] == starting_board[9] == marker_player:
            print("\n\n")
            print(board)
            print("You win!!")
            gameover = True
            
        elif starting_board[1] == starting_board[2] == starting_board[3] == marker_computer or starting_board[4] == starting_board[5] == starting_board[6] == marker_computer or starting_board[7] == starting_board[8] == starting_board[9] == marker_computer or starting_board[1] == starting_board[5] == starting_board[9] == marker_computer or starting_board[3] == starting_board[5] == starting_board[7] == marker_computer or starting_board[1] == starting_board[4] == starting_board[7] == marker_computer or starting_board[2] == starting_board[5] == starting_board[8] == marker_computer or starting_board[3] == starting_board[6] == starting_board[9] == marker_computer:
            print("\n\n")
            print(board)
            print("You lose!!")
            gameover = True

        elif starting_board[1] != " " and starting_board[2] != " " and starting_board[3] != " " and starting_board[4] != " " and starting_board[5] != " " and starting_board[6] != " " and starting_board[7] != " " and starting_board[8] != " " and starting_board[9] != " ":
            print("\n\n")
            print(board)
            print("It's a tie!!")
            gameover = True

        else:
            playerselect()
            computerselect()
            printboard()


def main():
    replay(game)

#allow to be imported to another file in folder
if __name__ == "__main__":
    main()