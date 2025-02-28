# given two string
#  artists and set_times
# length n

# 3 function lineup
# we are just making a dict


def lineup(artists, set_times):
    lineup = {}

    for i in range(len(artists)):
        lineup[artists[i]] = set_times[i]

    return lineup

artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))