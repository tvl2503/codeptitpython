def thapphan(s):
    s = s[::-1]
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])*(2**i)
    return sum
n = input()
mod = len(n) % 3
for i in range(3 - mod):
    n = '0' + n
s = ''
for i in range(0,len(n),3):
    s += str(thapphan(n[i:i+3]))
print(int(s))
