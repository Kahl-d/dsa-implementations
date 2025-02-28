def hulk_smash(n):
	
 
    answer = ["" for i in range(n+1)]
    
    
    
    for i in range(1, n+1 ,1):
        
        if i % 3 == 0:
            answer[i] = "Hulk"
            
        if i % 5 == 0:
            answer[i] += "Smash"
            
        if answer[i] == "":
            answer[i] = str(i)
            
            
    return answer

n = 3
print(hulk_smash(n))

n = 5
print(hulk_smash(n))

n = 15
print(hulk_smash(n))
            
        