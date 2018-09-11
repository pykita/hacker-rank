#!/bin/python3

import os
import sys
from functools import reduce


def get_all_factors_for_all(n_list):
    def is_factor_for_list(factor):
        return all([n % factor == 0 for n in n_list])

    biggest_number = n_list[-1]
    set_for_biggest = set(reduce(list.__add__, [[i, biggest_number//i] for i in range(2, int(biggest_number**0.5) + 1) if biggest_number % i == 0]))

    return filter(is_factor_for_list, set_for_biggest)

def get_total_x(a, b):
    res = set(reduce(list.__add__, [list(get_all_factors_for_all(b)) for i in b]))
    return res
    #
    # Write your code here.
    #

if __name__ == '__main__':
    a = [2, 4]
    b = [16,32,96]
    c = get_total_x(a, b)
    
    def is_divisor_for_list(divisor):
        return all([divisor % n == 0 for n in a])

    print(list(filter(is_divisor_for_list, c)))
    # n, m = map(int, input().split())

    # a = list(map(int, input().rstrip().split()))

    # b = list(map(int, input().rstrip().split()))

    # total = getTotalX(a, b)

    # with open(os.environ['OUTPUT_PATH'], 'w') as f:
    #     f.write(str(total) + '\n')