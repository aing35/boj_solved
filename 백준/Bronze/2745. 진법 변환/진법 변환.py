import sys

digit = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

N, B_10 = sys.stdin.readline().split()

sys.stdout.write(f"{int(N, int(B_10))}")