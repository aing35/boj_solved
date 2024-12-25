import sys

M = int(sys.stdin.readline())
S = []

for i in range(M):
    order = sys.stdin.readline().strip().split()
    if len(order) > 1:
        order[1] = int(order[1])

    if order[0] == 'add':
        if order[1] not in S:
            S.append(order[1])
    
    elif order[0] == 'remove':
        if order[1] in S:
            S.remove(order[1])
    
    elif order[0] == 'check':
        if order[1] in S:
            sys.stdout.write("1\n")
        else:
            sys.stdout.write("0\n")
    
    elif order[0] == 'toggle':
        if order[1] in S:
            S.remove(order[1])
        else:
            S.append(order[1])

    elif order[0] == 'all':
        S = [n for n in range(1, 21)]

    elif order[0] == 'empty':
        S = []