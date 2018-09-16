#!/bin/python3

from itertools import groupby
import os

def migratoryBirds(arr):
    return max(sorted([(k,len(list(g))) for k,g in groupby(sorted(arr))], key=lambda g: g[0] ), key=lambda m: m[1])[0]
    

if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        fptr.write(str(result) + '\n')