from collections import Counter
test = int(input())
while test > 0:
    test -= 1
    n = int(input())
    arr = list(map(int, input().split()))
    dem = Counter(arr)
    for i in dem:
        if(dem[i]%2==1):
            print(i)
            break