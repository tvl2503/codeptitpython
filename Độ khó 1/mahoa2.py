p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    S =input().split()
    k = int(S[0])
    if S[0] == '0':
        break
    s = str(S[1])
    t = ""
    for i in s:
        x = p.index(i)
        y = (x+k)%28
        t += p[y]

    print(t[::-1])