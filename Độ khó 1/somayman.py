st = input()
dem4 = 0
dem7 = 0
for i in st:
    if i =='4':
        dem4 += 1
    elif i == '7':
        dem7 += 1
sum = dem4 + dem7
if sum == 4 or sum == 7:
    print('YES')
else: print('NO')