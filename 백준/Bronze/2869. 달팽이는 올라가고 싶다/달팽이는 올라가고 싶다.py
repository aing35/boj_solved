import sys
import math

A, B, V = map(int, sys.stdin.readline().split())

sys.stdout.write(f"{math.ceil((V - B) / (A - B))}")