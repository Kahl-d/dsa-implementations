def organize_exhibition(collection):
    

    answer = []


    while collection:

        temp = set(collection)
        answer.append(list(temp))

        for item in temp:
            collection.remove(item)

    
    return answer


collection1 = ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol", 
              "Kahlo", "O'Keefe"]
collection2 = ["Kusama", "Monet", "Ofili", "Banksy"]

print(organize_exhibition(collection1))
print(organize_exhibition(collection2))