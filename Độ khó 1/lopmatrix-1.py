class Matrix:
    def __init__(self, n,m):
        self.n = n
        self.m = m
        self.maxtrix = []
        self.maxtrixb = []
        self.maxtrixc = []
    def nhap(self):
        for i in range(self.n):
            a = list(map(int, input().split()))
            self.maxtrix.append(a)
        for i in range(self.n):
            for j in range(self.m):
                self.maxtrixb[j][i] = self.maxtrix[i][j]
    def tich(self):
        for i in range(self.n):
            for j in range(self.m):
                for t in range(self.m):
                     self.maxtrixc[i][j] += self.maxtrix[i][t]*self.maxtrixb[t][j]
        for i in range(self.n):
            for j in range(self.m):
                print(self.maxtrixc[i][j], end= ' ')
            print()
a,b = list(map(int, input().split()))
mt = Matrix(a,b)
mt.nhap()
mt.tich()
        