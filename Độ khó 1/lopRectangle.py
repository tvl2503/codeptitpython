
class Rectangle:
    def __init__(self, cd, cr, cl):
        self.cd = cd
        self.cr = cr
        self.cl = cl
    def perimeter(self):
        return (int(self.cd) + int(self.cr))*2
    def area(self):
        return (int(self.cd) * int(self.cr))
    def color(self):
        return self.cl[0].upper() + self.cl[1:].lower()
    
arr = input().split()
if int(arr[0]) <=0 or int(arr[1]) <= 0:
    print("INVALID")
else:
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))