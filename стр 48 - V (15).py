import math
def func(i):
    if 2 * i ** 5 - 1 >= 0:
        return math.log(math.fabs(3 * i)) * math.sqrt(2 * i ** 5 - 1)
    else:
        return "not defined"

        
a = float(input("введите а "))
b = float(input("введите b "))
h = float(input("введите h "))

while a <= b :
    print("x = ", a, end = "\t")
    print("f(x) = ", func(a))

    a+=h


