class Bunga:
    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna

    def get_nama(self):
        return self.nama

    def get_warna(self):
        return self.warna
    
mawar = Bunga("Mawar", "Merah")

print(f"Nama bunga: {mawar.nama}")
print(f"Warna bunga: {mawar.warna}")