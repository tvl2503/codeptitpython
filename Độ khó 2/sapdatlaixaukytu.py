def kiemtra(string1,string2):
    s1 = set(string1)
    s2 = set(string2)
    if s1 == s2:
        for i in s1:
            if string1.count(i)!= string2.count(i):
                return False
    else:
        return False
    return True

test = int(input())
i = 1
while i <= test:
    string1 = input()
    string2 = input()
    if kiemtra(string1,string2):
        print(f"Test {i}: YES")
    else: print(f"Test {i}: NO")
    i += 1
