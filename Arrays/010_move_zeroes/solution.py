class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        m = 0
        for n in range(len(nums)):
            if nums[n] != 0:
                nums[m], nums[n] = nums[n], nums[m]
                m += 1
        