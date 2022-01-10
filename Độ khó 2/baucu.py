from collections import Counter 
N,M = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()
L = Counter(arr)
arr = list(L)
a = []
for i in L:
    a.append(L[i])
a.sort()
check = a[len(a) - 1]
if (a[0] == a[len(a) - 1]):
    print('NONE')
else:
    x = len(a) - 1
    while check == a[x]:
        x -= 1
    check = a[x]
    for i in range(1,10):
        if L[i] == check and i in L:
            print(i)
            break
