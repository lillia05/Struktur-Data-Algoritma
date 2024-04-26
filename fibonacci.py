def Fibonacci(n):
    deret = [0, 1]
    while len(deret) < n:
        nilai_berikutnya = deret[-1] + deret[-2]
        deret.append(nilai_berikutnya)
    return deret

n = int(input())

hasil = Fibonacci(n)
print(*hasil)