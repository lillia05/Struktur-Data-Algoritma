class Mahasiswa:
    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm
    def cetak_info(self):
        print(f"Nama: {self.nama}")
        print(f"NPM : {self.npm}")

mahasiswa = Mahasiswa("Lekok Indah Lia", "2317051097")
mahasiswa.cetak_info()