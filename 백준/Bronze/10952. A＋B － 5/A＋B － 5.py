while True:
    A, B = input().split()

    A = int(A)
    B = int(B)

    if A == 0 and B == 0:
        break
    else:
        print("%d" %(A + B))