#-------------------------------------------------------------------------------
# Name:        task1.py
# Purpose:     test
#
# Author:      Tkachuk Vitaliy
#
# Created:     17.12.2018
# Copyright:   (c) Tkachuk Vitaliy 2018
# Licence:     UNLICENSE
#-------------------------------------------------------------------------------
import re

try:
    x = int(input("Input unsigned integer: "))                # отримуємо вхідні дані

except ValueError:
    print('This is not a number.')

else:
    if ((re.match(r'[0-9]+', str(x)) != None) and (x != 0)):  #  перевіряємо вхідні дані
        print ('Wait...')
        num = 0

        z = bin(x)[-(len(bin(x))-2):]                        #   переводимо в бінарну систему і виділяємо числову частину
        for i in z:                                          #   рахуємо суму одиниць
            num = num+int(i)


    print('The number of bit that are represented as 1 in binary system: ', num )


elif x == 0:
    print('The number of bit that are represented as 1 in binary system: 0' )
else:
    print ('Input error!')




