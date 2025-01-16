import math

a = [2, 4, 5, 6, 3, 2, "Harry", 7, 3, 5, 7, "Harry", 2, 9, 4, 8, 9, 1, 9, 7, 4, 5, 6, 3, 7, 8, 9, 1]

# Step 1: Build frequency dictionary
frequency_dict = {}
for item in a:
    if item in frequency_dict:
        frequency_dict[item] += 1
    else:
        frequency_dict[item] = 1

print(frequency_dict)

# Step 2: Extract frequencies and sort them
frequencies = list(frequency_dict.values())
sorted_frequencies = sorted(set(frequencies), reverse=True)  # Sort unique frequencies in descending order

print(sorted_frequencies)

# Step 3: Map frequencies to elements
frequency_to_elements = {}
for key, value in frequency_dict.items():
    if value in frequency_to_elements:
        frequency_to_elements[value].append(key)
    else:
        frequency_to_elements[value] = [key]

print(frequency_to_elements)

# Step 4: Create a list of elements sorted by their frequencies
sorted_elements = []
for freq in sorted_frequencies:
    sorted_elements.extend(frequency_to_elements[freq])

print(sorted_elements)

# Print dictionary values
print(list(frequency_dict.values()))
