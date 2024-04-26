class NilaiMahasiswa:
    def __init__(self, nama, nilai_kuis, nilai_tugas, nilai_ujian):
        self.nama = nama
        self.nilai_kuis = nilai_kuis
        self.nilai_tugas = nilai_tugas
        self.nilai_ujian = nilai_ujian

    def getNama(self):
        return self.nama

    def nilaiAkhir(self):
        nilai_akhir = 0.2 * self.nilai_kuis + 0.4 * self.nilai_tugas + 0.4 * self.nilai_ujian
        return nilai_akhir

    def hurufMutu(self):
        nilai = self.nilaiAkhir()
        if nilai >= 76:
            return 'A'
        elif 71 <= nilai < 76:
            return 'B+'
        elif 66 <= nilai < 71:
            return 'B'
        elif 61 <= nilai < 66:
            return 'C+'
        elif 56 <= nilai < 61:
            return 'C'
        elif 50 <= nilai < 56:
            return 'D'
        else:
            return 'E'

nama = input() 
nilai_kuis, nilai_tugas, nilai_ujian = input().split()
nilai_kuis = float(nilai_kuis)
nilai_tugas = float(nilai_tugas)
nilai_ujian = float(nilai_ujian)

mahasiswa = NilaiMahasiswa(nama, nilai_kuis, nilai_tugas, nilai_ujian)

print("Nama Mahasiswa:", mahasiswa.getNama())
print("Nilai Akhir:", mahasiswa.nilaiAkhir())
print("Huruf Mutu:", mahasiswa.hurufMutu())
