import sys

A, B, C = map(int, sys.stdin.readline().split())

sys.stdout.write(f"{A + B + C - max(A, B, C) - min(A, B, C)}")