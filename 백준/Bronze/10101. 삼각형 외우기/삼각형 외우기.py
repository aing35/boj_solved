import sys

tri = []

for i in range(3):
    tri.append(int(sys.stdin.readline()))

if sum(tri) == 180:
    if tri[0] == tri[1] and tri[1] == tri[2]:
        sys.stdout.write("Equilateral\n")
    elif tri[0] == tri[1] or tri[1] == tri[2] or tri[0] == tri[2]:
        sys.stdout.write("Isosceles\n")
    else:
        sys.stdout.write("Scalene\n")

else:
    sys.stdout.write("Error\n")