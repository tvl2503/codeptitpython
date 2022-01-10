import math
def prime(n):
    if n < 2: return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i ==0: return False
    return True
def kiemtra(s):
    if(len(s) < 4):
        print('NO')
    number = s[len(s) - 4:len(s)]
    if prime(int(number)): print('YES')
    else: print('NO')

test = int(input())
while test > 0:
    test -= 1
    number = input()
    kiemtra(number)

