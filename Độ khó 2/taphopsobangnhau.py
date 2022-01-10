def arrayEqual(arrayA,arrayB):
    if arrayA!=arrayB:
        return False
    return True
n,m = list(map(int, input().split()))
arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))
arrayA = list(set(arrayA))
arrayB = list(set(arrayB))
arrayA.sort()
arrayB.sort()
if arrayEqual(arrayA,arrayB): print('YES')
else : print('NO')