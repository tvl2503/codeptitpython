
n = input()
l = ""
for i in range (1,len(n)+1):
    l += n[-i]
    if i%3 == 0 and i!= len(n):
        l += ","
for i in range(1,len(l)+1):
    print(l[-i],end="")


    