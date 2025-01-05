import sys

V = int(sys.stdin.readline())

get_V = sys.stdin.readline().strip()

A = get_V.count('A')
B = get_V.count('B')

if A > B:
    sys.stdout.write("A\n")
elif A < B:
    sys.stdout.write("B\n")
else:
    sys.stdout.write("Tie\n")