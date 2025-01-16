# importing "operator" for implementing itemgetter
from operator import itemgetter

# Initializing list of dictionaries
data_list = [{"name": "Nandini", "age": 20},
             {"name": "Manjeet", "age": 20},
             {"name": "Nikhil", "age": 19}]

# using sorted and itemgetter to print list sorted by age
print("The list printed sorting by age: ")
print(sorted(data_list, key=itemgetter('age')))

print("\r")

# using sorted and itemgetter to print
# list sorted by both age and name
# notice that "Manjeet" now comes before "Nandini"
print("The list printed sorting by age and name: ")
print(sorted(data_list, key=itemgetter('age', 'name')))

print("\r")

# using sorted and itemgetter to print list
# sorted by age in descending order
print("The list printed sorting by age in descending order: ")
print(sorted(data_list, key=itemgetter('age'), reverse=True))