import math
def prime(n):
    if n < 2: return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i ==0: return False
    return True
def quantity(number):
    dem = 0
    for i in number:
        if prime(int(i)):
            dem += 1
    if 2*dem > len(number):
        return True
    return False
test = int(input())
while test > 0:
    test -= 1
    number = input()
    if quantity(number) and prime(len(number)): print('YES')
    else: print('NO')