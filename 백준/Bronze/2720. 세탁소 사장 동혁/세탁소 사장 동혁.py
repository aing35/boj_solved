import sys

T = int(sys.stdin.readline())

for i in range(T):
    Quarter, Dime, Nickel, Penny = 0, 0, 0, 0
    C = int(sys.stdin.readline())
    Quarter = C // 25
    Quat_remainder = C % 25
    Dime = Quat_remainder // 10
    Dime_remainder = Quat_remainder % 10
    Nickel = Dime_remainder // 5
    Penny = Dime_remainder % 5
    sys.stdout.write(f"{Quarter} {Dime} {Nickel} {Penny}\n")