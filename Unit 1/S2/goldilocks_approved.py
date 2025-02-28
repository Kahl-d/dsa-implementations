# list of numbers
# not max and not min


def goldilocks_approved(nums):
    
    nums.remove(max(nums))
    nums.remove(min(nums))


    if nums:
        return nums[0]
    
    return -1


nums = [3, 2, 1, 4]
print(goldilocks_approved(nums))

nums = [1, 2]
print(goldilocks_approved(nums))

nums = [2, 1, 3]
print(goldilocks_approved(nums))
