def faktor_bilangan(n):
    faktor_bil = []
    for i in range(n, 0, -1):
        if n % i == 0:
            faktor_bil.append(i)
    return faktor_bil

n = int(input())
faktor_bil = faktor_bilangan(n)
for faktor in faktor_bil:
    print(faktor)
