#!/bin/python3

import os

def kangaroo(pos1, jump1, pos2, jump2):
    print(pos1, jump1, pos2, jump2)

    if pos1 == pos2 and jump1 == jump2:
        return 'YES'
    # equation system would be:
    #------------------
    # jump1 * x + pos1 = jump2 * y + pos2
    # x=y
    #------------------
    # jump1 * x + pos1 = jump2 * x + pos2
    
    pos_x = pos1 - pos2
    print('pos_x = %s' % pos_x)
    if pos_x == 0:
        return 'NO'

    jump_x = (jump1 - jump2)
    print('jump_x = %s' % jump_x)

    x = pos_x / jump_x
    print('x = %s' % x)

    return 'YES' if x == int(x) and x > 0 else 'NO'

if __name__ == '__main__':

    # uncomment when deploy
    # x1, v1, x2, v2 = map(int, input().split())

    x1, v1, x2, v2 = map(int, '0 3 4 2'.split())

    result = kangaroo(x1, v1, x2, v2)
    print(result)
    # with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
    #     fptr.write(result + '\n')
    