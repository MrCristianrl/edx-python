# -*- coding: utf-8 -*-
"""
Created on Tue May  8 18:27:15 2018

@author: cristian
"""

s = input('Introduce una frase ')
num_vowels = 0
for letter in s:
    if letter == 'a' or letter == 'e' or letter == 'i' \
        or letter == 'o' or letter == 'u':
            num_vowels += 1
print(num_vowels)
    