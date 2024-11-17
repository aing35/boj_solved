import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
minNum, maxNum = arr[0], arr[0]

for i in range(N):
    if minNum > arr[i]:
        minNum = arr[i]

    if maxNum < arr[i]:
        maxNum = arr[i]

print(f"{minNum}", end = " ")
print(f"{maxNum}", end = " ")