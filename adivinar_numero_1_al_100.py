# -*- coding: utf-8 -*-
"""
Created on Tue May 15 17:19:56 2018

@author: cristian
"""

initial_num = 50
low = 0
high = 100
print("Please think of a number between 0 and 100!")
while initial_num != "c":
    print("Is your secret number " + str(initial_num) + "? ")
    ans = str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. " ))
    if ans == 'l':
        low = initial_num
        initial_num = int((initial_num + high) / 2)
    elif ans == 'h':
        high = initial_num
        initial_num = int((initial_num + low) / 2)
    elif ans == 'c':
        print('Game over. Your secret number was: ' + str(initial_num))
        break
    else:
        print('Sorry, I did not understand your input.')
