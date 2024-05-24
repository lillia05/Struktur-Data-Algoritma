def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x <pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

#contoh array untuk diurutkan
arr = [38, 27, 43, 3, 9, 82, 10]

#memulai quick sort
sorted_arr = quick_sort(arr)

#menampilkan hasil array yang sudah diurutkamn
print("Array yang sudah diurutkan:", sorted_arr)