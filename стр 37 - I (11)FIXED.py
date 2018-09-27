import math

def f(x):
    s = 0
    t = 10
    for i in range(len(str(x))):
        s += (x % t) // (t/10) 
        t *= 10
    return int(s)

a = int(input("Enter a = "))
b = int(input("Enter b = "))

resSum = 0
for i in range(a,b + 1):
    print(i," - ",f(i))

