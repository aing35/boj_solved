import sys
import math

N, K = map(int, sys.stdin.readline().split())

div = []

for i in range(1, int(math.sqrt(N) + 1)):
  if N % i == 0:
    div.append(i)
    if i ** 2 != N:
      div.append(N // i)

div.sort()

if len(div) >= K:
  sys.stdout.write(f"{div[K - 1]}")
else:
  sys.stdout.write("0\n")