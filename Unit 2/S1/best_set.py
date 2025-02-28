# attendees can cast votes
# we want to find the artitst with most votes

def best_set(votes):

    answer = {}

    for artist in votes.values():

        if answer.get(artist):
            answer[artist] += 1
        else:
            answer[artist] = 1

    max_val = 0
    max_vote_artist = ''
    for key, value in answer.items():
        if value > max_val:
            max_val = value
            max_vote_artist = artist

    return max_vote_artist

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))
