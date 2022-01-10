n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
k = int(input())
sum1 = 0
sum2 = 0
for i in range(n):
    for j in range(n):
        if i < n - j - 1:
            sum1 += arr[i][j]
        elif i > n - j - 1:
            sum2 += arr[i][j]
if abs(sum1 - sum2) > k:
    print('NO')
else:
    print('YES')
print(abs(sum1-sum2))