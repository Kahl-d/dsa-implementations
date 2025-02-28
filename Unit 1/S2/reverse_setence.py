def reverse_sentence(sentence):
    words = sentence.split()

    print(words)
    answer = ''

    for i in range(len(words)-1, -1,-1):
        answer += words[i]


    return answer




print(reverse_sentence("fluff with stuffed all cubby little tubby"))


