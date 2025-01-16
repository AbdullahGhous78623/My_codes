String=input("Type:")
palindrome=""

j=-1

for i in String:
    
    palindrome+=String[j]
    j=j-1


if String==palindrome:
    print("The number is palindrome")
else:
    print("The number is not palindrome")