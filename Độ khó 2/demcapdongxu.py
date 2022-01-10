def giaithua(n):
    s = 1
    for i in range(1,n+1):
        s *=i
    return s
def toHop(n,k):
    return int(giaithua(n)/(giaithua(n-k)*giaithua(k)))
n = int(input())
arr = []
for i in range(n):
    arr.append(input())
dem = 0
for i in arr:
    s = i.count('C')
    dem += toHop(s,2)
for j in range(len(arr)):
    s = 0
    for i in range(len(arr)):
        if arr[i][j] == 'C': s += 1
    dem+= toHop(s,2)
print(dem)
