a = list(map (int, input().split()))


print("Initial array : ")
print(a)

res = [i for i in a if i!= min (a)]

print("Result array : ")
print(res)
