import math
def primeNumber(number):
    if number < 2:
        return False
    for i in range(2,int(math.sqrt(number))+1):
        if number %i ==0:
            return False
    return True
n,m = list(map(int, input().split()))
arr = []
prime = 0
for i in range(n):
    data = list(map(int, input().split()))
    for i in data:
        if i > prime and primeNumber(i):
                prime = i
    arr.append(data)
if prime == 0:
    print('NOT FOUND')
else:
    print(prime)
    for i in range(n):
        for j in range(m):
            if arr[i][j] == prime:
                print(f"Vi tri [{i}][{j}]")
