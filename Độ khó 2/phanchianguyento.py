
import math
def primeNumber(number):
    if number < 2: return False
    for i in range (2,int(math.sqrt(number)+ 1)):
        if number%i ==0:
            return False
    return True
def kiemtra(arr):
    for i in range(len(arr)):
        sum1 = 0
        sum2 = 0
        for j in range(len(arr)):
            if i>=j:
                sum1 += arr[j]
            else:
                sum2 += arr[j]
        if primeNumber(sum1) and primeNumber(sum2):
            print(i)
            return
    print('NOT FOUND')
n = int(input())
arr = list(map(int,input().split()))
a = []
for i in arr:
    if i not in a:
        a.append(i)
kiemtra(a)

