# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 14:46:43 2018

@author: cristian
"""
#Función para realizar la suma de los dígitos de un número.

def sumDigits(N):
    if  N < 10:
        return N
    else:
        return N%10 + sumDigits(N//10)