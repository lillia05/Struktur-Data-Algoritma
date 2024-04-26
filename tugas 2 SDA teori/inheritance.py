class Hewan:
    def __init__(self, nama):
        self.nama = nama
    def bersuara(self):
        print("...")

class Kucing(Hewan):
    def __init__(self, nama, jenis):
        super().__init__(nama)
        self.jenis = jenis
    def bersuara(self):
        print("Meow! Meow!")

kucing = Kucing("Loly", "Anggora")
print(f"Nama kucing: {kucing.nama}")
print(f"Jenis kucing: {kucing.jenis}")
kucing.bersuara()