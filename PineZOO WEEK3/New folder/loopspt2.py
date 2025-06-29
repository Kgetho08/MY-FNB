fruits=["apple", "banana", "cherry" ,"orange"]

for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)
    
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)
    
for fruit in fruits:
    if fruit == "banana":
        pass
    print(fruit)