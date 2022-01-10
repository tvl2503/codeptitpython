def tonglientiep(N):
     
    count = 0
    L = 1
    while( L * (L + 1) < 2 * N):
        a = (1.0 * N - (L * (L + 1) ) / 2) / (L + 1)
        if (a - int(a) == 0.0):
            count += 1
        L += 1
    return count
t = int(input())
while(t > 0):
    t -= 1
    n = int(input())
    print(tonglientiep(n))