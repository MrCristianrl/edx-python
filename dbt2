Write a program that uses these bounds and bisection search (for more info check out the Wikipedia page on bisection search) to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year. Try it out with large inputs, and notice how fast it is (try the same large inputs in your solution to Problem 2 to compare!). Produce the same return value as you did in Problem 2.

Note that if you do not use bisection search, your code will not run - your code only has 30 seconds to run on our servers.



InitBalance = balance
eps = 0.01
monthlyInterestRate = annualInterestRate/12
month = 0
lowerbound = balance/12
upperbound = (balance*(1+monthlyInterestRate)**12)/12
minPay = (lowerbound+upperbound)/2.0

def calculate(balance,month,monthlyInterestRate,minPay):
    while month < 12:
        unPaid = balance - minPay
        balance = unPaid + monthlyInterestRate*unPaid
        month += 1
    return balance
while abs(balance) > eps:
    balance = InitBalance
    month = 0
    balance = calculate(balance,month,monthlyInterestRate,minPay)
    if balance > 0:
        lowerbound = minPay
    else:
        upperbound = minPay
    minPay = (lowerbound+upperbound)/2.0
print('Lowest Payment: ' + str(round(minPay,2)))
