s = input("Enter string = ")
lst = s.split()

n = len(lst)
j = n // 2
for i in range(j):
    lst[i], lst[j + i] = lst[j + i], lst[i]
    
   # temp = lst[i]
    #lst[i] = lst[int(n / 2 + i)]
    #lst[int(n / 2 + i)] = temp
    
print(lst)
