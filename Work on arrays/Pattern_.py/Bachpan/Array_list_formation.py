import ctypes

# Define the capacity of the array
a = 5

# Create an array type with capacity slots, each slot can hold a Python object
ArrayType = a * ctypes.py_object

# Instantiate the array
array_instance = ArrayType()

# Assign values to the array
array_instance[0] = 10
array_instance[1] = 20
array_instance[2] = "hello"
array_instance[3] = [1, 2, 3]
array_instance[4] = (4, 5)

# Print the array elements
for i in range(a):
    print(array_instance[i])

# Output:
# 10
# 20
# hello
# [1, 2, 3]
# (4, 5)
