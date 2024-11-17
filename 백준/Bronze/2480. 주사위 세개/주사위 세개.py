A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)

if A == B == C:
    prize = 10000 + A * 1000
    print("%d" %prize)

elif (A == B) | (B == C) | (C == A):
    if A == B:
        prize = 1000 + A * 100
        print("%d" %prize)
    elif B == C:
        prize = 1000 + B * 100
        print("%d" %prize)
    else:
        prize = 1000 + C * 100
        print("%d" %prize)

elif (A != B) & (B != C) & (C != A):
    if (A > B) & (A > C):
        prize = A * 100
        print("%d" %prize)
    elif (B > A) & (B > C):
        prize = B * 100
        print("%d" %prize)
    else:
        prize = C * 100
        print("%d" %prize)