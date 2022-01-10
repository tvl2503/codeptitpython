import math
def prime(n):
    if n < 2: return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i ==0: return False
    return True
def kiemtra(n):
    for i in range(len(n)):
        if (prime(i) and not prime(int(n[i]))) or (not prime(i) and prime(int(n[i]))):
            return False
    return True
test = int(input())
while test > 0:
    number = input()
    if kiemtra(number): print('YES')
    else: print('NO')
    test -= 1