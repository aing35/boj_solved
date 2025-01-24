import sys

N = int(sys.stdin.readline())

a = 1
i = 1

if N == 1:
    result = 1

else:
    while a < N:
        a += 6 * i
        i += 1
    result = i

sys.stdout.write(f"{result}\n")