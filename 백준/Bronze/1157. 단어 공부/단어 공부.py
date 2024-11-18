import sys

word = list(sys.stdin.readline().strip().upper())
check_word = {a: 0 for a in set(word)}
highest = 0
answer = ""

for i in word:
  check_word[i] += 1

for j, k in check_word.items():
  if k > highest:
    highest = k
    answer = j
  elif highest == k:
    answer = "?"

sys.stdout.write(answer)