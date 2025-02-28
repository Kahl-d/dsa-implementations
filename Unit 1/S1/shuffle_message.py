def shuffle(message, indices):
    l = len(indices)
    
    answer = ["" for i in range(l)]
    
    
    for j in range(l):
        print(indices[j],message[j])
        answer[indices[j]] = message[j]
        
        
    
    s = ''
    
    for c in answer:
        s += c
        
    return s


message = "evil"
indices = [3, 1, 2, 0]
print(shuffle(message, indices))

message = "findme"
indices = [0, 1, 2, 3, 4, 5]
print(shuffle(message, indices))