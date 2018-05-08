#!/bin/python3

import os
import sys

# https://www.hackerrank.com/challenges/grading/problem
def gradingStudents(grades):
    for index, value in enumerate(grades):
        residual = (value % 5)
        grades[index] = value - residual + 5 if residual > 2 and value >= 38 else value
    return grades

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as f:
        f.write('\n'.join(map(str, gradingStudents([int(input()) for _ in range(int(input()))]))) + '\n')