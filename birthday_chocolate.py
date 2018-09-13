#!/bin/python3

import os
from functools import reduce

# Complete the birthday function below.
def birthday(chocolate_list, day, month, chocolate_length):
    if month > chocolate_length or month * 5 < day or month > day:
        return 0
    
    acc = 0

    for i in range(month - 1, chocolate_length):
        is_fit = reduce(lambda acc, curr: acc + curr, [chocolate_list[i-j] for j in range(0, month)]) == day
        acc += 1 if is_fit else 0

    return acc

if __name__ == '__main__':
    chocolate_length = int(input().strip())

    chocolate_list = list(map(int, input().rstrip().split()))

    day, month = map(int, input().rstrip().split())

    # result = birthday([1,2,3,4,1,2], 10, 4, 6)
    result = birthday(chocolate_list, day, month, chocolate_length)

    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        fptr.write(str(result) + '\n')
