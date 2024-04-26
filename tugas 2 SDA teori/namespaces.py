class Person:
    def __init__(self, nama):
        self.nama = nama

    def greeting(self):
        print(f"Halo, nama saya {self.nama}")

class Kuliah(Person):
    def __init__(self, nama, jurusan):
        super().__init__(nama)
        self.jurusan = jurusan

    def greeting(self):
        super().greeting()
        print(f"Saya berkuliah di jurusan {self.jurusan}")

lia = Kuliah("Lekok Indah Lia", "Ilmu Komputer")
lia.greeting()