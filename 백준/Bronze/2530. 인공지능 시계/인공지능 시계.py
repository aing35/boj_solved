import sys

hour, minute, second = map(int, sys.stdin.readline().split())
require = int(sys.stdin.readline())
tot_sec = hour * 3600 + minute * 60 + second + require

hour = (tot_sec // 3600) % 24
minute = (tot_sec % 3600) // 60
second = tot_sec % 60

sys.stdout.write(f"{hour} {minute} {second}")