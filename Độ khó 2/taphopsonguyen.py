n,m = list(map(int, input().split()))
arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))
arrayA = list(set(arrayA))
arrayB = list(set(arrayB))
arrayA.sort()
arrayB.sort()
arr = []
for i in arrayA:
    if i in arrayB:
        print(i,end=" ")
        arr.append(i)
print()
for i in arrayA:
    if i not in arr:
        print(i,end=" ")
print()
for i in arrayB:
    if i not in arr:
        print(i,end=" ")