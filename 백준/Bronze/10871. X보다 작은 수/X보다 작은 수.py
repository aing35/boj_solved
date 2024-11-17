N, X = input().split()

N = int(N)
X = int(X)

arr = list(map(int, input().split()))

for i in range(N):
    if arr[i] < X:
        print(arr[i], end = " ")