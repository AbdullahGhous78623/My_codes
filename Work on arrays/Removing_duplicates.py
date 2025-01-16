def Removing_duplicates(Argument):
    removed_duplicates=list(set(Argument))

    return removed_duplicates


Call=Removing_duplicates([2,2,3,4,5,6,5,4,3,2,7,6,8,9,8,7,6,5,4,7,9,0,9,8,7,6,5,5,4,3,3,4,6,7,8,9,0,0,9,9,6,5,4,])
print(Call)