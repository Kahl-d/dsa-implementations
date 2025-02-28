# two venues
# some artist will before at both venues

#  no make sure there are not conflicts
# accepts two dicts

def identify_conflicts(venue1_schedule, venue2_schedule):
    
    answer = {}

    for key, value in venue1_schedule.items():
        if venue2_schedule.get(key):
            if venue2_schedule[key] == value:

                answer[key] = value

    
    return answer

venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))