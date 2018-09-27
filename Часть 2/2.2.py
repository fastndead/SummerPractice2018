number = float(input("Enter element to insert : "))

a = list(map (int, input().split()))

print("Initial array : ", a)

i = 0
while i < len(a):
    if(a[i] < 100 and a[i] > 9):
                     a.insert(i + 1, number)
                     i += 1
    i += 1
    
print("Result array : ", a)

    
