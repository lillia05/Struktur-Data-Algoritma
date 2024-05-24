import math

ulang = 10
x = 5

for i in range(ulang):
    f = x**2 - 5*x + 6
    df = 2*x - 5
    xx = x - (f / df)
    x = xx
    print("nilai x, f(x), dan df(x) ke ", i, " adalah", x, f, df)
