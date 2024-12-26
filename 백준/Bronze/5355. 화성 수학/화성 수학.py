import sys

T = int(sys.stdin.readline())

for i in range(T):
    formula = sys.stdin.readline().strip().split()
    answer = 0

    for j in range(len(formula)):
        if j == 0:
            answer += float(formula[j])
        else:
            if formula[j] == '#':
                answer -= 7
            elif formula[j] == '%':
                answer += 5
            elif formula[j] == '@':
                answer *= 3

    sys.stdout.write(f"{answer:.2f}\n")