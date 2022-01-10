import math
def primeNumber(number):
    if number < 2: return False
    for i in range (2,int(math.sqrt(number)+ 1)):
        if number%i ==0:
            return False
    return True
n = int(input())
arr = list(map(int,input().split()))
for i in range(n-1):
    if(primeNumber(arr[i])):
        for j in range(i+1, n):
            if primeNumber(arr[j]) and arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
for i in arr:
    print(i,end=" ")