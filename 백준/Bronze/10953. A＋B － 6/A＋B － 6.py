import sys

T = int(sys.stdin.readline())
plus = []

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split(","))
    plus.append(a + b)

for i in range(T):
    sys.stdout.write(f"{plus[i]}\n")