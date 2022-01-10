
from collections import Counter
t = int(input())
while t>0:
    n = int(input())
    t = t-1
    l = []
    st = input()
    x = st.split()
    for i in x:
        l.append(int(i))
    d = Counter(l)
    res = 0
    dem = 0
    for i in d:
        if dem< d[i]:
            dem = d[i]
            res = i
        elif dem == d[i] :
            if res > i: res = i
    if(dem > n/2): print(res)
    else: print('NO')
