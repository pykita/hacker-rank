#!/bin/python3

import os
import sys

import math

def pageCount(n, p):
    steps = 0
    if 2 * p <= n:
        steps = p // 2
    else:
        steps = math.ceil((n - p) / 2)
        # steps += 1 if n % 2 == 0 else 0
    return  steps

if __name__ == '__main__':
    # n = int(input())

    # p = int(input())

    n, p = 6, 6

    result = pageCount(n, p)
    print(result)
    # with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
    #     fptr.write(str(result) + '\n')
