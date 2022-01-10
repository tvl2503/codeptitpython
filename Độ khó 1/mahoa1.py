t = int(input())
while t > 0:
    str1 = input()
    tes = [True]*len(str1)
    for i in range(len(str1)):
        dem = 0
        if tes[i]:
            tes[i] = False
            for j in range (i,len(str1)):
                if str1[i] != str1[j]:
                    break
                dem +=1
                tes[j] = False
        if dem > 0:
            print(dem,end='')
            print(str1[i],end='')
    
    print()
    t = t- 1
