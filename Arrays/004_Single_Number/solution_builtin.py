def single_number(nums):
    return 2 * sum(set(nums)) - sum(nums)

nums = [5,1,5,2,1]
print(single_number(nums))