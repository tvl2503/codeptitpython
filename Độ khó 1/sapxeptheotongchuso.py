def sum(n):
    n = str(n)
    s = 0
    for i in n:
        s += int(i)
    return s
t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n-1):
        for j in range(i+1,n):
            if(sum(arr[i]) > sum(arr[j])):
                arr[i] , arr[j] = arr[j] , arr[i]
            elif(sum(arr[i]) == sum(arr[j])):
                if arr[i] > arr[j]:
                    arr[i] , arr[j] = arr[j] , arr[i]
    for i in arr:
        print(i,end=" ")
    print()

