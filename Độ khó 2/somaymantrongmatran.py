import math
def thuanNghich(number):
    s1 = str(number)
    if len(s1) < 2:
        return False
    s2 = s1[::-1]
    if s1 == s2:
        return True
    return False
n,m = list(map(int, input().split()))
arr = []
min1 = 999999999999999999999999
max1 = 0
for i in range(n):
    data = list(map(int, input().split()))
    min1 = min(min1, min(data))
    max1 = max(max1, max(data))
    arr.append(data)
x = max1 - min1
t = 0
for i in range(n):
    if x in arr[i]:
        t = 1
        break
if t==0:
    print('NOT FOUND')
else:
    print(x) 
    for i in range(n):
        for j in range(m):
            if arr[i][j] == x:
                print(f"Vi tri [{i}][{j}]")
                t = 1

