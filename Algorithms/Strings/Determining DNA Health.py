#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    genes = input().rstrip().split()
    health = list(map(int, input().rstrip().split()))
    s = int(input())
    res =[]

    for s_itr in range(s):
        firstLastd = input().split()
        first = int(firstLastd[0])
        last = int(firstLastd[1])
        d = firstLastd[2]
        sum = 0
        for i in range(first,last+1):
            sum += health[i]*len(list(re.finditer("(?="+genes[i]+")",d)))
        res.append(sum)
    print(min(res),max(res))