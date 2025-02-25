import sys

X = int(sys.stdin.readline())
n = 1

while (n * (n + 1)) // 2 < X:
    n += 1

X -= (n * (n - 1)) // 2 # X를 목표 대각선의 첫 번째 분수로 바꾸기기

if n % 2 == 1: # 대각선이 홀수 번째
    sys.stdout.write(f"{n - X + 1}/{X}\n")
else: # 대각선이 짝수 번째
    sys.stdout.write(f"{X}/{n - X + 1}\n")