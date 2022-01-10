import math
def tinhTong(n):
    sum = 0
    for i in n:
        sum += int(i)
    return sum
def prime(s):
    n = tinhTong(s)
    if n < 2: return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i ==0: return False
    return True
test = int(input())
while test > 0:
    number = input()
    if prime(number): print('YES')
    else: print('NO')
    test -= 1