import time
from calculator import replay

def counter():
    n = int(input("\nHow hi do you want me to count? "))
    print("Count off!")
    for i in range(n):
        i += 1
        print("Number " + str(i))
        time.sleep(1)

def main():
    replay(counter)

if __name__ == "__main__":
    main()
