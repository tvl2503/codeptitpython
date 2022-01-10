n = int(input())
arr = list(map(int,input().split()))
dem = 0
for i in range (len(arr) - 1):
    if arr[i] != arr[i+1]:
        dem += 1
print(dem)