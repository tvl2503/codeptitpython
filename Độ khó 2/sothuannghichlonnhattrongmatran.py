import math
def thuanNghich(number):
    s1 = str(number)
    if len(s1) < 2:
        return False
    s2 = s1[::-1]
    if s1 == s2:
        return True
    return False
n,m = list(map(int, input().split()))
arr = []
prime = 0
for i in range(n):
    data = list(map(int, input().split()))
    for i in data:
        if i > prime and thuanNghich(i):
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
