# remove_name()
# accepts a list of names - people
# a string secret identify
# return the list with any isntances of secId removed



def remove_name(people, secret_identity):


    i = 0

    while i < len(people):

        if people[i] in secret_identity:
            people.pop(i)

        else:
            i+=1


    return people


people = ['Batman', 'Superman', 'Bruce Wayne', 'The Riddler', 'Bruce Wayne']
secret_identity = 'Bruce Wayne'
print(remove_name(people, secret_identity))
