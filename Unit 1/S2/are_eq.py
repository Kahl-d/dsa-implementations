# word1, word2 string arrays
# True - if same represnt
# False - oterwise
#  represented - array stsing concatenated in order makes the string


def are_equivalent(word1, word2):

    if ''.join(word1) == ''.join(word2):
        return True
    
    return False



word1 = ["bat", "man"]
word2 = ["b", "atman"]
print(are_equivalent(word1, word2))

word1 = ["alfred", "pennyworth"]
word2 = ["alfredpenny", "word"]
print(are_equivalent(word1, word2))

word1  = ["cat", "wom", "an"]
word2 = ["catwoman"]
print(are_equivalent(word1, word2))