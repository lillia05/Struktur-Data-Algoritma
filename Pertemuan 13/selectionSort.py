def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

arr = [8, 3, 1, 5, 2, 7, 4, 6]
sorted_arr = selection_sort(arr)
print("Array yang sudah diurutkan", sorted_arr)




































# Selection Sort (Pengurutan Pilihan) adalah salah satu algoritma pengurutan yang sederhana tetapi tidak efisien. Algoritma ini bekerja dengan 
# membagi daftar menjadi dua bagian: bagian yang terurut dan bagian yang belum terurut. Pada setiap langkah, algoritma akan mencari elemen 
# terkecil dari bagian yang belum terurut dan menukar posisinya dengan elemen pertama dari bagian terurut. Langkah-langkah ini diulang sampai 
# seluruh daftar menjadi terurut.
# Berikut adalah langkah-langkah untuk menjalankan algoritma Selection Sort:
# 1. Tentukan daftar yang akan diurutkan.
# 2. Bagi daftar menjadi dua bagian: bagian terurut (awalnya kosong) dan bagian belum terurut (berisi seluruh daftar).
# 3. Di setiap langkah, cari elemen terkecil dari bagian belum terurut dan tukar posisinya dengan elemen pertama dari bagian terurut.
# 4. Pindahkan batas antara bagian terurut dan bagian belum terurut satu langkah ke depan.
# 5. Ulangi langkah-langkah 3-4 sampai seluruh daftar menjadi terurut.
# Keuntungan dari Selection Sort adalah kesederhanaan dan kejelasan algoritmanya. Selain itu, Selection Sort dapat digunakan jika memori 
# terbatas karena hanya membutuhkan sedikit penambahan memori selain daftar yang akan diurutkan.
# Namun, Selection Sort memiliki kompleksitas waktu yang buruk, yaitu O(n^2), di mana n adalah jumlah elemen dalam daftar. Algoritma ini tidak 
# efisien untuk daftar yang besar karena melakukan banyak perbandingan dan pertukaran elemen, terlepas dari apakah daftar sudah terurut 
# sebagian atau tidak.
# Dalam praktiknya, Selection Sort jarang digunakan pada data yang besar, tetapi mungkin berguna dalam kasus di mana jumlah elemen sedikit 
# atau ketika daftar hampir terurut.
# Pemahaman tentang langkah-langkah dan konsep di balik Selection Sort dapat membantu Anda memahami cara kerja algoritma pengurutan dan 
# memilih algoritma yang lebih efisien tergantung pada kasus penggunaannya.