string=input("Type:")
empty_string=""
for i in string:
    if i not in "aeiouAEIOU":
        empty_string+=i

print(empty_string)