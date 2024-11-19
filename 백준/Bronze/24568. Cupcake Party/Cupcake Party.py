import sys

R = int(sys.stdin.readline())
S = int(sys.stdin.readline())

result = int((R * 8 + S * 3) - 28)

sys.stdout.write(f"{result}")