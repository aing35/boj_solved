import sys
T = int(sys.stdin.readline().strip())
arr = []
for _ in range(T):
  R, S = sys.stdin.readline().strip().split()
  R = int(R)
  S = list(S)
  for i in range(len(S)):
    S[i] = S[i] * R
  arr.append(''.join(S))
  
for j in range(len(arr)):
  sys.stdout.write(f"{arr[j]}\n")