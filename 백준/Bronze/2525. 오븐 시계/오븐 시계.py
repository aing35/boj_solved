A, B = input().split()
A = int(A)
B = int(B)
C = int(input())

if (B + C >= 60):
    if ((B + C) // 60 + A) >= 24:
        print(f"{(B + C) // 60 + A - 24} {(B + C) % 60}")
    else:
        print(f"{(B + C) // 60 + A} {(B + C) % 60}")
else:
    print(f"{A} {B + C}")