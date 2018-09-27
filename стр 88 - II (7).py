n = int(input("Enter n = ")) 
a = []
for i in range(n):
    a.append(int(input("Enter element : ")))

print("Initial array : ")
print(a)

num = 0
min = a[0]
for i in range(n):
    if a[i] < min:
        min = a[i]
        num = i

print("min element is on position", end = " ")
print(num + 1)
    
