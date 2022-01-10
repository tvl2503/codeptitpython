import math
def prime(n):
    if n < 2: return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i ==0: return False
    return True
def kiemtra(s):
    firstNumber = s[0:3]
    finalNumber = s[len(s) - 3:len(s)]

    if prime(int(finalNumber)) and prime(int(firstNumber)): print('YES')
    else: print('NO')

test = int(input())
while test > 0:
    test -= 1
    number = input()
    kiemtra(number)