import math
a=[2,4,5,6,3,2,"Harry",7,3,5,7,"Harry",2,9,4,8,9,1,9,7,4,5,6,3,7,8,9,1]

dict={}
for i in a:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1

e_l=list(dict.values())

print(e_l) 
e_2=[]
for k in range(len(e_l)):
    max_value=-math.inf
    for l in e_l:
        if max_value<l:
            max_value=l
    e_2+=[max_value]
    e_l.remove(max_value)
print(e_2)
e_set=set(e_2)
e_2=list(e_set)
e_2=sorted(e_2,reverse=True)
print(e_2)


e_3={}
for key,value in dict.items():
    if value in e_3:
        e_3[value].append(key)
    else:
        e_3[value]=[key]
print(e_3) 
Em_list=[]

for number in e_2:
    elements=e_3[number]
    for element in elements:
        Em_list+=[element]

print(Em_list)



# print(dict)
# e_l=[]
# for j in dict.values():
#     e_l.append(j)

# print(e_2)
# e_3=[]
# for key,values in dict.items():
#     for m in e_2:
#         if values==m:
#             e_3+=[key]
#             break
# print(e_3)  
    





