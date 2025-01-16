from collections import Counter

def NonRepeating(char):
    non_repeating=[]
    freq_dict=Counter(char)
    for key in freq_dict:
        if freq_dict[key] == 1:
            non_repeating.append(key)
    return non_repeating


user_input=input("Type someting:").strip()

a=NonRepeating(user_input)
print(a)


    

