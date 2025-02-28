# Harley Quinn
# contatin hills we want to find the highest hill
# n + 1 points


# starts at point 0 at alt 0
# gains is gain[i] between i and i+1 point


# in thiking

# 0 h1 h2 h3 h4 h5 ......... hn   n hills +  0 = n +1
# gain between all of then

# so hightest building 
# gains is is actually the height we keep adding to get the height


def highest_altitude(gain):

    hill = 0
    max_alt = 0

    for g in gain:
        hill += g
        if hill > max_alt:
            max_alt = hill
    print(max_alt)
    return max_alt

gain = [-5, 1, 5, 0, -7]
highest_altitude(gain)

gain = [-4, -3, -2, -1, 4, 3, 2]
highest_altitude(gain)