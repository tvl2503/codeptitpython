
n = int(input())
arr = list(map(int,input().split()))
sum = 99999999999999999999999999999
t = 0
for i in arr:
    dem = 0
    for j in arr:
        dem += abs(i-j)
    if(dem < sum):
        t = i
        sum = dem
print(f"{sum} {t}")

