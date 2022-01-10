a = [0]*93
a[0] = 0
a[1] = 1
for i in range(2,20):
    a[i] = a[i-1] + a[i-2]
t = int(input())
while t > 0:
    t -= 1
    arr = list(map(int, input().split()))
    x = arr[0]
    y = arr[1]
    for i in range(x,y+1):
        print(a[i], end=" ")
    print()
