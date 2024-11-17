import sys
S = sys.stdin.readline().strip()

alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in alphabet:
  print(f"{S.find(i)}", end = ' ')