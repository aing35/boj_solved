import sys

t = int(sys.stdin.readline())

Q1 = 0
Q2 = 0
Q3 = 0
Q4 = 0
AXIS = 0

for i in range(t):
  x, y = map(int, sys.stdin.readline().split())
  if x == 0 or y == 0:
    AXIS += 1
  else:
    if x > 0 and y > 0:
      Q1 += 1
    elif x < 0 and y > 0:
      Q2 += 1
    elif x < 0 and y < 0:
      Q3 += 1
    else:
      Q4 += 1

sys.stdout.write(f"Q1: {Q1}\nQ2: {Q2}\nQ3: {Q3}\nQ4: {Q4}\nAXIS: {AXIS}\n")