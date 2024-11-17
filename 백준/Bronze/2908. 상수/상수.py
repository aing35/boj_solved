import sys
A, B = map(list, sys.stdin.readline().strip().split())

A[0], A[2] = A[2], A[0]

B[0], B[2] = B[2], B[0]

A = int(''.join(A))
B = int(''.join(B))

if A > B:
  sys.stdout.write(f"{A}")
else:
  sys.stdout.write(f"{B}")