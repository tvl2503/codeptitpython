class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def Ucln(self):
        a = self.tu
        b = self.mau
        while a*b != 0 :
            if a > b: a %= b
            else: b %= a
        return a + b
    def toigian(self):
        i = PhanSo(self.tu, self.mau)
        self.tu = self.tu//i.Ucln()
        self.mau = self.mau//i.Ucln()
        print(f"{self.tu}/{self.mau}")

a,b = list(map(int, input().split()))
ps = PhanSo(a,b)
ps.toigian()
