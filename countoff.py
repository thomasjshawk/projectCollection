import time


def main():
    n = int(input("How hi do you want me to count? "))
    x = 1
    print("Count off!")
    for i in range(n):
        print("Number " + str(x))
        x += 1
        time.sleep(1)

if __name__ == "__main__":
    main()
