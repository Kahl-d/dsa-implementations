# Biggest honey jar possilbe
# accpets in array height of length n 

    #  #  #  #  #  #  #  
#   n1 n2 n3 n4 n5 n6 n7   
# 
#  its a two pointer thing
import math

def most_honey(height):
    p1 = 0
    p2 = len(height) - 1

    max_area = -math.inf
    while p1 < p2:
        area = (p2 - p1) * min(height[p1], height[p2])
        if area > max_area:
            max_area = area

        if height[p1] <= height[p2]:
            p1 +=1
        else:
            p2 -=1


    print(max_area)



height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
most_honey(height)

height = [1, 1]
most_honey(height)