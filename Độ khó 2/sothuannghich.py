def stn(n, base):
    reversed = 0;
    temp = n;
    while (temp > 0):
        reversed = reversed * base + temp % base;
        temp = int(temp / base);
     
    return reversed == n;
def check(n):
    n = bin(n)[2:]
    return n == n[::-1]
    
a,b,k = list(map(int, input().split()))
t = 0
if a == 0 and b > 1:
    if a == 0:
        t = 2
    elif a == 1:
        t = 1
    a = 2
val = [x for x in range(a,b+1) if check(x)]
for i in range(3,k+1):
    val = [x for x in val if stn(x,i)]
    if len(val) == 0:
        break
print(len(val) + t)