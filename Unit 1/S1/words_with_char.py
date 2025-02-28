def words_with_char(words, x):
	
    answer = []
    
    for i in range(len(words)):
        
        temp = set(words[i])
        
        if x in temp:
            answer.append(i)
            
            
    return answer


words = ["batman", "superman"]
x = "a"
print(words_with_char(words, x))

words = ["black panther", "hulk", "black widow", "thor"]
x = "a"
print(words_with_char(words, x))

words = ["star-lord", "gamora", "groot", "rocket"]
x = "z"
print(words_with_char(words, x))