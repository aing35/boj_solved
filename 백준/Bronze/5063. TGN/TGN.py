import sys

T = int(sys.stdin.readline())

for i in range(T):
    r, e, c = map(int, sys.stdin.readline().split())

    if r < e - c:
        sys.stdout.write("advertise\n")
    elif r > e - c:
        sys.stdout.write("do not advertise\n")
    elif r == e - c:
        sys.stdout.write("does not matter\n")