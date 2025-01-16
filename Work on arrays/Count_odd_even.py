# def count_odd_even(Argument):
#     e_d={}
#     for i in Argument:
#         if isinstance(i,int):
#             if i in e_d:
#                 e_d[i]+=1
#             else:
#                 e_d[i]=1            Jabardasti dictionary ka use
#     count_even=0
#     count_odd=0
    
#     for key in e_d:
#         if key %2 == 0:
#             count_even+=1
#         elif key%2!=0:
#             count_odd+=1
        
#     return (f'count of even is {count_even}\ncount of odd is {count_odd} ')

# Answer=count_odd_even([2,"harry","Harry",32,3,2,3,4,5,6,7,8,9,123,4,567,876,545,321,456,0.0008,"yo yo"])
# print(Answer)


def count_odd_even(Argument):
    count_even=0
    count_odd=0
    for i in Argument:
        if isinstance(i, int):
            if i%2==0:
                count_even+=1
            else:
                count_odd+=1
    return (f'count of even is {count_even}\ncount of odd is {count_odd} ')

Answer=count_odd_even([2,4,5,4,6,64,3,6,44,6,4,5,53,365,634,3544,4433,2])
print(Answer)
    
            
            


