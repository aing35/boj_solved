import sys
import math

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

prime = []
for a in range(M, N + 1):
    if a > 1:
        check = True
        for i in range(2, int(math.sqrt(a)) + 1):
            if a % i == 0:
                check = False
        if check:
            prime.append(a)

if not prime:
    sys.stdout.write("-1\n")

else:    
    sys.stdout.write(f"{sum(prime)}\n")
    sys.stdout.write(f"{prime[0]}\n")