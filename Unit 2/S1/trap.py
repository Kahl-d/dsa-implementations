#  dict of same values



def is_balanced(code):

    dictionary = {}

    for letter in code:

        if dictionary.get(letter):
            dictionary[letter] += 1

        else:
            dictionary[letter] = 1


    prev = list(dictionary.values())
    for value in dictionary.values():
        if value == prev[0] + 1 or value == prev[0] - 1:
            return True
        

    return False


code1 = "arghh"
code2 = "haha"

print(is_balanced(code1)) 
print(is_balanced(code2)) 