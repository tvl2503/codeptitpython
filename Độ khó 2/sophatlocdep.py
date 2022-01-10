def soPhatLocDep(n):
    if n[0] =='8' :
        return False
    for i in range(len(n)):
        if n[i]!='6' and n[i]!= '8':
            return False
        else:
            if i <= len(n) - 3 :
                if n[i] == '8' and n[i+1] == '8' and n[i+2] == '8':
                    return False
    return True

n = input()
if soPhatLocDep(n): print('YES')
else : print('NO')