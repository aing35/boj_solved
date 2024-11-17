import sys

N = int(sys.stdin.readline())
arr = sys.stdin.readline()
tot = 0

for i in range(N):
    tot += int(arr[i])

sys.stdout.write(f"{tot}")