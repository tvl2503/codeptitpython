
t = int(input())

while t > 0:
    def checkStr(str):
        for x in range(len(str) - 1):
            if int(str[x]) > int(str[x + 1]):
                return 0
            
        return 1
    str = input()
    if(checkStr(str) == 1):
        print('YES')
    else:
        print('NO')
    t -= 1