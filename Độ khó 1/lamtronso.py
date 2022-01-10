def myFunction(n):
    n = int(n)
    res = 0
    a = []
    while n > 10:
        s = n%10
        n = int(n/10)
        n += res
        res = 0
        if s >= 5:
            res = 1
        s = 0
        a.append(s)
    a.append(n+res)
    for i in range(1,len(a)+1):
        print(a[-i],end="")
    print()
        
t = int(input())
while t > 0:
    t -= 1
    n = input()
    if len(n) == 1:
        print(n)
    else: 
        myFunction(n)
