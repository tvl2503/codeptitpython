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
    def tong(self, ps2):
        self.tu = self.tu * ps2.mau + self.mau*ps2.tu
        self.mau = self.mau*ps2.mau

tu1, mau1, tu2, mau2 = list(map(int, input().split()))
ps1 = PhanSo(tu1,mau1)
ps2 = PhanSo(tu2,mau2)
ps1.tong(ps2)
ps1.toigian()

