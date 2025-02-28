def minimum_boxes(meals, capacity):
	
    total = 0 
    
    for meal in meals:
        total+=meal
        
    cap = sorted(capacity, reverse=True)
	
    count = 0
    
    for size in cap:
        total -= size
        
        count +=1
        
        if total <= 0:
            return count


    return False


meals = [1, 3, 2]
capacity = [4, 3, 1, 5, 2]
print(minimum_boxes(meals, capacity))

meals = [5, 5, 5]
capacity = [2, 4, 2, 7]
print(minimum_boxes(meals, capacity))
            
    
