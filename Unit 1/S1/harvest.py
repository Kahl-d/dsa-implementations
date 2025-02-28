def harvest(vegetable_patch):
    
    
    count = 0
    for row in vegetable_patch:
        
        for cell in row:
            if cell == 'c':
                count +=1
                
    return count


vegetable_patch = [
	['x', 'c', 'x'],
	['x', 'x', 'x'],
	['x', 'c', 'c'],
	['c', 'c', 'c']
]
print(harvest(vegetable_patch))