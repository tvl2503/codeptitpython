n = int(input())
string = input();
array = string.split()
s = 0
for x in range(n-1):
    for y in range(x+1, n):
        if int(array[x]) > int(array[y]):
            s = s + 1
print(s)