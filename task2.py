#-------------------------------------------------------------------------------
# Name:        task2.py
# Purpose:     test
#
# Author:      Tkachuk Vitaliy
#
# Created:     17.12.2018
# Copyright:   (c) Tkachuk Vitaliy 2018
# Licence:     UNLICENSE
#-------------------------------------------------------------------------------
item = str(input("Input password: "))          #  отримуємо пароль(не обов'язково через input)

def maskify (item):
    return  (len(item)-4)*'#'+item[-4:]     #  маскуємо зайві знаки


print (maskify(item))                          #  користуємось