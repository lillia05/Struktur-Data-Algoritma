import math

def hitung_luas_lingkaran(jari_jari):
  luas = math.pi * jari_jari ** 2
  return luas

jari_jari = float(input("Masukkan jari-jari lingkaran (cm): "))
luas_lingkaran = hitung_luas_lingkaran(jari_jari)
print(f"Luas lingkaran: {luas_lingkaran:.2f} cm persegi")