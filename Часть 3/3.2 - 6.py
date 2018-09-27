import numpy as np
#6
n = int(input("N = "))
m = int(input("M = "))
a = np.random.randint(1, 50, (n, m))
print("Initial array :\n", a)
#print('All elements sumed : ', np.sum(a))
#print('Sum for each column : ', (np.sum(a, axis = 0)))
print("Result :\n", np.vstack((a, (np.sum(a, axis = 0) / np.sum(a)))))
