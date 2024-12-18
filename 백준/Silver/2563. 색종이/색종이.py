import sys

dohwaji = [[0] * 100 for _ in range(100)]

n = int(sys.stdin.readline())

for _ in range(n):
    w, h = map(int, sys.stdin.readline().split())
    for i in range(h, h + 10):
        for j in range(w, w + 10):
            dohwaji[i][j] = 1

area = 0

for x in range(100):
    area += dohwaji[x].count(1)


sys.stdout.write(f"{area}")