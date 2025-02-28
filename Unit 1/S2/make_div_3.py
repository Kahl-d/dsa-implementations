# accepts int array nums
# number of operations to make each element divisible by three
# iwas thinking of summing them but 1,1,1 is 3

#  lets iterate

def make_divisible_by_3(nums):

    ops = 0

    for n in nums:
        if n%3 != 0:
            ops +=1

    print(ops)


nums = [1, 2, 3, 4]
make_divisible_by_3(nums)

nums = [3, 6, 9]
make_divisible_by_3(nums)