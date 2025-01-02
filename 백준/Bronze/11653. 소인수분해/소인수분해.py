import sys

N = int(sys.stdin.readline())

i = 2
f = []

if N != 1:

    while i ** 2 <= N:
        if N % i != 0:
            i += 1
        else:
            f.append(i)
            N //= i

    if N > 1:
        f.append(N)

for x in range(len(f)):
    sys.stdout.write(f"{f[x]}\n")