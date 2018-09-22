#!/bin/python3

import os

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    actual = int((sum(bill[:k]) + sum(bill[k+1:])) / 2)
    if b != actual:
        return b - actual
    else:
        return 'Bon Appetit'

if __name__ == '__main__':
    n, k = input().rstrip().split()

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    result = str(bonAppetit(bill, k, b))
    
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        fptr.write(result)
