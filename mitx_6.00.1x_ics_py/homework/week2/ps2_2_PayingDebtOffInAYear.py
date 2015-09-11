"""

PROBLEM 2: PAYING DEBT OFF IN A YEAR  (15 points possible)
Now write a program that calculates the minimum fixed monthly payment needed in 
order pay off a credit card balance within 12 months. By a fixed monthly 
payment, we mean a single number which does not change each month, but instead 
is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay 
off all debt in under 1 year, for example:

Lowest Payment: 180 
Assume that the interest is compounded monthly according to the balance at the 
end of the month (after the payment for that month is made). The monthly payment
must be a multiple of $10 and is the same for all months. Notice that it is 
possible for the balance to become negative using this payment scheme, which is 
okay. A summary of the required math is found below:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x
Monthly unpaid balance)

"""


"""
Guess and Check
using bisearch

"""

balance = 3329
annualInterestRate = 0.2
epsilon = 0.01
#correct(1/30)
def oneYearPayment(balance, annualInterestRate, fixedMonthlyPayment):
    paid = 0
    monthlyInterestRate = annualInterestRate / 12.0
    for month in range(12):  
        monthlyUnpaiedBalance = balance - fixedMonthlyPayment
        paid += fixedMonthlyPayment
        balance = monthlyUnpaiedBalance + \
        (monthlyInterestRate * monthlyUnpaiedBalance)
    return balance


def minPaymentWithinOneYear(balance, annualInterestRate, epsilon):
    numGuesses = 0
    low = 10.0
    high = balance
    ans = (high + low) / 2.0
    while True:
        unpaiedBalance = oneYearPayment(balance, annualInterestRate, ans)
        if unpaiedBalance > epsilon or unpaiedBalance < -epsilon:
            numGuesses += 1
            if unpaiedBalance > 0.0: # too low
                low = ans
            else:
                high = ans
            ans = (high + low) / 2.0
        elif numGuesses > 10000: # in case of infinate like loop
            break
        else:
            break
    print('Lowest Payment: ' + str(round(ans + 5.0, -1)))
minPaymentWithinOneYear(balance, annualInterestRate, epsilon)


"""
Test Case 1:
balance = 3329
annualInterestRate = 0.2

Test Case 2:
balance = 4773
annualInterestRate = 0.2

Test Case 3:
balance = 3926
annualInterestRate = 0.2
"""
minPaymentWithinOneYear(3329, 0.2, epsilon)
minPaymentWithinOneYear(4773, 0.2, epsilon)
minPaymentWithinOneYear(3926, 0.2, epsilon)
