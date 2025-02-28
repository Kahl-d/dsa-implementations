def split_haycorns(quantity):

    counter = 1
    answer = []

    while counter <= quantity:
        if quantity % counter == 0:
            answer.append(counter)
        counter += 1

    return answer


quantity = 6
print(split_haycorns(quantity))

quantity = 1
print(split_haycorns(quantity))