class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = nums[0]
        c = nums[0]

        for i in range(1, len(nums)):
            c = max(nums[i], c + nums[i])
            m = max(m, c)

        return m