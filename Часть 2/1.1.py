l = list (map (int, input().split()))

t = [i for i in l if i > 0 and i % 7 == 0]
        
print("Initial array : ",l)
print("Result array : ",t)
