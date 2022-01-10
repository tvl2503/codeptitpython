test = int(input())
while test > 0:
    test -= 1
    n,p = list(map(int, input().split()))
    dem = 0
    for i in range(p, n+1,p):
        a = 0
        while i%p == 0:
            a += 1
            i /= p
        dem += a
    print(dem)