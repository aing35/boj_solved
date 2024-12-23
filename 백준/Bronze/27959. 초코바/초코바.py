import sys

N, M = map(int, sys.stdin.readline().split())

if N * 100 >= M:
    sys.stdout.write("Yes")
else:
    sys.stdout.write("No")