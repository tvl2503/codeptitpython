t = int(input())
while t > 0: 
    arr = input()
    t = t - 1
    if arr[len(arr) - 1] == '6' and arr[len(arr) - 2] == '8': 
        print("YES")
    else :
        print("NO")
