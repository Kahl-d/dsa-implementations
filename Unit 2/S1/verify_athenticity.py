# verify atuhenticity
# is authentic if in permuatatiotn of a base arry[n]

# base[n] = [1,2,3 ..... n, n]
# length is n+1

def is_authentic_collection(art_pieces):

    n = len(art_pieces) - 1

    answer = {}

    for art in art_pieces:
        if art > 0 and art <= n:
            if answer.get(art):
                answer[art] +=1

                if art != n and answer[art] > 1:
                    return False
            else:
                answer[art] = 1
        else:
            return False
        
    for i in range(1,n,1):
        if answer[i] != 1:
            return False
        
    if answer[n] != 2:
        return False
    
    print(answer)
    return True



collection1 = [2, 1, 3]
collection2 = [1, 3, 3, 2]
collection3 = [1, 1]

print(is_authentic_collection(collection1))
print(is_authentic_collection(collection2))
print(is_authentic_collection(collection3))
