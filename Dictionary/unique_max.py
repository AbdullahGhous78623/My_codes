test_dict = {"Gfg" : [5, 7, 9, 4, 0], "is" : [6, 7, 4, 3, 3], "Best" : [9, 9, 6, 5, 5]} 
count_dict={}
for i,j in test_dict.items():
    
    count_unique=len(set(j))
    count_dict[i]=count_unique

max_count=max(count_dict.values())
list_max=[]
for k in count_dict.keys():
    if count_dict[k]==max_count:
        list_max.append(k)
print(list_max)