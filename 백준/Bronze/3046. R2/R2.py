import sys

R1, S = map(int, sys.stdin.readline().split())

sys.stdout.write(f"{S * 2 - R1}")