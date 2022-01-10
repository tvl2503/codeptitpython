n = int(input())
arr = []
even = []
odd = []
while n != len(arr):
    data = list(map(int, input().split()))
    arr += data
    for i in data:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
even.sort()
odd.sort(reverse=True)
for i in arr:
    if i%2 == 1 :
        print(odd[0],end=" ")
        odd.remove(odd[0])
    else:
        print(even[0],end=" ")
        even.remove(even[0])