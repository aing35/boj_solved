import sys
T = list(sys.stdin.readline().strip().split())
count = 0

for i in T:
  if i != " ":
    count += 1

sys.stdout.write(f"{count}")