# Lists

fruits = ["apple", "banana", "orange"]

print(fruits)          # Print the whole list
print(fruits[0])       # First item

fruits.append("mango") # Add to the end
print(fruits)

fruits.insert(1, "grape") # Add at index 1
print(fruits)

fruits.remove("banana")   # Remove by value
print(fruits)

fruits.pop(0)             # Remove by index
print(fruits)

print(len(fruits))        # Count items