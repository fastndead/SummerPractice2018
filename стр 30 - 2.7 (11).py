def f(x):
    if(x % 5 == 0):
        return x / 5
    else:
        return x + 1

n = float(input("Enter value = "))
print(f(n))

