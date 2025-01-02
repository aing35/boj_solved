import sys

student = []

for i in range(5):
    student.append(int(sys.stdin.readline()))

    if student[i] <= 40:
        student[i] = 40

average = sum(student) / len(student)

sys.stdout.write(f"{int(average)}")