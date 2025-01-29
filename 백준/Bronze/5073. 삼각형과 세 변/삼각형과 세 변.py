import sys

tri = [1, 1, 1]

while 1:
    tri[0], tri[1], tri[2] = map(int, sys.stdin.readline().split())

    if tri[0] == 0 and tri[1] == 0 and tri[2] == 0:
        break
    else:
        tri.sort()

        if tri[-1] < tri[0] + tri[1]:
            if tri[0] == tri[1] and tri[1] == tri[2]:
                sys.stdout.write("Equilateral\n")
            elif tri[0] == tri[1] or tri[1] == tri[2] or tri[0] == tri[2]:
                sys.stdout.write("Isosceles\n")
            else:
                sys.stdout.write("Scalene\n")

        else:
            sys.stdout.write("Invalid\n")