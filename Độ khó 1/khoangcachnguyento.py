def prime(x):
    if x < 2: return False
    for i in range(2, int(x/2) + 1):
        if(x%i==0):
            return False
    return True
n,x= list(map(int, input().split()))
dem = 0
i = 2
while True:
    if prime(i):
        print(x,end=" ")
        dem +=1
        x += i
    i +=1
    if dem == n + 1: break
        
