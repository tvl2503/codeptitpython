while True:
    n = int(input())
    if n==0:
        break
    arr = []
    for i in range(n):
        arr.append(int(input()))
    arr.sort()
    minNumber = arr[0]
    maxNumber = arr[len(arr)-1]
    if minNumber == maxNumber:
        print("BANG NHAU")
    else:
        print(f"{minNumber} {maxNumber}")
