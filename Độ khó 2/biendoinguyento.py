import math
def primeNumber(number):
    if number < 2:
        return False
    for i in range(2,int(math.sqrt(number))+1):
        if number %i ==0:
            return False
    return True
n = int(input())
arr = list(map(int,input().split()))
step = 0
for i in arr:
    if not primeNumber(i):
        for j in range(1,i):
            if primeNumber(i+j):
                step = max(step,j)
                break
            if primeNumber(i-j):
                step = max(step,j)
                break
print(step)