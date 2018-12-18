#-------------------------------------------------------------------------------
# Name:        task3.py
# Purpose:     test
#
# Author:      Tkachuk Vitaliy
#
# Created:     17.12.2018
# Copyright:   (c) Tkachuk Vitaliy 2018
# Licence:     UNLICENSE
#-------------------------------------------------------------------------------
import re

arr = ([ 11, [ 11, 11 ] ], [ 2, [ 2, 2 ] ] )

def matching (arr):
    first_struct = hash(re.sub(r'\w+', 'z', str(arr[0])))
# беремо перший елемент масиву, нормалізуєм його (заміняємо всі елементи
# на стандртні та робимо його hash)
    struct = True
    for i in range(1,len(arr)):
        if hash(re.sub(r'\w+', 'z', str(arr[i]))) == first_struct:
# повторюємо послідовно для всіх елементів масиву та порівнюємо їхні hash-і
# якщо рівні hash-і нормалізованих елементів, то їхні структури однакові.
            continue

        else:
            struct = False
            break

    return struct

print(str(matching(arr)))






