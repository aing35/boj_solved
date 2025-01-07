import sys

x_dic = {}
y_dic = {}

for i in range(3):
  x, y = map(int, sys.stdin.readline().split())
  
  if x in x_dic:
    x_dic[x] += 1
  else:
    x_dic[x] = 1

  if y in y_dic:
    y_dic[y] += 1
  else:
    y_dic[y] = 1

for a, b in x_dic.items():
  if b == 1:
    x_ans = a

for a, b in y_dic.items():
  if b == 1:
    y_ans = a

sys.stdout.write(f"{x_ans} {y_ans}\n")