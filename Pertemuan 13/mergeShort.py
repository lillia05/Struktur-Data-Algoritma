def merge_sort (arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        
        while i < len(left):
            result.append(left[i])
            i += 1
        
        while j < len(right):
            result.append(right[j])
            j += 1
        
        return result
    
arr = [8, 3, 1, 5, 2, 7, 4, 6]
sorted_arr = merge_sort(arr)
print("Array yang sudah diurutkan:", sorted_arr)

































# Merge Sort adalah salah satu algoritma pengurutan yang efisien dan stabil. Algoritma ini menggunakan pendekatan divide and conquer (bagi 
# dan taklukkan) untuk mengurutkan sebuah daftar (list) dengan membaginya menjadi bagian-bagian kecil, mengurutkan masing-masing bagian 
# secara terpisah, dan kemudian menggabungkan (merge) bagian-bagian tersebut secara berurutan untuk menghasilkan daftar yang terurut.
# Berikut adalah langkah-langkah untuk menjalankan algoritma Merge Sort:
# 1. Jika daftar memiliki satu elemen atau kurang, maka daftar tersebut sudah terurut dan dapat dikembalikan.
# 2. Bagi daftar menjadi dua bagian hampir sama dengan menentukan titik tengah.
# 3. Panggil rekursif Merge Sort untuk mengurutkan bagian kiri dan bagian kanan secara terpisah.
# 4. Gabungkan (merge) dua bagian yang sudah diurutkan menjadi satu daftar terurut dengan cara membandingkan elemen-elemen dari kedua 
# bagian dan menyusunnya secara berurutan.
# 5. Kembalikan daftar yang telah diurutkan.
# Keuntungan dari Merge Sort adalah bahwa ia memiliki kompleksitas waktu yang stabil, yaitu O(n log n), di mana n adalah jumlah elemen dalam 
# daftar. Algoritma ini juga tahan terhadap kasus terburuk dan baik dalam menangani daftar yang besar. Namun, Merge Sort menggunakan ruang 
# tambahan untuk menyimpan sementara elemen-elemen daftar selama proses penggabungan. Oleh karena itu, penggunaan ruang tambahan ini 
# perlu diperhatikan saat mengimplementasikan Merge Sort. Selain itu, Merge Sort memiliki beberapa varian, seperti Merge Sort Bawah ke Atas 
# (Bottom-Up Merge Sort) yang menggunakan pendekatan iteratif dan Merge Sort Alami (Natural Merge Sort) yang mengoptimalkan 
# penggabungan ketika daftar sudah terbagi menjadi beberapa subdaftar yang terurut. Dengan pemahaman yang baik tentang langkah-langkah 
# dan konsep di balik Merge Sort, Anda dapat mengimplementasikan algoritma ini dalam berbagai bahasa pemrograman dan menggunakannya 
# untuk mengurutkan daftar dengan efisien.
