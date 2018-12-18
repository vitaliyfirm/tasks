#-------------------------------------------------------------------------------
# Name:        task1_1.py
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

        while x > 0:
            y = x % 2                      #переводимо в бінарну систему та рахуємо суму 0 та 1,
            num = y + num                  #тобто кількість 1
            x = int(x / 2)

        print('The number of bits that are represented as 1 in binary system:', num )

    elif x == 0:
        print('The number of bit that are represented as 1 in binary system: 0' )
    else:
        print ('Input error!')


