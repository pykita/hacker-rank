#!/bin/python3

import os
import sys
from functools import reduce


def get_all_factors_for_all(n_list):
    def is_factor_for_list(factor):
        return all([n % factor == 0 for n in n_list])

    any_number = n_list[-1]
    set_for_any = set(reduce(list.__add__, [[i, any_number//i] for i in range(2, int(any_number**0.5) + 1) if any_number % i == 0]))

    return list(filter(is_factor_for_list, set_for_any))

def get_total_x(a, b):
    factors_for_b = get_all_factors_for_all(b)

    # res = set(reduce(list.__add__, [list(get_all_factors_for_all(b)) for i in b]))
    
    def is_divisor_for_list(divisor):
        return all([divisor % n == 0 for n in a])
    
    return len(list(filter(is_divisor_for_list, factors_for_b)))

if __name__ == '__main__':
    # a = [2,4]
    # b = [16,72,32]
    # print(get_total_x(a,b))
    n, m = map(int, input().split())

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = get_total_x(a, b)

    with open(os.environ['OUTPUT_PATH'], 'w') as f:
        f.write(str(total) + '\n')