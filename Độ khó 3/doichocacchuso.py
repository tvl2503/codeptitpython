def doicho(string,n):
    index = -1
    for i in range(n - 2, -1, -1):
        if int(string[i]) > int(string[i + 1]):
            index = i
            break
    smallGreatDgt = -1
    for i in range(n - 1, index, -1):
        if (smallGreatDgt == -1 and int(string[i]) < int(string[index])):
            smallGreatDgt = i
        elif (index > -1 and int(string[i]) >= int(string[smallGreatDgt]) and int(string[i]) < int(string[index])):
            smallGreatDgt = i
    if index == -1:
        return "" . join("-1")
    else:
         
        # Swap both values
        (string[index], string[smallGreatDgt]) = (string[smallGreatDgt],string[index])
    if string[0] == '0': return -1
    return "" . join(string)
    
test = int(input())
while test >0:
    test -= 1
    n = input()
    print(doicho(list(n), len(n)))
     
    