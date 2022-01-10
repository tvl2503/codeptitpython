
n = int(input())
arr = []
while n > 0:
    n -= 1
    s =input()
    a = ''
    for i in s:
        if i.isnumeric():
            a += i
        elif len(a) > 0:
            arr.append(int(a))
            a = ''
    if len(a) > 0:
        arr.append(int(a))
arr.sort()
for i in arr:
    print(i)