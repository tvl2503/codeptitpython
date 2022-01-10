
from collections import Counter
t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    arr.sort()
    arr1 = Counter(arr)
    res = 0
    dem = 0
    for i in arr1:
        if dem< arr1[i]:
            dem = arr1[i]
            res = i
    print(res)