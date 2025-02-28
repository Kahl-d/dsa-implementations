def running_sum(superhero_stats):
    
    yet = 0
    
    for i in range(len(superhero_stats)):
        yet += superhero_stats[i]
        superhero_stats[i] = yet
        
    return superhero_stats


superhero_stats = [1, 2, 3, 4]
print(running_sum(superhero_stats))

superhero_stats = [1, 1, 1, 1, 1]
print(running_sum(superhero_stats))

superhero_stats = [3, 1, 2, 10, 1]
print(running_sum(superhero_stats))