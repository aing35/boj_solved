import sys

N = int(sys.stdin.readline())
reward_list = []

for i in range(N):
    a, b, c = map(int, sys.stdin.readline().split())

    if a == b and b == c:
        reward = 10000 + a * 1000
    elif a == b or b == c or c == a:
        if a == b:
            reward = 1000 + a * 100
        elif b == c:
            reward = 1000 + b * 100
        else:
            reward = 1000 + c * 100
    else:
        reward = max(a, b, c) * 100

    reward_list.append(reward)

total = max(reward_list)

sys.stdout.write(f"{total}")