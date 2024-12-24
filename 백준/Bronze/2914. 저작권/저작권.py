import sys

A, I = map(int, sys.stdin.readline().split())

sys.stdout.write(f"{A * I - A + 1}")