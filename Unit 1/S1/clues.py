# clues = [0, 1, 3, 50, 75]
# lower = 0
# upper = 99

# OutPut: [[2, 2], [4, 49], [51, 74], [76, 99]]


def find_missing_clues(clues, lower, upper):
    
    
    if upper == lower:
        return []
    
    if not clues:
        return [[lower, upper]]
    
    answer = []
    clues.append(upper + 1)
    prev = lower
    
    for clue in clues:
        
        temp = clue - prev - 1
        
        if temp > 0:
            answer.append([prev + 1, clue -1])
            
        prev = clue
    
    
    return answer


clues = [0, 1, 3, 50, 75]

lower = 0
upper = 99

print(find_missing_clues(clues, lower, upper))
    
    
    
clues = [-1]
lower = -1
upper = -1

print(find_missing_clues(clues, lower, upper))