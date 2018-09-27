import math


def f(n, s, x, count):
    if (count != n + 1):
        x = x + math.sin(count)
        s += 1 / x
        f(n, s, x, count + 1)
    else:
        print(s)


s = 0
n = int(input('Введите n '))

# for i in range(1, n + 1):
#    temp = 0
#    for k in range(i + 1):
#        temp += math.sin(k)
#    s += 1 / temp
f(n, 0, 0, 1)
