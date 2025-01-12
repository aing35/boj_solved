import sys
import math

#(A와 B의 최소공배수) = (A * B) / (A와 B의 최대공약수)

T = int(sys.stdin.readline())

for _ in range(T):
  a, b = map(int, sys.stdin.readline().split())

  lcm = math.lcm(a, b)

  sys.stdout.write(f"{lcm}\n")