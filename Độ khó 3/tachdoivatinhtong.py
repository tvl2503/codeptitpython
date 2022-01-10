n = input()
while True:
    if len(n) == 1:
        break
    a = n[:int(len(n)/2)]
    b = n[int(len(n)/2):]
    x = int(a) + int(b)
    print(x)
    n = str(x)