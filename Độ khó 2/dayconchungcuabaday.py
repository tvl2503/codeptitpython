test = int(input())
while test > 0:
    test -= 1
    out=""
    n ,m, k = list(map(int, input().split()))
    a= list(map(int, input().split()))
    b= list(map(int, input().split()))
    c= list(map(int, input().split()))
    check,m1,m2,m3=0,0,0,0
    while m1<n and m2<m and m3<k:
        if a[m1]==b[m2]==c[m3]:
            out+=str(a[m1])+" "
            check=1
            m1,m2,m3=m1+1,m2+1,m3+1
        elif a[m1]<b[m2]:m1+=1
        elif b[m2]<c[m3]:m2+=1
        else:m3+=1
    if check==0:
        print("NO")
    else:
        print(out)

