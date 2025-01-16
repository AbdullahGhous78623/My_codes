def Repeating_elements(Argument):
    emp_dict={}
    for i in Argument:
        if i in emp_dict:
            emp_dict[i]+=1
        else:
            emp_dict[i]=1
    e_l=[]
    for key,value in emp_dict.items():
        if value==1:
            e_l.append(key)
    return(e_l)
          

a=Repeating_elements([4,5,6,7,2,3,4,5,6,7,8,9,1,2,4,5,6,7,8,9,1,2,4,6,7,9,767])
print(a)





