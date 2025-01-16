def primeRange(n1,n2):
    list_of_prime=[]
    for i in range(n1+1,n2):
        Prime=True
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                Prime=False
                break
        if Prime:
            list_of_prime.append(i)
    return list_of_prime


prime_numbers=primeRange(23,67)
print(prime_numbers)