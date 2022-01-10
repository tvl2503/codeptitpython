p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def Rotate(s):
    sum = 0
    t = ""
    for i in s:
        sum += p.index(i)
    for i in s:
        x = (p.index(i) + sum)%26
        t += p[x]
    return t
def merge(a,b):
    t = ''
    for i in range(len(a)):
        x = (p.index(a[i]) + p.index(b[i]))%26
        t += p[x]
    return t
test = int(input())
while test >0:
    test -= 1
    s = input()
    a = Rotate(s[:int(len(s)/2)])
    b = Rotate(s[int(len(s)/2):])
    print(merge(a,b))