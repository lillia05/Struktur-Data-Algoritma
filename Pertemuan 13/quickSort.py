def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x <pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


arr = [8, 3, 1, 5, 2, 7, 4, 6]
sorted_arr = quick_sort(arr)
print("Array yang sudah diurutkan:", sorted_arr)




































# Quick Sort adalah salah satu algoritma pengurutan yang efisien dan sering digunakan. Algoritma ini menggunakan pendekatan divide and 
# conquer (bagi dan taklukkan) untuk mengurutkan sebuah daftar (list) dengan memilih elemen pivot, membagi daftar menjadi dua bagian 
# berdasarkan pivot, mengurutkan kedua bagian secara terpisah, dan kemudian menggabungkan bagian-bagian tersebut untuk menghasilkan 
# daftar yang terurut.
# Berikut adalah langkah-langkah untuk menjalankan algoritma QuickSort:
# 1. Pilih elemen pivot dari daftar. Pivot dapat dipilih secara acak, tetapkan sebagai elemen terakhir daftar, atau menggunakan pendekatan 
# lainnya.
# 2. Bagi daftar menjadi dua bagian, di mana elemen-elemen yang lebih kecil dari pivot ditempatkan di sebelah kiri pivot, dan elemen-elemen 
# yang lebih besar ditempatkan di sebelah kanan pivot.
# 3. Rekursif, panggil QuickSort untuk mengurutkan bagian kiri dan bagian kanan secara terpisah.
# 4. Gabungkan (merge) bagian kiri yang sudah diurutkan, elemen pivot, dan bagian kanan yang sudah diurutkan untuk menghasilkan daftar yang 
# terurut.
# Keuntungan dari QuickSort adalah kompleksitas waktu yang baik dalam kasus rata-rata, yaitu O(n log n), di mana n adalah jumlah elemen dalam 
# daftar. Algoritma ini juga dapat berjalan dengan cepat dan efisien dalam praktik, terutama untuk daftar yang besar.
# Namun, QuickSort memiliki kasus terburuk yang jarang terjadi, di mana kompleksitas waktu bisa mencapai O(n^2) jika pivot yang dipilih tidak 
# seimbang dan daftar tidak terbagi secara merata. Untuk mengatasi hal ini, beberapa varian QuickSort telah dikembangkan, seperti QuickSort 
# dengan pivot acak atau dengan strategi pemilihan pivot yang lebih cerdas.
# Pemahaman yang baik tentang langkah-langkah dan konsep di balik QuickSort memungkinkan Anda untuk mengimplementasikan algoritma ini 
# dalam berbagai bahasa pemrograman dan menggunakannya untuk mengurutkan daftar secara efisien.
