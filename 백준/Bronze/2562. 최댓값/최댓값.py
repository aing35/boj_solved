arr = []
for j in range(9):
    arr.append(int(input()))
maxNum = 0
count = 0

for i in range(9):
    if arr[i] > maxNum:
        maxNum = arr[i]
        count = i + 1
 
print("%d\n%d" %(maxNum, count))