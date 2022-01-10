def myFunc(n):
    n = str(n)
    x = n[::-1]
    if (len(x)%2 == 1) : return False
    if x!=n: return False
    for i in n:
        if int(i)%2 !=0 : return False
    return True
t =int(input())
while t > 0:
    t -= 1
    n = int(input())
    for i in range(22,n,22):
        if myFunc(i): print(i,end=" ")

    print()


