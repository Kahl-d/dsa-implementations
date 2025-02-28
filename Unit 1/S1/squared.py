def squared(items):
    
    for i in range(len(items)):
        items[i] = items[i] ** 2
        
    return items


numbers = [1, 2, 3]
print(squared(numbers))