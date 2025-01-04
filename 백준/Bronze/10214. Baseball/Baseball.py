import sys

T = int(sys.stdin.readline())

for i in range(T):
    Y_list = []
    K_list = []
    
    for _ in range(9):
        Y, K = map(int, sys.stdin.readline().split())
        Y_list.append(Y)
        K_list.append(K)
    
    Y_score = sum(Y_list)
    K_score = sum(K_list)

    if Y_score > K_score:
        sys.stdout.write("Yonsei\n")
    elif K_score > Y_score:
        sys.stdout.write("Korea\n")
    else:
        sys.stdout.write("Draw\n")