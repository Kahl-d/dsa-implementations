def tiggerfy(s):
	
    answer = ""
    
    letters = set('TIGERtiger')
    
    
    for i in range(len(s)):
        if s[i] not in letters:
            answer += s[i]
        
        
    return answer


s = "suspicerous"
print(tiggerfy(s))
            