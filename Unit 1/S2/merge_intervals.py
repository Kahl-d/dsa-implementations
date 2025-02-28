# accepts an array integer


def merge_intervals(intervals):

    p1 = 0

    while p1 < len(intervals) - 1:

        if intervals[p1][1] >= intervals[p1 + 1][0]:
            intervals[p1] = [min(intervals[p1][0], intervals[p1+1][0]), max(intervals[p1][1], intervals[p1+1][1])]
            intervals.pop(p1+1)

        else:
            p1 +=1

    print(intervals)

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merge_intervals(intervals)

intervals = [[1, 4], [4, 5]]
merge_intervals(intervals)