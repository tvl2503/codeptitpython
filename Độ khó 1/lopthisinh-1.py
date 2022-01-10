class ThiSinh:
    def __init__(self, fullname, date, grade1, grade2, grade3):
        self.fullname = fullname
        self.date = date
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3
        self.total = grade1 + grade2 + grade3
    def print(self):
        total = format(self.total, '.1f')
        print(f"{self.fullname} {self.date} {total}")
fullName = input()
dateOfBirth = input()
grade1 = float(input())
grade2 = float(input())
grade3 = float(input())
ts = ThiSinh(fullName, dateOfBirth, grade1, grade2, grade3)
ts.print()
        
        