import numpy as np
#11
n = int(input("N = "))
a = np.random.randint(1, 50, (n, n))
print("Initial array :\n", a)
a = a.astype(float)
for i in range(n-1):
    temp = (a[i][i+1] + a[i+1][i]) / 2
    a[i][i+1] = temp
    a[i+1][i] = temp
print ('Result :\n', a)

