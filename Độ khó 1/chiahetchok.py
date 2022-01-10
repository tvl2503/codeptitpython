arr = list(map(int, input().split()))
a ,k , n = arr
t = 0
x = k - a%k
for i in range(x, n - a + 1, k ):
    s = a + i
    if s%k==0:
        print(i,end=" ")
        t = 1
if t == 0:
    print(-1)
