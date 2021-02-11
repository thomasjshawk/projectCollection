import calculator
import countoff
import rockpaperscissors
import compoundInterestCalculator
import tictactoe

#route user to chosen project
def select(selection):
    #route to calculator
    if selection == '1':
        calculator.main()
        print()
        main()

    #route to compound interest calculator
    elif selection == '2':
        compoundInterestCalculator.main()
        print()
        main()
        
    #route to rock paper scissors game    
    elif selection == '3':
        rockpaperscissors.main()
        print()
        main()

    #route to countoff game
    elif selection == '4':
        countoff.main()
        print()
        main()
    
    #route to tictactoe game
    elif selection == '5':
        tictactoe.main()
        print()
        main()

    #exit program
    elif selection == '6':
        print("Goodbye!")
        return

    #catch all invalid entries and restart main    
    else:
        print("Invalid Entry!")
        print()
        main()
    
    
def main():

    #initiate and show selection options
    print("Welcome to my project collection!\n\nWhich of the following would you like to try?\n(1) Calculator\n(2) Compound Interest Calculator\n(3) Rock, Paper, Scissors!\n(4) Count Off!\n(5) Tic Tac Toe\n(6) Exit")
    selection = input("Enter a number: ")

    #route to chosen project
    select(selection)
    

#call main
main()
