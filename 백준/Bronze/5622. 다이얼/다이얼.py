import sys

N = list(sys.stdin.readline().rstrip())

num = {2: "ABC", 3: "DEF", 4: "GHI", 5: "JKL", 6: "MNO", 7: "PQRS", 8: "TUV", 9: "WXYZ"}
time = 0

for i in range(len(N)):
    for j in range(2, len(num) + 2):
        if N[i] in num[j]:
            time += 1 + j

sys.stdout.write(f"{time}")