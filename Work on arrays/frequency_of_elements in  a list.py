# a=[2,4,5,6,3,2,6,7,3,5,7,8,2,9,4,8,9,1,9,7,4,5,6,3,7,8,9,1]
# frequency=0
# User_number=int(input("Type any integer number :"))

# for j in a:
#     if j==User_number :
#         frequency+=1
# if frequency>=1:
#     print(f"The {User_number} you entered has frequency {frequency}")
# else:
#     print("Error: The input entered is not in the list")


a=[2,4,5,6,3,2,"Harry",7,3,5,7,"Harry",2,9,4,8,9,1,9,7,4,5,6,3,7,8,9,1]
frequency=0
dict={}

for j in a:
    if j in dict:
        dict[j]+=1
    else:
        dict[j]=1

print (dict)

    

for k,l in dict.items():
    print(f"For number {k} the frequency is:{l}")
