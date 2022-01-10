def prime(x):
    if x < 2: return False
    for i in range(2, int(x/2) + 1):
        if(x%i==0):
            return False
    return True
n = int(input())
arr = list(map(int, input().split()))
tes = []
for i in arr:
    if i not in tes:
        tes.append(i)
for i in tes:
    if(prime(i)):
        print(i,arr.count(i),sep=" ")
