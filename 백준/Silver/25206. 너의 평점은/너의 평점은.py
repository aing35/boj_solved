import sys

grade_table = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

subject_arr, credit_arr, grade_arr = [], [], []
subArr, crdArr, grdArr = [], [], []
tot = 0

for _ in range(20):
  subject, credit, grade = map(str, sys.stdin.readline().split())
  subject_arr.append(subject)
  credit_arr.append(float(credit))
  grade_arr.append(grade)

for i in range(20):
  if grade_arr[i] != "P":
    subArr.append(subject_arr[i])
    crdArr.append(credit_arr[i])
    grdArr.append(grade_arr[i])

for j in range(len(subArr)):
  tot += grade_table[grdArr[j]] * crdArr[j]

tot = tot / sum(crdArr)

sys.stdout.write(f"{tot}")