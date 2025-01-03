import sys

K, N, M = map(int, sys.stdin.readline().split())

if M - K * N <= 0:
    sys.stdout.write(f"{K * N - M}")
else:
    sys.stdout.write(f"0")