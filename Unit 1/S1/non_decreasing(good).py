def non_decreasing(nums):
    
    count = 0
    limit = 1
    prev = nums[-1]
    
    for i in range(len(nums)-2, -1, -1):
        if nums[i] > prev:
            count +=1
            
            if count > limit:
                return False
        else:
            prev = nums[i]
            
    return True
    
    
nums = [4, 2, 3]
print(non_decreasing(nums))

nums = [4, 2, 1]
print(non_decreasing(nums))