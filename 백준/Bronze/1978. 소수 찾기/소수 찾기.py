import sys
import math

N = int(sys.stdin.readline())
prime = 0

lst = list(map(int, sys.stdin.readline().strip().split()))

for j in range(N):
    a = lst[j]
    if a > 2:
        check = True
        for i in range(2, int(math.sqrt(a)) + 1):
            if a % i == 0:
                check = False
        if check:
            prime += 1
    
    elif a == 2:
        prime += 1


sys.stdout.write(f"{prime}\n")