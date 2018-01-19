#!/usr/bin/python
import random
import sys
def grid(number):
    num1 = None
    num2 = None
    if number is 2:
        rando1 = random.randint(0,7)
        rando2 = random.randint(0,7)
        if rando1 is 0:
            num1 = 'A'
        elif rando1 is 1:
            num1 = 'B'
        elif rando1 is 2:
            num1 = 'C'
        elif rando1 is 3:
            num1 = 'D'
        elif rando1 is 4:
            num1 = 'E'
        elif rando1 is 5:
            num1 = 'F'
        elif rando1 is 6:
            num1 = 'G'
        elif rando1 is 7:
            num1 = 'H'
        if rando2 is 0:
            num2 = 'A'
        elif rando2 is 1:
            num2 = 'J'
        elif rando2 is 2:
            num2 = 'K'
        elif rando2 is 3:
            num2 = 'L'
        elif rando2 is 4:
            num2 = 'M'
        elif rando2 is 5:
            num2 = 'N'
        elif rando2 is 6:
            num2 = 'O'
        elif rando2 is 7:
            num2 = 'P'
    elif number is 1:
        rando1 = random.randint(0,7)
        rando2 = random.randint(0,7)
        if rando1 is 0:
            num1 = 'A'
        elif rando1 is 1:
            num1 = 'B'
        elif rando1 is 2:
            num1 = 'C'
        elif rando1 is 3:
            num1 = 'D'
        elif rando1 is 4:
            num1 = 'E'
        elif rando1 is 5:
            num1 = 'F'
        elif rando1 is 6:
            num1 = 'G'
        elif rando1 is 7:
            num1 = 'H'
        if rando2 is 0:
            num2 = 'A'
        elif rando2 is 1:
            num2 = 'J'
        elif rando2 is 2:
            num2 = 'K'
        elif rando2 is 3:
            num2 = 'L'
        elif rando2 is 4:
            num2 = 'M'
        elif rando2 is 5:
            num2 = 'N'
        elif rando2 is 6:
            num2 = 'O'
        elif rando2 is 7:
            num2 = 'P'
    result = num1 + num2
    return result

print(grid(1))