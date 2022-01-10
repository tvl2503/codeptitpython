import math
class Triangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def tinh(self, b):
        return math.sqrt((self.x - b.x)**2 + (self.y - b.y)**2)
t = int(input())
while t > 0:
    t -= 1
    x1,y1,x2,y2,x3,y3 = list(map(float, input().split()))
    A = Triangle(x1,y1)
    B = Triangle(x2,y2)
    C = Triangle(x3,y3)
    AB = A.tinh(B)
    AC = A.tinh(C)
    BC = B.tinh(C)
    if(AB + AC <= BC or AB + BC <= AC or AC + BC <= AB):
        print('INVALID')
    else:
        cv = AB + AC + BC
        print(format(cv, '.3f'))
        
        