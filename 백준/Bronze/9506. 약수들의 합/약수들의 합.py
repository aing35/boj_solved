import sys
import math

while True:
  n = int(sys.stdin.readline())
  if n == -1:
    break
  else:
    divisor = []
    for i in range(1, int(math.sqrt(n)) + 1):
      if n % i == 0:
        divisor.append(i)
        if i ** 2 != n:
          divisor.append(n // i)
    divisor.sort()

  if sum(divisor) - divisor[-1] == n:
    sys.stdout.write(f"{n} = ")
    for a in range(len(divisor) - 2):
      sys.stdout.write(f"{divisor[a]} + ")
    sys.stdout.write(f"{divisor[-2]}\n")
  else:
    sys.stdout.write(f"{n} is NOT perfect.\n")