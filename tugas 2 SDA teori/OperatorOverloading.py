class Bilangan:
    def __init__(self, nilai):
        self.nilai = nilai
    def __add__(self, other):
        return Bilangan(self.nilai + other.nilai)
    def __str__(self):
        return str(self.nilai)

a = Bilangan(12)
b = Bilangan(3)
c = a + b

print(c)