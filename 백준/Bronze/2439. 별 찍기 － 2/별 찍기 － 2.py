import sys

N = int(sys.stdin.readline())

for i in range(N):
    sys.stdout.write(" " * (N - i - 1) + "*" * (i + 1) +"\n")