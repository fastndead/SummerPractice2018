digit = int(input("Enter digit = "))
insertValue = int(input("Enter insert value = "))
n = int(input("Enter array length = "))
a = []
for i in range(n):
    a.append(int(input()))


i = 0
while i < len(a):
    if a[i] % 10 == digit:
        a.insert(i, insertValue)
        i += 1
    i += 1
print(a)

