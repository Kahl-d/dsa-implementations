# its sorted
# that would mean equal values will be adjacent to each other



def remove_dupes(items):


    for i in range(len(items)-1):

        if items[i] == items[i+1]:
            items.remove(items[i+1])

    print(items)
    return len(items)

items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
print(remove_dupes(items))

items = ["extract of malt", "haycorns", "honey", "thistle"]
print(remove_dupes(items))