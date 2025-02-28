# array words 
# string s

# is acronym - True if s in an acronym of words

def is_acronym(words, s):

    for i in range(len(words)):
        if s[i] != words[i][0]:
            return False
        

    return True



words = ["christopher", "robin", "milne"]
s = "crm"
print(is_acronym(words, s))
