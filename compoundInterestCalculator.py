from calculator import replay


#function to find percentage of total balance that comes from deposits and earned interest
def percentageCalc(deposits, balance, accruedInterest):
    percentInvested = (deposits / balance) * 100
    percentGained = (accruedInterest / balance) * 100
    print("\nPercent Invested: " + str(round(percentInvested, 2)) + "%  " + "Percent Gained: " + str(round(percentGained, 2)) + "%")


#main calculator to find the amount of money earned over given period of time
def calc():
    #establish starting year and starting interest earned
    year = 0
    accruedInterest = 0

    #ask user how much is in the account to start
    deposits = float(input("\nHow much is currently in the investment? "))
    balance = deposits

    #ask user for estimated interest rate
    interest = float(input("\nWhat is the estimated interest rate? "))
    
    #ask user for how much they plan to contribute per month
    monthlycontributions = float(input("\nHow much will you contibute per month? "))

    #ask user how long investment will have to accrue interest
    yearLimit = int(input("\nHow many years will this accrue interest? "))

    #function to calculate the interest earned and new balance for each year
    while year < yearLimit:
        year += 1
        balance += (monthlycontributions * 12)
        deposits += float(monthlycontributions * 12)
        accruedInterest += (balance * interest)
        balance += balance * interest 

    #prints year, amount deposited by user, amount of interest earned, and the estimated total balance of the account
    print("\nYear: " + str(year) + "  " + "Deposits: " + str(round(deposits, 2)) + "  " + "Interest Gained: " + str(round(accruedInterest, 2)) + "  " + "Balance: " + str(round(balance, 2)))
    percentageCalc(deposits, balance, accruedInterest)
    print("\n")


#puts calculator inside loop which allows user to choose when to exit program
def main():
    replay(calc)


#allows compound interest calculator to be imported into other projects in folder
if __name__ == "__main__":
    main()
    




    
