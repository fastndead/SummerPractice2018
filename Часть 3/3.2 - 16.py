import numpy as np
#16
n = int(input("N = "))
m = int(input("M = "))
a = np.random.randint(1, 50, (n, m))
print("Initial array :\n", a)
l = int(input("Enter number of row to delete : "))
a = np.delete(a, l, 0)
print("Result array :\n", a)
