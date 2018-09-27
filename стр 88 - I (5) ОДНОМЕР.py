number = float(input("Enter Number to compare = "))
a = [] 
n = int(input('n = ')) 
for i in range(n):
    a.append(int(input()))

for i in range(n):
    if a[i] < number:
        a[i] *= 2

print(a)
    
