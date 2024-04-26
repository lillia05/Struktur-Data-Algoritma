class Bilangan:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        for i in range(1, self.n + 1):
            yield i

bilangan = Bilangan(5)

for i in bilangan:
    print(i)