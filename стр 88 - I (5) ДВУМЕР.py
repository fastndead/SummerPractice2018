number = float(input("Enter Number to compare = "))
a = [] 
n = int(input('n = ')) 
m = int(input('m = ')) 
for i in range(n): 
    a.append([])
    for j in range(m): 
        a[i].append(int(input('Enter element: ')))
        
print('Initial array: ')
print(a)

for j in range(n):
    for k in range(m):
        if (a[j][k] < number):
            a[j][k] *= 2

print("Result array: ")
print(a)


        
    
