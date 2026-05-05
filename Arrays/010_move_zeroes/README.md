# 🚀 Move Zeroes (LeetCode #283)

## 📌 Problem Statement
Given an integer array `nums`, move all `0`s to the end while maintaining the relative order of the non-zero elements.

⚠️ Constraint:
- Must be done **in-place**
- No extra array allowed

---

## 🧠 Approach (Two Pointer Technique)

We use two pointers:

- `i` → traverses the array
- `j` → tracks position for next non-zero element

### Logic:
- If `nums[i] != 0`, swap it with `nums[j]`
- Increment `j`
- This pushes non-zero elements forward and zeros to the end

---

## 💻 Code

```python
class Solution:
    def moveZeroes(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1