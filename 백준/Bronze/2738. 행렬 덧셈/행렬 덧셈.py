import sys

N, M = map(int, sys.stdin.readline().split())
A = []
B = []

for i in range(N):
  A_col = list(map(int, sys.stdin.readline().split()))
  A.append(A_col)
    
for i in range(N):
  B_col = list(map(int, sys.stdin.readline().split()))
  B.append(B_col)

for i in range(N):
  for j in range(M):
    tot = A[i][j] + B[i][j]
    sys.stdout.write(f"{tot} ")
  sys.stdout.write("\n")