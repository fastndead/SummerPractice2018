import math
x = float(input('Введите x '))
y = float(input('Введите y '))
if y == 12 and  math.fabs(x) < 12 or y <= 12 and y == math.fabs(x):
    print('На границе')
elif y < 12 and y > math.fabs(x):
    print('Да')
else:
    print('Нет')
