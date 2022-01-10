def myFunc(a,b):
    if (b == 0):
        return a;
    return myFunc(b, a % b);
test = int(input())
while test > 0:
    test -= 1
    number = input()
    islandsNumber = number[::-1]
    if myFunc(int(number),int(islandsNumber)) == 1:
        print('YES')
    else: print('NO')
    