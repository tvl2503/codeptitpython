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
t = int(input())
while t>0:
    t -= 1
    n = int(input())
    dem = 0
    for i in range(1,n):
        if myFunc(i,n) == 1:
            dem += 1
    if(prime(dem)): print('YES')
    else : print('NO')
