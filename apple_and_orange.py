#!/bin/python3

import os
import sys
from functools import reduce

# https://www.hackerrank.com/challenges/apple-and-orange/problem
def countApplesAndOranges(s, t, a, b, apples, oranges):
    print(len([h for h in apples if a + h >= s and a + h <= t]))
    print(len([h for h in oranges if b + h >= s and b + h <= t]))

if __name__ == '__main__':
    s, t, a, b, m, n = reduce((lambda x,y: x + y), [[int(st) for st in input().split()] for inpt in range(3)])

    apple, orange = ([int(app) for app in input().rstrip().split()] for inpt in range(2))

    countApplesAndOranges(s, t, a, b, apple, orange)