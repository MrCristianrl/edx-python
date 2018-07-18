# -*- coding: utf-8 -*-
"""
Created on Tue May 29 21:15:24 2018

@author: cristian
"""

def gcdRecur(a,b):
    if b == 0:
        return a
    else:
        return gcdRecur(b,a%b)