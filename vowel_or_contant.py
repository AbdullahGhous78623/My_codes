def vowel_or_consonant(character):
    
    if not character.isalpha():
        print("Error!")
    elif character=="a" or character=="e" or character=="i" or character=="o" or character=="u"  :
        print ("The character is vowel")
    else:
        print("The character is not vowel")


vowel_or_consonant(input("Type the character:"))







# def isLowercaseVowel(c):
#     # returns 1 if char matches any of below
#     return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'


# def isUppercaseVowel(c):
#     # returns 1 if char matches any of below
#     return c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U'


# c =input("Type the character:")

# # show error message if c is not an alphabet
# if not c.isalpha():
#     print("Non alphabet")
# elif isLowercaseVowel(c) or isUppercaseVowel(c):
#     print(c, "is a Vowel")
# else:
#     print(c, "is a consonant")


