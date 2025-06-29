my_set=[1, 2, 3, 4, 5]
print(my_set)  # Output: [1, 2, 3, 4, 5]
my_set.add(6)  # Adding an item to the set  
print(my_set)  # Output: [1, 2, 3, 4, 5, 6]
my_set.remove(3)  # Removing an item from the set
print(my_set)  # Output: [1, 2, 4, 5, 6]
my_set.discard(2)  # Discarding an item (no error if not
# present)
print(my_set)  # Output: [1, 4, 5, 6]
my_set.clear()  # Clearing the set  
print(my_set)  # Output: []