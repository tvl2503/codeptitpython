while True:
    arr = list(map(int, input().split()))
    if arr.count(0) == 4: break;
    dem = 0
    while True:
        if arr.count(arr[0])==4:
            break;
        x = arr[0]
        for i in range(3):
            arr[i] = abs(arr[i] - arr[i+1])
    
        arr[3] = abs(arr[3] - x)
        dem +=1
        
    print(dem)