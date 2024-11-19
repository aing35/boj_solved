import sys

N = int(sys.stdin.readline())
plus = 0
cube = 0

for i in range(N + 1):
    plus += i
    cube += i ** 3

sys.stdout.write(f"{plus}\n")
sys.stdout.write(f"{plus ** 2}\n")
sys.stdout.write(f"{cube}")