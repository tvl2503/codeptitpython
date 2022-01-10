
n,m = list(map(int, input().split()))
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
if n > m:
    x =  n - m
    for i in range(0,x):
        arr.remove(arr[i])
elif m > n:
   x = m - n
   for i in range(1,x+1):
       for j in arr:
           del j[i]

for i in range(len(arr)):
    for j in range(len(arr)):
        print(arr[i][j],end=" ")
    print()