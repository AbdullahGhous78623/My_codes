f="23 43 54"
m1=f.split()
print(m1)

text = "Hello world welcome"
result = text.split()
print(result)
text = "one two three four five"
result = text.split(" ", 2)
print(result)
text = "apple,banana,grape"
result = text.split(",")
print(result)
text = "   Hello    world   "
result = text.split()
print(result)
['a', 'b', 'c', '', 'd', '', '']
text = "hello"
result = text.split("")  # This will raise a ValueError
text = "apple|banana|grape"
result = text.split("|")
print(result)
