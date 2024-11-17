N = int(input())
tot = 0

grade = [int(i) for i in input().split()]
M = max(grade)
    
for j in range(N):
    grade[j] = (grade[j] / M) * 100

for k in range(N):
    tot += grade[k]

average = tot / N

print(f"{average:.2f}")