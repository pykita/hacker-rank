#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(chocolate_list, day, month, chocolate_length):
    if month > chocolate_length:
        return 0
    
    acc = 0

    for i in range(month - 1, chocolate_length - month + 1):
        

if __name__ == '__main__':
    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    d, m = map(int, input().rstrip().split())

    result = birthday([1,2,3,4], 10, 4, 4)

    # with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
    #     fptr.write(str(result) + '\n')
