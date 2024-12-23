import sys

N = sys.stdin.readline().strip()

N_check = N
count = 0
digit_1 = 0

if len(N) == 1:
    N = '0' + N
    N_check = N

while True:
    digit_1 = int(N[0]) + int(N[1])
    N = N[-1] + str(digit_1)[-1]
    count += 1
    if N_check == N:
        break

sys.stdout.write(f"{count}")