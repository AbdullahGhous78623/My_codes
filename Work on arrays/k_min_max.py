def func(tup,k):
    min_e_k=sorted(tup)
    min_e_k=min_e_k[0:k]

    max_e_k=sorted(tup)
    max_e_k=max_e_k[-k:]
    result=tuple(min_e_k+max_e_k)
    print(type(result))
    return result



a=func((5, 20, 3, 7, 6, 8),2)

print(a)
print(type(a))