from abc import ABC, abstractmethod

class BangunDatar(ABC):
    @abstractmethod
    def hitung_luas(self):
        pass

class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    def hitung_luas(self):
        return (self.alas * self.tinggi) / 2

segitiga = Segitiga(9, 7)
luas_segitiga = segitiga.hitung_luas()
print(f"Luas segitiga: {luas_segitiga}")