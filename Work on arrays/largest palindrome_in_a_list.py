def Extended_list(Argument):

    E_l=[]
    for a in Argument :
        palindrome=""

        a_star=str(a)
        for j in range(len(a_star)):
            palindrome+=a_star[-1-j]
        if palindrome==a_star:
            E_l.append(a)
        
    print(E_l)

    if E_l:
        E_l.sort()
        print(f"The longest palindrome in the list is {E_l[-1]}")
    else:
        print(f"The list has no palindrome")

Extended_list([123456787654321,6552362536,3762871638716,38127382783,32876287163,31268736872362786,12345678987654321,123454321])




