def smaller_than_current(nums):

    answer = [-1 for i in range(len(nums))]

    for i in range(len(nums)):
        
        el = nums[i]
        smaller = 0

        for j in range(len(nums)):
            if j!= i and nums[j] < el:
                smaller +=1

        answer[i] = smaller


    return answer


nums = [8, 1, 2, 2, 3]
print(smaller_than_current(nums))

nums = [6, 5, 4, 8]
print(smaller_than_current(nums))

nums = [7, 7, 7, 7]
print(smaller_than_current(nums))