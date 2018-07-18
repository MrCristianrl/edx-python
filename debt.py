#Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.
#
#In this problem, we will not be dealing with a minimum monthly payment rate.
#
#The following variables contain values as described below:
#
 #   balance - the outstanding balance on the credit card
#
 #   annualInterestRate - annual interest rate as a decimal





balanceInit = balance
#annualInterestRate
monthlyInterestRate = annualInterestRate/12.0
f = 10
month = 0

def calculate(balance,month,monthlyInterestRate,f):
    while month < 12:
        u = balance - f
        balance = u + monthlyInterestRate*u
        month += 1
    return balance
while calculate(balance,month,monthlyInterestRate,f)>0 :
    balance = balanceInit
    f += 10
    month = 0
    calculate(balance,month,monthlyInterestRate,f)
print('Lowest Payment: ' + str(f))
