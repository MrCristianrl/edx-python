# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 12:47:49 2018

@author: cristian
"""
#Función para contar el número de 7 que tiene un número
def count7(N):
    if N<10:
        if N == 7:
            return 1
        else:
            return 0
    elif N%10 == 7:
        return 1 + count7(N//10)
    else:
        return 0+count7(N//10)
    