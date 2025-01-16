from collections import Counter

dictionary={")":"(","]":"[","}":"{"}
dictionary=Counter(dictionary)


if ")" in dictionary.keys():
    print(True)