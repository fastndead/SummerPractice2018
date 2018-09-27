import numpy as np
#16
n = int(input("N = "))
m = int(input("M = "))
a = np.random.randint(1, 50, (n, m))
L = int(input('Row to divide matrix by : '))
K = int(input('Coulumn to divide matrix by : '))

print("Initial array : \n", a)
print("Part 1:\n", a[0:L+1, 0:K+1])
print("Part 2:\n", a[L+1:n, 0:K+1])
print("Part 3:\n", a[0:L+1, K+1:m])
print("Part 4:\n", a[L+1:n, K+1:m])


print ('Mean value in 1 part\n', np.mean(a[0:L+1, 0:K+1]))
print ('Mean value in 2 part\n', np.mean(a[L+1:n, 0:K+1]))
print ('Mean value in 3 part\n', np.mean(a[0:L+1, K+1:m]))
print ('Mean value in 4 part\n', np.mean(a[L+1:n, K+1:m]))

