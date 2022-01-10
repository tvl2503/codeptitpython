def multiply(n):
    mul = 1
    for i in n:
        if i != '0':
            mul *= int(i)
    return mul
test = int(input())
while test > 0:
    number = input()
    print(multiply(number))
    test -= 1