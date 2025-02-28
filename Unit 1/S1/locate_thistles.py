def locate_thistles(items):

    answer = []
    
    for i in range(len(items)):
        if items[i] == 'thistle':
            answer.append(i)
            
    return answer


items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
print(locate_thistles(items))

items = ["book", "bouncy ball", "leaf", "red balloon"]
print(locate_thistles(items))