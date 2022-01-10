def myFunc(st):
    st1 = reversed(st)
    st1 = ''.join(st1)
    for i in range(int(len(st)/2)+1):
            if abs(ord(st[i])-ord(st[i+1])) != abs(ord(st1[i])-ord(st1[i+1])):
                return False
    return True


t = int(input())
while t > 0:
    t -= 1
    st = input()
    if myFunc(st):
        print('YES')
    else: print('NO')

