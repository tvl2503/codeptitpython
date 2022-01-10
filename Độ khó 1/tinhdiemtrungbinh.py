
import functools
def caculate(arr):
    minNumber = min(arr)
    maxNumber = max(arr)
    arr = list(filter(lambda a: a!=minNumber, arr))
    arr = list(filter(lambda a: a!=maxNumber, arr))
    return float(functools.reduce(lambda total, sum: total + sum, arr)/len(arr))
n = int(input())
arr = list(map(float, input().split()))
print(round(caculate(arr),2))
