import sys

digit = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

N, B = map(int, sys.stdin.readline().split())
result = ''

while N > 0:
    result = digit[N % B] + result
    N //= B

sys.stdout.write(f"{result}")