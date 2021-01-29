import random
import time


#player selection process
def choose():

    #define global variable and attempt to select
    global you
    you = input("Rock(r), paper(p), scissors(s)? ")

    #check for invalid slection and loop till fixed
    while(you != "r" and you != "p" and you != "s"):
        print("Invalid entry! Choose 'r', 'p', or 's'!")
        you = input("Rock (r), paper (p), scissors (s)? ")

    #Print player selection, pause for effect
    global letterChoices 
    letterChoices = {'r' : 'rock', 'p' : 'paper', 's' : 'scissors'}
    print(f'You chose {letterChoices[you]}!')
    time.sleep(2)


#computer selection fucntion
def selector():

    #define global variable and randomly select
    global computer
    computer = random.randint(1, 3)
    options = {1 : 'r', 2 : 'p', 3 : 's'}
    computer = options[computer]

    #print computer choice
    print(f'Computer chose {letterChoices[computer]}!')
    time.sleep(1) 
    

#determine winner based on selections
def winner(you, computer):

    #all winning results
    if (you == "s" and computer == "p") or (you == "p" and computer == "r") or (you == "r" and computer == "s"):
        print("You win!")

    #all losing results
    elif (you == "p" and computer == "s") or (you == "r" and computer == "p") or (you == "s" and computer == "r"):
        print("You lose!")

    #all ties
    else:
        print("It's a tie!")


#main function structure
def main():

    #welcome and establish looping variable
    print("Welcome to rock, paper, scissors!")
    newGame = 'Y'
    
    #while loop to allow user to exit the calculator when finished
    while(newGame != "N" and newGame != "n"):
        choose()

        selector()

        winner(you, computer)

        #asking if they want to play again, changing variable to break while loop if desired
        newGame = input("Would you like to play again?(Y/N): ")
        while(newGame != "Y" and newGame != "y" and newGame != "N" and newGame != "n"):
            print("Please enter Y or N")
            newGame = input("Would you like to play again?(Y/N): ")
                
    else:
        print("Goodbye!")


if __name__ == "__main__":
    main()