
import math

def local_maximums(grid):
    
    def max_val(grid, i,j):
        
        
        m_val = -math.inf
        for k in range(i, i+3, 1):
            
            for t in range(j, j+3, 1):
                
                if grid[k][t] > m_val:
                    m_val = grid[k][t]
                    
        return m_val                
	
    n = len(grid[0])
    
    answer = [[-1 for j in range(n-2)] for k in range(n-2)]
    
    
    for i in range(n-2):
        
        for j in range(n-2):
            
            val = max_val(grid, i,j)
            answer[i][j] = val
            
        
        
    print(answer)
    
    
grid = 	[[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 2, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1]
]


    
local_maximums(grid)