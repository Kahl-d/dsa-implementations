# return answer as 
#  i = left sum - right sum


# How
# cummalative sum
# keep adding subtrac cking elemts



def left_right_difference(nums):

    left_sum = 0
    right_sum = sum(nums)

    answer = []

    for n in nums:
        right_sum -= n
        answer.append(left_sum-right_sum)

        left_sum += n
        
    print(answer)
    return answer


nums = [10, 4, 8, 3]
left_right_difference(nums)

nums = [1]
left_right_difference(nums)