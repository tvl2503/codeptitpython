t = int(input())
while t > 0:
    t-=1
    str = input()
    res = "";
    for i in range(1,len(str),2):
        for j in range(0, int(str[i]),1):
            res+=str[i-1]
    print(res)   