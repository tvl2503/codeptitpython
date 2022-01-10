p = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
test = int(input())
while test > 0:
    test -= 1
    N, b = list(map(int, input().split()))
    s =""
    while N > 0:
        mod = N%b
        s += p[mod]
        N = int(N/b)
    print(s[::-1])
