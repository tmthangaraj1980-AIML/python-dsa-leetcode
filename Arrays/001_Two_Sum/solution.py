class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}

        for i, num in enumerate(nums):
            n = target - num

            if n in s:
                return [s[n], i]

            s[num] = i