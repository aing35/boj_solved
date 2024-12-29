import sys
import math

def is_prime(num):
    for i in range(2, int(num)):
        if num % i == 0:
            return False
    return True

N = int(sys.stdin.readline())

result = N

if result >= 98689:
    sys.stdout.write("1003001")

elif result <= 2:
    sys.stdout.write("2")

else:
    for result in range(result, 98690):
        if is_prime(result) and str(result) == str(result)[::-1]:
            sys.stdout.write(f"{result}")
            break