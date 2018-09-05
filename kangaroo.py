#!/bin/python3

import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
    
    return 'NO'

if __name__ == '__main__':

    # uncomment when deploy
    # x1, v1, x2, v2 = map(int, input().split())

    x1, v1, x2, v2 = map(int, '0 2 5 3'.split())

    result = kangaroo(x1, v1, x2, v2)

    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        fptr.write(result + '\n')