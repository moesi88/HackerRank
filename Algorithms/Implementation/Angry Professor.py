import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    if len([time for time in a if time <=0]) >= k:
        print("NO")
    else:
        print("YES")