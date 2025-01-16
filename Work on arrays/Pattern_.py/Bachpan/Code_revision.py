# def num(num_value):
#     if num_value>=0:
#         return "The number is positive"
#     else:
#         return "The number is negative"

# a=int(input("Type a number:"))
# b=num(a)
# print(b)



# def even_odd(num):
#     if num%2==0:
#         return "The number is even"
#     else:
#         return "The number is odd"
    
# a=int(input("Type a number:"))
# b=even_odd(a)
# print(b)



# def sum_func(num):
#     total=0
#     for i in range(num+1):
#         total+=i
#     return(f'The sum of 1st {num} natural number is {total}')

# a=int(input("Type the number:"))
# b=sum_func(a)
# print(b)



# def sum_num(num1,num2):
#     if num1>=num2 or num2==num1+1:
#         return "There is no possible number between num1 and num2"
    
#     total=0
#     for i in range(num1+1,num2):
#         total+=i
#     return (f"The sum of number in range of {num1} and {num2} is {total}")


# n1=int(input("Type the 1st number:"))
# n2=int(input("Type the 2nd number:"))
# a=sum_num(n1,n2)
# print(a)



# def greatest(n1,n2):
#     if n1>n2:
#         return (f"The number {n1} is greater than {n2}")
#     else:
#         return (f"The number {n2} is greater than {n1}")
    
# a=greatest(8,786)
# print(a)

# def greatest(n1,n2,n3):
#     if n1>n2:
#         n=n1
#     else:
#         n=n2
#     if n3>n:
#         return f"The greatest number is {n3}"
#     else:
#         return f"The greatest number is {n}"
    
# a=greatest(2,2,2)
# print(a)



# def leap_year(year):
#     if (year%4==0and year%100!=0) or year%400==0 :
#         return "The year is a leap year"
#     else:
#         return "The year is not a leap year"
# a=leap_year(2000)
# print(a)


# def Prime(n1):
#     if n1<2:
#          return "The number is not prime"
#     if n1==2:
#          return "The number is prime"
#     for i in range(2,n1):
        
#             if n1%i==0:
#                 return "The number is not prime"
    
#     return "The number is prime"

# a=Prime(7)
# print(a)


# def prime(n1,n2):
    
#     if n1>=n2 :
#         return "##Error----Range not defined-------"
#     for i in range (n1+1,n2):
        
#         if i<2 :
#             continue

        
#         is_prime=True
#         for j in range(2,int(i**0.5)+1):
#             if i%j==0:
#                 is_prime=False
                
#                 break
#         if is_prime:
#             print(i)
#     return "Above are the primes in the desired"      

# a=prime(2,2)
# print(a)



# def digit_sum(num):
#     total_sum=0
#     for i in num:
#         if not i.isdigit():
#             return "Invalid input given"
#         total_sum+=int(i)
#     return total_sum
    
# a=input("Type the number:")
# b=digit_sum(a)
# print(b)

# def rev_num(num):
#     rev_number=""
#     for i in range(1,len(num)+1):
#         if not num[i-1].isdigit():
#             return "Invalid input given"
#         rev_number+=num[-i]
#     return int(rev_number)

# a=input("Type the number:")
# b=rev_num(a)
# print(b)

# def rev_num(num):
    
#     for i in num:
#         if not i.isdigit():
#             return "Invalid input given"
#         rev_number=num[::-1]
#     return int(rev_number)

# a=input("Type the number:")
# b=rev_num(a)
# print(b)

# a=input("Type a number:")


# if not a.isdigit():
#     print ("Invalid input")
# else:
#     c=(a[::-1])
#     if int(a)==int(c):
#         print("The number is palindrome")
#     else:
#         print("The numeber is not palindrome")






# def palindrome(num):
#     if not num.isdigit():
#         return "Invalid input passed"
#     reverse_string=num[::-1]
#     if int(num)==int(reverse_string):
#         return "The number is palindrome"
#     else:
#         return "The number is not palindrome"


# a=input("Type a number:")
# b=palindrome(a)
# print(b)



# def Armstrong(num):
#     if not num.isdigit():
#         return "Invalid input passed"
#     Arm_strong=0
#     for i in num:
#         Arm_strong+=(int(i))**len(num)
#     if int(num)==(Arm_strong):
#         return "The number is ARMSTRONG"
#     else:
#         return "The number is not ARMSTRONG"
    
# a=input("Type a number:")
# b=Armstrong(a)
# print(b)



# def Arm_range(n1,n2):
#     if n1>=n2 :
#         return "Invalid range provided"
#     list_arm=[]
#     if n1<=0 :
#         n1=0
#     if n2<0:
#         return "invalid range provided"
    
#     for i in range (n1+1,n2):
        
#         i=str(i)
#         Arm_strong=0
#         for j in i:
#             Arm_strong+=int(j)**len(i)
#         if Arm_strong==int(i):
#             list_arm.append(Arm_strong)
#     return list_arm


# a=Arm_range(10000,10000000)
# print(a)

# def fibonacci(n):
#     if n<=0:
        
#         return("invalid input given")
#     if n==1:
#         return [0]
#     n1=0
#     n2=1
#     list_fib=[0,1]
#     for _ in range(n-2):
#         n_r=n1+n2
#         print(n_r,end="")
#         n1=n2
#         n2=n_r
#     return list_fib
# a=fibonacci(342)
# print(a)

# def factorial(n):
#     if n<0:
#         return "factorial not defined"
#     if (n==0 or n==1) :
#         return 1
#     else:
#         return n* factorial(n-1)

# a=factorial(6)
# print(a)

# def factorial(n):
#     if n<0:
#         return "invalid input given"
#     if n==0 or n==1:
#         return 1
#     factorial=1
#     for i in range(2,n+1):
#         factorial=factorial*i
#     return  factorial

# a=factorial(3)
# print(a)


# def power(n1,n2):
#     return n1**n2

# n1=int(input("Type the first number:"))
# n2=int(input("type tye second number:"))
# a=power(n1,n2)
# print(a)


# def factors(n):
#     if n<=0:
#         return "Invalid input given"
#     list_=[]
#     for i in range(1,n+1):
#         if n%i==0:
#             list_.append(i)
#     return f'The factors of {n} are : {list_}'

# a=factors(76)
# print(a)


# def prime_factor_num(n):
#     list_prime=[]

#     for i in range(2,n+1):
#         prime_factor=True
#         if n%i==0:
#             for j in range(2,i):
#                 if i%j==0:
#                     prime_factor=False
#                     break
#             if prime_factor:
#                 list_prime.append(i)
            
#     return list_prime

# a=prime_factor_num(789)
# print(a)

# def factorial (n):
#     if n<0:
#         return("factorial not defined")
        
#     if n==0 or n==1:
#         return 1
#     fact=1
#     for i in range(2,n+1):
#         fact*=i
#     return fact

# def is_strong_number(num):
#     if num<0:
#         return False
#     sum_digit=0
#     for i in str(num):
#         sum_digit+=factorial(int(i))
#     if num==sum_digit:
#         return "The number is strong number"
#     else:
#         return "The number is not a strong number"

# a=is_strong_number(22250)
# print(a)

# def is_perfect_number(num):
#     if num<=0:
#         return False
#     sum_num=0
#     for i in range (1,int(num*0.5)+1):
#         if num%i==0:
#             sum_num+=i
#     if sum_num==num:
#         return True
#     else:
#         return False
            
    
    
# def perfect_square(n):
#     sr=int(n**0.5)
#     return sr**2==n
        
    

# a=perfect_square(9)

# if a:
#     print("The number is Perfect Square")
# else:
#     print("The number is not a Perfect Square")


# def automorphic_num(n):
#     if n<0:
#         return "Wrong input given"
#     sq=n**2
    
#     if str(sq).endswith(str(n)):
#         return "The number is automorphic"
#     else:
#         return "The number is not automorphic"
    

# a=automorphic_num(0)
# print(a)

# def harshad_num(n):
#     if n<=0:
#         return "Wrong input given"
#     sum_=0
#     for i in str(n):
#         sum_+=int(i)
#     if n%sum_==0:
#         return "The number is harshad Number"
#     else:
#         return "The number is not harshad number"



# a=harshad_num(18)
# print(a)


# def Abundant(n):
#     if n<=0:
#         return "Invalid input given"
#     sum_=0
#     for i in range(1,n):
#         if n%i==0:
#             sum_+=i
#     if sum_>n:
#         return "The number is Abundant"
#     else:
#         return "The number is not Abundant"

# a=Abundant(54)
# print(a)


# def Friendly_pair(n1,n2):
#     if n1 <=0 or n2<=0:
#         return "Invalid input given"
#     sum1=1
#     sum2=1
#     for i in range(2,n1):
#         if n1 % i==0:
#             sum1+=i
#     for j in range(2,n2):
#         if n2 % j==0:
#             sum2+=j
#     if sum1==n2 and sum2==n1:
#         return "The numbers are frindly Pair"
#     else:
#         return "The numbers are not frindly Pair"
    
# a=Friendly_pair(34,45)
# print(a)

# def HCF_FUNC(n1,n2):
#     if n1<=0 or n2<=0:
#         return -1
    
#     for i in range (1,min(n1,n2)+1):
#         if n1%i==0 and n2%i==0:
#             HCF=i
#     return HCF
    
            
# a=HCF_FUNC(8,72)
# print(a)

# def euclid_gcd(n1, n2):
#     # Ensure both numbers are positive
#     if n1 <= 0 or n2 <= 0:
#         return -1  # Error case for non-positive inputs
    
#     while n2 != 0:
#         n1, n2 = n2, n1 % n2  # Apply Euclid's algorithm
    
#     return n1  # n1 now holds the GCD

# # Test case
# result = euclid_gcd(8, 72)
# print(result)  # Output: 8


# def LCM_FUNC(n1,n2):
#     if n1<=0 or n2<=0:
#         return -1
#     for i in range (1,min(n1,n2)+1):
#         if n1%i==0 and n2%i==0:
#             HCF=i
#     return (n1*n2)//HCF





# a=LCM_FUNC(43,42)
# print(a)


# def array_max_min(arr):
#     value1=arr[0]
#     for i in arr:
#         if value1>i:
#             value1=i
#     min=value1
#     value2=arr[0]
#     for j in arr:
#         if value2<j:
#             value2=j
#     max=value2
#     return f'The max value of array is {max}, The min value of te array is {min}'


# a=array_max_min([75,4,3,2,4,42,63,2,35,6,36,6,3,6,46,4,3,543,653,6,5,6,353,3,6])
# print(a)
# import math
# a=[23,65,64,33,32,56,62,43,65,87,98]
# value1=a[0]
# for i in a :
#     if value1>i:
#         value1=i
# value2=math.inf
# for j in a:
#     if j!=value1 and value2>j:
        
#         value2=j

# print(value2)

# a=[2,3,4,5,6,6]
# sum=0
# for i in a:
#     sum+=i
# print(sum)


# a=[2,4,5,3,2,5]
# b=a[::-1]
# print(b)

# def rev(arr):
#     rev_list=[]
#     for i in range(1,len(arr)+1):
#         rev_list.append(arr[-i])
#     return rev_list

# a=rev([45,35,332,53,64,4,23,4,33,3345,5])
# print(a)




# a=[233,54,65,334,345,76,554,87,44]
# a.sort()
# print(a)







    






    






                
            









    
        

   
        













