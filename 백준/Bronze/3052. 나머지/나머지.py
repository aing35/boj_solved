import sys

remainder = []

for _ in range(10):
    x = int(sys.stdin.readline())
    remainder.append(x % 42)
    
set_remainder = set(remainder)
sys.stdout.write(str(len(set_remainder)))