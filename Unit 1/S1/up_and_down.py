def up_and_down(lst):
	num_odds = 0
	num_evens = 0
 
 
	for item in lst:
		if item % 2 == 0:
			num_evens += 1
		else:
			num_odds += 1
   
   
	return num_odds - num_evens


lst = [1, 2, 3]
print(up_and_down(lst))

lst = [1, 3, 5]
print(up_and_down(lst))

lst = [2, 4, 10, 2]
print(up_and_down(lst))