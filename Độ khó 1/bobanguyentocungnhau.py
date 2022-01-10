def myFunc(a,b):
    r = 0
    while b >0:
        r = a%b
        a = b
        b = r
    return a == 1
arr = list(map(int,input().split()))
l,r = arr
dem = 0
for a in range(l, r-1):
    for b in range(a+1,r):
        if myFunc(a,b):
            for c in range(b+1,r+1):
                if myFunc(c,b) and myFunc(a,c) :
                    print(f"({a}, {b}, {c})")
