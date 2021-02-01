import calculator
import countoff
import rockpaperscissors
import compoundinterestcalculator


def select(selection):

    if selection == '1':
        calculator.main()
        print()
        main()

    elif selection == '2':
        compoundinterestcalculator.main()
        print()
        main()
        
    elif selection == '3':
        rockpaperscissors.main()
        print()
        main()

    elif selection == '4':
        countoff.main()
        print()
        main()

    elif selection == '5':
        print("Goodbye!")
        return
        
    else:
        print("Invalid Entry!")
        print()
        main()
    
    
def main():

    #initiate and get selection
    print("Welcome to my project collection!\n\nWhich of the following would you like to try?\n(1) Calculator\n(2) Compound Interst Calculator\n(3) Rock, Paper, Scissors!\n(4) Count Off!\n(5) Exit")
    selection = input("Enter a number: ")

    select(selection)
    


main()
