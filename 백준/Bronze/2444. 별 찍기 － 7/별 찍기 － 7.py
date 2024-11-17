N = int(input())

for i in range(1, 1 + N):
    print(" " * (N - i) + "*" * (i - 1) + "*" + "*" * (i - 1))

for j in range(N - 1, 0, -1):
    print(" " * (N - j) + "*" * (j - 1) + "*" + "*" * (j - 1))