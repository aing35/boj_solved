import sys

arr = [[0 for i in range(9)] for j in range(9)]
max_num = 0
coordinate = [0] * 2

for x in range(9):
  a1, a2, a3, a4, a5, a6, a7, a8, a9 = map(int, sys.stdin.readline().split())
  a_list = [a1, a2, a3, a4, a5, a6, a7, a8, a9]
  for y in range(9):
    arr[x][y] = a_list[y]

for x in range(9):
  for y in range(9):
    if arr[x][y] >= max_num:
      max_num = arr[x][y]
      coordinate[0] = x + 1
      coordinate[1] = y + 1

sys.stdout.write(f"{max_num}\n")
sys.stdout.write(f"{coordinate[0]} {coordinate[1]}")