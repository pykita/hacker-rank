#!/bin/python3

import os

def kangaroo(pos1, jump1, pos2, jump2):
    if pos1 == pos2 and jump1 == jump2:
        return 'YES'
    # equation system would be:
    # pos1 * x + jump1 = pos2 * y + jump2
    # x=y
    # pos1 * x + jump1 = pos2 * x + jump2
    
    pos_x = pos1 - pos2;

    if pos_x == 0:
        return 'NO'

    jump_x = jump1 - jump2;

    x = jump_x / pos_x

    return 'YES' if x == int(x) else 'NO'

if __name__ == '__main__':

    # uncomment when deploy
    # x1, v1, x2, v2 = map(int, input().split())

    x1, v1, x2, v2 = map(int, '0 2 5 3'.split())

    result = kangaroo(x1, v1, x2, v2)

    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        fptr.write(result + '\n')