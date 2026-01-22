tuple_example = ("apple", "banana", "cherry")
print("Tuple contents:", tuple_example)

# Accessing elements in a tuple
first_element = tuple_example[0]
print("First element:", first_element)

# Tuples are immutable, so we cannot change their contents
# The following line would raise an error if uncommented    

tuple_example[1] = "blueberry"  # This will raise a TypeError
# Instead, we can create a new tuple if we want to change values
new_tuple = (tuple_example[0], "blueberry", tuple_example[2])
print("New tuple contents:", new_tuple)