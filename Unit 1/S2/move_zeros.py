# accepts an int array
# return a new list with 0 at the end of the list
# relative order in the orioginal order should be  maintained




def move_zeroes(lst):

    answer = [0 for _ in range(len(lst))]


    p1 = 0
    p2 = 0

    while p1 < len(lst):
        if lst[p1] != 0:
            answer[p2] = lst[p1]
            p2 +=1
        p1 +=1

    return answer



lst = [1, 0, 2, 0, 3, 0]
print(move_zeroes(lst))
    