# given a string s
# reverse only the vowels in the string
# vowels are both upper and lower case and more than once



def reverse_vowels(s):

    vowels = set('AEIOUaeiou')
    s = list(s)
    p1 = 0
    p2 = len(s) -1 

    while p1 < p2:
        if s[p1] in vowels and s[p2] in vowels:
            temp = s[p1]
            s[p1] = s[p2]
            s[p2] = temp

            p1 +=1
            p2 -=1
        else:
            if s[p1] not in vowels:
                p1 +=1
            
            if s[p2] not in vowels:
                p2 -=1

    s = ''.join(s)
    print(s)


s = "robin"
reverse_vowels(s)

s = "BATgirl"
reverse_vowels(s)

s = "batman"
reverse_vowels(s)