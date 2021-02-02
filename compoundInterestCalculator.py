from calculator import replay

def percentageCalc(deposits, balance, accruedInterest):
    percentInvested = (deposits / balance) * 100
    percentGained = (accruedInterest / balance) * 100
    print("\nPercent Invested: " + str(round(percentInvested, 2)) + "%  " + "Percent Gained: " + str(round(percentGained, 2)) + "%")

def calc():
    year = 0
    accruedInterest = 0

    deposits = float(input("\nHow much will you invest? "))
    balance = deposits

    interest = float(input("\nWhat is the interest rate? "))
    
    monthlycontributions = float(input("\nHow much will you contibute per month? "))

    yearLimit = int(input("\nHow many years will this accrue interest? "))

    while year < yearLimit:
        year += 1
        balance += (monthlycontributions * 12)
        deposits += float(monthlycontributions * 12)
        accruedInterest += (balance * interest)
        balance += balance * interest 


    print("\nYear: " + str(year) + "  " + "Deposits: " + str(round(deposits, 2)) + "  " + "Interest Gained: " + str(round(accruedInterest, 2)) + "  " + "Balance: " + str(round(balance, 2)))
    percentageCalc(deposits, balance, accruedInterest)
    print("\n")


def main():
    replay(calc)


if __name__ == "__main__":
    main()
    




    
