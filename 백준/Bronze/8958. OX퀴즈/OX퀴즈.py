import sys

T = int(sys.stdin.readline())

for _ in range(T):
  result = sys.stdin.readline().strip()

  score = 0
  bonus = 0
  
  for i in range(len(result)):
    if result[i] == 'O':
      bonus += 1
      score += bonus

    elif result[i] == 'X':
      bonus = 0
  sys.stdout.write(f"{score}\n")