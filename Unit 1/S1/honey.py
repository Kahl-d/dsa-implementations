def sum_honey(arr):

    sum = 0

    for h in arr:
        sum += h

    return sum


hunny_jars = [2, 3, 4, 5]
print(sum_honey(hunny_jars))

hunny_jars = []
print(sum_honey(hunny_jars))