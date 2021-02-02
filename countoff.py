import time
from calculator import replay

#function to count
def counter():
    #ask for number user wants game to count to
    n = int(input("\nHow hi do you want me to count? "))
    print("Count off!")

    #print and count up for every number in the given range
    for i in range(n):
        i += 1
        print("Number " + str(i))
        time.sleep(0.5)


#game housed inside function allowing for looping game until user chooses to exit
def main():
    replay(counter)


#allows countoff to be imported into other files in project folder
if __name__ == "__main__":
    main()
