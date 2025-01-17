# def factors(factors):
#     if factors==1:
#         return [1]
    
#     if factors>=2:
#         factors_count=[1,factors]
#         for i in range(2,factors//2+1):
#             if factors%i==0:
#                 factors_count.append(i)
                
#         return sorted(factors_count)
#     else:
#         return []
    




# factors_of_n1=factors(54)
# factors_of_n2=factors(50)
# common_factors=set(factors_of_n1)& set(factors_of_n2)

# if common_factors:
#     print(max(common_factors))
# else:
#     print("No common factors found")
  

# num1=25
# num2=50
# hcf=1
# for i in range(1,min(num1,num2)+1):
#     if num1%i==0 and num2%i==0:
#         hcf=i
# print(hcf)

# LCM
# n1=100
# n2=899
# hcf=1
# for i in range(1,min(n1,n2)+1):
#     if n1%i==0 and n2%i==0:
#         hcf=i
    

# lcm=(n1*n2)//hcf
# print(lcm)


