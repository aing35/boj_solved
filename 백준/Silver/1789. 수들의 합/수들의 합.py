import sys

S = int(sys.stdin.readline())
i = 0
count = 0

while True:
    if S > i:
        i += 1
        S = S - i
        count += 1
    else:
        sys.stdout.write(f"{count}")
        break