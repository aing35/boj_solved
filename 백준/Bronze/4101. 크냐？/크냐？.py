import sys

x, y = 1, 1

while True:
    x, y = map(int, sys.stdin.readline(). split())

    if x == 0 and y == 0:
        break

    else:
        if x > y:
            sys.stdout.write("Yes\n")

        else:
            sys.stdout.write("No\n")