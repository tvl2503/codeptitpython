def myFunc(a,b):
    if (b == 0):
        return a;
    return myFunc(b, a % b);
[n,k] = list(map(int,input().split()))
dem = 0
for i in range(10**(k-1),10**k - 1):
    if myFunc(i,n) == 1:
        print(i,end=" ")
        dem += 1
    if dem == 10:
        dem = 0
        print()