t = int(input())
while t > 0:
    n = int(input())
    n = str(n)
    if n[0] == n[-2] and n[1] == n[-1]:
        print('YES')
    else: print('NO')
    t = t - 1