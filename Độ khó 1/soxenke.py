def soxenke(n):
    s = n[0]
    if len(n) % 2 == 0 or s == n[1]:
        return False
    for i in range(0,len(n),2):
            if n[i] != s:
                return False
    return True
test = int(input())
while test > 0:
    number = input()
    if soxenke(number): print('YES')
    else: print('NO')
    test -= 1