def tinhTong(n):
    sum = 0
    for i in n:
        sum += int(i)
    return sum
def chiahet3(s):
    n = tinhTong(s)
    if n%3 == 0: print('YES')
    else: print('NO')
test = int(input())
while test > 0:
    number = input()
    chiahet3(number)
    test -= 1