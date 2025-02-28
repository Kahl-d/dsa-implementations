# merge alternate letters in a string


def merge_alternately(word1, word2):

    answer = ""

    if len(word1) < len(word2):
        i = 0
        while i < len(word1):
            answer += word1[i]
            answer += word2[i]
            i+=1

        answer += word2[i:]
    else:
        i = 0
        while i < len(word2):
            answer += word1[i]
            answer += word2[i]
            i+=1

        answer += word1[i:]



    print(answer)

word1 = "wol"
word2 = "oze"
merge_alternately(word1, word2)

word1 = "hfa"
word2 = "eflump"
merge_alternately(word1, word2)

word1 = "eyre"
word2 = "eo"
merge_alternately(word1, word2)



