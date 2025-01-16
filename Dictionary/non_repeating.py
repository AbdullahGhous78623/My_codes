from collections import Counter

def kth_non_repeating(str,k):
    dict_={}
    k=k-1

    for i in str:
        count_=0
        for j in str:
            if i==j:
                count_+=1
        if count_==1:
            dict_[i]=count_
    k_element=list(dict_.keys())
    return k_element[k]



def kth_non_repeating(str,k):
    counter_dict=(Counter(str))
    list_keys=[]
    for key,value in counter_dict.items():
        if value==1:
            list_keys.append(key)
    if 1<=k<=len(list_keys):
        return list_keys[k-1]
    else:
        return "Wrong input"





a=kth_non_repeating("geeksforgeeks",int(input("Type any k:")))
print(a)