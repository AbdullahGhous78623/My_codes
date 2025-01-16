a=(input("Write any number:"))

Original=a
palindrome=""

for i in range(len(a)):
    palindrome+=(a[-1-i])

Original=int(Original)
palindrome=int(palindrome)
    
if Original==palindrome:
    print("The number is palindrome")
else:
    print("The number is not palindrome")







