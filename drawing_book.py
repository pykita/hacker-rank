#!/bin/python3

import os
import math

def pageCount(n, p):
    steps = 0
    if 2 * p <= n:
        steps = p // 2
    else:
        steps = math.ceil((n - p) / 2) if n % 2 == 0 else (n - p) // 2
    return  steps

if __name__ == '__main__':
    n, p = int(input()), int(input())

    result = pageCount(n, p)
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        fptr.write(str(result) + '\n')
