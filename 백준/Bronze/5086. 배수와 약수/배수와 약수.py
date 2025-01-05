import sys

while True:
  a, b = map(int, sys.stdin.readline().split())

  if a == 0 and b == 0:
    break
  else:
    if b % a == 0:
      sys.stdout.write("factor\n")
    elif a % b == 0:
      sys.stdout.write("multiple\n")
    else:
      sys.stdout.write("neither\n")