fruits=["apple", "banana", "cherry"]

fruits.append("orange")  # Adding an item to the end of the list
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

fruits.remove("banana")  # Removing an item from the list
print(fruits)  # Output: ['apple', 'cherry', 'orange']

fruits.sort()  # Sorting the list
print(fruits)  # Output: ['apple', 'cherry', 'orange']

fruits.insert(1, "kiwi")  # Inserting an item at a specific position
print(fruits)  # Output: ['apple', 'kiwi', 'cherry',