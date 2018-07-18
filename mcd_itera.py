# -*- coding: utf-8 -*-
"""
Created on Tue May 29 20:33:43 2018

@author: cristian
"""

def gcdIter(a,b):
    if a<b:
        guess = a
        for i in range((a+b)):
            if b%guess == 0:
                if a%guess == 0:
                    return guess
                    break
                else:
                    guess -= 1
            else:
                guess -= 1
    else:
        guess = b
        for i in range((a+b)):
            if a%guess == 0:
                if b%guess == 0:
                    return guess
                    break
                else:
                    guess -= 1
            else:
                guess -= 1
        return guess