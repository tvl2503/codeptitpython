s = input()
def myfunc(str1):
    dem = 0
    for i in str1:
        if i.isupper():
            dem += 1
    if 2*dem > len(str1):
        return True
    else: return False
if(myfunc(s)):
    print(s.upper())
else: 
    print(s.lower())