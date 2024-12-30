import sys

A = int(sys.stdin.readline())
op = sys.stdin.readline().strip()
B = int(sys.stdin.readline())

result = 0

if op == '+':
    result = A + B
elif op == '*':
    result = A * B

sys.stdout.write(f"{result}")