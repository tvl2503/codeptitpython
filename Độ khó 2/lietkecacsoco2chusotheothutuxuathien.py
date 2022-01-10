n = input()
if len(n)%2 == 1:
    n = n[:len(n)-1]
arr = []
s = ''
for i in range(0,len(n),2):
    s += n[i] + n[i+1]
    if int(s) not in arr:
        arr.append(int(s))
    s = ''

for i in arr:
    print(i,end=" ")
