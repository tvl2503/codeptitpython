def myFunc(st):
    for i in st:
        if i !='4' and  i != '7' :
            return False
    return True
t = int(input())
while t>0:
    t -= 1
    st = input()
    if myFunc(st): print('YES')
    else: print('NO')