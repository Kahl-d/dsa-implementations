def linear_search(lst, target):
	# function should return the first index of target in items
    #  -1 if target is not in the lst
    
    
    for items in lst:
        if items == target:
            return lst.index(items)
    return -1




items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
print(linear_search(items, target))

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
print(linear_search(items, target))