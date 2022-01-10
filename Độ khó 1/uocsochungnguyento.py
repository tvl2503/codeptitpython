def myFunc(a,b):
    if (b == 0):
        return a;
    return myFunc(b, a % b);
def prime(x):
    if x < 2: return False
    for i in range(2, int(x/2) + 1):
        if(x%i==0):
            return False
    return True
def sum(z):
    n = 0
    while z > 0:
        n += z%10
        z = int(z/10)
    return n
t = int(input())
while t>0 :
    t -= 1
    arr = list(map(int, input().split()))
    x = arr[0]
    y = arr[1]
    z = myFunc(x,y)
    if prime(sum(z)): print('YES')
    else: print('NO')