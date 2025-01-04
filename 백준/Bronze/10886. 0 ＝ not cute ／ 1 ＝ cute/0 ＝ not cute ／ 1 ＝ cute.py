import sys

N = int(sys.stdin.readline())

cute = 0
ncute = 0

if N % 2 != 0:
    for i in range(N):
        is_cute = sys.stdin.readline().strip()

        if is_cute == '1':
            cute += 1
        else:
            ncute += 1

    if cute > ncute:
        sys.stdout.write("Junhee is cute!\n")
    else:
        sys.stdout.write("Junhee is not cute!\n")