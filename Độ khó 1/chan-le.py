def tong10(n):
    sum = 0
    for i in n:
        sum += int(i)
    if sum%10 == 0:
        return True
    return False
def cach2(n):
    for i in range(len(n) - 1):
        if abs(int(n[i] )- int(n[i+1])) != 2:
            return False
    return True
t = int(input())
while t>0 :
    t -= 1
    n = input()
    if tong10(n) and cach2(n):
        print('YES')
    else: print('NO')