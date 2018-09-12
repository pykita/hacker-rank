#!/bin/python3

import os

def breakingRecords(scores):
    lowest = highest = scores[0]
    lowest_counter = highest_counter = 0

    for score in scores[1:]:
        if score > highest:
            highest = score
            highest_counter += 1

        if score < lowest:
            lowest = score
            lowest_counter += 1

    return (highest_counter, lowest_counter)

if __name__ == '__main__':
    n = int(input())

    scores = list(map(int, input().rstrip().split()))
#
    result = breakingRecords(scores)

    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')
    