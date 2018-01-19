#!/usr/bin/python
import random
import sys
grid1x = ['A','B','C','D','E','F','G','H']
grid1y = ['A','J','K','L','M','N','O','P']
grid2x = ['A','B','C','D','E','F','G','H']
grid2y = ['A','J','K','L','M','N','O','P']
def grid(number):
    num1 = None
    num2 = None
    if number is 2:
        rando1 = random.randint(0,7)
        rando2 = random.randint(0,7)
        num1 = grid2x[rando1]
        num2 = grid2y[rando2]
    elif number is 1:
        rando1 = random.randint(0,7)
        rando2 = random.randint(0,7)
        num1 = grid1x[rando1]
        num2 = grid1y[rando2]
    result = num1 + num2
    return result