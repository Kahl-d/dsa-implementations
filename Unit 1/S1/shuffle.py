def shuffle(cards):
    n = len(cards) // 2
    
    answer = []
 
    for i in range(n):
        answer.append(cards[i])
        answer.append(cards[i+n])
        
        
    return answer


cards = ['Joker', 'Queen', 2, 3, 'Ace', 7]
print(shuffle(cards))

cards = [9, 2, 3, 'Joker', 'Joker', 3, 2, 9]
print(shuffle(cards))

cards = [10, 10, 2, 2]
print(shuffle(cards))