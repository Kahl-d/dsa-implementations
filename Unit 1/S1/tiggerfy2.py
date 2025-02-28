def tiggerfy(word):
    
    answer = ''
    i =0
    while i < len(word):
        if word[i].lower() == 'g':
            if i + 1 < len(word) and word[i + 1].lower() == 'g':
                i +=2
            else:
                answer += 'g'
                i = i+1
        elif word[i] == 'e':
            if i + 1 < len(word) and word[i + 1].lower() == 'r':
                i += 2  
            else:
                answer += 'e'
                i = i+1  
        
        elif word[i].lower() == 'i' or word[i].lower() == 't':
            i+=1
        else:
            answer += word[i]
            i+=1
            
            
    return answer


word = "Trigger"
print(tiggerfy(word))

word = "eggplant"
print(tiggerfy(word))

word = "Choir"
print(tiggerfy(word))
            
            