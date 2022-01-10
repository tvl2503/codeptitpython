def myFunc(a,b):
    if (b == 0):
        return a;
    return myFunc(b, a % b);
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
for i in arr:
    for j in arr:
        if i<j:
            if myFunc(i,j) == 1:
                print(i,j, sep=" ")