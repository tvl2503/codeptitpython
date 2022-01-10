def tinhTong(n):
    sum = 0
    for i in n:
        sum += int(i)
    return sum
def thuannghich(s):
    str1 = str(tinhTong(s))
    if len(str1) == 1: 
        print('NO')
        return 
    a = str1[::-1]
    if(a == str1): print('YES')
    else: print('NO')
test = int(input())
while test > 0:
    number = input()
    thuannghich(number)
    test -= 1