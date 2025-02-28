def find_villain(crowd, villian):
    
    answer = []
    
    for i in range(len(crowd)):
        
        if crowd[i] == villian:
            answer.append(i)
            
    return answer



crowd = ['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker']
villain = 'The Joker'
print(find_villain(crowd, villain))