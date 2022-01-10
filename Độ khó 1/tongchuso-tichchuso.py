def add(n):
    sum = 0
    for i in range(len(n)):
        if i%2==0:
            sum += int(n[i])
    return sum
def multiply(n):
    s = 1
    dem = 0
    x = 0
    for i in range(len(n)):
        if i%2==1:
            if n[i] != '0':
                s *= int(n[i])
            else:
                dem +=1
            x += 1
    if dem == x:
        return 0
    else:
        return s 
test = int(input())
while test > 0:
    number = input()
    print(add(number),multiply(number),sep=" ")
    test -= 1