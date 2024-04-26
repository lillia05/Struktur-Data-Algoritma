class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
    def bersuara(self):
        if self.jenis == "Kucing":
            print(f"Meow! Meow! (Suara {self.nama})")
        elif self.jenis == "Bebek":
            print(f"Kwek! Kwek! (Suara {self.nama})")
        elif self.jenis == "Ayam":
            print(f"ptok! (Suara {self.nama})")
        else:
            print(f"Suara {self.jenis} {self.nama}: ...")

kucing = Hewan("oyen", "Kucing")
bebek = Hewan("piti", "Bebek")

print(f"Jenis Hewan: {kucing.jenis}")
print(f"Nama Hewan : {kucing.nama}\n")
print(f"Jenis Hewan: {bebek.jenis}")
print(f"Nama Hewan : {bebek.nama}\n")

kucing.bersuara()
bebek.bersuara()