list=[2,3,5,4,6,5,2,5,75,3]
value=list[0]

for i in list:
    if value>i:
        value=i
balue=list[0]
for i in list:
    if balue<i:
        balue=i

min_value=balue

for i in list :
    if value==i:
        continue
    elif balue>i :
        min_value=i
print(min_value)
    

        

list=[2,3,5,4,6,5,2,5,75,3]
value=list[0]

for i in list:
    if value>i:
        value=i

second_min_value = float('inf')

for i in list :
    if value!=i and second_min_value>i:
        
    
       second_min_value =i
print(second_min_value)