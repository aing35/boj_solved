import sys

N = int(sys.stdin.readline())
checker = 0

for _ in range(N):
  word = sys.stdin.readline().strip()
  if list(word) == sorted(word, key = word.find): #sort함수 사용
    checker += 1

sys.stdout.write(f"{checker}")