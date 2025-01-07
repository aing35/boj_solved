import sys

plates = sys.stdin.readline().strip()
height = 10

for i in range(len(plates) - 2):
  if plates[i] != plates[i + 1]:
    height += 10
  else:
    height += 5

if plates[-1] != plates[-2]:
  height += 10
else:
  height += 5

sys.stdout.write(f"{height}\n")