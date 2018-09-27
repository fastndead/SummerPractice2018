import math
def func(i, a, b):
    if(i < 93):
        temp = a + b * i
    elif(i <= 120):
        temp = b - a * i
    else:
        temp = a * b * i
    print("x = ", i, end = "\t")
    print("f(x) = ", temp)
         

a = float(input("введите а "))
b = float(input("введите b "))
h = float(input("введите h "))
i = a
while i <= b:
    func(i, a, b)
    i += h
