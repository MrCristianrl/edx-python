# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 21:16:27 2018

@author: cristian
"""

balance = 2000
annualInterestRate = 0.2
initBalance = balance
monthlyInterestRate = annualInterestRate / 12.0
month = 0
minPay = 10
def calculate(month, balance, minPay, monthlyInterestRate):
    while month <12:
        unpaidBalance = balance - minPay
        balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
        month += 1
    return balance
while calculate(month, balance, minPay, monthlyInterestRate) > 0:
    balance = initBalance
    minPay +=10
    month = 0
    calculate(month, balance, minPay, monthlyInterestRate)
print('Lowest Payment: ' + str(minPay))
