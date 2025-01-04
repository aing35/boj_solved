import sys

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    school_drink = {}

    for j in range(N):
        school, drink = sys.stdin.readline().strip().split()
        school_drink[school] = int(drink)
    
    sys.stdout.write(f"{max(school_drink, key = school_drink.get)}\n")