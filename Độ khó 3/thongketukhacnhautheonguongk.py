from collections import Counter
import re
n,k = list(map(int, input().split()))
arr = []
while n >0:
    n -= 1
    a = input().lower()
    arr += re.split("[^{a-z}\d]+", a)
for i in range(arr.count('')):
    arr.remove("")
arr.sort()
arr = Counter(arr)
arr = dict(sorted(arr.items(),reverse= True, key = lambda x: x[1]))
for i in arr:
    if arr[i] >= k:
        print(i,arr[i], sep=" ")