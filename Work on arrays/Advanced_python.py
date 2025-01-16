# class Addition:
#     def __init__(self,n1,n2):
#         self.a=n1
#         self.b=n2
#     def addition(self):
#         return f"The sum of two number is {self.a+self.b}"
        
    

# obj1=Addition(8,9)
# a=obj1.addition()
# print(a)


# class Max_two:
#     a=500
#     def __init__(self,n2):
#         self.a=2
#         self.b=n2
#     def biggest(self):
#         if self.a>self.b:
#             return f"The biggest number is {self.a}"
#         else:
#             return f"The biggest number is {self.b}"
        
# obj=Max_two(92)



# a=obj.biggest()
# print(a)
# print(obj.a)


# class factorial:
#     def __init__(self,n):
#         if n<0:
#             raise Exception("Factorial is not defined for negative number")
#         self.a=n
#     def fact(self):
#         product=1
#         for i in range(1,(self.a)+1):
#             product*=i
#         return product
    
    
# try:
#     obj1=factorial(-7)
#     a=obj1.fact()
#     print(a)
# except Exception as e:
#     print(e)


# print("Important code that has to eun in any case")


# class Simple_interest:
#     def __init__(self,p,q,r):
#         if p<=0 or q<=0 or r<=0:
#             raise Exception("The simple interest is not defined")
            
#         self.p=p
#         self.q=q
#         self.r=r
#     def sim_int(self):
#         return (self.p*self.q*self.r)/100
    

# try:
#     obj=Simple_interest(4,-5,6)
#     a=obj.sim_int()
#     print(a)
# except Exception as e:
#     print(e)

# class Armstrong:
#     def __init__(self,n):
#          if n<0:
#                 raise Exception("The number should not be negative")
#          self.n=n
#     def Arm(self):
#         Armstrong_n=0
#         Str_n=str(self.n)
#         for i in Str_n:
#             Armstrong_n+=(int(i))**len(Str_n)
#         return Armstrong_n==self.n
# try:
#     obj=Armstrong(154)
#     if obj.Arm():
#         print("The number is Armstrong")
#     else:
#          print("The number is not Armstrong")
# except Exception as e:
#      print(e)
# from math import pi

# class circle:
#     def __init__(self,r):
#         if r<0:
#             raise Exception("Radius can't be nagative")
#         self.r=r
#     def area(self):
#         return f"Area of circle is {pi*(self.r**2)}"
# try:
#     obj=circle(pi**0.5) 
#     print(obj.area())
# except Exception as e:
#     print(e)

# import math
# class Prime:
#     def __init__(self,n1,n2):
        
#         self.n1=max(2,n1)
        
#         self.n2=n2
#     def prime_range(self):
        
#         E_l=[]
#         for i in range(self.n1,self.n2+1):
#             prime=True
#             for j in range(2,int(math.sqrt(i)) + 1):
#                 if i%j==0:
#                     prime=False
#                     break
#             if prime:
#                 E_l.append(i)
#         return E_l


# obj=Prime(0,1000)
# a=obj.prime_range()
# print(a)

# import math
# class Prime:
#     def __init__(self,n1):
#         if n1<2:
#             raise ValueError("Out_of_range")
#         self.n1=n1
#     def prime_num(self):
#         for i in range(2,int(math.sqrt(self.n1)+1)):
#             if self.n1%i==0:
#                 return "The number is not prime"
            
#         return "The number is prime"

# obj=Prime(89)
# a=obj.prime_num()
# print(a)

# class fibonacci:
#     def __init__(self,n):
#         if n<=0:
#             raise ValueError("Out_of_range")
#         self.n=n
#     def fib_series(self):
#         if self.n==1:
#             print(0)
#             return
#         if self.n==2:
#             print(0,1)
#             return

        
#         a,b=0,1
#         print(a,b, end=" ")
        
#         for _ in range (self.n-2):
#             print(a+b,end=" ")
#             a,b=b,a+b
# obj=fibonacci(500)
# obj.fib_series()


# class Sum_Array:
#     def __init__(self,n):
#         self.n=n
#     def sum_element(self):
#         add=0
#         for i in self.n:
#             add+=i
#         return add

# obj=Sum_Array([2,3,4,5,6,5,4])
# a=obj.sum_element()
# print(a)


# test_dict = {'gfg': [5, 6, 7, 8],
#              'is': [10, 11, 7, 5],
#              'best': [6, 12, 10, 8],
#              'for': [1, 2, 5]}

# unique_elements=set()
# for key in test_dict:
#     for value in test_dict[key]:
#         unique_elements.add(value)


# print(unique_elements)


# dict = {'a': 100, 'b': 200, 'c': 300}
# addition=0
# for key,value in dict.items():
#     addition+=value
# print(addition)

# dict={'Anuradha': 21, 'Haritha': 21, 'Arushi': 22, 'Mani': 21}

# del dict["Mani"]
# print(dict)

# dict1 = {'a': 10, 'b': 8}
# dict2 = {'d': 6, 'c': 4}

# dict3={**dict1,**dict2}
# print(dict3)

#### REAL WORLD SCENERIOS
# from operator import itemgetter
# data_list = [{"name": "Nandini", "age": 20},
#              {"name": "Manjeet", "age": 20},
#              {"name": "Nikhil", "age": 19}]
# print(sorted(data_list,key=itemgetter("age","name"),reverse=True))
#### REAL WORLD SCENERIOS USING LAMBDA FUNCTION.
# list = [{"name": "Nandini", "age": 20},
#        {"name": "Manjeet", "age": 20},
#        {"name": "Nikhil", "age": 19}]
 
# # using sorted and lambda to print list sorted
# # by age
# print("The list printed sorting by age: ")
# print(sorted(list, key=lambda i: i['age']))


# test_dict = {'month' : [1, 2, 3],
#             'name' : ['Jan', 'Feb', 'March']}

# x=list(test_dict.values())
# print(x)

# a=x[0]
# b=x[1]
# c={}
# for i in range(0,len(a)):
#     c[a[i]]=b[i]

# print((c))


