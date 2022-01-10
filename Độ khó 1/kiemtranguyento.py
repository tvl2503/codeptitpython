
def prime(n):
    if n < 2: return False
    for i in range(2, int(n/2) +1):
        if n%i ==0: return False
    return True
n,m =list(map(int, input().split()))
a = []
for i in range(n):
    b =list(map(int, input().split()))
    a.append(b)
for i in range(n):
    for j in range(m):
        if prime(a[i][j]) : print(1,end=" ")
        else : print(0,end=" ")
    print()
