import sys

N, M = map(int, sys.stdin.readline().split())

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())

if len(str(A)) == N and len(str(B)) == M:
    sys.stdout.write(f"{A * B}")