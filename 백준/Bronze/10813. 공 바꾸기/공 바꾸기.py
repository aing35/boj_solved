import sys

N, M = map(int, sys.stdin.readline().strip().split())
arr = []

for x in range(N):
    arr.append(x + 1)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().strip().split())
    temp = arr[i - 1]
    arr[i - 1] = arr[j - 1]
    arr[j - 1] = temp

for y in range(N):
    sys.stdout.write(f"{arr[y]} ")