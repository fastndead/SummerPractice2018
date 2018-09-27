import numpy as np 
#1
ar = np.random.randint(0, 100, (4, 4)) 
print("Initial array : \n",ar) 
#2
print("Element [2,3] : ",ar[2,3]) 
#3
print("First row of array : ",ar[0])
#4
print("Every second element of third row : ")
print(ar[2,1::2])
#5
ar = np.reshape(ar, (8, 2))
print("Array after reshaping : \n",ar) 
#6
ar = ar * float(input("Multiplier = "))
print("Result of multiplication : \n",ar)
#7
print("Min elems in each row : \n",ar.min(axis = 1))
#8
height, width = ar.shape
print("Max elem in last column :\n", ar.max(axis = 0)[-1])
#9
x = np.random.randint(0, 10, (30))
print(x)
print( np.max([x[i] for i in range(len(x)) if x[i - 1] == 0]))
#10
ar3 = np.random.randint(0, 10, (10, 10))
print("Square matrix : \n", ar3)
print(np.prod([ar3.diagonal()[i] for i in np.nonzero(ar3.diagonal())]))
