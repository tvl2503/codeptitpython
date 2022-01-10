import math
def myFunc(n,x,m):
    i = 0
    while True:
        t = float(n*pow(1 + x/100,i))
        if t >= m:
            return i
        i += 1
t = int(input())
while t > 0:
    t -= 1
    arr = list(map(float, input().split()))
    n , x, m = arr
    print(myFunc(n,x,m))