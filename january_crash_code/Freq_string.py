# Calculate frequency of characters in a string


def FreqString(char):
    freq_dict={}

    for i in char:
        if i not in freq_dict :
            freq_dict[i]=1
        else :
            freq_dict[i]+=1
    return freq_dict

a=FreqString("ihfdshidfishdhidhgdiqgdigqwigdiwhedhki")


print(a)
