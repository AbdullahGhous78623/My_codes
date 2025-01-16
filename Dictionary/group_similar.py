from collections import Counter

est_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8] 

dict_=Counter(est_list)
final_dict={}

for i,j in dict_.items():
    final_dict[i]=j*[i]

print(final_dict)
