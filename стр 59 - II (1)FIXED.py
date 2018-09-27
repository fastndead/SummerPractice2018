import math


def f(n, s, x, count, xPrev):
    if (count != n + 1):
        x = x * xPrev
        s += x / count
        f(n, s, x, count + 1, xPrev)
    else:
        print(s)


s = 0
n = int(input('Enter n '))
x = float(input("Enter x = "))

f(n, x, x, 2, x)
