#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def super_reduced_string(s):
    if not s:
        return 'Empty String'
    stack = ''
    for i, c in enumerate(s):
        if stack and stack[-1] == c:
            stack = stack[:-1]
        else:
            stack += c
    if stack:
        return stack
    return 'Empty String'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = super_reduced_string(s)

    fptr.write(result + '\n')

    fptr.close()
