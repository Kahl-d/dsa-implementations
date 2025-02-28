def get_odds(items):
    
    answer = []
    
    for item in items:
        if item % 2 != 0:
            answer.append(item)
            
    return answer



nums = [1, 2, 3, 4]
print(get_odds(nums))

nums = [2, 4, 6, 8]
print(get_odds(nums))   