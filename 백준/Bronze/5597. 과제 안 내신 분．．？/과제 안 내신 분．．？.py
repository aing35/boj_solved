import sys

allStudent = {}

for i in range(1, 31):    
    allStudent[i] = 0

for _ in range(28):
    submitted = int(sys.stdin.readline().strip())
    allStudent[submitted] = submitted

for j in range(1, 31):
    if allStudent[j] == 0:
        sys.stdout.write(f"{j}\n")