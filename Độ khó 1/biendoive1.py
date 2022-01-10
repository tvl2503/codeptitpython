def dem(n):
    s = 1
    while n > 1:
        s += 1
        if n%2 == 0:
            n /= 2
        else:
            n = n*3 + 1
    return s

while True:
    n = int(input())
    if n == 0 : break
    print(dem(n))
    