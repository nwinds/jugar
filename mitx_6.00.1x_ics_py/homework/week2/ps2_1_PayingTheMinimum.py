"""
PROBLEM 1: PAYING THE MINIMUM  (10 points possible)
Write a program to calculate the credit card balance after one year if a person 
only pays the minimum monthly payment required by the credit card company each 
month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining 
balance, and print to screen something of the format:

Month: 1
Minimum monthly payment: 96.0
Remaining balance: 4784.0
Be sure to print out no more than two decimal digits of accuracy - so print

Remaining balance: 813.41
instead of

Remaining balance: 813.4141998135 
Finally, print out the total amount paid that year and the remaining balance at 
the end of the year in the format:

Total paid: 96.0
Remaining balance: 4784.0
A summary of the required math is found below:

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x 
Monthly unpaid balance)

Note that the grading script looks for the order in which each value is printed 
out. We provide sample test cases below; we suggest you develop your code on 
your own machine, and make sure your code passes the sample test cases, before 
you paste it into the box below.

Test Cases to Test Your Code With. Be sure to test these on your own machine - 
and that you get the same output! - before running your code on this webpage!
Click to See Problem 1 Test Cases

The code you paste into the following box should not specify the values for the 
variables balance, annualInterestRate, or monthlyPaymentRate - our test code 
will define those values before testing your submission.

"""
# correct(1/30)

# helper for float formating
def formatedFloatStr(f):
    d1 = '%.1f' % f
    d2 = '%.2f' % f
    if d1 + '0' == d2:
        return d1
    else:
        return d2


def oneYearBalance(balance, annualInterestRate, monthlyPaymentRate):
    paid = 0
    monthlyInterestRate = annualInterestRate / 12.0
    monthlyPayment = 0
    for month in range(12+1):
        # debug info
        if month > 0:
            print('Month: %d' % month)
            print('Minimum monthly payment: %s' % formatedFloatStr(monthlyPayment))
            print('Remaining balance: %s' % formatedFloatStr(balance))
            #print('Balance: %s | MP: %s ' % \
            #(formatedFloatStr(balance), formatedFloatStr(monthlyPayment)))

        monthlyPayment = monthlyPaymentRate * balance
        
        monthlyUnpaiedBalance = balance - monthlyPayment
        # update balance
        if month < 12:
            paid += monthlyPayment
            balance = monthlyUnpaiedBalance + \
            (monthlyInterestRate * monthlyUnpaiedBalance)

    print('Total paid: %s' % formatedFloatStr(paid))
    print('Remaining balance: %s' % formatedFloatStr(balance))

#oneYearBalance(balance, annualInterestRate, monthlyPaymentRate)



# Test Case 1:
print('Running Test Case 1')
balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
oneYearBalance(balance, annualInterestRate, monthlyPaymentRate)

print('')
# Test Case 2:
print('Running Test Case 2')
balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
oneYearBalance(balance, annualInterestRate, monthlyPaymentRate)
