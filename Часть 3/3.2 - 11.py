import numpy as np
#11
n = int(input("N = "))
m = int(input("M = "))
a = np.random.randint(1, 50, (n, m))
print("Initial array :\n", a)
l = int(input("Enter number of row to sum : "))
print("Result :\n", np.array([a[i] + a[l] for i in range(n)]))
