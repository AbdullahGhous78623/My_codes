from collections import Counter

input =['john','johnny','jackie','johnny',
            'john','jackie','jamie','jamie',
            'john','johnny','jamie','johnny',
            'john'] 
# dict={}
# for i in input:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# result=[]
# list_=max(dict.values())
# print(dict.values())
# for j in dict:
    
#     if dict[j]==list_:
#         result.append(j)

# result=sorted(result)
# print(result[0])
counter_dict=((Counter(input)))
result=[]
list_=max(counter_dict.values())
# print(counter_dict.values())
for j in counter_dict:
    
    if counter_dict[j]==list_:
        result.append(j)

print(sorted(result)[0])
