import numpy as np
#1
n = int(input("N = "))
m = int(input("M = "))
a = np.random.randint(1, 50, (n, m))
print("Initial array :\n", a)
a1 = np.array([np.sum(np.abs(a[:,i])) for i in range(m)])
print("\nSUMS :\n",a1)
print("Max elem: ", max(a[:,np.unravel_index(a1.argmax(), a1.shape)]))



