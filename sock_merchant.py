
import os
from itertools import groupby

def sockMerchant(n, ar):
    return sum([len(list(g)) //2 for k, g in groupby(sorted(ar))])

if __name__ == '__main__':
    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        fptr.write(str(result) + '\n')