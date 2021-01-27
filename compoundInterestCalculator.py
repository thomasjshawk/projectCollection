
def percentageCalc(initialDeposit, balance, accruedInterest):
    percentInvested = (initialDeposit / balance) * 100
    percentGained = (accruedInterest / balance) * 100
    print("\nPercent Invested: " + str(round(percentInvested, 2)) + "%  " + "Percent Gained: " + str(round(percentGained, 2)) + "%")

def main():
    year = 0
    accruedInterest = 0

    initialDeposit = float(input("\nHow much will you invest? "))
    balance = initialDeposit

    interest = float(input("\nWhat is the interest rate? "))

    yearLimit = int(input("\nHow many years will this accrue interest? "))

    while year < yearLimit:
        year += 1
        accruedInterest += balance * interest
        balance += balance * interest


    print("\nYear: " + str(year) + "  " + "Interest: " + str(round(accruedInterest, 2)) + "  " + "Balance: " + str(round(balance, 2)))
    percentageCalc(initialDeposit, balance, accruedInterest)
    print("\n\n")




if __name__ == "__main__":
    main()
    




    
