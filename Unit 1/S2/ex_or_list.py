# lst1
# lst2

def exclusive_elemts(lst1, lst2):
	

    answer = []
    for el in lst1:
        if el not in lst2:
            answer.append(el)

    for el in lst2:
        if el not in lst1:
            answer.append(el)

    print(answer)


lst1 = ["pooh", "roo", "piglet"]
lst2 = ["piglet", "eeyore", "owl"]
exclusive_elemts(lst1, lst2)

lst1 = ["pooh", "roo"]
lst2 = ["piglet", "eeyore", "owl", "kanga"]
exclusive_elemts(lst1, lst2)

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["pooh", "roo", "piglet"]
exclusive_elemts(lst1, lst2)