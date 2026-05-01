class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l = 0
        r = len(numbers) - 1

        while left < right:
            two_sum = numbers[left] + numbers[right]

            if two_sum == target:
                return [l + 1, r + 1]
            elif two_sum > target:
                r -= 1
            else:
                l += 1

        