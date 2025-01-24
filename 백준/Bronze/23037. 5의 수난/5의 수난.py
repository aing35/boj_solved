import sys

n = list(sys.stdin.readline().strip())

tot = 0

for i in range(5):
    tot += int(n[i]) ** 5

sys.stdout.write(f"{tot}\n")