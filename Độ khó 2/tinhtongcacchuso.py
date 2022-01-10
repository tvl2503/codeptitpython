
t = int(input())
while t > 0:
    t -= 1
    s = input()
    sum = 0
    for i in s:
        if i >= '0' and i <='9':
            sum += int(i)
            s = s.replace(i,'')
    s = ''.join(sorted(s))
    if sum > 0:
         print(s,sum,sep="")
    else:
        print(s)