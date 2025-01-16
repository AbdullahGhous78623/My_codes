numbers=[1,3,4,4,5]
new_list=map(lambda x:x*x,numbers)
print(list(new_list))



def filter_func(a):
    return a>3

newnewl=filter(filter_func,numbers)

print(tuple(newnewl))

# print(list(newnewl))

# print(set(newnewl))

from functools import reduce
sum_=reduce(lambda x,y:x+y,numbers)

print(sum_)

