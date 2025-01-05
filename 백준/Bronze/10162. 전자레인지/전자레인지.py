import sys

T = int(sys.stdin.readline())

A = 300
B = 60
C = 10

A_cnt, B_cnt, C_cnt = 0, 0, 0
A_remainder, B_remainder = 0, 0

if T % 10 != 0:
    sys.stdout.write("-1\n")
else:
    if T >= A:
        A_cnt = T // A
        A_remainder = T % A
    else:
        A_remainder = T

    if A_remainder >= B:
        B_cnt = A_remainder // B
        B_remainder = A_remainder % B
        C_cnt = B_remainder // C
    else:
        C_cnt = A_remainder // C
    sys.stdout.write(f"{A_cnt} {B_cnt} {C_cnt}\n")
