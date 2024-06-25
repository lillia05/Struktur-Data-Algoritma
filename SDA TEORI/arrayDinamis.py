class DynamicArray:
    def __init__(self):
        self._data = []
    
    def __getitem__(self, idx):
        return self._data[idx]
    
    def __setitem__(self, idx, value):
        self._data[idx] = value
    
    def append(self, value):
        self._data.append(value)
    
    def pop(self):
        if len(self._data) == 0:
            raise IndexError("pop from empty list")
        return self._data.pop()
    
    def __len__(self):
        return len(self._data)
    
    def __str__(self):
        return str(self._data)

arr = DynamicArray()
arr.append(1)
arr.append(2)
arr.append(3)
print("Array:", arr)
print("Panjang array:", len(arr))
print("Elemen ke-1:", arr[0])
print("Elemen ke-2:", arr[1])
print("Elemen ke-3:", arr[2])
arr[1] = 5
print("Array setelah diubah:", arr)
print("Panjang array setelah diubah:", len(arr))
print("Elemen terakhir dihapus:", arr.pop())
print("Array setelah pop:", arr)
