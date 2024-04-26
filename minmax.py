def find_min_max(sequence):
    def find_min_max_recursive(bil, awal, akhir):
        if awal == akhir:
            return bil[awal], bil[awal]
        if akhir - awal == 1:
            return (bil[awal], bil[akhir]) if bil[awal] < bil[akhir] else (bil[akhir], bil[awal])
        mid = (awal + akhir) // 2
        min1, max1 = find_min_max_recursive(bil, awal, mid)
        min2, max2 = find_min_max_recursive(bil, mid + 1, akhir)
        return min(min1, min2), max(max1, max2)

    bil = list(map(int, sequence.split()))
    nilai_min, nilai_max = find_min_max_recursive(bil, 0, len(bil) - 1)
    return nilai_min, nilai_max

n = int(input())
sequence = input()
nilai_min, nilai_max = find_min_max(sequence)
print(nilai_min, nilai_max)
