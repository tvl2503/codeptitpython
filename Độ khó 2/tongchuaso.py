n = input()
dem = 0
while len(n) > 1:
    dem += 1
    s = 0
    for i in  n:
        s+= int(ord(i))
    n = str(s)
print(dem)

