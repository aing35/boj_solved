import sys

score = sys.stdin.readline().strip()

tot = 0

if score[0] == 'F':
    tot = 0.0
    sys.stdout.write(f"{tot}")
else:
    if score[0] == 'D':
        tot = 1.0
    elif score[0] == 'C':
        tot = 2.0
    elif score[0] == 'B':
        tot = 3.0
    elif score[0] == 'A':
        tot = 4.0
    
    if score[1] == '+':
        tot += 0.3
    elif score[1] == '0':
        pass
    elif score[1] == '-':
        tot -= 0.3
    
    sys.stdout.write(f"{tot}")