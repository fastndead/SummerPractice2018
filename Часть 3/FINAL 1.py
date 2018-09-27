#1 первый способ list
def printMat(a, n, m):
    for i in range(n):
        for k in range(m):
            print(a[i][k], end = "\t")
        print()


a = [] 
n = int(input('n = ')) 
m = int(input('m = ')) 
for i in range(n): 
    a.append([])
    for j in range(m): 
        a[i].append(int(input('Enter element: ')))

b = []
while(True):
    n1 = int(input('n1 = '))
    m1 = int(input('m1 = '))
    if(n1 == n):
        break
    else:
        print("Invalid data! Try again")
for i in range(n1): 
    b.append([])
    for j in range(m1): 
        b[i].append(int(input('Enter element: ')))

print("Initial matrix 1:")
printMat(a, n, m)
print("\nInitial matrix 2:")
printMat(b, n1, m1)

for i in range(n):
    for k in range(m1):
        a[i].append(b[i][k])

print("\nResult: ")
printMat(a, n, m + m1)
