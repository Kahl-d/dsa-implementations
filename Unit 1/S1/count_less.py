def count_less_than(race_times, threshold):
    count = 0

    for time in race_times:
        if time < threshold:
            count += 1


    return count


race_times = []
threshold = 4
print(count_less_than(race_times, threshold))