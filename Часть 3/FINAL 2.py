#2 второй способ numpy arra
import numpy as np
n = int(input('n = ')) 
m = int(input('m = ')) 
a = np.random.randint(0, 10, (n, m))

while(True):
    n1 = int(input('n1 = '))
    m1 = int(input('m1 = '))
    if(n1 == n):
        break
    else:
        print("Invalid data! Try again")
        
b = np.random.randint(0, 10, (n1, m1))

print("Initial matrix 1:")
print(a)
print("\nInitial matrix 2:")
print(b)

a = np.append(a, b, axis = 1)
        
print("\nResult: ")
print(a)

      
