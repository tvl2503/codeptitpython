t = 10 
arr = []
while t>0: 
    data=list(map(int,input().split()))
    arr += data
    t-=len(data)
dem = []
for i in arr:
    if (i%42) not in dem:
        dem.append(i%42)
    else:
        continue
print(len(dem))