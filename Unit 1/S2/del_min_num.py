
# eating from smallest to largest


def delete_minimum_elements(hunny_jar_sizes):
	
    answer = []

    while hunny_jar_sizes:
        eat = min(hunny_jar_sizes)
        answer.append(eat)
        hunny_jar_sizes.remove(eat)


    return answer


hunny_jar_sizes = [5, 3, 2, 4, 1]
print(delete_minimum_elements(hunny_jar_sizes))

hunny_jar_sizes = [5, 2, 1, 8, 2]
print(delete_minimum_elements(hunny_jar_sizes))
