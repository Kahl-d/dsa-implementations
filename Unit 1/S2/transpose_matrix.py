def transpose(m):

    print(m)
    for i in range(len(m[0])):

        for j in range(i,len(m)):

            if i != j:
                print(i,j, "in there")
                temp = m[i][j]
                m[i][j] = m[j][i]
                m[j][i] = temp

            else:
                print(i,j, "not in there")
    print(m)
    return m



matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpose(matrix) 


