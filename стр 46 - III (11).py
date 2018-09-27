import math
a = int(input('Введите a '))
b = int(input('Введите b '))
x = int(input('Введите x '))
y = int(input('Введите y '))
while a <= b:
    if a % 10 == x or a % 10 == y:
        print(a)
    a += 1
    
