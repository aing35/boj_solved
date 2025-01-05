import sys

changyoung = 100
sangduk = 100

n = int(sys.stdin.readline())

for i in range(n):
  changyoung_num, sangduk_num = map(int, sys.stdin.readline().split())
  
  if changyoung_num == sangduk_num:
    pass
  elif changyoung_num > sangduk_num:
    sangduk -= changyoung_num
  else:
    changyoung -= sangduk_num

sys.stdout.write(f"{changyoung}\n{sangduk}")