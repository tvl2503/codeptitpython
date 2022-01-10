def myFunc(n, arr):
    for i in range (1, n+1):
        if i not in arr:
            return i
    return n + 1

n = int(input())
arr = list(map(int, input().split()))
print(myFunc(n,arr))