#addition
def add(num1, num2):
    return num1 + num2


#subtraction
def subtract(num1, num2):
    return num1 - num2


#multiplication
def multiply(num1, num2):
    return num1 * num2


#division
def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Handled dividing by zero, returning zero")
        return 0

    
#run operation
def runOperation(operation, num1, num2):
    #detect operation and perform function
    if(operation == "+"):
        print()
        print(add(num1, num2))
    elif(operation == "-"):
        print()
        print(subtract(num1, num2))
    elif(operation == "*"):
        print()
        print(multiply(num1, num2))
    else:
        print()
        print(divide(num1, num2))


#asking if another calculation is wanted
def replay(func):
    func()
    while True:
        newCalc = input("\nWould you like to try again?(Y/N): ")
        while(newCalc != "Y" and newCalc != "y" and newCalc != "N" and newCalc != "n"):
            print("Please enter Y or N")
            newCalc = input("Would you like to try again?(Y/N): ")
        
        if newCalc == "Y" or newCalc == "y":
            func()
                    
        else:
            print("Goodbye!")
            return

def calc():
    #assign vairables for while loops
    myNum1 = "F"
    myNum2 = "F"
    validInput = False

    print("\nWelcome to your calculator!")

    #while loop to ensure proper entry of numbers and symbols
    while not validInput:

        #input first value, change to float
        try:
            myNum1 = float(input("Enter first number: "))
            
            #ensures first number was entered correctly
            if isinstance(myNum1, float):
                #receives operation selection
                operation = input("Enter an operation(+, -, *, /): ")
                while(operation != "+" and operation != "-" and operation != "*" and operation != "/"):
                    #invalid operation
                    print("Error! Please enter +, -, *, or /")
                    operation = input("Enter an operation(+, -, *, /): ")
            
            #input second value, change to float
            myNum2 = float(input("Enter second number: "))
            validInput = True
            
        except ValueError:
            print("Invalid Entry, please try again!\n")
    
            
            
    runOperation(operation, myNum1, myNum2)


#main function
def main():
    replay(calc)
   


#Import calculator to another file
if __name__ == "__main__":
    main()


