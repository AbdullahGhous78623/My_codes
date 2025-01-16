# string=input("Type:")
# j=0
# for i in string:
#     k=ord(i)
#     if k>=48 and k<=57:
#         j+=int(i)
    
# print(j)

string=input("Type:")
j=0
for i in string:
    if i>="0" and i<="9":
        j+=int(i)
    
print(j)

