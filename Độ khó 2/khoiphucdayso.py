n = int(input())
arr = []
A = [0]*n
for i in range(n):
    arr.append(list(map(int,input().split())))
if n == 1:
    print(0)
elif n == 2:
    print("1 1")
else:
    A[2] = int((arr[0][1] + arr[0][2] + arr[1][2])/2) - arr[0][1]
    A[0] = arr[0][2] - A[2]
    A[1] = arr[1][2] - A[2]
    for i in range(n):
        for j in range(n):
            if(j>i):
                A[j] = arr[i][j] - A[i]
    for i in A:
        print(i,end=" ")
