ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
ar_r1=[]
for i in ar1:
    if i in ar2:
        ar_r1.append(i)
ar_r2=[]
for j in ar_r1:
    if j in ar3:
        ar_r2.append(j)
print(ar_r2)


ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

# Using set intersection to find common elements
common_elements = set(ar1) & set(ar2) & set(ar3)

print(list(common_elements))


def dict_to_list(l):
    dict={}
    for i in l:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    return dict


common_list=(dict_to_list(ar1).keys()& dict_to_list(ar2).keys()&dict_to_list(ar3).keys())
print(common_list)