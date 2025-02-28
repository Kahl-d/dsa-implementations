def diagonal_sum(grid):

    l = len(grid)

    i = 0
    j = 0

    first_sum = 0
    while i < l:
        first_sum += grid[i][j]
        i +=1
        j +=1

    i = 0
    j = l -1
    second_sum = 0
    while j >= 0:
        second_sum += grid[i][j]
        i +=1
        j -=1
        

    if l % 2 != 0:
        
        return first_sum + second_sum - grid[l//2][l//2]
    
    else:
        return first_sum + second_sum
    

grid = [
	[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(diagonal_sum(grid))

grid = [
	[1, 1, 1, 1],
    [1, 1, 1, 1],
	[1, 1, 1, 1],
    [1, 1, 1, 1]
]
print(diagonal_sum(grid))

grid = [
	[5]
]
print(diagonal_sum(grid))