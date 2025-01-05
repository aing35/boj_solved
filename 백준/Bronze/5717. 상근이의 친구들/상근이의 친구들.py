import sys

M = 1
F = 1

while True:
    M, F = map(int, sys.stdin.readline().split())
    
    if M == 0 and F == 0:
        break

    else:
        sys.stdout.write(f"{M + F}\n")