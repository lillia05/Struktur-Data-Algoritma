def PolaSegitiga(n):
    for i in range(n):
        print(" " * (n - i) + "*" * (2 * i - 1))
n = int(input())
PolaSegitiga(n)