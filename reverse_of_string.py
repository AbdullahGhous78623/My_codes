String=input("Type:")
palindrome=""

j=-1

for i in String:
    
    palindrome+=String[j]
    j=j-1


print(palindrome)