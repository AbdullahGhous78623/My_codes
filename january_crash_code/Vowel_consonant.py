class VowelConsonant:
    def __init__(self,n):
        self.n=n
    def check(self):
        if len(self.n)!=1 or not self.n.isalpha():
            return "Give valid input (one character alphabet)"
        elif self.n.lower() in ["a","e","i","o","u"]:
            return "The character is Vowel"
        else:
            return "The character is not Vowel"

user_input=input("Type a character:").strip()
obj1=VowelConsonant(user_input)
result=obj1.check()

print(result)